#存储游戏中运行的函数
import sys
import time
import random
import pygame
from settings import Settings
from data import Data
from camera import Camera
from component import *


#终止程序
def terminate():
	pygame.quit()
	sys.exit()


def keyEventToEachComponent(data,settings,event):
	if len(data.components)>0:
		for component in data.components:
			if component.isListenKeyEvent:
				component.handleKeyEvent(event)

def mouseMotionEventToEachComponent(data,settings,event):
	if len(data.components)>0:
		for component in data.components:
			if component.isListenMouseMotionEvent:
				component.handleMouseMotionEvent(event)

def mouseEventToEachComponent(data,settings,event):
	if len(data.components)>0:
		for component in data.components:
			if component.isListenMouseEvent:
				component.handleMouseEvent(event)

#检查事件
def check_events(data,settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			data.save()
			terminate()
		elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
			keyEventToEachComponent(data,settings,event)
		elif event.type == pygame.MOUSEMOTION:
			mouseMotionEventToEachComponent(data,settings,event)
		elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
			mouseEventToEachComponent(data,settings,event)


#刷新屏幕
def update_screen(surface):
	screen=pygame.display.get_surface()
	screen.blit(surface,(0,0))
	pygame.display.update()

#绘制组件
def draw_components(data,settings):
	data.components.update()
	data.components.draw(data.screen_buff)




#游戏进入菜单，执行
def enter_menu(data,settings):
	#播放背景音乐
	pygame.mixer.music.load(data.menu_music_path)
	pygame.mixer.music.play(-1,0.0)

	#清除所有组件
	data.components.empty()

	
	zombie=Zombie(data,settings,data.zombie_data[0])
	zombie.status=settings.STAND
	x,y=data.map[0][3]
	zombie.rect.centerx=x
	zombie.rect.centery=y
	data.components.add(zombie)



	#添加开始按钮
	beginButton=BeginButton(data,settings)
	beginButton.image=data.menu_begin_image.copy()
	beginButton.image_back=data.menu_begin_image.copy()
	beginButton.set_size(300,200)
	beginButton.rect.centerx=int(settings.screen_width/2)
	beginButton.rect.centery=int(settings.screen_height-settings.screen_height/3)
	beginButton.auto_scale()
	beginButton.isListenMouseEvent=True
	beginButton.isListenMouseMotionEvent=True
	data.components.add(beginButton)

	#显示等级
	textView=TextView(data,settings)
	textView.set_size(200,50)
	textView.rect.right=settings.screen_width
	textView.rect.top=10
	textView.set_text("Level:"+str(data.game_file["level"]))
	data.components.add(textView)

	data.is_execute_sleep=False
	data.is_lua_end=False

#显示英雄选择界面
def show_hero_selection(data,settings):


	top=4
	left=404

	for i in range(len(data.hero_data)):
		hero_selection=HeroSelection(data,settings,data.hero_data[i])
		hero_selection.rect.top=top
		hero_selection.rect.left=left
		hero_selection.auto_scale()
		data.components.add(hero_selection)
		left+=hero_selection.rect.width
		if left >= 1000:
			left=404
			top+=hero_selection.rect.height+4
	


	selection_done=SelectionDone(data,settings)
	selection_done.set_size(200,100)
	selection_done.rect.centerx=1300
	selection_done.rect.centery=300
	selection_done.auto_scale()
	data.components.add(selection_done)

	textView=TextView(data,settings)
	textView.set_size(400,50)
	textView.rect.right=settings.screen_width+400
	textView.rect.top=10
	textView.set_text("Please select "+str(settings.max_allowed_hero)+" Heroes")
	data.components.add(textView)


def camera_move_to_right(data,settings):
	#清除所有组件
	if len(data.components)>0:
		data.components.empty()
	if data.camera.rect.right < settings.screen_buff_width:
		data.camera.rect.right+=1
	else:

		#随机添加几个僵尸
		for i in range(1,8):
			x=random.randint(1100,1300)
			y=random.randint(110,500)
			j=random.randint(0,len(data.zombie_data)-1)
			zombie=Zombie(data,settings,data.zombie_data[j])
			zombie.status=settings.STAND
			zombie.rect.centerx=x
			zombie.rect.centery=y
			data.components.add(zombie)

		show_hero_selection(data,settings)

		settings.game_status=settings.STATUSNONE
		settings.game_status2=settings.UNHANDLED


def gaming_init(data,settings):

	#显示等级
	textView=TextView(data,settings)
	textView.set_size(200,50)
	textView.rect.right=settings.screen_width
	textView.rect.top=10
	textView.set_text("Level:"+str(data.game_file["level"]))
	data.components.add(textView)

	top=4
	for i in range(len(data.selected_hero)):
		hero_switch=HeroSwitch(data,settings,data.hero_data[data.selected_hero[i]])
		hero_switch.rect.left=4
		hero_switch.rect.top=top
		top+=20+hero_switch.rect.width
		hero_switch.auto_scale()
		data.components.add(hero_switch)


	data.is_lua_end=False
	data.is_execute_sleep=False
	data.last_lua_ticks=0
	data.current_lua=0
	data.pc=0
	data.r0=0
	data.current_lua=data.level_lua[data.game_file["level"]-1]
	data.last_lua_ticks=settings.ticks
	data.hero_map=[[False,False,False,False,False,False,False,False,False],
				   [False,False,False,False,False,False,False,False,False],
				   [False,False,False,False,False,False,False,False,False],
				   [False,False,False,False,False,False,False,False,False],
				   [False,False,False,False,False,False,False,False,False]
		]


def camera_move_to_left(data,settings):

	if data.camera.rect.left > 0:
		data.camera.rect.left-=1
	else:
		#清空所有组件
		data.components.empty()
		#游戏开始之前初始化组件
		gaming_init(data,settings)
		#正式开始游戏
		settings.game_status=settings.STATUSGAMING
		settings.game_status2=settings.UNHANDLED
	

def add_new_zombie(data,settings,r0):
	zombie=Zombie(data,settings,data.zombie_data[r0])
	zombie.status=settings.WALK
	zombie.frame=0
	zombie.speed=data.zombie_data[r0]["move_speed"]
	zombie.target=data.target
	i=random.randint(0,4)
	x,y=data.map[i][9]
	zombie.rows=i
	zombie.rect.centerx=x
	zombie.rect.centery=y
	zombie.float_x=float(x)
	zombie.float_y=float(y)
	data.components.add(zombie)




def gaming(data,settings):
	
	#解析关卡脚本
	


	#判断是否执行了sleep
	if data.is_execute_sleep:
		if settings.ticks - data.last_lua_ticks >= data.r0:
			data.is_execute_sleep=False
		return True


	if data.is_lua_end:
		count = 0
		for component in data.components.sprites():
			if component.class_name == "Zombie":
				count += 1

		if count == 0 :
			#胜利
			data.win_music.play()
			settings.game_status=settings.STATUSMENU
			settings.game_status2=settings.UNHANDLED
			pygame.mixer.music.stop()
			pygame.mixer.music.load(data.menu_music_path)
			pygame.mixer.music.play()
			data.is_execute_sleep=False
			data.is_lua_end=False
			data.game_file["level"]+=1
			data.save()
		return True

	
	#读取一条指令
	instruction=data.current_lua[data.pc]
	data.pc+=1
	function_name=instruction["function"]
	if function_name == "sleep":
		data.r0=instruction["r0"]
		data.is_execute_sleep=True
		data.last_lua_ticks=settings.ticks
	elif function_name == "zombie":
		add_new_zombie(data,settings,instruction["r0"])
	elif function_name == "awooga":
		data.awooga_music.play()
	elif function_name == "wait_for_win":
		data.is_lua_end=True
	


def game_over(data,settings):
	#清空所有组件
	data.components.empty()
	#返回Menu
	settings.game_status = settings.STATUSMENU
	settings.game_status2 = settings.UNHANDLED

#游戏状态处理
def handle_game_status(data,settings):
	if settings.game_status == settings.STATUSMENU and settings.game_status2 == settings.UNHANDLED:
		#当游戏进入菜单时
		settings.game_status2 = settings.HANDLED
		enter_menu(data,settings)
	elif settings.game_status == settings.STATUSCAMERAMOVETORIGHT:
		#进行相机移动到最右边
		camera_move_to_right(data,settings)
	elif settings.game_status == settings.STATUSCAMERAMOVETOLEFT:
		#进行相机移动到最右边
		camera_move_to_left(data,settings)
	elif settings.game_status == settings.STATUSGAMING:
		gaming(data,settings)
	elif settings.game_status == settings.STATUSGAMEOVER:
		game_over(data,settings)
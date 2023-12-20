#游戏全部组件
import pygame
import random
import math
from pygame.sprite import Sprite

#基本组件，继承Sprite
#可以设置图像，大小，位置，监听事件
class Component(Sprite):
	def __init__(self,data,settings):
		super().__init__()
		self.class_name="Component"
		self.data=data
		self.settings=settings
		self.rect = pygame.Rect(0,0,0,0)          #获取默认rect
		self.image = pygame.Surface((1,1))        #获取默认image
		self.isListenKeyEvent = False             #是否监听键盘点击事件
		self.isListenMouseMotionEvent = False     #是否监听鼠标移动事件
		self.isListenMouseEvent = False           #是否监听鼠标点击事件
	def set_image(self,image):
		self.image = image
	def set_size(self,width,height):
		self.rect.width = width
		self.rect.height = height
	def set_location(self,x,y):
		self.rect.left = x
		self.rect.top = y
	def set_bounds(self,x,y,width,height):
		self.rect.left = x
		self.rect.top = y
		self.rect.width = width
		self.rect.height = height
	def get_width(self):
		return self.rect.width
	def get_height(self):
		return self.rect.height
	def get_top(self):
		return self.rect.top
	def get_bottom(self):
		return self.rect.bottom
	def get_left(self):
		return self.rect.left
	def get_right(self):
		return self.rect.right
	#自动调整image与rect一样大小
	def auto_scale(self):
		self.image=pygame.transform.scale(self.image,(self.rect.width,self.rect.height))

	#处理键盘点击事件，由子类重写此函数
	def handleKeyEvent(self,event):
		pass
	#处理鼠标移动事件，由子类重写此函数
	def handleMouseMotionEvent(self,event):
		pass
	#处理鼠标点击事件，由子类重写此函数
	def handleMouseEvent(self,event):
		pass

	#检查point是否在rect之中
	def check_point_in_rect(self,point,rect):

		#point为屏幕上的坐标，需要转化为对应屏幕缓冲区的坐标
		offset=self.data.camera.rect.left
		point.x+=offset

		if point.x > rect.left and point.x < rect.right and point.y > rect.top and point.y < rect.bottom:
			return True
		else:
			return False

	def update(self):
		pass

	def blitme(self):
		self.data.screen_buff.blit(self.image,self.rect)


class Point():
	def __init__(self,x=0,y=0):
		self.class_name="Point"
		self.x=x
		self.y=y


#显示文本的类
class TextView(Component):
	def __init__(self,data,settings):
		super().__init__(data,settings)
		self.class_name="TextView"
		self.data=data
		self.settings=settings
		self.text="none"
		self.font=pygame.font.Font(None,32)
		self.image=self.data.void_image.copy()
		self.color=pygame.Color(255,0,0)
	def set_text(self,text):
		self.text=text
	def set_font(self,font):
		self.font=font
	def set_color(self,color):
		self.color=color
	def update(self):
		self.image=self.data.void_image.copy()
		self.auto_scale()
		ObjFont=self.font.render(self.text,True,self.color)
		ObjRect=ObjFont.get_rect()
		ObjRect.centerx=self.rect.width//2
		ObjRect.centery=self.rect.height//2
		self.image.blit(ObjFont,ObjRect)

#开始按钮
class BeginButton(Component):
	def __init__(self,data,settings):
		super().__init__(data,settings)
		self.class_name="BeginButton"
		self.data=data
		self.settings=settings
		self.isMouseEntered=False
		self.mouseEnterStatus=0

	def handleMouseMotionEvent(self,event):
		
		#检查是否在rect内
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		if self.check_point_in_rect(point,self.rect):
			self.isMouseEntered=True
			#检查是否已经播放进入音乐
			if self.mouseEnterStatus == 0:
				self.data.mouse_entered_music.play()
				self.mouseEnterStatus =1
				self.rect.width+=10
				self.rect.height+=10
				self.rect.centerx=int(self.settings.screen_width/2)
				self.rect.centery=int(self.settings.screen_height-self.settings.screen_height/3)
				self.auto_scale()
		elif self.mouseEnterStatus == 1:
			self.isMouseEntered=False
			self.mouseEnterStatus =0
			self.rect.width-=10
			self.rect.height-=10
			self.rect.centerx=int(self.settings.screen_width/2)
			self.rect.centery=int(self.settings.screen_height-self.settings.screen_height/3)
			self.image=self.image_back.copy()
			self.auto_scale()
		

	def handleMouseEvent(self,event):
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		if self.check_point_in_rect(point,self.rect) and event.button == 1 and event.type == pygame.MOUSEBUTTONDOWN:
			self.settings.game_status=self.settings.STATUSCAMERAMOVETORIGHT
			self.settings.game_status2=self.settings.UNHANDLED
			self.data.button_clicked_music.play()
			pygame.mixer.music.stop()
			pygame.mixer.music.load(self.data.choose_hero_music_path)
			pygame.mixer.music.play(-1,0.0)




#僵尸类
class Zombie(Component):
	def __init__(self,data,settings,zombie_data):
		super().__init__(data,settings)
		self.class_name="Zombie"
		self.data=data
		self.settings=settings
		self.zombie_data=zombie_data
		self.status=self.settings.STAND
		self.frame=0
		self.speed=0
		self.float_x=-1
		self.float_y=-1
		self.rows=-1
		self.health=self.zombie_data["health"]
		self.rect=pygame.Rect(0,0,self.zombie_data["width"],self.zombie_data["height"])
		self.stand_image=self.zombie_data["stand_image"]
		self.walk_image=self.zombie_data["walk_image"]
		self.attack_image=self.zombie_data["attack_image"]
		self.attack_music=self.zombie_data["attack_music"]
		self.last_ticks=self.settings.ticks
		self.isAttack=False
		self.game_over_flag=False
		self.last_attack_ticks=0
	def update(self):
		#绘制图像
		if self.status == self.settings.STAND and (self.settings.ticks-self.last_ticks) >= 100:
			self.last_ticks=self.settings.ticks
			self.frame+=1
			if self.frame >= self.zombie_data["stand_frame_total"]:
				self.frame=0
			self.image=self.stand_image.subsurface((self.zombie_data["stand_image_width"]*self.frame+self.zombie_data["stand_margin_left_cut"],0,self.zombie_data["stand_image_width"]-self.zombie_data["stand_margin_left_cut"],self.zombie_data["stand_image_height"]))
			self.image=self.image.copy()
			self.auto_scale()
		elif self.status == self.settings.WALK and (self.settings.ticks-self.last_ticks) >= 100:
			self.last_ticks=self.settings.ticks
			self.frame+=1
			if self.frame >= self.zombie_data["walk_frame_total"]:
				self.frame=0
			self.image=self.walk_image.subsurface((self.zombie_data["walk_image_width"]*self.frame+self.zombie_data["walk_margin_left_cut"],0,self.zombie_data["walk_image_width"]-self.zombie_data["walk_margin_left_cut"],self.zombie_data["walk_image_height"]))
			self.image=self.image.copy()
			self.auto_scale()
		elif self.status == self.settings.ATTACK and (self.settings.ticks-self.last_ticks) >= 100:
			self.last_ticks=self.settings.ticks
			self.frame+=1
			if self.frame >= self.zombie_data["attack_frame_total"]:
				self.frame=0
			self.image=self.attack_image.subsurface((self.zombie_data["attack_image_width"]*self.frame+self.zombie_data["attack_margin_left_cut"],0,self.zombie_data["attack_image_width"]-self.zombie_data["attack_margin_left_cut"],self.zombie_data["attack_image_height"]))
			self.image=self.image.copy()
			self.auto_scale()


		if self.float_x == -1 or self.float_y==-1:
			return False

		#游戏结束，僵尸走进房子
		if self.game_over_flag:
			offset_x=float(self.target[0]-self.rect.centerx)
			offset_y=float(self.target[1]-self.rect.centery)
			offset_x/=50
			offset_y/=50
			self.float_x+=offset_x
			self.float_y+=offset_y
			self.rect.centerx=int(self.float_x)
			self.rect.centery=int(self.float_y)

			if abs(self.target[0]-self.rect.centerx) < 10 and abs(self.target[1]-self.rect.centery) < 10:
				self.settings.game_status=self.settings.STATUSGAMEOVER
				self.settings.game_status2=self.settings.UNHANDLED
				self.data.lose_music.play()
			
			return True

		#没有处于攻击状态的时候就可以移动
		if self.isAttack==False:
			self.float_x-=self.speed
			self.rect.centerx=int(self.float_x)
			#如果僵尸到达[y][0]
			target_x,null=self.data.map[0][0]
			if self.rect.centerx >= (target_x-10) and self.rect.centerx <= (target_x-10):
				self.game_over_flag=True

		#检查前方是否碰到英雄，如果碰到，就攻击
		flag=False	#标记  如果碰到英雄 值为True 否则为 False
		collide_hero=0
		for component in self.data.components.sprites():
			if component.class_name == "Hero":
				if component.rows == self.rows:
					margin_right=component.hero_data["margin_right"]
					right=component.rect.right
					actual_right=right-margin_right
					sub=self.rect.left-actual_right
					#如果sub大于小于一定值 说明发生碰撞了
					if sub >= -100 and sub <= 10:
						#标记正在攻击
						self.status=self.settings.ATTACK
						if self.isAttack==False:
							self.frame=0
						self.isAttack=True
						flag=True
						collide_hero=component
		#如果flag为false，说明无碰撞，切换到行走模式
		if flag == False:
			self.status=self.settings.WALK
			if self.isAttack==True:
				self.frame=0
			self.isAttack=False

		#如果正在攻击
		if self.isAttack:
			if self.settings.ticks-self.last_attack_ticks >= self.zombie_data["attack_ticks"]:
				self.last_attack_ticks=self.settings.ticks
				collide_hero.health-=self.zombie_data["attack_power"]
				self.attack_music.play()
				#如果目标英雄的生命值小于0 删除英雄
				if collide_hero.health <= 0:
					self.data.hero_map[collide_hero.rows][collide_hero.columns]=False
					self.data.components.remove(collide_hero)

class HeroSelection(Component):
	def __init__(self,data,settings,hero_data):
		super().__init__(data,settings)
		self.class_name="HeroSelection"
		self.data=data
		self.settings=settings
		self.hero_data=hero_data
		self.rect=pygame.Rect(0,0,self.hero_data["width"],self.hero_data["height"])
		self.image=self.hero_data["icon"]
		self.image_back=self.image.copy()
		self.isMouseEntered=False
		self.mouseEnterStatus=0
		self.isListenMouseEvent=True
		self.isListenMouseMotionEvent=True
		self.isSelected=False

	def handleMouseMotionEvent(self,event):
		#检查是否在rect内
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		if self.check_point_in_rect(point,self.rect):
			self.isMouseEntered=True

			#检查是否已经播放进入音乐
			if self.mouseEnterStatus == 0:
				self.data.mouse_entered_music.play()
				self.mouseEnterStatus =1
				centerx=self.rect.centerx
				centery=self.rect.centery
				self.rect.width+=10
				self.rect.height+=10
				self.rect.centery=centery
				self.rect.centerx=centerx
				self.auto_scale()
		elif self.mouseEnterStatus == 1:
			self.isMouseEntered=False
			self.mouseEnterStatus =0
			centerx=self.rect.centerx
			centery=self.rect.centery
			self.rect.width-=10
			self.rect.height-=10
			self.rect.centery=centery
			self.rect.centerx=centerx
			self.image=self.image_back.copy()
			self.auto_scale()

	def handleMouseEvent(self,event):
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		if self.check_point_in_rect(point,self.rect) and event.button == 1 and event.type == pygame.MOUSEBUTTONDOWN:
			self.data.button_clicked_music.play()
			#判断是否选中
			if self.isSelected:
				self.isSelected=False
				self.image=self.hero_data["icon"]
				self.image_back=self.image.copy()
				self.auto_scale()
			else:
				self.isSelected=True
				self.image=self.hero_data["icon_selected"]
				self.image_back=self.image.copy()
				self.auto_scale()


class SelectionDone(Component):
	def __init__(self,data,settings):
		super().__init__(data,settings)
		self.class_name="SelectionDone"
		self.data=data
		self.settings=settings
		self.isMouseEntered=False
		self.mouseEnterStatus=0
		self.image=self.data.selection_done_image
		self.image_back=self.image.copy()
		self.isListenMouseEvent=True
		self.isListenMouseMotionEvent=True

	def handleMouseMotionEvent(self,event):
		
		#检查是否在rect内
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		if self.check_point_in_rect(point,self.rect):
			self.isMouseEntered=True
			#检查是否已经播放进入音乐
			if self.mouseEnterStatus == 0:
				self.data.mouse_entered_music.play()
				self.mouseEnterStatus =1
				centerx=self.rect.centerx
				centery=self.rect.centery
				self.rect.width+=10
				self.rect.height+=10
				self.rect.centery=centery
				self.rect.centerx=centerx
				self.auto_scale()
		elif self.mouseEnterStatus == 1:
			self.isMouseEntered=False
			self.mouseEnterStatus =0
			centerx=self.rect.centerx
			centery=self.rect.centery
			self.rect.width-=10
			self.rect.height-=10
			self.rect.centery=centery
			self.rect.centerx=centerx
			self.image=self.image_back.copy()
			self.auto_scale()
		

	def handleMouseEvent(self,event):
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		if self.check_point_in_rect(point,self.rect) and event.button == 1 and event.type == pygame.MOUSEBUTTONDOWN:
			

			#计算已选择英雄
			total=0 
			self.data.selected_hero=[]
			for component in self.data.components:
				if component.class_name == "HeroSelection":
					if component.isSelected:
						total+=1
						self.data.selected_hero.append(component.hero_data["id"])

			if total != self.settings.max_allowed_hero:
				self.data.error_music.play()
			else:
				self.data.button_clicked_music.play()
				self.settings.game_status=self.settings.STATUSCAMERAMOVETOLEFT
				self.settings.game_status2=self.settings.UNHANDLED

				#清除其它组件
				for component in self.data.components.copy():
					if component.class_name != "Zombie":
						self.data.components.remove(component)

				#随机播放背景音乐
				rand=random.randint(0,5)
				pygame.mixer.music.stop()
				if rand == 0:
					pygame.mixer.music.load(self.data.game0_music_path)
				elif rand == 1:
					pygame.mixer.music.load(self.data.game1_music_path)
				elif rand == 2:
					pygame.mixer.music.load(self.data.game2_music_path)
				elif rand == 3:
					pygame.mixer.music.load(self.data.game3_music_path)
				else :
					pygame.mixer.music.load(self.data.game4_music_path)
				pygame.mixer.music.play(-1,0.0)

class Hero(Component):
	def __init__(self,data,settings,hero_data):
		super().__init__(data,settings)
		self.class_name="Hero"
		self.data=data
		self.settings=settings
		self.hero_data=hero_data
		self.status=self.settings.STAND
		self.frame=0
		self.rows=-1
		self.columns=-1
		self.health=self.hero_data["health"]
		self.rect=pygame.Rect(0,0,self.hero_data["width"],self.hero_data["height"])
		self.last_ticks=self.settings.ticks
		self.stand_image=self.hero_data["stand_image"]
		self.attack_image=self.hero_data["attack_image"]
		self.attack_music=self.hero_data["attack_music"]
		self.isAttack=False
		self.last_attack_ticks=0
		self.isSelected=False
	def update(self):
		#绘制图像

		if self.status == self.settings.STAND and (self.settings.ticks-self.last_ticks) >= 100:
			self.last_ticks=self.settings.ticks
			self.frame+=1
			if self.frame >= self.hero_data["stand_frame_total"]:
				self.frame=0
			self.image=self.stand_image.subsurface((self.hero_data["stand_image_width"]*self.frame,0,self.hero_data["stand_image_width"],self.hero_data["stand_image_height"]))
			self.image=self.image.copy()
			self.rect.width=self.hero_data["stand_width"]
			self.rect.height=self.hero_data["stand_height"]
			self.auto_scale()
		elif self.status == self.settings.ATTACK and (self.settings.ticks-self.last_ticks) >= 100:
			self.last_ticks=self.settings.ticks
			self.frame+=1
			if self.frame >= self.hero_data["attack_frame_total"]:
				self.frame=0
			self.image=self.attack_image.subsurface((self.hero_data["attack_image_width"]*self.frame,0,self.hero_data["attack_image_width"],self.hero_data["attack_image_height"]))
			self.image=self.image.copy()
			self.rect.width=self.hero_data["attack_width"]
			self.rect.height=self.hero_data["attack_height"]
			self.auto_scale()

		if self.isSelected:
			return False


		#检查前方是否碰到僵尸，如果碰到，就攻击
		flag=False	#标记  如果碰到僵尸 值为True 否则为 False
		collide_zombie=0
		for component in self.data.components.sprites():
			if component.class_name == "Zombie":
				if component.rows == self.rows:
					centerx=self.rect.centerx
					left=component.rect.left
					offset=left-centerx
					#如果offset大于0 && 小于该英雄攻击范围 说明可以攻击
					if offset >= -100 and offset <= self.hero_data["attack_range"]:
						#标记正在攻击
						self.status=self.settings.ATTACK
						if self.isAttack==False:
							self.frame=0
						self.isAttack=True
						flag=True
						collide_zombie=component
		#如果flag为false，说明攻击范围内无僵尸，切换到站立模式
		if flag == False:
			self.status=self.settings.STAND
			if self.isAttack==True:
				self.frame=0
			self.isAttack=False

		#如果正在攻击
		if self.isAttack:
			if self.settings.ticks-self.last_attack_ticks >= self.hero_data["attack_ticks"]:
				self.last_attack_ticks=self.settings.ticks
				collide_zombie.health-=self.hero_data["attack_power"]
				self.attack_music.play()
				#如果目标僵尸的生命值小于0 删除僵尸
				if collide_zombie.health <= 0:
					self.data.components.remove(collide_zombie)

class HeroSwitch(Component):
	def __init__(self,data,settings,hero_data):
		super().__init__(data,settings)
		self.class_name="HeroSwitch"
		self.data=data
		self.settings=settings
		self.hero_data=hero_data
		self.isMouseEntered=False
		self.rect=pygame.Rect(0,0,self.hero_data["width"],self.hero_data["height"])
		self.image=self.hero_data["icon_card"]
		self.isMouseEntered=False
		self.isListenMouseEvent=True
		self.isListenMouseMotionEvent=True
		self.isSelected=False
		self.last_ticks=0
		self.isCool=False


	def handleMouseMotionEvent(self,event):
		#检查是否在rect内
		x,y=pygame.mouse.get_pos()
		point=Point(x,y)
		self.isMouseEntered=self.check_point_in_rect(point,self.rect)	

	def handleMouseEvent(self,event):

		if self.isMouseEntered and event.button == 1 and event.type == pygame.MOUSEBUTTONDOWN:
			self.data.button_clicked_music.play()
			if self.settings.ticks - self.last_ticks >= self.hero_data["cooldown_time"]:
				self.isSelected=True
				self.heroObj=Hero(self.data,self.settings,self.hero_data)
				self.heroObj.isSelected=True
				self.heroObj.rows=-1
				x,y=pygame.mouse.get_pos()
				self.heroObj.rect.centerx=x
				self.heroObj.rect.centery=y
				self.data.components.add(self.heroObj)

		elif event.button == 1 and event.type == pygame.MOUSEBUTTONUP and self.isSelected == True:
			self.isSelected=False
			#查找距离最低的点放下
			min_array=[]
			min_value=999999.0
			min_pos=0,0
			min_rows=-1
			min_columns=-1
			for i in range(0,5):
				for j in range(0,9):
					x,y=self.data.map[i][j]
					length=math.sqrt((x-self.heroObj.rect.centerx)**2+(y-self.heroObj.rect.centery)**2)
					tmp={"len":length,"pos":self.data.map[i][j],"rows":i,"columns":j}
					min_array.append(tmp)
			if min_array:
				for i in range(len(min_array)):
					if min_array[i]["len"] < min_value:
						min_value=min_array[i]["len"]
						min_pos=(min_array[i]["pos"][0],min_array[i]["pos"][1])
						min_rows=min_array[i]["rows"]
						min_columns=min_array[i]["columns"]

			#检查对应坐标上是否有英雄
			if self.data.hero_map[min_rows][min_columns] == False and min_value <= 50:
				self.data.hero_map[min_rows][min_columns]=True
				self.heroObj.rect.centerx,self.heroObj.rect.centery=min_pos
				self.heroObj.isSelected=False
				self.heroObj.rows=min_rows
				self.heroObj.columns=min_columns
				self.last_ticks=self.settings.ticks

				self.image=pygame.Surface((10,10))
				self.auto_scale()
				self.isCool=True
			else:
				self.data.components.remove(self.heroObj)

		
	def update(self):
		if self.isSelected:
			x,y=pygame.mouse.get_pos()
			self.heroObj.rect.centerx=x
			self.heroObj.rect.centery=y
		if self.settings.ticks - self.last_ticks >= self.hero_data["cooldown_time"] and self.isCool == True:
			#大于冷却时间
			self.isCool=False
			self.image=self.hero_data["icon_card"]
			self.auto_scale()

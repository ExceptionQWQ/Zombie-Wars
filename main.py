import sys
import time
import random
import pygame
import game_functions as gf
from settings import Settings
from data import Data
from camera import Camera
from component import *



#运行游戏
def run_game(data,settings):

	FpsClock=pygame.time.Clock()
	while True:
		#写入背景
		data.screen_buff.blit(data.background_image,(0,0))
		#获取ticks
		settings.ticks=pygame.time.get_ticks()

		#检查事件
		gf.check_events(data,settings)

		#游戏状态处理
		gf.handle_game_status(data,settings)

		#绘制组件&刷新
		if settings.isPause == False:
			gf.draw_components(data,settings)

		#从相机中获取要显示的图像
		image=data.camera.get_screen_image()
		gf.update_screen(image)
		FpsClock.tick(settings.FPS)

#游戏初始化
def init():	
	#创建settings对象
	settings=Settings()

	#pygame初始化
	pygame.init()
	#设置屏幕大小
	screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
	#设置标题
	pygame.display.set_caption(settings.game_title)
	#设置初始背景
	start_image=pygame.image.load("images/start.png").convert_alpha()
	start_image=pygame.transform.smoothscale(start_image,(settings.screen_width,settings.screen_height))
	screen.blit(start_image,start_image.get_rect())
	pygame.display.update()

	#读取数据
	data = Data()

	#创建相机
	data.camera=Camera(data,settings)

	#创建屏幕缓冲区
	data.screen_buff=pygame.Surface((settings.screen_buff_width,settings.screen_buff_height)).convert_alpha()
	#写入背景
	data.screen_buff.blit(data.background_image,(0,0))

	#创建组件组，游戏中所有组件都会放在这里
	data.components=pygame.sprite.Group()
	
	#运行游戏
	run_game(data,settings)

#主函数
def main():
	init()
	run_game()


if __name__ == "__main__":
	main()


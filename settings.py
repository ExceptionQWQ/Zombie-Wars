import pygame

class Settings():
	def __init__(self):
		self.game_title="Zombie Wars"
		self.screen_width=1000
		self.screen_height=600

		self.screen_buff_width=1400
		self.screen_buff_height=600

		self.FPS=120


		#游戏是否被暂停
		self.isPause=False

		#游戏状态
		self.STATUSMENU=0              #菜单
		self.STATUSCAMERAMOVETORIGHT=1 #相机移动到最右边
		self.STATUSCAMERAMOVETOLEFT=2  #相机移动到最左边
		self.STATUSNONE=3              #执行空操作
		self.STATUSGAMING=4			   #游戏中
		self.STATUSGAMEOVER=5          #游戏结束

		#游戏状态2
		self.HANDLED=0      #已经处理
		self.UNHANDLED=1    #未经处理

		self.game_status=self.STATUSMENU
		self.game_status2=self.UNHANDLED

		#僵尸状态
		self.STAND=0
		self.WALK=1
		self.ATTACK=2

	


		#游戏从启动起到现在的时间(ms)
		self.ticks=0

		#最多选择英雄数量
		self.max_allowed_hero=5

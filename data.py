import pygame
import time
import json

class Data():
	def __init__(self):


		self.game_file={} #游戏存档
		try:
			file=open("data/game_file.dat","r")
			self.game_file=json.load(file)
			if self.game_file["level"] == 0:
				1/0
			file.close()
		except:
			#重新建立存档
			print("重新建立存档")
			self.game_file={"level":1}



		self.background_image=pygame.image.load("images/background.png").convert_alpha()	
		self.menu_begin_image=pygame.image.load("images/begin.png").convert_alpha()	
		self.selection_done_image=pygame.image.load("images/begin.png").convert_alpha()	
		self.void_image=pygame.image.load("images/void.png").convert_alpha()	



		#各种僵尸数据
		self.zombie_data=[{"id":0, 
						   "name":"zombie0", 
						   "health":100,                                      #生命值
						   "attack_power":10,								    #攻击力
						   "width":90,    									#实际显示宽
						   "height":130,										#实际显示高
						   "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						   "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						   "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						   "margin_right":50,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						   "stand_margin_left_cut":20,
						   "walk_margin_left_cut":50,
						   "attack_margin_left_cut":50,
		                   "stand_image_width":166,							#站立源图像宽
		                   "stand_image_height":144,							#站立源图像高
		                   "stand_frame_total":22,								#站立源图像总帧数
		                   "stand_image":pygame.image.load("images/zombie0_stand.png").convert_alpha(),		#站立源图像路径
		                   "walk_image_width":166,							#站立源图像宽
		                   "walk_image_height":144,							#站立源图像高
		                   "walk_frame_total":22,								#站立源图像总帧数
		                   "walk_image":pygame.image.load("images/zombie0_walk.png").convert_alpha(),		#站立源图像路径
		                   "attack_image_width":166,							#攻击源图像宽
		                   "attack_image_height":144,							#攻击源图像高
		                   "attack_frame_total":22,							#攻击源图像总帧数
		                   "attack_image":pygame.image.load("images/zombie0_attack.png").convert_alpha(),     #攻击源图像路径
		                   "attack_ticks":1000,                               #攻击ticks间隔
		                   "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                   "move_speed":0.1,										#移动速度
						  },
						  {"id":1, 
						   "name":"zombie1", 
						   "health":150,                                      #生命值
						   "attack_power":10,								    #攻击力
						   "width":90,    									#实际显示宽
						   "height":130,										#实际显示高
						   "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						   "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						   "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						   "margin_right":50,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						   "stand_margin_left_cut":20,
						   "walk_margin_left_cut":50,
						   "attack_margin_left_cut":50,
		                   "stand_image_width":166,							#站立源图像宽
		                   "stand_image_height":144,							#站立源图像高
		                   "stand_frame_total":8,								#站立源图像总帧数
		                   "stand_image":pygame.image.load("images/zombie1_stand.png").convert_alpha(),		#站立源图像路径
		                   "walk_image_width":166,							#站立源图像宽
		                   "walk_image_height":144,							#站立源图像高
		                   "walk_frame_total":21,								#站立源图像总帧数
		                   "walk_image":pygame.image.load("images/zombie1_walk.png").convert_alpha(),		#站立源图像路径
		                   "attack_image_width":166,							#攻击源图像宽
		                   "attack_image_height":144,							#攻击源图像高
		                   "attack_frame_total":11,							#攻击源图像总帧数
		                   "attack_image":pygame.image.load("images/zombie1_attack.png").convert_alpha(),     #攻击源图像路径
		                   "attack_ticks":1000,                               #攻击ticks间隔
		                   "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                   "move_speed":0.1,										#移动速度
						  },
						  {"id":2, 
						   "name":"zombie2", 
						   "health":200,                                      #生命值
						   "attack_power":10,								    #攻击力
						   "width":90,    									#实际显示宽
						   "height":130,										#实际显示高
						   "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						   "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						   "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						   "margin_right":50,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						   "stand_margin_left_cut":20,
						   "walk_margin_left_cut":50,
						   "attack_margin_left_cut":50,
		                   "stand_image_width":166,							#站立源图像宽
		                   "stand_image_height":144,							#站立源图像高
		                   "stand_frame_total":6,								#站立源图像总帧数
		                   "stand_image":pygame.image.load("images/zombie2_stand.png").convert_alpha(),		#站立源图像路径
		                   "walk_image_width":166,							#站立源图像宽
		                   "walk_image_height":144,							#站立源图像高
		                   "walk_frame_total":15,								#站立源图像总帧数
		                   "walk_image":pygame.image.load("images/zombie2_walk.png").convert_alpha(),		#站立源图像路径
		                   "attack_image_width":166,							#攻击源图像宽
		                   "attack_image_height":144,							#攻击源图像高
		                   "attack_frame_total":11,							#攻击源图像总帧数
		                   "attack_image":pygame.image.load("images/zombie2_attack.png").convert_alpha(),     #攻击源图像路径
		                   "attack_ticks":1000,                               #攻击ticks间隔
		                   "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                   "move_speed":0.1,										#移动速度
						  },
		]


		#各种英雄数据
		self.hero_data=[{"id":0,                                            #id
						 "name":"Annie",                                    #名字
						 "icon":pygame.image.load("images/Annie_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Annie_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Annie_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":100,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":130,
						 "stand_height":160,
		                 "stand_image_width":675,							#站立源图像宽
		                 "stand_image_height":584,							#站立源图像高
		                 "stand_frame_total":1,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Annie_stand.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":130,
						 "attack_height":160,
		                 "attack_image_width":675,							#攻击源图像宽
		                 "attack_image_height":584,							#攻击源图像高
		                 "attack_frame_total":21,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Annie_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		                 {"id":1,                                            #id
						 "name":"Ashe",                                    #名字
						 "icon":pygame.image.load("images/Ashe_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Ashe_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Ashe_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":100,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":100,
						 "stand_height":130,
		                 "stand_image_width":405,							#站立源图像宽
		                 "stand_image_height":312,							#站立源图像高
		                 "stand_frame_total":1,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Ashe_attack.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":100,
						 "attack_height":130,
		                 "attack_image_width":405,							#攻击源图像宽
		                 "attack_image_height":312,							#攻击源图像高
		                 "attack_frame_total":18,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Ashe_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		                 {"id":2,                                            #id
						 "name":"Blitzcrank",                                    #名字
						 "icon":pygame.image.load("images/Blitzcrank_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Blitzcrank_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Blitzcrank_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":60,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":130,
						 "stand_height":140,
		                 "stand_image_width":520,							#站立源图像宽
		                 "stand_image_height":392,							#站立源图像高
		                 "stand_frame_total":1,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Blitzcrank_attack.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":130,
						 "attack_height":140,
		                 "attack_image_width":520,							#攻击源图像宽
		                 "attack_image_height":392,							#攻击源图像高
		                 "attack_frame_total":28,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Blitzcrank_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		                 {"id":3,                                            #id
						 "name":"Caitlyn",                                    #名字
						 "icon":pygame.image.load("images/Caitlyn_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Caitlyn_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Caitlyn_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":60,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":100,
						 "stand_height":140,
		                 "stand_image_width":221,							#站立源图像宽
		                 "stand_image_height":329,							#站立源图像高
		                 "stand_frame_total":1,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Caitlyn_attack.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":100,
						 "attack_height":140,
		                 "attack_image_width":221,							#攻击源图像宽
		                 "attack_image_height":329,							#攻击源图像高
		                 "attack_frame_total":14,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Caitlyn_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		                 {"id":4,                                            #id
						 "name":"Corki",                                    #名字
						 "icon":pygame.image.load("images/Corki_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Corki_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Corki_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":60,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":140,
						 "stand_height":140,
		                 "stand_image_width":250,							#站立源图像宽
		                 "stand_image_height":200,							#站立源图像高
		                 "stand_frame_total":4,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Corki_stand.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":140,
						 "attack_height":140,
		                 "attack_image_width":250,							#攻击源图像宽
		                 "attack_image_height":200,							#攻击源图像高
		                 "attack_frame_total":4,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Corki_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		                 {"id":5,                                            #id
						 "name":"Darius",                                    #名字
						 "icon":pygame.image.load("images/Darius_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Darius_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Darius_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":60,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":140,
						 "stand_height":140,
		                 "stand_image_width":250,							#站立源图像宽
		                 "stand_image_height":200,							#站立源图像高
		                 "stand_frame_total":4,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Darius_stand.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":140,
						 "attack_height":140,
		                 "attack_image_width":250,							#攻击源图像宽
		                 "attack_image_height":200,							#攻击源图像高
		                 "attack_frame_total":4,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Darius_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		                 {"id":6,                                            #id
						 "name":"Diana",                                    #名字
						 "icon":pygame.image.load("images/Diana_icon.png").convert_alpha(),				#缩略图
						 "icon_selected":pygame.image.load("images/Diana_selected.png").convert_alpha(),  #选中图标
						 "icon_card":pygame.image.load("images/Diana_card.png").convert_alpha(),          #卡片图标
						 "health":100,                                      #生命值
						 "attack_power":10,								    #攻击力
						 "width":80,    									#英雄缩略图宽
						 "height":90,										#英雄缩略图高
						 "margin_top":10,									#碰撞检测，碰撞rect.top到英雄实际rect.top的距离
						 "margin_bottom":10,								#碰撞检测，碰撞rect.bottom到英雄实际rect.bottom的距离
						 "margin_left":10,									#碰撞检测，碰撞rect.left到英雄实际rect.left的距离
						 "margin_right":60,									#碰撞检测，碰撞rect.right到英雄实际rect.right的距离
						 "stand_width":140,
						 "stand_height":140,
		                 "stand_image_width":250,							#站立源图像宽
		                 "stand_image_height":200,							#站立源图像高
		                 "stand_frame_total":4,								#站立源图像总帧数
		                 "stand_image":pygame.image.load("images/Diana_stand.png").convert_alpha(),		#站立源图像路径
		                 "attack_width":140,
						 "attack_height":140,
		                 "attack_image_width":250,							#攻击源图像宽
		                 "attack_image_height":200,							#攻击源图像高
		                 "attack_frame_total":4,							#攻击源图像总帧数
		                 "attack_image":pygame.image.load("images/Diana_attack.png").convert_alpha(),     #攻击源图像路径
		                 "cooldown_time":10000,								#冷却时间
		                 "attack_ticks":1000,                               #攻击ticks间隔
		                 "attack_range":60 ,								#攻击范围
		                 "attack_music":pygame.mixer.Sound("audio/seedlift.ogg"),			#攻击音效路径
		                 },	
		]


		self.menu_music_path="audio/crazydave.mp3"	
		self.choose_hero_music_path="audio/chooseyourseeds.mp3"		
		self.game0_music_path="audio/game0.mp3"
		self.game1_music_path="audio/game1.mp3"
		self.game2_music_path="audio/game2.mp3"
		self.game3_music_path="audio/game3.mp3"
		self.game4_music_path="audio/game4.mp3"
		


		self.mouse_entered_music=pygame.mixer.Sound("audio/puff.ogg")   
		self.button_clicked_music=pygame.mixer.Sound("audio/buttonclick.ogg")
		self.error_music=pygame.mixer.Sound("audio/error.ogg")
		self.chomp_music=pygame.mixer.Sound("audio/chompsoft.ogg")
		self.lose_music=pygame.mixer.Sound("audio/losemusic.ogg")
		self.awooga_music=pygame.mixer.Sound("audio/awooga.ogg")
		self.win_music=pygame.mixer.Sound("audio/winmusic.ogg")

		#地图坐标对应像素
		#              0	     1         2         3         4         5         6         7         8        屏幕外
		self.map=[[(300,110),(375,110),(450,110),(535,110),(615,110),(700,110),(777,110),(855,110),(940,110),(1040,110)], #0
				  [(300,210),(375,210),(450,210),(535,210),(615,210),(700,210),(777,210),(855,210),(940,210),(1040,210)], #1
				  [(300,310),(375,310),(450,310),(535,310),(615,310),(700,310),(777,310),(855,310),(940,310),(1040,310)], #2
				  [(300,410),(375,410),(450,410),(535,410),(615,410),(700,410),(777,410),(855,410),(940,410),(1040,410)], #3
				  [(300,510),(375,510),(450,510),(535,510),(615,510),(700,510),(777,510),(855,510),(940,510),(1040,510)]  #4
		]
		#地图对应坐标是否有英雄
		self.hero_map=[[False,False,False,False,False,False,False,False,False],
					   [False,False,False,False,False,False,False,False,False],
					   [False,False,False,False,False,False,False,False,False],
					   [False,False,False,False,False,False,False,False,False],
					   [False,False,False,False,False,False,False,False,False]
		]

		self.target=(140,380)
		



		self.is_lua_end=False
		self.is_execute_sleep=False
		self.last_lua_ticks=0
		self.current_lua=0
		self.pc=0
		self.r0=0
		#关卡脚本
		self.level_lua=[[{"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":12000},   
						 {"function":"awooga","r0":0},	
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},  
						 {"function":"wait_for_win"},		   
						],
						#第二关
						[{"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"awooga","r0":0},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":2000},  
						 {"function":"wait_for_win"},		   
						],
						#第三关
						[{"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":8000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"awooga","r0":0},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":2000},  
						 {"function":"wait_for_win"},		   
						],
						#第四关
						[{"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":8000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"awooga","r0":0},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},  
						 {"function":"wait_for_win"},		   
						],
						#第五关
						[{"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":8000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"awooga","r0":2},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},  
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":16000},   
						 {"function":"zombie","r0":0},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":4000},   
						 {"function":"awooga","r0":2},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":1},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},  
						 {"function":"wait_for_win"},		   
						],
						#第六关
						[{"function":"sleep","r0":4000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":8000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"awooga","r0":2},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},  
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"awooga","r0":2},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000}, 
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"awooga","r0":2},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},  
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"awooga","r0":2},	
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},   
						 {"function":"zombie","r0":2},           
						 {"function":"sleep","r0":2000},  
						 {"function":"wait_for_win"},		   
						],
		]



	#保存数据
	def save(self):
		try:
			file=open("data/game_file.dat","w")
			json.dump(self.game_file,file)
			file.close()
		except:
			print("保存数据失败")

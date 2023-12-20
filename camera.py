import pygame

class Camera():
	def __init__(self,data,settings):
		self.data=data
		self.settings=settings
		self.rect=pygame.Rect((0,0,settings.screen_width,settings.screen_height))
		

	def get_screen_image(self):
		return self.data.screen_buff.subsurface(self.rect)
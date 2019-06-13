#IMPORTS======================================================================
import os
import sys
import time

import pygame
from pygame.locals import *

import socket
import pickle

import linecache
import inspect
#=============================================================================



#VARIABLES====================================================================
window_size = [960, 540]
loop_main = True
window = pygame.display.set_mode(window_size, RESIZABLE)

#UI Element is a dictionary of items: {name, ID?, Position, Parent, Children, Type, Other?} <-INACCURATE
panel_main_menu = {"name": "menu", "ID": 0, "dimensions_1": [0, 0], "dimensions_2": [100, 100], "parent": None, "children": [], "type": 0}
panel_menu_2 = {"name": "menu2", "ID": 1, "dimensions_1": [0, 75], "dimensions_2": [100, 100], "parent": None, "children": [], "type": 0}
'''TYPES INDEX:
0 = Panel
1 = ???
2 = profit
'''
#Naming inherets from parent - each item will start with its type, followed by its scene, followed by its parent, followed by itself
scene_main = [panel_main_menu, panel_menu_2]

scenes = [scene_main]


test_texture = pygame.image.load("test_texture.png")

panel_tile_dimensions = [4, 4]
panel_background_texture = pygame.image.load("panel_background.png")
panel_border_top_texture = pygame.image.load("panel_border_top.png")
panel_border_right_texture = pygame.image.load("panel_border_right.png")
panel_border_left_texture = pygame.image.load("panel_border_left.png")
panel_border_bottom_texture = pygame.image.load("panel_border_bottom.png")
panel_corner_top_right_texture = pygame.image.load("panel_corner_top_right.png")
panel_corner_top_left_texture = pygame.image.load("panel_corner_top_left.png")
panel_corner_bottom_right_texture = pygame.image.load("panel_corner_bottom_right.png")
panel_corner_bottom_left_texture = pygame.image.load("panel_corner_bottom_left.png")
#=============================================================================



#FUNCTIONS====================================================================
def _init():
	pygame.init()
	_window_render(960, 540, False)

def _window_render(new_width, new_height, window_resize):
	global window_size
	if window_resize == True:
		window_size = [new_width, new_height]
		print("New size: " + str(window_size))
		#other resize info/stuff
	window = pygame.display.set_mode(window_size, RESIZABLE)
	_scene_render(scene_main)

def _scene_render(current_scene):
	x = 0
	while x < len(scene_main):
		_element_render(scene_main[x])
		x += 1
	pygame.display.update()

def _element_render(element):
	if element["type"] == 0:
		actual_dimensions_1 = [round((element["dimensions_1"][0] / 100) * window_size[0]), round((element["dimensions_1"][1] / 100) * window_size[1])]
		actual_dimensions_2 = [round((element["dimensions_2"][0] / 100) * window_size[0]), round((element["dimensions_2"][1] / 100) * window_size[1])]
		panel_width = actual_dimensions_2[0] - actual_dimensions_1[0]
		panel_height = actual_dimensions_2[1] - actual_dimensions_1[1]
		tiles_wide = panel_width / panel_tile_dimensions[0]
		tiles_wide = round(tiles_wide)
		tiles_high = panel_height / panel_tile_dimensions[1]
		tiles_high = round(tiles_high)
		tiles_offset = [(round(actual_dimensions_1[0] / 16) * panel_tile_dimensions[0]), (round(actual_dimensions_1[1] / 16) * panel_tile_dimensions[1])]
		print("actual_dimensions_1: " + str(actual_dimensions_1))
		print("actual_dimensions_2: " + str(actual_dimensions_2))
		print("panel_width: " + str(panel_width))
		print("panel_height: " + str(panel_height))
		print("Tiles Wide: " + str(tiles_wide))
		print("Tiles High: " + str(tiles_high))

		y = 0
		while y < tiles_high:
			x = 0
			while x < tiles_wide:
				print("X: " + str(x) + " Y: " + str(y))
				if x == 0:
					if y == 0:
						window.blit(panel_corner_top_left_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
					elif y == tiles_high - 1:
						window.blit(panel_corner_bottom_left_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
					else:
						window.blit(panel_border_left_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
				elif x == tiles_wide - 1:
					if y == 0:
						window.blit(panel_corner_top_right_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
					elif y == tiles_high - 1:
						window.blit(panel_corner_bottom_right_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
					else:
						window.blit(panel_border_right_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
				elif y == 0:
					window.blit(panel_border_top_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
				elif y == tiles_high - 1:
					window.blit(panel_border_bottom_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
				else:
					window.blit(panel_background_texture, (x * panel_tile_dimensions[0] + tiles_offset[0], y * panel_tile_dimensions[1] + tiles_offset[1]))
				x += 1
			y += 1

	else:
		print("ERROR! INVALID ELEMENT TYPE!")
#=============================================================================



#MAIN=========================================================================
_init()
while loop_main:
	for event in pygame.event.get():
		if event.type == pygame.VIDEORESIZE:
			window_resize = True
			_window_render(event.w, event.h, True)




	pygame.time.Clock().tick(30)
	#print("Tick")
	if pygame.time.get_ticks() >= 60000:
		print("Ticks: " + str(pygame.time.get_ticks()))
		loop_main = False
#=============================================================================

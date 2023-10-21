import pygame
import math
import copy
pygame.init()


class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]

	FONT = pygame.font.SysFont('comicsans', 30)
	CONTROL_FONT = pygame.font.SysFont('comicsans', 20)
	LARGE_FONT = pygame.font.SysFont('comicsans', 40)
	NUMBER_FONT = pygame.font.SysFont('comicsans', 10)

	SIDE_PAD = 100
	TOP_PAD = 150
	BOTTOM_PAD = 50

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")
		self.set_list(lst)
		self.prev_lst = copy.deepcopy(lst)

	def set_list(self, lst):
		self.lst = lst
		self.prev_lst = copy.deepcopy(lst)
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending):
	draw_info.window.fill(draw_info.BACKGROUND_COLOR)

	title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
	draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))

	controls = draw_info.CONTROL_FONT.render("N - New List | R - Reset List | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
	draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 55))

	sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
	draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 75))



	draw_list(draw_info)
	pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
	lst = draw_info.lst

	if clear_bg:
		clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
						draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
		pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.GRADIENTS[i % 3]

		if i in color_positions:
			color = color_positions[i]

		rect_obj = pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
		text_surface_object = draw_info.NUMBER_FONT.render(str(val), True, draw_info.BLACK)
		text_rect = text_surface_object.get_rect(center=rect_obj.center)
		draw_info.window.blit(text_surface_object, text_rect)


	if clear_bg:
		pygame.display.update()
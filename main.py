import pygame
import random
import copy
import pygame_visualizer as pv
pygame.init()
from algorithms import bubble_sort as bsort
from algorithms import insertion_sort as isort


def generate_starting_list(n, min_val, max_val):
	lst = []

	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)
	return lst


def main():
	run = True

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = pv.DrawInformation(1000,750, lst)
	sorting = False
	ascending = True

	sorting_algorithm = bsort.bubble_sort
	sorting_algo_name = "Bubble Sort"
	sorting_algorithm_generator = None
	sorted = False

	while run:
		#clock.tick(60)

		if sorting:
			try:
				next(sorting_algorithm_generator)
			except StopIteration:
				sorting = False
				sorted = True

		else:
			pv.draw(draw_info, sorting_algo_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				sorted = False
				lst = copy.deepcopy(draw_info.prev_lst)
				print(lst)
				print(draw_info.prev_lst)
				draw_info.set_list(lst)
				sorting = False
			elif event.key == pygame.K_n:
				sorted = False
				lst = generate_starting_list(random.randint(2,50), min_val, max_val)
				draw_info.set_list(lst)
				sorting = False
			elif event.key == pygame.K_SPACE and sorting == False and sorted == False:
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False
			elif event.key == pygame.K_i and not sorting:
				sorting_algorithm = isort.insertion_sort
				sorting_algo_name = "Insertion Sort"
			elif event.key == pygame.K_b and not sorting:
				sorting_algorithm = bsort.bubble_sort
				sorting_algo_name = "Bubble Sort"


	pygame.quit()


if __name__ == "__main__":
	main()
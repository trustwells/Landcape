#Trust Wells
import numpy as np
import random
import time
import os
import sys

#Initializing Variables
mat = np.full((33, 33), 0)
size = 33
depth = 0
num_seed = int(sys.argv[1])
random.seed(num_seed)
magnitude = int(sys.argv[2])
offset = 0

mat[0][0] = random.randint(0,100)
mat[32][32] = random.randint(0,100)
mat[0][32] = random.randint(0,100)
mat[32][0] = random.randint(0,100)

def print_mat(mat):
	for i in range(33):
		for j in range(33):		
			if (mat[i][j] <= 25):
				print("\u001b[37;44m~", end="")
			elif (mat[i][j] > 25) and (mat[i][j] <= 50):
				print("\u001b[37;43m^", end="")
			elif (mat[i][j] > 50) and (mat[i][j] <= 75):
				print("\u001b[37;42m.", end="")
			else:
				print("\u001b[37;47m.", end="")
		print("\u001b[0;0m")
	print("\u001b[0;0m")

def recur(tp_left, tp_right, bot_left, bot_right, depth, magnitude):
	if (depth > 5):
		return
	
	#This takes the magnitude the user enters and divides by the magnitude which is affected by the depth when
	#it's greater than zero because you can't divide by zero.
	if (depth > 0):
		magnitude *= depth
		offset = random.randint(-30//magnitude,30//magnitude)
		offset2 = random.randint(-30//magnitude,30//magnitude)
		offset3 = random.randint(-30//magnitude,30//magnitude)
		offset4 = random.randint(-30//magnitude,30//magnitude)
		offset5 = random.randint(-30//magnitude,30//magnitude)
		
		
	else:
		offset5 =  random.randint(-30,30) 
		offset4 =  random.randint(-30,30) 
		offset3 =  random.randint(-30,30) 
		offset2 = random.randint(-30,30) 
		offset = random.randint(-30,30)

	mid_x = (tp_left[1]+tp_right[1]) // 2
	mid_y = (tp_right[0]+bot_right[0]) // 2
	#Setting the center of the board or recursion it's on
	mat[(tp_right[0]+bot_right[0]) // 2][(tp_left[1]+tp_right[1]) // 2] = ((mat[tp_left[0]][tp_left[1]] + mat[tp_right[0]][tp_right[1]] + mat[bot_left[0]][bot_left[1]] + mat[bot_right[0]][bot_right[1]]) // 4) + offset
	#Setting the top middle, then left middle, then right middle, then bottom middle.
	#Top Middle
	mat[(tp_right[0]+tp_left[0]) // 2][(tp_left[1]+tp_right[1]) // 2] = ((mat[(tp_right[0]+bot_right[0]) // 2][(tp_left[1]+tp_right[1]) // 2] + mat[tp_left[0]][tp_left[1]] + mat[tp_right[0]][tp_right[1]]) // 3) + offset2
	#Left Middle
	mat[(tp_left[0]+bot_left[0]) // 2][(tp_left[1]+bot_left[1]) // 2] = ((mat[(tp_right[0]+bot_right[0]) // 2][(tp_left[1]+tp_right[1]) // 2] + mat[tp_left[0]][tp_left[1]] + mat[bot_left[0]][bot_left[1]]) // 3) + offset3
	#Right Middle
	mat[(tp_right[0]+bot_right[0]) // 2][(tp_right[1]+bot_right[1]) // 2] = ((mat[(tp_right[0]+bot_right[0]) // 2][(tp_left[1]+tp_right[1]) // 2] + mat[tp_right[0]][tp_right[1]] + mat[bot_right[0]][bot_right[1]]) // 3) + offset4
	#Bottom Middle
	mat[(bot_right[0]+bot_left[0]) // 2][(bot_left[1]+bot_right[1]) // 2] = ((mat[(tp_right[0]+bot_right[0]) // 2][(tp_left[1]+tp_right[1]) // 2] + mat[bot_left[0]][bot_left[1]] + mat[bot_right[0]][bot_right[1]]) // 3) + offset5

	time.sleep(.01)
	os.system("cls||clear")
	print_mat(mat)
	#Recursion statements
	#We need 4 of them

	#Top Left Quadrant
	recur((tp_left[0],tp_left[1]), (tp_right[0],mid_x), (mid_y, bot_left[1]), (mid_y, mid_x), depth + 1, magnitude)
	#Top Right
	recur((tp_left[0],mid_x), (tp_right[0], tp_right[1]), (mid_y, mid_x), (mid_y, tp_right[1]), depth + 1, magnitude)
	#Bottom Left
	recur((mid_y, tp_left[1]), (mid_y, mid_x), (bot_left[0], bot_left[1]), (bot_left[0], mid_x), depth + 1, magnitude)	
	#Bottom Right
	recur((mid_y, mid_x), (mid_y, tp_right[1]), (bot_left[0], mid_x), (bot_right[0], bot_right[1]), depth + 1, magnitude)	

recur((0,0), (0, size - 1), (size - 1, 0), (size - 1, size - 1), depth, magnitude)






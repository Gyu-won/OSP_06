#!/usr/bin/python
from my_pkg.conversion import input1_data
from my_pkg.set import input2_data

while True:
	num = int(input('Select menu: 1)conversion 2)union/intersection 3)exit  ? '))
	if num == 1:
		input1_data()
	if num == 2:
		input2_data()
	if num == 3:
		print('exit the program...')
		break

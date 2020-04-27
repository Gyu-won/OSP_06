#!/usr/bin/python

def input2_data():
	list_1 = []
	list_2 = []
	s = input("1st list: ")
	s = s.lstrip('[')
	s = s.rstrip(']')
	list_1 = list(map(int, s.split(',')))
	s = input("2nd list: ")
	s = s.lstrip('[')
	s = s.rstrip(']')
	list_2 = list(map(int, s.split(',')))
	union(list_1, list_2)
	intersection(list_1, list_2)


def union(a, b):
	set1 = set(a)
	set2 = set(b)
	value = list(set1 | set2)
	print('=> union ', end='')
	print(value)


def intersection(a, b):
	set1 = set(a)
	set2 = set(b)
	value = list(set1 & set2)
	print('=> intersection ', end='')
	print(value)

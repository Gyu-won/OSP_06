#!/usr/bin/python

def input1_data():
	n = input('input binary number: ')
	dec(n)
	oct(n)
	hex(n)


def oct(num):
	n = 0
	for i in range(len(num)):
		n += ((int(((int(num)) % (10 ** (i+1))) / (10 ** i))) * (2 ** i))
	value = "{0:o}".format(n)
	print('=> OCT> ' + value)


def dec(num):
	value = 0
	for i in range(len(num)):
		value += ((int(((int(num)) % (10 ** (i+1))) / (10 ** i))) * (2 ** i))
	print('=> DEC> ' + (str(value)))


def hex(num):
	n = 0
	for i in range(len(num)):
		n += ((int(((int(num)) % (10 ** (i+1))) / (10 ** i))) * (2 ** i))
	value = "{0:X}".format(n)
	print('=> HEX> ' + value)


if __name__ == '__main__':
	print("메인함수 실행")	

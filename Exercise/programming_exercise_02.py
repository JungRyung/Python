#!/usr/bin/python3
import math as m

def is_ture(X,Y):
	if 5 <= m.log10(m.pow(X,Y)) <= 10:
		return True
	else:
		return False

if __name__ == "__main__":
	X = float(input('input float X :'))
	Y = float(input('input float Y :'))
	result = is_ture(X,Y)
	print('result = ',result)

#!/usr/bin/python3
import math as m

def calculate(X):
	return m.sqrt((X-1)*m.pow((X-3),2)*m.pow((X-5),3))

if __name__ == "__main__":
	X = float(input('input float X :'))
	result = calculate(X)
	print('result = ',result)
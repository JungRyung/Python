#!/usr/bin/python3
import math as m

def calculate(N):
	result=1
	for i in range(1,N+1):
		for k in range(i):
			result*=i
	return result
	
if __name__ == "__main__":
	N = int(input('input float N :'))
	result = calculate(N)
	print('result = ',result)

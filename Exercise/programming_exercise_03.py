#!/usr/bin/python3
import math as m

def combination(n,m):
	num1=1
	num2=1
	for i in range(m):
		num1 *= n-i
	for k in range(m):
		num2 *= k+1

	return num1/num2

if __name__ == "__main__":
	n = int(input('input float n :'))
	m = int(input('input float m :'))
	result = combination(n,m)
	print('result = ',result)

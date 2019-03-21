from random import choice
from numpy import matrix, array, dot, random

unit_step = lambda x: -1 if x < 0 else 1		#step function

def step_func(a):
	for i in range(0,len(a)):
		if a[i] < 0:
			a[i] = -1
		else:
			a[i] = 1
	return a

training_data = [
	(array([0,0,1,0,0,1,0,0,1]), array([-1,-1])),
	(array([0,0,0,0,0,0,1,1,1]), array([-1,1])),
	(array([0,1,0,0,1,1,0,1,0]), array([1,-1])),
	(array([0,0,0,1,1,1,0,1,0]), array([1,1])),
]
# print(training_data)

w = array([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]])	#weights는 1로 초기화
# print(w)

errors = []
eta = 1			#learning rate
n = 10			#epochs

for i in range(n):
	for x, expected in training_data:
		# print(x)
		# print(expected)
		result = dot(x,w.T)
		result = step_func(result)
		# print(result)
		error = expected - step_func(result)#step function까지 완료하면 actual output 완성
		# print(error)
		# errors.append(error)
		for j in range(0, len(w)):
			w[j] += eta * error[j] * x				#오차가 없고 트레이닝을 완료하면 w값은 바뀌지 않음

print(w)

y = array([1,0,0,0,0,0,1,1,1])
result = dot(y,w.T)
print(result)
result = step_func(result)
print(result)

# for x, _ in training_data:
# 	result = dot(x, w)
# 	print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
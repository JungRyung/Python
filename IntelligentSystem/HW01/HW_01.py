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
	#########0#########
	(array([0,0,0,0,0,0,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,0,0,
			0,0,0,0,0,0]), array([-1,-1,-1,-1])),
	#########1#########
	(array([0,0,0,0,0,0,
			0,0,1,0,0,0,
			0,1,1,0,0,0,
			0,0,1,0,0,0,
			0,0,1,0,0,0,
			0,0,1,0,0,0,
			0,1,1,1,0,0,
			0,0,0,0,0,0]), array([-1,-1,-1,1])),
	#########2#########
	(array([0,0,0,0,0,0,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,1,0,0,
			0,0,1,0,0,0,
			0,1,1,1,1,0,
			0,0,0,0,0,0]), array([-1,-1,1,-1])),
	#########3#########
	(array([0,0,0,0,0,0,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,1,0,0,
			0,0,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,0,0]), array([-1,-1,1,1])),
	#########4#########
	(array([0,0,0,0,0,0,
			0,0,0,1,1,0,
			0,0,1,0,1,0,
			0,0,1,0,1,0,
			0,1,0,0,1,0,
			0,1,1,1,1,1,
			0,0,0,0,1,0,
			0,0,0,0,0,0]), array([-1,1,-1,-1])),
	#########5#########
	(array([0,0,0,0,0,0,
			0,1,1,1,1,0,
			0,1,0,0,0,0,
			0,1,1,1,0,0,
			0,0,0,0,1,0,
			0,0,0,0,1,0,
			0,1,1,1,0,0,
			0,0,0,0,0,0]), array([-1,1,-1,1])),
	#########6#########
	(array([0,0,0,0,0,0,
			0,0,1,1,1,0,
			0,1,0,0,0,0,
			0,1,0,0,0,0,
			0,1,1,1,0,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,0,0]), array([-1,1,1,-1])),
	#########7#########
	(array([0,0,0,0,0,0,
			0,1,1,1,1,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,0,0,0]), array([-1,1,1,1])),
	#########8#########
	(array([0,0,0,0,0,0,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,0,0]), array([1,-1,-1,-1])),
	#########9#########
	(array([0,0,0,0,0,0,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,1,0,
			0,0,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,0,0,0]), array([1,-1,-1,1])),
]

######### weights ###########
w = array([[1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1],
			[1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1],
			[1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1],
			[1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1,
			1,1,1,1,1,1]])	#weights는 1로 초기화

####### training ########
errors = []
eta = 1			#learning rate
n = 20			#epochs

for i in range(n):

	print('-------epochs(%3d/%3d)-------'%(i+1,n))

	for x, expected in training_data:
		result = dot(x,w.T)
		result = step_func(result)
		error = expected - step_func(result)		#step function까지 완료하면 actual output 완성

		print('error',error)	

		for j in range(0, len(w)):
			w[j] += eta * error[j] * x				#오차가 없고 트레이닝을 완료하면 w값은 바뀌지 않음


print('weights : ', w)

####### test noise data ############
y = array([0,0,0,0,0,1,
			0,0,1,1,0,0,
			0,1,0,0,1,0,
			0,0,0,0,1,0,
			0,0,0,1,0,0,
			0,0,0,0,1,0,
			0,1,0,0,1,0,
			0,0,1,1,0,1])
result = dot(y,w.T)
result = step_func(result)

####### print test result ##########
print('result : ', result)
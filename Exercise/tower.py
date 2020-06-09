# def solution(heights):
# 	answer = []
# 	idx = 0
# 	tallest = 0
# 	num = 1
# 	for i in heights:
# 		if tallest >= i:
# 			answer.append(idx)
# 		else:
# 			answer.append(0)
# 			tallest = i
# 			idx = num
# 		num+=1
# 	return answer

def solution(heights):
	answer = []
	tower_stack = Stack()
	temp_stack = Stack()
	tower_stack.push(heights[0])
	answer.append(0)
	for idx in range(1:len(tower_stack)):
		while tower_stack.is_empty() != True:
			

	return answer

# Stack 클래스 정의 - python list 활용
class Stack(list):
    push = list.append    # Insert
                          # Delete - 내장 pop 메소드 활용
    def is_empty(self):   # 데이터가 없는지 확인
        if not self:
            return True
        else:
            return False

    def top(self):        # 최상단 데이터 확인
        return self[-1]

heights = [6,9,5,7,4]

answer = solution(heights)
print(answer)

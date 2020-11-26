#! /bin/zsh
def solution(prices):
    answer = []
    hist_stack = []
    # tmp_stack = []
    
    while len(prices):
        time = 0
        num = prices.pop()
        for i in range(len(hist_stack)):
            time += 1
            tmp_num = hist_stack[-i-1]
            if tmp_num < num:
                break
        # while len(hist_stack):
        #     time += 1
        #     tmp_num = hist_stack.pop()
        #     tmp_stack.append(tmp_num)
        #     if tmp_num<num:
        #         break
        # while len(tmp_stack):
        #     hist_stack.append(tmp_stack.pop())
        hist_stack.append(num)
        answer.insert(0,time)
    return answer

prices = [1,2,3,2,3]

answer = []

answer = solution(prices)

print(answer)
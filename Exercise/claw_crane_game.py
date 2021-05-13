def solution(board, moves):
    answer = 0
    stack = [[] for _ in range(len(board)+1)]
    basket = []
    
    # 인형스택에 나누어 담기
    for dolls in board:
        tmp = 1
        for doll in dolls:
            if doll!=0:
                stack[tmp].append(doll)
            tmp += 1
    
    for move in moves:
        if stack[move]:
            doll = stack[move].pop(0)
            if basket:
                if basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
            else:
                basket.append(doll)
    
    
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = solution(board, moves)
print(answer)

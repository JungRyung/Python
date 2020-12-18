import heapq

def solution(operations):
    queue = []
    for operation in operations:
        operator, num = operation.split(' ')
        if operator=='I':
            heapq.heappush(queue, int(num))
        elif num==-1:
            if(len(queue)!=0):
                queue.pop()
        else:
            if(len(queue)!=0):
                queue.pop(0)
    if len(queue)==0:
        return [0,0]
    else:
        return [queue[0],queue[-1]]
    return answer

operations = ["I 7","I 5","I -5","D -1"]
answer = solution(operations)
print(answer)
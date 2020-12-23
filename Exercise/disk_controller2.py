import heapq

def solution(jobs):
    jobs.sort()
    job_heap = []
    total = 0
    work = 0
    need_work = 0
    idx = 0

    while 1:
        while idx!=len(jobs):
            if jobs[idx][0] == work:
                temp1 = jobs[idx]
                heapq.heappush(job_heap, [temp1[1],temp1[0]])
                idx+=1
            else:
                break
        
        if need_work<=0 and len(job_heap):
            temp2 = heapq.heappop(job_heap)
            need_work = temp2[0]
            total += temp2[0]
        
        total += len(job_heap)
        need_work -= 1
        work += 1

        if len(job_heap)==0 and need_work==0 and idx==len(jobs):
            break
    answer = int(total/len(jobs))

    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
answer = solution(jobs)
print(answer)
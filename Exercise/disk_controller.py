import heapq

def solution(jobs):
    jobs.sort()
    job_heap = []
    temp_time = 0
    jobs_len = len(jobs)
    job_times = 0
    # print(jobs[0][0])

    while len(jobs)>0 or len(job_heap):
        # priority queue에 남은 작업이 있는 경우
        if job_heap:
            temp = heapq.heappop(job_heap)
            job_times += temp_time - temp[1] + temp[0]
            print(job_times)
            temp_time += temp[0]
            print("debug00",len(jobs))
        # priority queue에 남은 작업이 없는 경우 -> jobs에서 끌어온다.
        else:
            print("debug01",len(jobs))
            if len(jobs)>0 and jobs[0][0]<=temp_time:
                while len(jobs)>0 and jobs[0][0]<=temp_time:
                    if jobs[0][0]<=temp_time:
                        print("debug02",job_heap,len(jobs),jobs[0][0],temp_time)
                        tmp = jobs.pop(0)
                        heapq.heappush(job_heap, [tmp[1],tmp[0]])
                        # print("debug03",job_heap,len(jobs),jobs[0][0],temp_time)
                    else:
                        print("break")
                        break
            # priority queue에 남은 작업이 없는데 jobs에서 끌어 올 작업도 없으면?(시간을 흘려야 한다.)
            else:
                temp_time += 1
    answer = int(job_times/jobs_len)

    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
answer = solution(jobs)
print(answer)
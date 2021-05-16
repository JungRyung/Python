import string
from bisect import bisect_left

info_dict = {}
def make_dict(front, n, list, score):
    if n==3:
        if front+list[3] in info_dict:
            info_dict[front+list[3]].append(score)
        else:
            info_dict[front+list[3]] = [score]
        if front+'-' in info_dict:
            info_dict[front+'-'].append(score)
        else:
            info_dict[front+'-'] = [score]
    else:
        make_dict(front+list[n], n+1, list, score)
        make_dict(front+'-', n+1, list, score)

def solution(info, query):
    answer = []
    specs = []
    
    # info에 대한 dictionary 만들어주기
    for inf in info:
        # info에서 점수만 분리해내기
        inf_list = inf.split(' ')
        score = int(inf_list.pop())
        make_dict(inf_list[0],1,inf_list,score)
        make_dict('-',1,inf_list,score)

    # info_dict의 value를 정렬
    for value in info_dict.values():
        value.sort()

    # query도 파싱해주고 이분탐색 진행
    for demands in query:
        demand = demands.split(' and ')
        demand[3], demand_score = demand[3].split(' ')
        demand_score = int(demand_score)
        demand_str = demand[0]+demand[1]+demand[2]+demand[3]
        
        if demand_str in info_dict:
            answer.append(len(info_dict[demand_str]) - bisect_left(info_dict[demand_str], demand_score))
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

answer = solution(info, query)
print(answer)
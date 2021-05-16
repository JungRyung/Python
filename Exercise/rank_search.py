import string
def solution(info, query):
    answer = []
    specs = []
    for i in range(len(info)):
        specs.append(info[i].split(' '))

    for demands in query:
        demand = demands.split(' and ')
        demand.append([])
        demand[3], demand[4] = demand[-2].split(' ')
        num = 0
        for spec in specs:
            if spec[0] != demand[0] and demand[0] != '-':
                continue
            if spec[1] != demand[1] and demand[1] != '-':
                continue
            if spec[2] != demand[2] and demand[2] != '-':
                continue
            if spec[3] != demand[3] and demand[3] != '-':
                continue
            if int(spec[4]) < int(demand[4]):
                continue
            num += 1
        answer.append(num)
    # for specifications in info:
    #     spec = specifications.split(' ')
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

answer = solution(info, query)
print(answer)
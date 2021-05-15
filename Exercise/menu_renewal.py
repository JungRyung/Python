from itertools import combinations

def solution(orders, course):
    answer = []

    for meal_num in course:
        order_dict = {}
        order_combi_list = []
        for order in orders:
            order_combi_list.extend(list(combinations(sorted(order),meal_num)))
        for order_combi in order_combi_list:
            order_combi_str = ''.join(order_combi)
            if order_combi_str in order_dict:
                order_dict[order_combi_str] += 1
            else:
                order_dict[order_combi_str] = 1
        for order in order_dict:
            if order_dict[order] == max([order_dict[orders] for orders in order_dict]):
                if order_dict[order] > 1:
                    answer.append(order)
    answer.sort()
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]

course = [2,3,4]

answer = solution(orders, course)

print(answer)
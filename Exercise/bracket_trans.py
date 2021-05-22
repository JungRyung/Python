##### 2020 카카오 블라인드 신입 채용 #####
##### 괄호 변환 #####
def is_right_string(p):
    stack_list = []
    for ch in p:
        if ch == '(':
            stack_list.append('(')
        else:
            if len(stack_list) != 0:
                stack_list.pop()
            else:
                return False
    return True

def split(p):
    left_num = 0
    right_num = 0
    idx = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_num += 1
        else:
            right_num += 1
        if left_num == right_num:
            idx = i+1
            break
    return p[:idx], p[idx:]

def is_balanced_string(p):
    left_num = 0
    right_num = 0
    for ch in p:
        if ch == '(':
            left_num += 1
        else:
            right_num += 1
    if left_num == right_num:
        return True
    else:
        return False

def make_right_string(p):
    # 빈 문자열이면 빈 문자열을 반환
    if p =='':
        return p
    # 문자열을 두 균형잡힌 문자열로 나눔
    u, v = split(p)
    if is_right_string(u):
        return u + make_right_string(v)
    else:
        u = u[1:-1]
        new_string = ""
        for ch in u:
            if ch == '(':
                new_string += ')'
            else:
                new_string += '('
        return '(' + make_right_string(v) + ')' + new_string

def solution(p):
    answer = ''
    
    answer = make_right_string(p)

    return answer

p = "()))((()"
answer = solution(p)

print(answer)
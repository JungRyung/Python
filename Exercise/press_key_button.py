def numToMatrix(number):
    if number == 0:
        return 3,1
    else:
        i = (number - 1) // 3
        j = (number - 1) % 3
        return i,j

def cal_distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def solution(numbers, hand):
    answer = ''
    left_x_tmp=3
    left_y_tmp=0
    right_x_tmp=3
    right_y_tmp=2

    for number in numbers:
        x, y = numToMatrix(number)
        # 좌측 키패드인 경우 -> 왼손으로 조작
        if y == 0:
            answer += 'L'
            left_x_tmp = x
            left_y_tmp = y
        # 우측 키패드인 경우 -> 오른손으로 조작
        elif y == 2:
            answer += 'R'
            right_x_tmp = x
            right_y_tmp = y
        # 키패드 중앙인 경우
        else:
            # 왼손이 가까운 경우 -> 왼손으로 조작
            if cal_distance(x,y,left_x_tmp,left_y_tmp) < cal_distance(x,y,right_x_tmp,right_y_tmp):
                answer += 'L'
                left_x_tmp = x
                left_y_tmp = y
            # 오른손이 가까운 경우 -> 오른손으로 조작
            elif cal_distance(x,y,left_x_tmp,left_y_tmp) > cal_distance(x,y,right_x_tmp,right_y_tmp):
                answer += 'R'
                right_x_tmp = x
                right_y_tmp = y
            # 거리가 같을 경우 -> hand에 따라
            else:
                if hand == "left":
                    answer += 'L'
                    left_x_tmp = x
                    left_y_tmp = y
                else:
                    answer += 'R'
                    right_x_tmp = x
                    right_y_tmp = y
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

answer = solution(numbers,hand)

print(answer)
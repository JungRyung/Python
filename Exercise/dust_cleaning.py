########## 2021 ㅈㅍㄱㅅ ###########
def area_print(area):
    for row in area:
        print(row)

def solution(area):
    answer = 0
    height = len(area)
    width = len(area[0])
    
    for i in range(height-1):   # 바닥은 검색하지 않는다
        for j in range(width):
            # 해당 칸에 먼지가 있는 경우
            if area[i][j] == '$':
                area[i] = area[i][:j] + '.' + area[i][j+1:]
                answer += 1
                # 바로 아래에 바닥이나 선반이 있는 경우
                # 바로 아래에 바닥이나 선반이 없는 경우
                if area[i+1][j] != '#':
                    for k in range(i,height-1):
                        if area[k+1][j] == '#':
                            area[k] = area[k][:j] + '$' + area[k][j+1:]
                            break
                # area_print(area)
    return answer

area = [".$...$..","......$.","$....###","..$.....","...$....","..$...$.","########"]
# area_print(area)
answer = solution(area)
print(answer)

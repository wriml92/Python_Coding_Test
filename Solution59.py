def solution(n, m, section):
    answer = 1  # 칠하는 횟수
    paint = section[0]  # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
    
    return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 무조건 1번이라도 칠해야 하므로 answer를 1로 초기화
# 덧칠 시작점 paint를 section[0]으로 정해 놓고 for문을 통하여 paint와 section[i] 간의 간격 구함
# m-1까지 1번으로 가능하므로 m부터는 2번 칠하게 되는 것
# 1번 칠을 완료한 다음 다음으로 칠할 구간을 찾기 위해 section[i]를 paint 시작점으로 바꾸고 다시 범위를 찾는 for문을 반복
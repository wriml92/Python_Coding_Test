def solution(n):
    str = "수박"*n
    return str[:n]

# 처음 내가 작성한 코드
def solution(n):
    ans = ''
    for i in range(n):
        if i%2 == 0:
            ans += '수'
        else:
            ans += '박'
    return ans

# 수박수박수박수박수박수? (https://school.programmers.co.kr/learn/courses/30/lessons/12922)
# 예를 들어 n이 3이면 "수박수", 4라면 "수박수박" 리턴
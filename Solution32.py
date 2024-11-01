def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

# 처음 내가 작성한 코드
def solution(a, b):
    ans = 0
    for i in range(len(a)):
        answer += (a[i]*b[i])
    return answer 

# 내적 (https://school.programmers.co.kr/learn/courses/30/lessons/70128)
# 길이가 같은 두 1차원 정수 배열 a, b가 주어졌을 때
# a와 b의 내적을 return
# zip(iterable) -> 튜플 형태로 차례로 접근할 수 있는 iterator 반환
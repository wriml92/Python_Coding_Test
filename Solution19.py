def solution(n):
    return (n**0.5+1)**2 if int(n**0.5) == n**0.5 else -1

# 정수 제곱근 판별 (https://school.programmers.co.kr/learn/courses/30/lessons/12934)
# 주어진 n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n의 양의 정수 x의 제곱이 아니라면 -1을 리턴
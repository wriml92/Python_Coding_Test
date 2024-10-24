def solution(x, n):
    return [i*x+x for i in range(n)]

# 처음 내가 풀었던 문장
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 정수 x와 자연수 n을 입력받아, x부터 시작해 x씩 증가하는 숫자를 n개 가진 리스트 반환
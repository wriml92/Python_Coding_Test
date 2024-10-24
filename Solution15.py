def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]

# 처음 풀었던 코드
def solution(n):
    for i in range(1, n):
        if(n % i) == 1:
            break
    return i

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 리스트 안에 n를 x로 나눈 나머지가 1인 정수 중 제일 첫 번째 수를 반환
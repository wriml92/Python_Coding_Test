def solution(n):
    return sum(i for i in range(1, n+1) if(n%i)==0)

# 처음 내가 풀었던 코드
def solution(n):
    sum = 0
    for i in range(1, n+1):
        if(n % i) == 0:
            sum += i
    return sum

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 약수의 합을 구하는 코드로 아래 문장들을 위에 한 문장으로 합쳐 다시 풀었다.
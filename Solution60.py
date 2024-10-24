import math

def solution(number, limit, power):
    divisors = [] # 약수 리스트
    for i in range(1, number+1): # 1부터 number까지의 반복문
        divisor = 0
        for j in range(1, int(math.sqrt(i)) + 1): # 1부터 i의 제곱근까지의 반복문
            if i % j == 0:
                divisor += 1
                if math.pow(j,2) != i: # 제곱이 되는 수는 count에 1을 더해 중복 방지
                    divisor += 1
            if divisor > limit: # limit 값을 초과하면 power 값으로 반환
                divisor = power
                break
        divisors.append(divisor)
    return sum(divisors)

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 문제가 점점 길어지면서 읽는 시간도 많이 들어간다. 분발해야겠다.
# 약수를 구하는 데 (1, i+1)까지에 범위를 지정해 버리면
# 시간초과(시간복잡도가 O(n**2))가 되어버리면서 몇몇 테스트에서 실패가 뜬다.
# 그래서 시간복잡도를 줄이기 위해 i의 제곱근까지 범위를 지정하면 된다.
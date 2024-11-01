def solution(left, right):
    ans = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i%j == 0:
                cnt += 1
        if cnt%2 == 0:
            ans += i
        else:
            ans -= 1
    return ans

# 약수의 개수와 덧셈 (https://school.programmers.co.kr/learn/courses/30/lessons/77884)
# left부터 right까지의 모든 수들 중에서 약수의 갯수가 짝수인 수는 더하고, 약수의 갯수가 홀수인 수는 뺀 수 return
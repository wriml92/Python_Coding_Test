def solution(price,money,count):
    sum = 0
    for i in range(count):
        sum += price*(i+1)
    if sum - money > 0:
        return sum - money
    else:
        return 0

# 부족한 금액 계산하기 (https://school.programmers.co.kr/learn/courses/30/lessons/82612)
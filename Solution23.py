def solution(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1

# 처음 내가 작성한 코드
def solution(num):
    for i in range(500):
        if num != 1:
            if num%2 == 0:
                num = num/2
            else:
                num = (num*3) + 1
        else:
            return i
            break
    return -1

# 문제 : 콜라츠 추측 (https://school.programmers.co.kr/learn/courses/30/lessons/12943)
# 입력된 수가 짝수라면 2로 나누고 입력된 수가 홀수라면 3을 곱하고 1을 더함.
# 위의 연산의 값이 1이라면 i에다가 1을 더해 반환
# 결과로 나온 수에 같은 작업을 1이 될 때까지 반복
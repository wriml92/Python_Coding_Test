def solution(n):
    return sum([int(i) for i in str(n)])

# 내가 처음 풀었을 때 작성한 코드
# def solution(n):
#     str_n = str(n)
#     answer = 0
#     for i in range(len(str_n)):
#         answer += int(str_n[i])
#     return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12931
# n의 각 자릿수의 합을 구하는 코드로 for문을 한줄로 표현하였다.
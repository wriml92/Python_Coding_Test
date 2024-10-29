def solution(s):
    cnt1 = 0
    cnt2 = 0
    answer = 0
    k = ""
    for i in s:
        if cnt1 == cnt2:
            cnt1 += 1
            k = i
            answer += 1
        elif k == i:
            cnt1 += 1
        else:
            cnt2 += 1
    return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 이번 문제는 문제를 이해하기 어려워서 몇 번 계속 봐서야 그제야 이해가 됐다.
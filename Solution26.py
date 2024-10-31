def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# 음양 더하기 (https://school.programmers.co.kr/learn/courses/30/lessons/76501)
# zip 함수를 통해 정수들과 부호들을 서로 엮어줌.
# zip() 함수를 사용하면 여러 그룹의 데이터를 루프 한 번만 돌면서 처리할 수 있음
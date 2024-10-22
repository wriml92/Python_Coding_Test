def solution(angle):
    if angle <= 90:
        return 1 if angle < 90 else 2
    else:
        return 3 if angle < 180 else 4
    
# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 주어진 각이 예각일 때 1, 직각일 때는 2를 반환
# 둔각일 때 3, 평각 즉 180도일 때 4를 반환
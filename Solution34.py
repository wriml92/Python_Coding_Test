def solution(s):
    return ''.join(sorted(s, reverse=True))

# 문자열 내림차순으로 배치하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12917)
# 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬해 새로운 문자열을 리턴
def solution(s):
    return s.isdigit() and len(s) in [4,6]

# 처음 내가 작성한 코드
def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False

# 문자열 다루기 기본 (https://school.programmers.co.kr/learn/courses/30/lessons/12918)
# isdigit() 함수 : 문자열이 숫자로만 이루어져있는지 확인하는 함수
# and 연산자는 전부 True일 경우만 True이며, 하나라도 False라면 전부 False
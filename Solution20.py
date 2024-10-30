def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))

# 처음 작성한 코드
def solution(n):
    arr = list(str(n))
    arr.sort(reverse = True)
    return int(''.join(arr))

# 정수 내림차순으로 배치하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12933)
# 먼저 정수 n을 문자열 함수 str로 이용하여 문자열 변환
# 변환한 문자열을 리스트 함수로 변환
# sorted 함수로 문자열 정수를 역순으로 정렬 (reverse=True)
# join 함수를 이용하여 서로 각각의 문자들을 붙여줌.
# int 함수를 이용하여 합친 문자들을 다시 정수형으로 변환
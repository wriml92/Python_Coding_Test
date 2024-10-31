def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor==0]) or [-1]

# 처음 내가 짠 코드 (오류 발생)
def solution(arr, divisor):
    array = []
    for i in arr:
        if arr[i]%divisor == 0:
            array.append(arr[i])
    return array

# 나누어 떨어지는 숫자 배열 (https://school.programmers.co.kr/learn/courses/30/lessons/12910)
# array의 각 element 중 divisor로 나누어 떨어지는 값을 먼저 for문을 통해 리스트로 반환
# 오름차순으로 정렬하기 위해 sorted 함수 사용
# arr 모든 원소가 나누어 떨어지지 않는 경우는 -1를 반환
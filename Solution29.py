# 처음 내가 작성한 코드
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

# 제일 작은 수 제거하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12935)
# arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수
# remove 메서드를 사용하여 제거
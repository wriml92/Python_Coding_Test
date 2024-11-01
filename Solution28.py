def solution(numbers):
    return 45 - sum(numbers)

# 없는 숫자 더하기 (https://school.programmers.co.kr/learn/courses/30/lessons/86051)
# 0에서 9까지 모두 더한 값이 45이므로 45에 numbers 원소들의 합을 빼면
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수임.
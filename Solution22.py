def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))

# 두 정수 사이의 합 (https://school.programmers.co.kr/learn/courses/30/lessons/12912)
# 두 정수 사이의 합을 구해야 하므로 먼저 두 수의 최소값과 최대값을 먼저 구함.
# 최소값과 최대값을 range 함수를 이용하여 범위를 지정함.
# 그 범위 안의 값을 sum 함수를 사용하여 모두 더 하게 되면 두 정수 사이의 합이 완섬.
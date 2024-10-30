def solution(n):
    return n % sum(int(x) for x in str(n)) == 0

# 처음 내가 작성한 코드
def solution(n):
    arr = list(map(int, list(str(n))))
    return n % sum(arr) == 0

# 하샤드 수 (https://school.programmers.co.kr/learn/courses/30/lessons/12947)
# 각 자리 수의 합을 구해야 하므로 n을 문자열을 변환한 후
# for 문을 이용하여 각 자리의 수를 구해준 뒤 sum 함수를 이용하여 모두 합함.
# 거기에 n을 나눠서 0이라면 나누어 떨어진다는 뜻이라는 것이므로
# 나누어 떨어지면 0 즉 true를 반환하며 아니면 1 즉 false를 반환.
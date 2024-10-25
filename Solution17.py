def solution(n):
    return list(map(int, reversed(str(n))))

# 처음 내가 푼 문장
def solution(n):
    arr = list(str(n))
    arr.reverse()
    return list(map(int, arr))

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12932
# reverse() 함수 말고도 reversed(iterable)를 사용하여 거꾸로 출력할 수도 있음.
# 처음 내가 푼 문장보다 훨씬 깔끔해 보인다.
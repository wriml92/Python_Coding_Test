def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz" # 총 문자열
    ans = "" 
    for i in list(skip):  # 총 문자열에서 skip 문자열을 찾아서
        alpha = alpha.replace(i, "")  # 빈 공백으로 대체
        
    for j in s:  # s 문자열 안에서 반복
        ans += alpha[(alpha.find(j) + index) % len(alpha)]
    return ans

# 둘만의 암호 (https://school.programmers.co.kr/learn/courses/30/lessons/155652)
# a에서 z까지 문자열을 만들어 skip 문자열을 빼주면 된다.
# 그 후, index만큼 진행하고, 문자열의 최대길이가 넘어갈 경우 a로 돌아가기 위해 % 연산 적용
# 문자열에는 append 함수 적용이 불가
# find(찾을 문자열) -> 인덱스 번호 반환
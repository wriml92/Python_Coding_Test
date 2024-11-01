def solution(ingredient):
    hbg = []
    ans = 0
    for i in ingredient:
        hbg.append(i)
        if hbg[-4:] == [1,2,3,1]:
            ans += 1
            for _ in range(4): # 의미없는 변수라서 _로
                hbg.pop()
            # hbg = hbg[:-4] # 해당 부분은 채점 때 시간복잡도 문제 발생
    return ans

# 햄버거 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/133502)
# 빵(1) 1개, 야채(2) 1개, 고기(3) 1개, 다시 빵(1) 1개 순서대로 있어야 하나의 햄버거를 만들 수 있음. [1,2,3,1]
# 최종으로 만들 수 있는 햄버거 갯수(answer) 리턴
# pop 메서드를 통해 리스트의 일부 요소를 제거
# [list].pop()을 사용하게 되면, 해당 리스트의 맨 마지막 요소가 제거
# pop 함수에 인덱스를 정해주지 않아서 for 문을 이용해 마지막 요소 4개가 제거
# 8~9번 줄에 대신 del s[-4:] 대신 사용 가능
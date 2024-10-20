def solution(k, m, score):  # 사과 최대 점수, 한 상자에 들어가는 사과의 수, 사과들의 점수
    answer = 0  # 이익
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            answer += min(score[i:i+m]) * m
    return answer  # 과일장수가 얻을 수 있는 최대 이익

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/135808
# score를 내림차순 정렬하여 m개씩 분할 -> 한 상자에 담기는 사과의 점수들
# 과일장수가 얻을 수 있는 최대 이익을 구하라고 했기 때문에 score를 내림차순으로 정렬
# 최대 이익을 구하기 위해서는 각 상자의 점수들도 최대이어야 함
# for문을 통해 0부터 score 길이까지 반복하되, m씩 증가시킴
# 한 상자에 m개씩 담겨야 하기 때문에 슬라이싱 한 score를 m개씩 슬라이싱
# 가격이 최저 점수*m이므로 min(score[i:i+m])*m이 됨.
# 구한 가격을 answer에 계속 누적시켜 주고 모두 완료되면 사과 장수가 얻는 이익 answer 리턴
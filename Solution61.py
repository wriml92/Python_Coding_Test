def solution(lottos, win_nums):
    cnt_corr = 0 # 당첨 가능한 최저 개수
    cnt_zero = 0 # 알아볼 수 없는 번호
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt_corr += 1
        if lottos[i] == 0:
            cnt_zero += 1
            
    total = cnt_corr + cnt_zero # 당첨 가능한 최고 개수
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} # 순위와 당첨 내용 딕셔너리
    answer = [rank[total],rank[cnt_corr]]
    return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 0이 아닌 숫자가 몇 개 일치하는지는 cnt_corr, 0의 개수는 몇 개인지는 cnt_zero로 받아냄.
# 두 값을 더한 total이 당첨 가능한 최고 개수이며, cnt_corr이 당첨 가능한 최저 개수
# 딕셔너리를 활용하여 순위와 당첨 내용을 출력값으로 받아낼 수 있게 함.
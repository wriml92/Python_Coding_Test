def solution(answers):
    one = [1,2,3,4,5]  # 1번 수포자의 찍기 패턴
    two = [2,1,2,3,2,4,2,5]  # 2번 수포자의 찍기 패턴
    three = [3,3,1,1,2,2,4,4,5,5]  # 3번 수포자의 찍기 패턴
    
    ans = [0,0,0]  # 수포자의 정답 수 리스트 초기화
    
    for i in range(len(answers)):  # answers가 다 돌기까지
        if answers[i] == one[i % len(one)]:  # i가 패턴보다 더 클 수 있기 때문에 
            ans[0] += 1  # 1번이 정답을 맞추었을 때
        if answers[i] == two[i % len(two)]:  # 패턴 개수만큼 나눈 나머지로 
            ans[1] += 1  # 2번이 정답을 맞추었을 때
        if answers[i] == three[i % len(three)]:  # 계속 비교
            ans[2] += 1  # 3번이 정답을 맞추었을 때

    answer = []  # 최종으로 정답을 많이 맞춘 사람을 추가하기 위한 리스트
    for i in range(len(ans)):  # ans가 다 돌기까지
        if ans[i] == max(ans):  # ans의 최대값이 많이 맞춘 사람과 같을 때
            answer.append(i+1)  # answer 리스트에 추가
    return answer  # 많이 맞춘 사람 출력

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

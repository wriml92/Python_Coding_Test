def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.pop(0)
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/159994
# goal의 모든 요소들을 순차적으로 돌며 해당 요소가 cards1 또는 cards2의 0번째 요소와 같은지 비교
# for문을 문제없이 마무리하면 Yes을 리턴
# 중간에 cards1 또는 cards2의 0번째 요소와 다르다면 순서대로 만들어진 문장이 아니므로 No를 리턴한다.
# cards1[0] 또는 cards2[0]에 접근하려면 cards1 또는 cards2가 빈 리스트가 아닌 상태이어야 함.
# 리스트에 값이 존재하는 경우에 True가 되므로 그때 [0]번 인덱스와 비교
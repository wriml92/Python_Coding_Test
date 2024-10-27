def solution(X, Y):
    answer = ''
    
    for i in range(9,-1,-1):
        answer += (str(i)*min(X.count(str(i)),Y.count(str(i))))
    
    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
    
# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 가장 큰 정수를 만들기 위해서는 공통되는 수를 내림차순으로 정렬한 후 한줄로 출력하면 됨.
# min 함수로 최소로 같은 숫자들을 구하고 그 수를 더함.
# 문자로 출력해달라 했으므로 str 함수 적용
# 처음부터 9~0 역순으로 숫자를 조회해서 answer 성분이 내림차순으로 더해짐.
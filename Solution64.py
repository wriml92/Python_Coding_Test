def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()

    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 가장 먼저 lost, reserve를 오름차순 정렬
# 예제에서는 모두 정렬되어 있어서 정렬 문을 적지 않았는데 결과 나오는데는 문제가 없었는데 
# 정렬되지 않은 예제가 만약 있다는 가정을 든다면 채점하는 데 일부 오류가 나 정렬문을 작성
# reserve 기준으로 for문 작성
# reserve의 요소 i를 기준으로 왼쪽인 i-1부터 lost에 존재하는지 확인
# i-1이 없으면 i+1을 확인
# i-1 또는 i+1이 lost에 존재하면 lost에서 해당 값을 제거
# 한 명에게만 빌려줄 수 있으므로 if ~ elif문으로 작성
# n명의 학생에게서 체육복을 잃어버린 학생 수를 빼면 체육 수업을 들을 수 있는 학생 수가 구해짐.
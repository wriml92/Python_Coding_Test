from itertools import combinations

def solution(nums):
    answer = 0
    for a in combinations(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand % j==0:
                break
        else:
            answer += 1
    return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12977
# itertools는 효율적인 루핑을 위한 이터레이터를 만드는 함수로
# combinations, product, permutation 등이 있음
# combinations(iterable, r)
# 반복 가능한 자료형에서 원소 개수가 r개인 조합을 뽑아주는 함수
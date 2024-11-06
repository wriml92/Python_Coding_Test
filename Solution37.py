# numpy 사용하여 짠 코드
import numpy as np

def solution(arr1, arr2):
    arr1_np = np.array(arr1)
    arr2_np = np.array(arr2)
    result = arr1_np + arr2_np
    return result.tolist()

# numpy 없이 짠 코드
def solution(arr1, arr2):
    answer =[]
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j]+arr2[i][j])
        answer.append(arr_sum)
    return answer    

# 행렬의 덧셈 (https://docs.google.com/spreadsheets/d/1ZVlg443mTBi93rqxE-h1tzAzYRGV0xTeHSqlPdofzt4/edit?gid=1513665583#gid=1513665583)
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수
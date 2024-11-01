def solution(s):
    return s[len(s)//2] if len(s)%2==1 else s[(len(s)//2)-1:len(s)//2+1]

# 가운데 글자 가져오기 (https://school.programmers.co.kr/learn/courses/30/lessons/12903)
# 단어 s의 가운데 글자를 반환
# 단어의 길이가 짝수라면 가운데 두글자를 반환
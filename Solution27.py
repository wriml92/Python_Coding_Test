def solution(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]

# 핸드폰 번호 가리기 (https://school.programmers.co.kr/learn/courses/30/lessons/12948)
# 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴
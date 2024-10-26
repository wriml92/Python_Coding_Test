def Solution(babbling):
    answer = 0
    able = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling: # babbling의 단어 하나씩 확인
        for c in able:
            if c*2 not in bab: # 연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(c, ' ')
            
            if bab.isspace(): # 공백으로만 이루어져 있으면 answer+1
                answer += 1

    return answer

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3
# 발음할 수 있는 단어들을 공백(' ')으로 대체
# 대체 후 남는 문자들이 존재하면 해당 단어는 발음할 수 없는 단어
# c*2가 bab에 존재하는지 확인함과 공백을 ''이 아닌 ' '으로 대체해야 함
# 연속으로 발음할 수 없다고 명시했기에 c*2가 존재하지 않을 때만 공백으로 대체
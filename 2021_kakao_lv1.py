# 프로그래머스 '숫자 문자열과 영단어'
s = "one4seveneight"

def solution(s):
    textMap = {'zero':'0' , 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for text in list(textMap.keys()):
        s = s.replace(text,textMap[text])

    return int(s)

result = solution(s)
print(result)

programmers
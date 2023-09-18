def solution(s):
    d = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    answer = ''
    temp = ''

    for i in s:
        if i.isdigit():
            answer += i
        elif i.isalpha():
            temp += i
            if temp in d:
                answer += d[temp]
                temp = ''

    return int(answer)


s = "one4seveneight"
a = solution(s)
print(a)
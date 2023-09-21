def solution(id_list, report, k):
    n = len(id_list)
    mail = [0]*n
    arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(report)):
        a, b = map(str, report[i].split())
        arr[id_list.index(a)][id_list.index(b)] = 1

    # for i in range(n):
    #     print(*arr[i])
    killed = [False] * n
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += arr[j][i]
        if sum >= k:
            killed[i] = True
    
    for i in range(n):
        if killed[i]:
            for j in range(n):
                if(arr[j][i] == 1):
                    mail[j] += 1

    return mail



id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))
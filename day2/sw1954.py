tc = int(input())
for t in range(tc):
    n = int(input())

    # n * n 배열의 상하좌우에 1칸의 안전구역 추가로 만들기
    arr = [[0 for j in range(n+2)] for i in range(n+2)]

    # 안전구역에 임의의 숫자 1 넣기
    for i in range(n + 2):
        arr[i][n + 1] = 1
        arr[i][0] = 1
        arr[0][i] = 1
        arr[n+1][i] = 1
   
    rp = 1  # 행 위치
    cp = 1  # 열 위치
    num = 1
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    dir = 0 # 0부터 우,하,좌,상

    while num <= n*n:
        if arr[rp][cp] == 0:   # 현재 위치에 숫자가 있으면 (visit 하지 않았으면)
            arr[rp][cp] = num   # 현재 위치에 숫자 넣기 (visit 체크 겸용)
            num += 1
            rp += dirs[dir%4][0]    # 이동
            cp += dirs[dir%4][1]
        else:   # 현재 위치에 숫자가 없으면
            rp += dirs[(dir+2)%4][0]   # 다시 뒤로 이동
            cp += dirs[(dir+2)%4][1]
            dir = (dir + 1) % 4   # 방향 바꾼 후
            rp += dirs[dir%4][0]   # 바뀐 방향으로 이동
            cp += dirs[dir%4][1]

    print('#%s'%(t+1))
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(arr[i][j], end=' ')
        print('')
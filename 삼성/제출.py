def rotate(board,r,c):
    tmp = list(zip(*board))
    for q in range(N-1, -1, -1):
        board[q] = list(tmp[q][::-1])
    return c,N-1-r


tornado = {(-1,1):1, (1,1):1, (-2,0):2,(2,0):2, (-1,0):7,(1,0):7,(-1,-1):10,(1,-1):10,(0,-2):5}
def move(board,r,c,cnt):
    global ans
    while cnt>0:
        c-=1
        cnt-=1
        whole = board[r][c]
        board[r][c] = 0
        legacy = whole
        ratio = whole/100
        for k,v in tornado.items():
            nr,nc = r+k[0], c+k[1]
            sand = int(ratio*v)
            legacy -= sand
            if not (0<=nr<N and 0<=nc<N):
                ans+=sand
                continue
            board[nr][nc] += sand
        if c-1<0:
            ans += legacy
        else:
            board[r][c-1] += legacy
    return r,c


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
distance = 0
r,c = N//2, N//2
ans = 0

for dis in range(1,N):
    for _ in range(2):
        r,c = move(board,r,c,dis)
        r,c = rotate(board,r,c)
r,c = move(board,r,c,N-1)
r,c = rotate(board,r,c)

print(ans)
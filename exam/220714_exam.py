# 미로가 있어서 출발지점에서 도착지점으로 가려고 해 (시작점 -1, 장애물 1, 갈 수 있는 곳 0, 도착점 2)
## [-1, 0, 1]
## [ 1, 0, 0]
## [ 1, 1, 0]
## [ 1, 0, 0]
## [ 2, 0, 1]

# 1. 최소 몇 번의 점으로 갈 수 있나요?
# 2. 어떤 점을 거쳐서 갈 수 있나요?


cur = [0,0]
VISITED = [[False]*3 for x in range(5)]
endflag = False
DIR = [[-1,0],[1,0],[0,-1],[0,1]]
path = []
MAZE = [[-1, 0, 1], [ 1, 0, 0], [ 1, 1, 0], [ 1, 0, 0], [ 2, 0, 1]]
cnt = 0

for i in MAZE:
    print(i)
    
path.append((0,0))
while True:
    for row, col in DIR:
        newRow = row+cur[0]
        newCol = col+cur[1]
        if newRow>4 or newRow<0 or newCol>2 or newCol<0:
            print("초과", newRow, newCol)
            continue
        elif MAZE[newRow][newCol] ==1:
            print("장애물", newRow, newCol)
            continue
        elif VISITED[newRow][newCol] ==True:
            print("이미 갔다", newRow, newCol)
            continue    
        elif MAZE[newRow][newCol] ==0:
            print("새로운 곳", newRow, newCol)
            VISITED[newRow][newCol]=True
            path.append((newRow, newCol))
            cur[0] = newRow
            cur[1] = newCol
            break
        elif MAZE[newRow][newCol] ==2: 
            print("끝", newRow, newCol)
            endflag=True
            path.append((newRow, newCol))
            break
    if endflag==True:
        break
print(path)

print(len(path))
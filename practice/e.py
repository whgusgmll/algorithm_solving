# 4. 미로가 있어서 출발지점에서 도착지점으로 가려고 해 (시작점 -1, 장애물 1, 갈 수 있는 곳 0, 도착점 2)
## [-1, 0, 1]
## [ 1, 0, 0]
## [ 1, 1, 0]
## [ 1, 1, 2]
## MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]]
## 몇 번 거쳐서 갈 수 있는 지? 나타내기 4
## 어느 점을 거쳐서 갈 수 있는지? 나타내기 (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)
## (-1은 (0,0)이고, 2는 (2,2)이고, 맨 오른쪽 상단은 (0,2)라고 가정)
## (미로 밖으로 나갈 수는 없음, 최소 거리를 구해야 함)


MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]]
path = []
DIR= [[-1,0], [1,0], [0,-1], [0,1]]
cur = [0,0]
endFlag = False
VISITED = [[False]*3 for x in range(4)]
path.append((0,0))

while True:
    for row, col in DIR:
        newRow = cur[0]+row
        newCol = cur[1]+col
        if newRow<0 or newRow>3 or newCol<0 or  newCol>2:
            print("초과", newRow, newCol)
            continue
        elif MAZE[newRow][newCol]==1:
            print("장애물", newRow, newCol)
            continue
        elif VISITED[newRow][newCol]==True:
            print("이미", newRow, newCol)
        elif MAZE[newRow][newCol]==2:
            print("도착", newRow, newCol)
            path.append((newRow, newCol))
            endFlag=True
            break
        elif MAZE[newRow][newCol]==0:
            print("새로운", newRow, newCol)
            VISITED[newRow][newCol]=True
            cur[0]=newRow
            cur[1]=newCol
            path.append((newRow,newCol))
    if endFlag:
        break
print(len(path))
print(path)

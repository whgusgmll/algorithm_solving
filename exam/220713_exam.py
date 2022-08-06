# 4. 미로가 있어서 출발지점에서 도착지점으로 가려고 해 (시작점 -1, 장애물 1, 갈 수 있는 곳 0, 도착점 2)
## [-1, 0, 1]
## [ 1, 0, 0]
## [ 1, 1, 0]
## [ 1, 1, 2]
## MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 2]]
## 몇 번 거쳐서 갈 수 있는 지? 나타내기
MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 2]]
maze = [-1, 0, 1, 1, 0, 0, 0, 1, 2]
b=0
for a in maze:
    if a==0 or a==2:
        b+=1
print(b)

## 어느 점을 거쳐서 갈 수 있는지? 나타내기
d=[]
for c in MAZE:
    if c==0 or c==-1 or c==2:
        d+=c
print(d)

## (-1은 (0,0)이고, 2는 (2,2)이고, 맨 오른쪽 상단은 (0,2)라고 가정)
## (미로 밖으로 나갈 수는 없음, 최소 거리를 구해야 함)

j=[2,3]
VISITED = [[False]*6 for x in range(4)]
DIR = [[-1,0], [1,0],  [0,-1],  [0,1]] 
for i in VISITED:
    print(i)

VISITED[j[0]][j[1]] = True
for row, col in DIR:
    print(j)
    newRow = j[0]+row
    newCol = j[1]+col
    VISITED[newRow][newCol] = True

for i  in VISITED:
    print(i)

VISITED = [[False]*3 for x in range(5)]
CUR =[3,4]
DIR = [[-1,0], [1,0], [0,-1], [0,1]]
for row, col in DIR:
    newRow = CUR[0]+row
    newCol = CUR[1]+col
    print(newRow, newCol)

PNTS = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,4], [2,1], [2,2], [2,3], [2,4], [3,4], [4,4]]

print("3번")

VISITED=[[False]*6 for x in range(5)]
for x in VISITED:
    print(x)
print() 

for row, col in PNTS:
    VISITED[row][col] = True
    
for x in VISITED:
    print(x)
print()
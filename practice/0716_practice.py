DIR = [[-1,0], [1,0], [0,-1], [0,1]]
for row, col in DIR:
    if row != 0:
        continue
    print(row, col)


for row, col in DIR:
    if row != 0:
        break
    print(row, col)
    
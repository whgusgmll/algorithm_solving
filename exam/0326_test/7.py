i =int(input())

for j in range(1, i+1):
    print(" " * (i-j) + "*" * (2*j-1))
for num in range(i):
    print(" " * (num+1) + "*" * (-2*num+(i*2)-3))
n = int(input())

for i in range(1, n+1):
    print("*" * i +" " * (i*-2+2*n) +"*" * i )

for j in range(n):
    print("*" *(n-j-1)+ " " * (j*2+2) +"*" *(n-j-1))
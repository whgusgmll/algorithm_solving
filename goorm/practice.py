#별 찍기1
n=int(input())
for a in range(1,n+1):
    print("*" * a)

#별 찍기2
n=int(input())
for num in range(1,n+1):
    print(" " * (n-num)+ "*" * num)

#별 찍기3
n=int(input())
for num in range(n,0,-1):
    print("*" * num)

#별 찍기4
n = int(input())
for num in range(n, 0, -1):
    print(' '* num+ '*' * (n-num+1))

#별 찍기5
n=int(input())
for num in range(1,n+1):
    print(" " *(n-num) + "*" * (num*2-1))

#별 찍기6
n =int(input())
for num in range(n):
    print(' '* num + '*' * (2*(n-num)-1))

#별 찍기6
n=int(input())
for num in range(1,n+1):
    print(" " *(n-num) + "*" * (num*2-1))

for i in range(1,n):
    print(' '* i + '*' * (2*(n-i)-1))

#별 찍기7
n = int(input())
for i in range(1,n+1):
    print('*' * num + " " * (n*(-2*num))

#별 찍기8
n = int(input())
for i in range(1,n+1):
    print('*' * i + " " * (-2*i+n*2) + '*' * i)

for j in range(1,n):
    print('*' * (n-j) + " " * (j*2) + '*' * (n-j))
i = int(input())
for j in range(1,i+1):
    print(" "*(i-j)+"*"*(j*2-1))
for num in range(1, i):
    print(" "*num+"*"*(2*(i-num)-1))

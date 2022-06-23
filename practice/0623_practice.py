
#정유림
for i in range(2,7,2):
    for x in range(1,10):
        print(i,"*",x,"=",i*x)
    print()

#선생님
for a in [2,4,6]:
    for b in range(1,10):
        print(a,"*",b,"=",a*b)
    print()

#조현희
for j in range(1,7):
    if j%2==0:
        for i in range(1, 10):
            b = j*i
            print(str(j)+ "*"+str(i)+"="+str(b))
        print()

a="10"
b="5"
print(int(a)+int(b))
print(str(int(a))+str(int(b)))


#for a in [2,4,6]:
    #for b in range(1,10):
        #print(a,chr(42),b,chr(61),sum(a for x in range(b)))
    #print()
#sum(a for x in range(b))
#chr(42)
#int("5")
#str(53)
#str(53) -> "53"
#chr????
#ord
#ord()
#ascii code => ord(), chr()
#형변환 => int(), float(), str()

print(ord("*"), ord("="))
print(ord("ㅔ"))



#조현희
for i in range(1, 10):
    if i%2==0 and i!=8:
        for j in range(1,7):
            if j%2==0:
                b = j*i
                print(str(j)+ "*"+str(i)+"="+str(b),end="\t")
        print( )

#방법2 - 2,4,6쌩으로 찾기
for x in range(1,9):
    if x in [2,4,6]:
        for i in range(2,7,2):
            print( i,"*",x,"=",i*x, end="\t")
        print()



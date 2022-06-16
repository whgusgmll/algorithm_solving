a = []
for i in range(1,11):
    a.append(i)
print(a)

b = []
for i in range(1,101):
    b.append(i)
print(b)

c = [x for x in range(1, 101)]
print(c)

d = []
for i in range(1,101):
    if i%3==0:
        d.append(i)
print(d)

e = []
i = 1
while True:
    if i%4==0:
        e.append(i)
    i+=1
    if i>100:
        break
print(e)

f = []
i =1
while i<=100:
    if i%4==0:
        f.append(i)
    i+=1
print(f)

g= [0,0,0]
g[0]+= 10
g[1]+=1
g[2]+=7
print(g)

g.pop()
g.pop(0)
print(g)

h = [2,5,3,7,1,2,5,8,2,9]
j=0
for i in h:
    if i==2:
        j+=1
print(j)

print(len(h))
print(max(h))
print(min(h))
print(sum(h))

i = sorted(h)
print(i)

h.sort()
print(h)

i_reverse = sorted(h, reverse=True)
print(i_reverse)

h.sort(reverse=True)
print(h)
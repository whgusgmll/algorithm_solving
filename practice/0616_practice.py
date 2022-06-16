a = set()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
print(a)

b = set( i for i in range(1,6))
print(b)

a= [1,2,3,4,5]
c = set(a)
print(c)

## 4-2. 가지고 있는 숫자카드는 
## 1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1
## 이 있다. 총 몇가지의 숫자 카드를 가지고 있나요?
d = [1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1]
e = set(d)
print(len(e))

## 4-3. 새롭게 다른 카드 팩을 구했어 1,5,2,3,4,6,2,76,2,3,5,4 카드가 있대
## 4-2가지고 있던 숫자 카드종류에서 4-3. 카드 종류를 뺀 숫자 카드의 종류 총 몇개?
f = [1,5,2,3,4,6,2,88,2,3,5,4]
g = set(f)
print(e-g)
print(len(e-g))

h = (e|g)
print(len(h))

h = (e&g)
print(len(e&g))

c = {}
c['성현'] = 181
c['유림'] = 162
c['현희'] = 171
sorted_dict=sorted(c.items(), key=lambda x:x[1])
print(sorted(c.items(), key=lambda x:x[1]))

reverse_sorted_dict = sorted(c.items(), key=lambda x:x[1], reverse=True)
print(reverse_sorted_dict)

sorted_dict=sorted(c.items(), key=lambda x:x[0])
print(sorted(c.items(), key=lambda x:x[0]))

sorted_dict=sorted(c.items(), key=lambda x:x[0], reverse=True)
print(sorted(c.items(), key=lambda x:x[0]))
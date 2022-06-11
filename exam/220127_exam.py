# Do it 점프 투 파이썬 1,2,3장 시험

index = 1

## 1번
print(f'{index} : ', end='')
index += 1
print(type(4.36))

## 2번
print(f'{index} : ', end='')
index += 1
print(type(4))

## 3번
print(f'{index} : ', end='')
index += 1
print(type('abced'))

## 4번
print(f'{index} : ', end='')
index += 1
print(type(True))

## 5번
print(f'{index} : ', end='')
index += 1
print(type([1,2,3]))

## 6번
print(f'{index} : ', end='')
index += 1
print(type((2,3)))

## 7번
print(f'{index} : ', end='')
index += 1
print(type({1: 'a', 2: 'c'}))

## 8번
print(f'{index} : ', end='')
index += 1
print(type({2, 3}))

## 9번
print(f'{index} : ', end='')
index += 1
print(3 ** 2)

## 10번
print(f'{index} : ', end='')
index += 1
print(3%2)

## 11번
print(f'{index} : ', end='')
index += 1
print(3*2)

## 12번
print(f'{index} : ', end='')
index += 1
print(3/2)

## 13번
print(f'{index} : ', end='')
index += 1
print(3//2)

temp1 = 'hello world' # 14 ~ 17문제에 사용
## 14번
print(f'{index} : ', end='')
index += 1
print(temp1[0])

## 15번
print(f'{index} : ', end='')
index += 1
print(temp1[0:3])

## 16번
print(f'{index} : ', end='')
index += 1
print(temp1[:3])

## 17번
print(f'{index} : ', end='')
index += 1
print(temp1[3:])

temp2 = [3,5,2,4,3,2] # 18 ~ 23에 사용
## 18번
print(f'{index} : ', end='')
index += 1
temp2.pop()
print(temp2)

## 19번
print(f'{index} : ', end='')
index += 1
temp2.append(3)
print(temp2)

## 20번
print(f'{index} : ', end='')
index += 1
temp2.extend([2,3])
print(temp2)

## 21번
print(f'{index} : ', end='')
index += 1
temp2.sort()
print(temp2)

## 22번
print(f'{index} : ', end='')
index += 1
print(temp2.index(3))

## 23번
print(f'{index} : ', end='')
index += 1
print(temp2.count(2))

temp3 = {1: '푸', 2:'른', 3:'꿈'} # 24 ~ 30에 사용
## 24번
print(f'{index} : ', end='')
index += 1
print(temp3.keys())

## 25번
print(f'{index} : ', end='')
index += 1
print(temp3.values())

## 26번
print(f'{index} : ', end='')
index += 1
print(temp3.items())

## 27번
print(f'{index} : ', end='')
index += 1
print(temp3.get(1))

## 28번
print(f'{index} : ', end='')
index += 1
print(temp3.get(4))

## 29번
print(f'{index} : ', end='')
index += 1
print(1 in temp3)

## 30번
print(f'{index} : ', end='')
index += 1
print('푸' in temp3)

temp4 = (3, 4) # 31 ~ 32에 사용
## 31번
print(f'{index} : ', end='')
index += 1
print(temp4 * 3)

## 32번
print(f'{index} : ', end='')
index += 1
print(temp4 + temp4)

temp5 = {1,2,3} # 33 ~ 40에 사용
## 33번
print(f'{index} : ', end='')
index += 1
print(temp5 | {4})

## 34번
print(f'{index} : ', end='')
index += 1
print(temp5 - {4})

## 35번
print(f'{index} : ', end='')
index += 1
print(temp5 - {1})

## 36번
print(f'{index} : ', end='')
index += 1
print(temp5 & {4})

## 37번
print(f'{index} : ', end='')
index += 1
print(temp5 & {1})

## 38번
print(f'{index} : ', end='')
index += 1
temp5.add(4)
print(temp5)

## 39번
print(f'{index} : ', end='')
index += 1
temp5.update([1,2,3,4])
print(temp5)

## 40번
print(f'{index} : ', end='')
index += 1
temp5.remove(4)
print(temp5)

## 41번
print(f'{index} : ', end='')
index += 1
if []: print(True)
else: print(False)

## 42번
print(f'{index} : ', end='')
index += 1
if 'a': print(True)
else: print(False)

## 43번
print(f'{index} : ', end='')
index += 1
if '': print(True)
else: print(False)

## 44번
print(f'{index} : ', end='')
index += 1
if (): print(True)
else: print(False)

## 45번
print(f'{index} : ', end='')
index += 1
if {}: print(True)
else: print(False)

## 46번
print(f'{index} : ', end='')
index += 1
if 1: print(True)
else: print(False)

## 47번
print(f'{index} : ', end='')
index += 1
if 0: print(True)
else: print(False)

## 48번
print(f'{index} : ', end='')
index += 1
if None: print(True)
else: print(False)

## 49번
print(f'{index} : ', end='')
index += 1
print(3<2)

## 50번
print(f'{index} : ', end='')
index += 1
print(3>2)

## 51번
print(f'{index} : ', end='')
index += 1
print(3==2)

## 52번
print(f'{index} : ', end='')
index += 1
print(3!=2)

## 53번
print(f'{index} : ', end='')
index += 1
print(True and True)

## 54번
print(f'{index} : ', end='')
index += 1
print(True or True)

## 55번
print(f'{index} : ', end='')
index += 1
print(not True)

## 56번
print(f'{index} : ', end='')
index += 1
print(False and True)

## 57번
print(f'{index} : ', end='')
index += 1
print(False or True)

## 58번
print(f'{index} : ', end='')
index += 1
print(not False)

## 59번
print(f'{index} : ', end='')
index += 1
print(3 in [1,2,3])

## 60번
print(f'{index} : ', end='')
index += 1
print(4 in [1,2,3])

temp6 = [1,2,3] # 61 ~ 63에 사용
## 61번
print(f'{index} : ', end='')
index += 1
result = []
for num in temp6:
    result.append(num*3)
print(result)

## 62번
print(f'{index} : ', end='')
index += 1
result = []
for num in temp6:
    if num%2 == 0:
        result.append(num*3)
print(result)

## 63번
print(f'{index} : ', end='')
index += 1
result = []
for x in range(2, 5):
    for y in range(1, 3):
        result.append(x * y)
print(result)
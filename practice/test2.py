
for i in exam_input:## 75번
from pkgutil import iter_modules


scoreDict = {'배성현': 60, '조현희': 70, '정유림': 80, '채필곤': 90}
gradeDict = {}
for key, val in scoreDict.items():
    if val >= 90:
        gradeDict[key] = 'A'
    elif val >= 80:
        gradeDict[key] = 'B'
    elif val >= 70:
        gradeDict[key] = 'C'
    else:
        gradeDict[key] = 'D'
print('75번 : ', gradeDict)

## 76번
input = [ x for x in range(1, 101)]
visited = [False] * 101
result = []
for item in input:
    if item == 1: continue
    if visited[item] == False:
        result.append(item)
        for i in range(item, 101, item):
            visited[i] = True
print('76번 : ', result)

## 77번
itemList = [1,2,3,4]
print('77-1 : length(길이) 약자 구하기', len(itemList))
print('77-2 : 최소 값 구하기', min(itemList))
print('77-3 : 최대 값 구하기', max(itemList))
print('77-4 : 합 구하기', sum(itemList))

## 78번
print("78-1 : 테스트입니다.", end="")
print("78-2 : 테스트입니다", "테스트입니다", sep="@")
print("78-3 : 테스트입니다.", end="\t")
print("78-4 : 테스트입니다.", end="\n")
print("78-5 : {0}월 {1}일 입니다.".format(4,9))

## 79번 
student = ['조현희', '정유림', '배성현', '배성현']
print('79-1 : ', student * 2)
print('79-2 : ', student.index('배성현'))
print('79-3 : ', student.count('배성현'))

## 80번
student = ['조현희', '정유림', '배성현', '배성현']
print('80-1 : reversedStudent = sorted(student, reversed=True)')
print('80-2 : studnet.sort()')

## 81번
student = ['조현희', '정유림', '배성현', '배성현']
print('81-1 : tmp = student[:]', student[:])
print('81-2 : tmp = [x for x in student]', [x for x in student])

## 82번
def temp(x,y,z):
    return x+y+z
print('82 : \ndef temp(x,y,z):\n\treturn x+y+z')

## 83번
s = ' abcabcabcefgj abcabcabcefgj '
print('83-1 : ', s.count('a'))
print('83-2 : ', s.index('a'))
s = s.strip()
print('83-3 : ',s.startswith('abc'))
print('83-4 : ',s.endswith('fgj'))
print('83-5 : ',s.partition(' '))
print('83-6 : ',s.find('abce'))
print('83-7 : ',s.upper())
print('83-8 : ',s.lower())

## 84번
print('84 : from, import, from')
    exam_output.append(int(i))
print(exam_output)
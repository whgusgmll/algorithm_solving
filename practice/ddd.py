flout
int
string
bool
list
tuple
dict
set
9
1
6
1
1.5
hello world
hello worl
rl
lo world
[3,5,2,4,3,2]
[5,2,4,3,2]
[5,2,4,3,-5,2]
[5,2,4,3,-5,2,2,3]
[-5,2,2,2,3,3,5]
2
2
푸, 른 , 꿈
1,2,3,
dict
푸
None
True
True
(3,4,3,4,3,4,)
(3,4,3,4,)
{1,2,3,4}
{1,2,3}
true
false
{1,2,3,1}
{1,2,3,1,4}
[1,2,3,4]
(1,2,3)
False
True
False
False
False
True
False
False
False
True
True
#52
True
True
False
true
true
false
[1,2,3,1,2,3,1,2,3,]

#62
[2,4,3,6,4,8,]

#64
exam_input = ('4', '6', '-3')
exam_output = [int(x) for x in exam_input]
print(exam_output)

#65
exam_input = ('4', '6', '-3')
exam_output = []
for i in exam_input:
    exam_output.append(int(i))
print(exam_output)
#66
lst = [6,2,7,4,5,1]
lst.reverse
ans = lst
print(ans)

#66-2
ans = sorted(lst, reverse = True)
print('66-2:', ans)

#67
ans = sorted.lst
print('67: ', ans)

#68
blueDream = dict()
blueDream['배성현'] = 6
blueDream['정유림'] = 9
blueDream['조현희'] = 3
print('68 :', blueDream)

#68 -2
for key, vlaue in blueDream.items():
    if key in ['정유림', '조현희']:
        blueDream[key] *= 2
print('68 - 2', blueDream)

#69 
camel_Case

#70
snake_Case

#71
Paskal_Case

#72
abc = 1,2,3,
print(abc)

#73번
seq = [1,2,3,4,5]
first, *left = seq
print('73 : first, *left = seq')

#74번
ans = "for i in rnage(2, 4): \n\tfor j in range(1,4): \n\t\tprint(i, '*', j, '=', i*j)\n\tprint()"
print('74: \n, ans')

for i in range(2, 4):
    for j in range(1, 4):
        print(i, '*', j, '=', i*j)
    print()

#75
scoreDict = {'배성현':60, '조현희':70, '정유림':80, '채필곤':90}
gradeDict = {}
for key, val in scoreDict.items():
    if val>=90:
        gradeDict[key] = 'A'
    elif val >=80:
        gradeDict[key] = 'B'
    elif val >=70:
        else:
            gradeDict[key] = 'D'
print('75번:', gradeDict)

#76번
input = [x for x in range(1, 101)]
visited = [False] * 101
result = []
for item in input:
    if item == 1: continue
    if visited[item] == False:
        result.append(item)
        for i in range(item, 101, item):
            visited[i] = True
print('76번 :', result)

#77번
itemlist = [1,2,3,4]
print('77-1 : lenght(길이) 약자 구하기', len(itemlist))
print('77-2 : 최소 값 구하기', min(itemlist))
print('77-3 : 최대 값 구하기', max(itemlist))
print('77-4 : 합 구하기', sum(itemlist))

#78번
print("78-1 : 테스트입니다", end="")
print("78-2 : 테스트입니다", "테스트입니다", sep="@")
print("78-3 : 테스트입니다", end="\t")
print("78-4 : 테스트입니다", end="\n")
print("78-5 : {0}월 {1}일 입니다.".format(4,9))

#79번
student = ['조현희', '정유림', '배성현', '배성현']
print('79-1 : ', student * 2)
print ('79-2 : ', student.index('배성현'))
print('79-3 : ', student.count('배성현'))

#80번
student = ['조현희', '정유림', '배성현', '배성현']
print('80-1 : reversedStudent = sorted(stuedent,reversed=True)')
print('80-2 : student.sort()')

#81번
student = ['조현희', '정유림', '배성현', '배성현']
print('81-1 : tmp = student[:]', student[:])
print('82-1 : tmp = [x for x in student]', [x for x in student])

#82번
def temp(x,y,z):
    return x+y+z
print('82 : \ndef temp(x,y,z):\n\trerurn x+y+z')

#83번
s = ' abcabcabcefgj abcabcabcefgj '
print('83-1 : ', s.count('a'))
print('83-2 : ', s.index('a'))
s = s.strip()
print('83-3 : ', s.startswith('abc'))
print('83-4 : ', s.endswith ('fgj'))
print('83-5 : ', s.partition(' '))
print('83-6 : ', s.find('abce'))
print('83-7 : ', s.upper())
print('83-8 : ', s.lower())

#84번
print('84 : from, import, from')
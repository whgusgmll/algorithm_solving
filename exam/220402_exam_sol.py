## 64번
### list comprehension을 사용하여
### exam_input = ('4', '6', '-3') 일 때 exam_output변수를 [4,6,3]으로 만드세요
exam_input = ('4', '6' ,'-3')
exam_output = [int(x) for x in exam_input]
print('64 : ', exam_output)

## 65번
### list comprehension을 사용하지 않고,
### exam_input = ('4', '6', '-3') 일 때 exam_output변수를 [4,6,3]으로 만드세요
exam_input = ('4', '6', '-3')
exam_output = []
for i in exam_input:
    exam_output.append(int(i))
print('65 : ', exam_output)

## 66번
### lst = [6,2,7,4,5,1] 을 내림차순으로 sorting해서 ans라는 변수에 넣으세요 (2가지 방법 다 사용)
lst = [6,2,7,4,5,1]
lst.reverse()
ans = lst
print('66 : ', ans)

## 66-2번 (2번째 방법은 여기에)
ans = sorted(lst, reverse = True)
print('66-2 : ', ans)

## 67번
### lst = [6,2,7,4,5,1] 을 오름차순으로 sorting해서 ans라는 변수에 넣으세요
ans = sorted(lst)
print('67 : ', ans)

## 68번
### key가 사람이름 (배성현, 정유림, 조현희) value가 (6,9,3) 인 blueDream이라는 변수의 dictoinary를 만드세요
blueDream = dict()
blueDream['배성현'] = 6
blueDream['정유림'] = 9
blueDream['조현희'] = 3
print('68 : ', blueDream)

## 68 - 2 번 
### blueDream 딕셔너리를 for문으로 돌리면서 정유림, 조현희 key의 값에 *2를 하고 blueDream이라는 변수에 업데이트 하세요
for key, value in blueDream.items():
    if key in ['정유림', '조현희']:
        blueDream[key] *= 2
print('68 - 2', blueDream)

## 68 - 3 번
### blueDream 딕셔너리에서 key만 다 뽑아서 keyList라는 변수에 list형태로 바꾸어서 print하세요
print('68 - 3', list(blueDream.keys()))

## 68 - 4 번
### blueDream 딕셔너리에서 value만 다 뽑아서 valueList라는 변수에 list형태로 바꾸어서 print하세요
print('68 - 4', list(blueDream.values()))

## 68 - 5 번
### blueDream 딕셔너리에서 key가 배성현인 item을 제거하고 items를 다 뽑아서 itemsList라는 변수에 list 형태로 바꾸어서 print하세요
itemList = list(blueDream.items())
print('68 - 5', itemList)

## 69번
### 해당하는 Naming Convention은??
#### 소문자 시작, 중간중간에 단어구분을 대문자로
#### 변수 명명에 주로 쓰임
print('69 : camelCase')

## 70번
### 해당하는 Naming Convention은??
#### 소문자 시작, 중간중간에 _ 로 단어 구분
#### 변수 명명에 주로 쓰임
print('70 : snake_case')

## 71번
### 해당하는 Naming Convention은??
## 대문자 시작, 중간중간에 단어구분을 대문자로
## 클래스, 함수명명에 주로 쓰임
print('71 : PascalCase')

## 72번
### 변수 a,b,c 에 각각 1,2,3을 할당하세요
a,b,c = 1,2,3
print('72 : a,b,c = 1,2,3')

## 72-1
### 할당 된 변수 a,b,c의 값이 각각 2,3,1 이 되도록 만드세요(swap 이용)
a,b,c = b,c,a
print('72-1 : a,b,c = b, c, a')


## 73번
### seq = [1,2,3,4,5] 가정했을 때 first = 1, left = [2,3,4,5]로 나누세요
seq = [1,2,3,4,5]
first, *left = seq
print('73 : first, *left = seq')

## 74번 간이 구구단 만들기
### 2 * 1 = 2
### 2 * 2 = 4
### 2 * 3 = 6
### 
### 3 * 1 = 3
### 3 * 2 = 6
### 3 * 3 = 9
### 결과 값이 이렇게 나오게 코딩하세요
ans = "for i in range(2, 4):\n\tfor j in range(1, 4):\n\t\tprint(i,'*',j,'=',i*j)\n\tprint()"
print('74 : \n',ans)

for i in range(2, 4):
    for j in range(1, 4):
        print(i,'*',j,'=',i*j)
    print()
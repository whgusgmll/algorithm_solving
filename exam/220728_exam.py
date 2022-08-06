## 문제설명

#시험 점수에 따라 학생의 순위를 매기려 합니다. 동점자 순위는 가능한 순위 중 가장 높은 순위로 매깁니다.
# 예를 들어 학생별 점수가 [90, 87, 87, 23, 35, 28, 12, 46]이면, 학생별 순위는 [1, 2, 2, 7, 5, 6, 8, 4]입니다.
#모든 학생의 점수를 담은 배열 score, 배열 score의 길이 score_len이 매개변수로 주어질 때, 순위를 담은 배열을 return 하도록 solution 함수를 작성해주세요.

## 매개변수 설명
#모든 학생의 점수를 담은 배열 score, 배열 score의 길이 score_len이 solution 함수의 매개변수로 주어집니다.
#score_len은 1 이상 1,000 이하인 자연수입니다.
#점수는 1 이상 100 이하인 정수입니다.

## return 값 설명
#예시
#score   scorelen_len
#1   [90, 87, 87, 23, 35, 28, 12, 46]      
#2   [10, 20, 20, 30]  

## 실행 화면 예시
#solution함수의반환값은[1,2,2,7,5,6,8,4]입니다.
#solution함수의반환값은[4,2,2,1]입니다.

def solution(score):

    # 1. 순위를 저장하기 (중복가능, 없는 순위가 있을 수 있음)
    
    scoreDict = {} ## key-vlue
    sortedScore = sorted(score, reverse=True) #기존의 score는 살린다
    print(score, sortedScore)
    for idx, item in enumerate(sortedScore):
        print(idx, item)
        rank = idx+1
        if item == sortedScore[idx-1]:
            continue
        else:
            scoreDict[item] = rank
    print(scoreDict)
    # 2. 순위에 맞게 score를 대입시기
    answer = []
    for item in score:
        answer.append(scoreDict[item])
    print(answer)
    return answer

test_1 = [90, 87, 87, 23, 35, 28, 12, 46]   
test_2 = [10, 20, 20, 30]  

print(solution(test_1))
print(solution(test_2))
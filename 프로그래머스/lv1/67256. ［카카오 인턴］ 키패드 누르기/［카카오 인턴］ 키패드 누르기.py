def solution(numbers, hand):
    answer = ''
    numDic = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    temp = {'Left':[3,0], 'Right':[3,2]}
    
    for num in numbers:
        useHand = ''
        distanceL = 0
        distanceR = 0
        
        if num in [1,4,7]:
            useHand = 'L'
            temp['Left'] = numDic[num]
        elif num in [3,6,9]:
            useHand = 'R'
            temp['Right'] = numDic[num]
        else:
            distanceL = abs(temp['Left'][0]-numDic[num][0]) + abs(temp['Left'][1]-numDic[num][1])
            distanceR = abs(temp['Right'][0]-numDic[num][0]) + abs(temp['Right'][1]-numDic[num][1])
            if distanceL<distanceR:
                useHand = 'L'
                temp['Left'] = numDic[num]
            elif distanceL>distanceR:
                useHand = 'R'
                temp['Right'] = numDic[num]
            else:
                if hand == 'left':
                    useHand = 'L'
                    temp['Left'] = numDic[num]
                else:
                    useHand = 'R'
                    temp['Right'] = numDic[num]
        
        answer = answer + useHand

    return answer

# 위치를 [0,0] 형태로 -> 숫자1=[0,0] 숫자3=[0,2] 기호*=[3,0] 기호#=[3,2]
# temp에 왼손과 오른손이 누른 숫자의 위치정보 기억
# 눌러야할 숫자위치와 손 위치 거리 -> [x,y]에서 (x끼리 차이 + y끼리 차이)
def solution(lottos, win_nums):
    resultCorrect = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} #일치개수:순위
    countZero = 0
    countCorrect = 0
    
    for lotto in lottos:
        if lotto==0:
            countZero = countZero + 1
        if lotto in win_nums:
            countCorrect = countCorrect + 1
    
    highResult = resultCorrect[countCorrect + countZero]
    lowResult = resultCorrect[countCorrect]
    result = [highResult, lowResult]
    
    return result
    
    
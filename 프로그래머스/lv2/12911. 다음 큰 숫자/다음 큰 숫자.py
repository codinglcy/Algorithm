def solution(n):
    count1 = 0
    nChange = bin(n)[2:]
    for num in nChange:
        if num == '1':
            count1 = count1 + 1
    
    nPlus = n + 1
    while True:
        count11 = 0
        for nPlusBin in bin(nPlus)[2:]:
            if nPlusBin == '1':
                count11 = count11 + 1
        if count11 == count1:
            return nPlus
        nPlus = nPlus + 1
        
    
# n을 2진수로 변환, 1의 개수 세기
# n에서 1씩 더하면서 각 숫자들을 2진수로 변환, 1의 개수 세기
#   - 1의 개수가 같으면 그 숫자를 return
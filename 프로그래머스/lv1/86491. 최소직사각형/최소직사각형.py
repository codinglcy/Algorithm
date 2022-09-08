def solution(sizes):
    walletLen = [0,0]
    
    for card in sizes:
        card.sort()
    
    for card in sizes:
        if walletLen[0]<card[0]:
            walletLen[0] = card[0]
        if walletLen[1]<card[1]:
            walletLen[1] = card[1]
            
    answer = walletLen[0]*walletLen[1]
    
    return answer
def solution(cards1, cards2, goal):
    
    for word in goal:
        if word in set(cards1):
            if word == cards1[0]:
                cards1.pop(0)
            else:
                return "No"
        else:
            if word == cards2[0]:
                cards2.pop(0)
            else:
                return "No"
        
    
    return "Yes"
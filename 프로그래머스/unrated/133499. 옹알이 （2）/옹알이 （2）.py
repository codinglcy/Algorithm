def solution(babbling):
    count = 0
    canSpeak = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in canSpeak:
            if j+j in i:
                break
            else:
                i = i.replace(j," ")
        if i.strip() == '':
            count += 1

            
    return count
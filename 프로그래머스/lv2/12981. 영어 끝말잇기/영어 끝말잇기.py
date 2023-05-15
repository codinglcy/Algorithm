def solution(n, words):
    temp = set()
    tempAl = ''
    count = 0

    for word in words:
        count = count + 1
        
        if len(temp) == 0:
            temp.add(word)
            tempAl = word[-1]
            continue
        
        if word in temp:
            break
        
        if tempAl == word[0]:
            temp.add(word)
            tempAl = word[-1]
        else:
            break
            
        if count == len(words):
            return [0,0]
    
    if count % n == 0:
        return [n, count//n]
    else:
        return [count%n, (count//n)+1]
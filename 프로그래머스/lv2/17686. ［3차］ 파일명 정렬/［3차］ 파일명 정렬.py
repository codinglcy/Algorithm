def solution(files):
    tempList = []
    
    for file in files:
        head = ""
        number = ""
        tail = ""
        for i in range(len(file)):
            if len(head) == 0:
                if file[i].isdigit():
                    head = file[:i]
                    headnum = i
            elif not(file[i].isdigit()):
                number = file[headnum:i]
                tail = file[i:]
                break
            elif i == headnum+5:
                number = file[headnum:i]
                tail = file[i:]
                break
                
            if len(number) == 0 and i == len(file)-1:
                number = file[headnum:]
                break
                
        tempList.append((head,number,tail))
    
    tempAnswer = sorted(tempList, key = lambda x: (str.lower(x[0]), int(x[1])))
    
    answer = list(map(lambda x: "".join(x), tempAnswer))
    
    return answer

# isdigit() True 나오면 잘라서 앞부분까지 HEAD
# 그 뒤에 isdigit() False 나오는 부분까지 NUMBER
# 나머지 부분 TAIL

# HEAD: 대소문자 구분 없이 정렬 (list.sort(key=str.lower))
#   NUMBER: 숫자순 정렬 (list.sort(key=int))
#       TAIL: 주어진 순서
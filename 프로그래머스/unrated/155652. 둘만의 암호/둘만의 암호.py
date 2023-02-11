def solution(s, skip, index):
    temp = []
    sCodeList = list(map(ord,list(s)))
    skipCodeSet = set(map(ord,list(skip)))
    
    for a in sCodeList:
        count = 0
        changeA = a
        
        while count<index:
            if changeA<122:
                changeA = changeA + 1
            else:
                changeA = 97
            
            if changeA not in skipCodeSet:
                count = count + 1
        
        temp.append(changeA)
    
    answer = ''.join(list(map(chr,temp)))

    return answer


# 아스키코드 사용 -> 'a'=97, 'z'=122 / ord(알파벳)=숫자 chr(숫자)=알파벳
# while문 - count 변수를 선언해서 알파벳을 셀 때 마다 1 더하기
#           count와 index가 같아지면 탈출
#           skip - split리스트->set. in으로 확인, 있으면 count 더하지 않음
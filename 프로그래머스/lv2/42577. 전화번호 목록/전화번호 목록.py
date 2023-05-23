def solution(phone_book):
    phone_book.sort(key=lambda x: (x,len(x)))
    
    for i in range(len(phone_book)-1):
        short = phone_book[i]
        long = phone_book[i+1]
        
        if short == long[:len(short)]:
            return False
    
    return True

# 각 번호의 길이가 짧은 순 정렬
# len(phone_book)-2 까지 각 번호의 뒤에 있는 번호들과 비교
# 하나라도 있으면 return False
# 다 돌았는데 없으면 return True
def solution(price, money, count):
    totalPrice = 0
    
    for count in range(1,count+1):
        totalPrice = totalPrice + count*price
    
    result = money - totalPrice
    
    if result>=0:
        return 0
    else:
        return abs(result)
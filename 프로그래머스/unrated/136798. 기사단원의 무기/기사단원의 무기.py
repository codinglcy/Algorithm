def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        count = 0
        for i in range(1, int(num**(1/2))+1):
            if num%i == 0:
                if num == i*i:
                    count += 1
                else:
                    count += 2
            
            if count > limit:
                answer = answer + power
                break
        
        if count <= limit:
            answer = answer + count
    
    return answer

# 약수의 개수 구하는 반복문 작성 - 개수가 limit을 넘어가면 power 출력
from itertools import permutations

def solution(numbers):
    nums = set()
    
    for permuR in range(1,len(numbers)+1):
        numlist = list(permutations(numbers,permuR))

        for nset in numlist:
            temp = ''
            for i in range(len(nset)):
                temp += nset[i]
            
            temp = int(temp)
            
            if isPrime(temp):
                nums.add(temp)
    
    return len(nums)
        
def isPrime(num):
    print(num)
    if num == 1 or num == 0:
        return False
    if num in [2,3,5,7]:
        return True
    for n in range(2,(num//2)+1):
        if num%n == 0:
            return False
    return True
    


# 중복을 피하기 위해 만든 숫자조합을 저장하는 공간은 set()
# 앞에 붙은 0은 없는 것과 같은 수로 취급하기 위해 만든 숫자조합을 저장하기 전에 숫자형식으로 변환
#
# 숫자 n이 소수인지 아닌지 구분하는 함수 생성
#  - n을 2부터 n//2까지의 수로 나누었을때 나누어 떨어지지 않아야함
#
# 조합 만들기 - permutations 사용
# (https://docs.python.org/ko/3/library/itertools.html)

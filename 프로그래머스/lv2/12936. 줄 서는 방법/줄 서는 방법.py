def solution(n, k):
    answer = []
    nums = []
    for nn in range(1,n+1):
        nums.append(nn)
    
    for i in range(n-1, 0, -1):
        fac = factorial(i)
        for j in range(1, i+2):
            if fac*j >= k:
                answer.append(nums[j-1])
                nums.pop(j-1)
                k = k - fac*(j-1)
                break
    answer.append(nums[0])
    
    return answer

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

# 2명 -> 12 / 21
# 3명 -> 123 132 / 213 231 / 312 321
# 4명 -> 1234 1243 1324 1342 1423 1432 / 2134 2143 2314 2341 2413 2431 / 3124 3142 3214 3241 3412 3421 / 4123 4132 4213 4231 4312 4321
#
# n명일때 1이 맨앞에 오는 개수: n-1개
# k가 (n-1)!보다 크고 (n-1)!*2보다 작을때 제일 앞의 숫자는 2이다.
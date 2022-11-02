def solution(a, b, n):
    answer = 0
    
#     def coke(a, b, n, count):
#         if n < a:
#             return count
#         count = count + b*(n//a)
#         n = b*(n//a) + n%a
#         return coke(a, b, n, count)
    
    while n >= a:
        answer = answer + b*(n//a)
        n = b*(n//a) + n%a
    
    return answer
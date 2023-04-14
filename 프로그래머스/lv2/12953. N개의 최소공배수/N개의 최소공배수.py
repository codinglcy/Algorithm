def solution(arr):
    temp = []

    for num in arr:
        if len(temp) == 0:
            temp.append(num)
        else:
            temp.append(lcm(temp[-1], num))
    
    return temp[-1]

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)


# 세 수의 최소공배수 = 두 수의 최소공배수 l과 나머지 한 수의 최소공배수
# temp 리스트에 각 두 수의 최소공배수를 구해 append하고 마지막 요소와 새 수의 최소공배수를 구해 또 append 하는 방식으로 result를 구한다.

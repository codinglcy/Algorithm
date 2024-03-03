def solution(numbers):
    answer = ''

    numbers.sort(key=lambda num:str(num)*3, reverse=True)
    numberstr = [str(num) for num in numbers]
    
    answer = str(int("".join(numberstr)))

    return answer


# 숫자로 된 문자열을 정렬하면 사전규칙에 따라 정렬된다 (ex.6,10,67 -> 10,6,67)
#
# 3,30,34중 조합했을때 가장 큰 수를 만들려면 34,3,30순으로 정렬되어야한다.
#  -> 각 문자열을 세번씩 반복시켜 만든 문자열로 비교 (3-333, 30-303030, 34-343434)
#  -> 사전순 정렬하면 303030,333,343434가 된다. reverse=True로 거꾸로 정렬해주면 됨
arrLength = int(input())
numbers = list(map(int, input().split()))

sortedNum = sorted(numbers)
numIndex = []
result = ''

for i in numbers:
    numIndex.append(sortedNum.index(i))
    sortedNum[sortedNum.index(i)] = -1

result = ' '.join(str(n) for n in numIndex)
print(result)
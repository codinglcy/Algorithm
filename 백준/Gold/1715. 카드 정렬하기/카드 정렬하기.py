import heapq

arrLength = int(input())
arr = []
for i in range(0, arrLength):
    arr.append(int(input()))

heapq.heapify(arr)

result = 0

while len(arr) != 1 :
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    plusAB = a+b
    
    result += plusAB
    heapq.heappush(arr, plusAB)


print(result)



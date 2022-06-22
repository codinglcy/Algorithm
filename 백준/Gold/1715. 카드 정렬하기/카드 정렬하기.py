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

    heapq.heappush(arr, a+b)
    result += (a+b)

    if len(arr) == 1 :
        break

print(result)


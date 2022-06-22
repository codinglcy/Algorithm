arrLength = int(input())
words = []
for i in range(0,arrLength):
    words.append(input())

# 2. 사전 순

words.sort()

# 1. 단어길이로 sort

words.sort(key=len)

# 중복제거
sortedWords = []

for w in words:
    if w not in sortedWords:
        sortedWords.append(w)

# 출력
for i in sortedWords:
    print(i)


from collections import deque

def solution(cacheSize, cities):
    totalTime = 0
    Q = deque(maxlen=cacheSize)
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        if city not in Q:
            Q.append(city)
            totalTime = totalTime + 5
        else:
            Q.remove(city)
            Q.append(city)
            totalTime = totalTime + 1
        
    
    return totalTime

# deque 사용, 크기는 주어진 캐시크기로 지정
# 도시 이름을 순서대로 deque에 넣는다
# 넣을 도시이름이 deque에 이미 있다면 cache hit, 아니면 cache miss
# cache hit이면 이미 있는 것을 제거 후 새롭게 넣어준다.
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    def mix(first, second):
        return first + (second * 2)
    
    while len(scoville) >= 2:
        minS = heapq.heappop(scoville)
        if minS >= K:
            return answer
        else:
            secS = heapq.heappop(scoville)
            heapq.heappush(scoville, mix(minS,secS))
            answer = answer + 1
    
    if heapq.heappop(scoville) >= K:
        return answer
    else:
        return -1



# 한번 섞을 때 마다 sort...는 시간복잡도가 걸림.. 그래도 해보기
# 전체가 아니라 K보다 작은 리스트(lowS)를 따로 작성해서 거기서 sort 하면 그래도 나을것같음..
# 섞은 뒤 K보다 크면 K이상인 수중 가장 작은 수 minOverK와 비교, 아니면 lowS에 추가

#45분

# heapq 사용 -> heappop 하면 자동으로 가장 작은 수 pop해줌

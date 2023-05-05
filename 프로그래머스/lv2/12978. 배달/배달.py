import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    dic = {}
    for i in range(1,N+1):
        dic[i] = float("inf")
    # print(graph, dic)
    
    for r in road:
        a, b, c = r
        graph[a].append((b,c))
        graph[b].append((a,c))
    # print(graph)
    
    def dijkstra(start):
        q = []
        dic[start] = 0
        heapq.heappush(q, (0, start))
        # print(dic, q)
        
        while q:
            dist, now = heapq.heappop(q)
            # print("q,dist,now",q, dist, now, dic[now])

            if dic[now] < dist:
                continue 

            for i in graph[now]:
                # print("i", i)
                cost = dist + i[1]

                if cost < dic[i[0]]:
                    dic[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    dijkstra(1)
    # print(dic)
    
    return len([d for d in dic if dic[d] <= K])
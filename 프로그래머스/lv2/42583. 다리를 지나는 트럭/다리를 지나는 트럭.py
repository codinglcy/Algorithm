from functools import reduce

def solution(bridge_length, weight, truck_weights):
    time = 0
    now = []

    while len(truck_weights) > 0:
        if len(now) > 0 and time - now[0][1] == bridge_length:
            now.pop(0)
        
        now_weight = reduce(lambda acc, value: acc+value, list(map(lambda x: x[0], now)), 0)
        
        if now_weight + truck_weights[0] <= weight:
            if len(truck_weights) == 1:
                time = time + bridge_length+1
                break
            popTruck = truck_weights.pop(0)
            now.append((popTruck,time))
        time = time + 1
        
    return time
    
    
# 0         []      []      [10]
# 1~100     []      [10]    []
# 101       [10]    []      []

# 0         []      []      [10,10,10,10,10,10,10,10,10,10]
# 1         []      [10]       [10,10,10,10,10,10,10,10,10]
# 2         []      [10,10]       [10,10,10,10,10,10,10,10]
# 3         []      [10,10,10]       [10,10,10,10,10,10,10]
# 4         []      [10,10,10,10]       [10,10,10,10,10,10]
# 5         []      [10,10,10,10,10]       [10,10,10,10,10]
# 6         []      [10,10,10,10,10,10]       [10,10,10,10]
# 7         []      [10,10,10,10,10,10,10]       [10,10,10]
# 8         []      [10,10,10,10,10,10,10,10]       [10,10]
# 9         []      [10,10,10,10,10,10,10,10,10]       [10]
# 10~100    []      [10,10,10,10,10,10,10,10,10,10]      []
# 101       [10]       [10,10,10,10,10,10,10,10,10]      []
# 102       [10,10]       [10,10,10,10,10,10,10,10]      []
# 103       [10,10,10]       [10,10,10,10,10,10,10]      []
# 104       [10,10,10,10]       [10,10,10,10,10,10]      []
# 105       [10,10,10,10,10]       [10,10,10,10,10]      []
# 106       [10,10,10,10,10,10]       [10,10,10,10]      []
# 107       [10,10,10,10,10,10,10]       [10,10,10]      []
# 108       [10,10,10,10,10,10,10,10]       [10,10]      []
# 109       [10,10,10,10,10,10,10,10,10]       [10]      []
# 110       [10,10,10,10,10,10,10,10,10,10]      []      []

# 차가 들어섬과 동시에 1초
# 길이 10의 다리를 차 한대가 지나가는 시간 11초
# 차 한대가 들어서면 truck_weights.pop(0)와 now.append((truck_weights.pop(0),time))와 time+1
#
# while truck_weights 길이가 0보다 큰 동안
#   time - (now의 첫번째 요소가 들어간 시간) 이 bridge_length와 같으면 pop(0)
#   now_weight + (대기 첫번째 트럭 weight) 가 bridge_length 보다 작거나 같을때
#       truck_weights 길이가 1이면
#           time = time + bridge_length+1
#           break
#       popTruck = truck_weights.pop(0)
#       now.append((popTruck,time))
#   time = time + 1

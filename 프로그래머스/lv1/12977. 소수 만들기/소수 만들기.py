import math

def solution(nums):
    resDic = {}
    noAns = set()
    answer = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                res = nums[i] + nums[j] + nums[k]
                if resDic.get(res) == None:
                    resDic[res] = 1
                else:
                    resDic[res] = resDic[res] + 1

    for r in set(resDic.keys()):
        for n in range(2,int(math.sqrt(r))+1):
            if r%n == 0:
                noAns.add(r)
                break

    ans = set(resDic.keys())-noAns
    for a in ans:
        answer = answer + resDic[a]
        
    return answer
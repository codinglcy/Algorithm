def solution(nums):
    pick = len(nums)//2
    setNums = set(nums)
    
    return min(pick, len(setNums))
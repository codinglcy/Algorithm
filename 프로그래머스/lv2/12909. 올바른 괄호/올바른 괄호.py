from collections import deque

def solution(s):
    answer = True
    q = deque()

    for thing in s:
        if thing == "(":
            q.append(thing)
        else:
            if not q:
                answer = False
                break
            elif q[-1] == "(":
                q.pop()
            else:
                answer = False
                break 

    if q:
        answer = False
    return answer
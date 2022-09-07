def solution(id_list, report, k):
    answer = {}
    userRepo = {}
    repoDic = {}
    stopId = []
    
    for id in id_list:
        answer[id] = 0
        userRepo[id] = 0
        repoDic[id] = []
    
    for repo in report:
        [user, reportedUser] = repo.split(" ")
        
        if user not in repoDic[reportedUser]:
            userRepo[reportedUser] = userRepo[reportedUser] + 1
            repoDic[reportedUser].append(user)
    
    for id in id_list:
        if userRepo[id] >= k:
            stopId.append(id)
        
    for stop in stopId:
        for user in repoDic[stop]:
            answer[user] = answer[user] + 1
    
    return list(answer.values())
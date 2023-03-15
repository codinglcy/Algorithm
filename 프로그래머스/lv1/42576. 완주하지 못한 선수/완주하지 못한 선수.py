def solution(participant, completion):
    parSet = set(participant)
    comSet = set(completion)
    parDic = {}

    if parSet == comSet:
        for name in participant:
            if parDic.get(name) == None:
                parDic[name] = 1
            else:
                parDic[name] = parDic[name] + 1
        for name in completion:
            if parDic[name] > 1:
                parDic[name] = parDic[name] - 1
            else:
                parDic.pop(name)
        return next(iter(parDic))
    else:
        return (parSet-comSet).pop()
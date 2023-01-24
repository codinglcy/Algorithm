def solution(new_id):
    result = ''
    rule = {'-', '_', '.'}
    
    print('0단계', new_id)
    
    for char in new_id:
        if char.isdigit() or char.islower() or (char in rule):
            continue
        elif char.isupper():
            new_id = new_id.replace(char, char.lower())
        else:
            new_id = new_id.replace(char,'') # 2단계
    # print('1단계&2단계', new_id)
    
    while '..' in new_id:
        new_id = new_id.replace("..", ".") # 3단계
    # print('3단계', new_id)
    
    new_id = new_id.strip(".") # 4단계  
    # print('4단계', new_id)
    
    if len(new_id)==0:
        result = 'a'
    else:
        result = new_id # 5단계
    # print('5단계', result)
    
    if len(result)>=16:
        result = result[:15]
        if result[-1]=='.':
            result = result[:14] # 6단계
    # print('6단계', result)
    
    if len(result)<=2:
        while len(result)<3:
            result = result + result[-1] # 7단계
    # print('7단계', result)
    
    return result
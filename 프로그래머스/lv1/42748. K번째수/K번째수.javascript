function solution(array, commands) {
    let answer = [];
    let middleResult = [];
    
    commands.map((cmd) => {
        middleResult = array.slice(cmd[0]-1, cmd[1])
                            .sort((a,b) => a - b);
        answer.push(middleResult[cmd[2] - 1]);
    });
    
    return answer;
}
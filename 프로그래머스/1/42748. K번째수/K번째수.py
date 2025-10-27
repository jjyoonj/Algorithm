def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        a=[]
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        for x in range(i-1,j):
            a.append(array[x])
        a.sort()
        if len(a) == 1:
            answer.append(a[0])
        else:
            answer.append(a[k-1])
    
    return answer


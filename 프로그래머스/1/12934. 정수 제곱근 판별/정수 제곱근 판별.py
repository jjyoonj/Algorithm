def solution(n):
    answer = 0
    x = n**(1/2)
    if x.is_integer():
        answer = (x+1)**2
    else:
        answer = -1
    return answer
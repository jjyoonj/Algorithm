def solution(n):
    answer = 0
    n = ''.join(sorted(str(n),reverse=True))
    answer = int(n)
    return answer
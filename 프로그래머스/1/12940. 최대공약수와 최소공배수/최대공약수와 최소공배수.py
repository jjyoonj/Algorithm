def solution(n, m):
    answer = []
    def gcd(n,m):
        while m!=0:
            n, m = m, n % m
        return n
    def lcm(n,m):
        return n*m//gcd(n,m)
    
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
        
        
    return answer
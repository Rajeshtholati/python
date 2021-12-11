def prime(n):
    if n==1:
        return False
    for i in range(2, n//2+1):
        if n%i==0:
            return False
        return True
def prime_in_series(a,b):
    for i in range(a,b+1):
        if prime(i):
            print(i,end=' ')
a,b=map(int, input().split())
prime_in_series(a,b)
    

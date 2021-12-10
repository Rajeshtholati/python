def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
        if fc==2:
            return True
        else:
            return False
x=int(input())
if prime(x)==True:
    print(x,'is prime')
else:
    print(x,'is not prime')

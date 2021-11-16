# collatz sequence number of steps to reach 1
n=int(input())

count=0
print(n,end=' ')
while n!=1:
    if n%2==0:
       n=n//2
    else:
        n=3*n+1
    count+=1
    print(n,end=' ')
print('\n no of steps taken',count)



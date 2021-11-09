n=int(input())

print(a,b,end=' ')
c=a+b
while(c<=n):
    print(c,end=' ')
    a,b=b,c
    c=a+b

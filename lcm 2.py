a,b=map(int,input().split())
if a>b:
    a,b=b,a
m=b
while b%a !=0:
    b +=m
print(b)

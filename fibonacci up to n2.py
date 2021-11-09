# fibonacci up to n
n=int(input())
a=0
b=1
while n>1:
    a,b=b,a+b
    n-=1
print(a)

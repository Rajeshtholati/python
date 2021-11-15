#finding odd and even in a number and sum of their sqaers
z=int(input())
n=0
while z:
    r=z%10
    n=n*10+r
    z=z//10
print(n)
e=0
o=0
while n:
    r=n%10
    if r%2==0:
        e=e*10+r
    else:
        o=o*10+r
    n=n//10
print(e,o)
print(e**2+o**2)

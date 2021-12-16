#euclid algorithm to find gcd
a,b=map(int,input().split())
r=0
while b:
    if a>b:
        a,b=b,a
    b=b%a
print(a)

# second model
a,b=map(int,input().split())
while b:
    a,b=b,a%b
print (a)

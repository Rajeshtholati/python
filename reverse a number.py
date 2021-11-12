#reversing a given number
n=int(input())
r=0
while n:
    x=n%10
    r=r*10+x
    n=n//10
    if r==n:
        print('palindrome')
        else:
            print('not palindrome')
print(r)

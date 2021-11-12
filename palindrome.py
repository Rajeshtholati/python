#palindrome or not
n=int(input())
t=n
r=0
while n:
    x=n%10
    r=r*10+x
    n=n//10
if r==t:
    print('palindrome')
else:
    print('not palindrome')


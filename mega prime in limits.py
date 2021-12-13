#mega prime
#function to find given is prime or ot
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
#function to find if all digits are prime or not

def digit_prime(x):
    while x:
        r=x%10
        if is_prime(r)==False:
            return False
        x=x//10
    return True
#function to find if the number is mega prime or not
def mega_prime(z):
    if is_prime(z) and digit_prime(z):
        return True
    return False

a,b=map(int,input().split())
for i in range(a,b+1):
    if mega_prime(i):
        print(i,end=' ')

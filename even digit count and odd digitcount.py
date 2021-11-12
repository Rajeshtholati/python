#find out the even digit count and odd digit count in given n
n=int(input())
e_d_c=0
o_d_c=0
while n:
    r=n%10
    if r%2==0:
        e_d_c+=1
    else:
        o_d_c+=1
    n=n//10
print(e_d_c,o_d_c)

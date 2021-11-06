#program to print different tables in reverse order
a=int(input())
b=int(input())
if (b!=a):
    while b>=a:
        i=12
        c=1
        if(i!=c):
            while(i>=c):
                print(a,'x',i,'=',a*i)
                i-=1
        print()
        b-=1

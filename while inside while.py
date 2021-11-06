#program to print different tables
a=int(input())
b=int(input())
while a<=b:
    i=1
    while i<=12:
        print(a,'x',i,'=',a*i)
        i+=1
    print()
    a+=1

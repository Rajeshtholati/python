a=int(input('enter a number'))
b=int(input('enter a number'))
c=int(input('enter a number'))
if (a>b and a>c):
    print(a,'is big')
elif (b>c and b>a):
    print(b,'is big')
elif (c>a and c>b):
    print(c,'is big')
else:
    print('equal')
    

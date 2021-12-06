#to print 1 on both the diagonals
n=int(input())
for i in range(n):
    for j in range(n):
       if i+j==n-1:
           print(1,end=' ')
       elif i==j:
           print(1,end=' ')
       else:
           print(0,end=' ')
    print()

#list in list
n=int(input())
super_list=[]
for i in range(n):
    sub_list=list(map(int,input().split()))
    super_list.append(sub_list)
y=z=0
for i in range(n):
    for j in range(n):

        if i==j:
            y+=super_list[i][j]
        if i+j==n-1:
            z+=super_list[i][j]
print(abs(y-z))

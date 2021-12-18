#find max of list without using max() or sort()
m=0
l=list(map(int,input().split()))
for i in l:
    if i>m:
        m=i
print(m)
#find min with out using min() or sort()
m=100000
l=list(map(int,input().split()))
for i in l:
    if i<m:
        m=i
print(m)

fom random import *
marks=[[randint(45,100)for i in range(5)]for j in range(10)]
a=list(map(max,marks))
b=list(map(min,marks))
c=list(map(sum,marks))
print(a)
print(b)
print(c)



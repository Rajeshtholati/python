# user defined functions
def location(x,y,z):
    print(x,'is a city that is located in',y,'which is in',z)
city,country,asia=map(str,input().split())    
location(city,country,asia)

     #factioral#
def sample(n):
    r=1 
    for i in range(1,n+1):#range(n,0-1)
        r*=i
    return r
n=int(input())
print(sample(n))

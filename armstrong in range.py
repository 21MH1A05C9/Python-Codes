a=int(input())
b=int(input())
for n in range(a, b+1):
    l=0
    t=n
    while n:
       l+=1
       n=n//10
    s=0
    t1=t
    while t:
        s+=(t%10)**l
        t=t//10
    
    if s==t1:
        print(t1)



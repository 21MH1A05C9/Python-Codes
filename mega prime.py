'''
n=int(input())
c=0
d=0
p=0
temp=n
for i in range(2,n+1):
     if n%i==0:
        c+=1
if c==1:
    while(n):
        d+=1
        if n&10==2 or n%10==3 or n%10==5 or n%10==7:
            p+=1
        else:
            break
        n//=10
if n==0 and d==p:
    print(temp,'is mega prime')
else:
    print(temp,'is  not mega prime')
'''

'''
n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        print('Not prime')
        break
else:
        d=0
        pd=0
        while n:
            n=n//10
            r=n%10
            d+=1
        
            for i in range(2,(r//2)+1):
                if r%i==0:
                    break
            else:
                pd+=1
        if d==pd:
            print('mega prime')
        else:
            print('Not a mega prime')
'''

'''
n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        print('Not prime')
        break
else:
        d=0
        pd=0
        while n:
            r=n%10
            n=n//10
            d+=1
            if r==1 or r==2 or r==3 or r==5 or r==7:
                pd+=1
        if d==pd:
            print('mega prime')
        else:
            print('Not a mega prime')

'''

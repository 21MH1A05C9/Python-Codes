##function is used for code re-usability
##fuction has two types--->function defination--->actual code(total code we store in function defination)
##                        --->function call--------->

##def sample(a,b):
##    print(a+b)
##    
##a=int(input())
##b=int(input())
##sample(a,b)

##def sample(a,b):
##    print(a-b)
##    
##a=int(input())
##b=int(input())
##sample(a,b)

##def sample(a,b):
##    print(a*b)
##    
##a=int(input())
##b=int(input())
##sample(a,b)

##def sample(a,b):
##    print(a//b)
##    
##a=int(input())
##b=int(input())
##sample(a,b)

##def sample(a,b):#formal parameters
##    print('addition =',a+b)
##    print('subtration =',a-b)
##    print('multiplication=',a*b)
##    print('division =',a//b)
##    
##a=int(input())
##b=int(input())
##sample(a,b)#actual parameters

##def sample(a,b):
##    print(a+b)
##    
##a=int(input())
##b=int(input())
##sample(a,b)
##print('hi')
##sample(20,60)

def add(a,b):
    print('addition =',a+b)
def sub(a,b):
    print('subtration =',a-b)
def mulit(a,b):
    print('multiplication=',a*b)
def div(a,b):
    print('division =',a//b)

a=int(input())
b=int(input())
c=int(input())
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    mulit(a,b)
elif c==4:
    div(a,b)
else:
    print('invalid')

import math
#1st way to find out the length of a number 
n=int(input())
l=0
t=n
while n:
    l=l+1
    n=n//10
print(l)

s=0
t1=t
while t:
    r=t%10
    s+=r**1
    t=t//10
    
print(t1,"is Armstrong") if s==t1 else print(t1,"is Not")


#2 nd way to find the length of a given number
#le=int(math.log10(n)+1

#3 rd way to find tne length of a given number
#length=len(str(n))

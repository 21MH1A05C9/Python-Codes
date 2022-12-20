##arr=list(map(int,input().split()))
##s=0
##for i in arr:
##    s+=1
##print(s)

##a=list(map(int,input().split()))
##m=a[0]
##for i in a:
##    if i<m:
##        m=i
##print(m)

##a=list(map(int,input().split()))
##m=a[0]
##for i in a:
##    if i>m:
##        m=i
##print(m)

##a=list(map(int,input().split()))
##b=int(input())
##print(a.count(b))

##a=list(map(int,input().split()))
##b=int(input())
##c=0
##for i in a:
##    if b==i:
##      c+=1
##print(c)

##arr=list(map(int,input().split()))
##b=int(input())
##for i in range(0,len(arr)):##(len(a))
##    if b==arr[i]:
##        print(i)##(i,end=' ')

##a=list(map(int,input().split()))
##b=int(input())
##for i in range(0,len(a)):
##    if a[i]==b:
##        print(a.index(b))
##        a[i]+=1 ##a[i]=-1 ## a[i]=1
##    '''if(max(arr)!=x):
##        arr[i]=max(arr)
##    elif min(arr)!=x:
##        arr[i]=min(arr)'''

a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b and a.count(i)>1:
        b.append(i)
print(*b)
##for i in b:
##    print(i,end=' ')








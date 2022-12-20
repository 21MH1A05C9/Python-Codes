def decbin(n):
    while n>0;
          r=n%2
          print(r,end=' ')
          n//=2
          print(n)
n=int(input())
print(decbin(n))

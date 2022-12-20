##0, 1, 1, 2, 3, 5,  8,  13,  21, 34, 55, 89
##1  2  3  4  5  6   7   8    9  10   11  12

   ## fibnocci ##
##def fib(n):
##   a,b=0,1
##   print(a,b,end=' ')
##   for i in range(2,n+1):
##       c=a+b
##       print(c,end=' ')
##       a=b
##       b=c
##
##n=int(input())
##fib(n)
       

## fibnocci of near number ##
def fib(n):
    a,b=0,1
    i=2
    while True:
        c=a+b
        a=b
        b=c
        if b>n:
            print(a)
            break
        i+=1
n=int(input())
fib(n)

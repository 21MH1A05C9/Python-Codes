##def fin(n):
##    if n<=1:
##        return n
##    return fib(n-1)+fib(n-2)
##
##n=int(input())
##for i in range(n):
##    print(fib(i))

def bindec(n):
    i=0
    r=0
    while True:
        rem=n%10
        r=r+rem*(2**i)
        n//=10
         i+=1
    return r
n=int(input())
print(bindec(n))

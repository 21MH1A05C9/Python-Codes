def maxSumLCM(n):
    max_sum=0
    i=1
    while(i*i<=n):
        if(n%i==0):
            max_sum=max_sum+i
            if(n//i!=i):
                max_sum=max_sum+(n//i)
        i=i+1
    return max_sum
n=2
print(maxSumLCM(n))

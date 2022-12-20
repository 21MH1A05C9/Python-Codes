n=int(input())
arr=list(map(int,input().split()))
k=sorted(arr)
k1=k[::-2]
print(*k1)

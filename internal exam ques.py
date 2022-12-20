file=open("file1.txt",'w')
try:
 file.write("Hello students, how are you guys?")
finally:
 file.close()
with open("file2.txt",'w') as file:
 file.write("Hello teacher, how are you guys?")

 

 
from itertools import permutations
s=input()
for i in range(2,len(s)):
 for p in permutations(s,i):
     print("".join(p),end=" ")

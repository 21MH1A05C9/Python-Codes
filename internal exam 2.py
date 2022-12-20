file=open("file1.txt",'w')
try:
 file.write("Hello students, how are you guys?")
finally:
 file.close()
with open("file2.txt",'w') as file:
 file.write("Hello teacher, how are you guys?")
 print("hello students,how are you guys?")
 print("hello teacher,how are you guys?")

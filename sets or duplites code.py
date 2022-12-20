##set:unordered list,without duplicates
##declare:{}
##access:len(a),min(a),max(a)
##modify:a.add(4)
##delete:a.remove(4) del a
##a.capitalize(),a.split(),a.find('a'),a.index()
##------------------------------------------------------------
##a=list(map(int,input().split()))
##b=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##print(b)
##------------------------------------------------------------
##a='my_name_is_hari_yuktha_nanda'
##a.split('_')
##['my', 'name', 'is', 'hari', 'yuktha', 'nanda']
##------------------------------------------------------------
##a='my name is hari yuktha nanda'
##a.split()
##['my', 'name', 'is', 'hari', 'yuktha', 'nanda']
##------------------------------------------------------------
##a='hari yuktha nanda'
##a.upper()
##'HARI YUKTHA NANDA'
##a.lower()
##'hari yuktha nanda'
##------------------------------------------------------------
##a='nanda'
##a[::-1]
##'adnan'
##a[::1]
##'nanda'
##------------------------------------------------------------
##a=input()
##for i in a:
##    print(i,end=' ')
##print()
##for i in range
##------------------------------------------------------------
a=input()
c=0
for i in a:
    ##if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
    if i in 'aAeEiIoOuU':
        c+=1;
print(c)        

##class Car():
##    def __init__(self):#constructor
##        pass
##a=Car()#object
##b=Car()

             # class basic code #
##class Car():
##    def __init__(self):
##        print('Hai')
##    def display(self):
##        print('Hello')
##a=Car()#object
##a.display()
##
##b=Car()
##b.display()

##class Car():
##    country='india'
##    def __init__(self,name,model):
##        self.name=name
##        self.model=model
##        
##    def display(self):
##        print(self.name,self.model,self.country)
##        
##a=Car('kia',1234)#object
##a.display()
##
##b=Car('tata',5678)#object
##b.display()

class Student():
    college='Aditya'
    def __init__(self,name,roll,college):
        self.name=name
        self.roll=roll
        self.college=college
        
    def display(self):
        print(self.name,self.roll,self.college)
        
a=Student('kia','1234','ACOE')#object
a.display()

b=Student('tata','5678','ACET')#object
b.display()





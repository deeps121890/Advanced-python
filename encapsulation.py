'''
class Student:
    def __init__(self,no,name,sub):
        print('no:',no)
        print('name:',name)
        print('sub:',sub)
    def display(self,no,name,sub):
        print('no:',no)
        print('name:',name)
        print('sub:',sub)
one=Student(10,'deepika','python')  #object creation
one.display(10,'deepika','python')  #calling the method
'''
o/p: 
no: 10
name: deepika
sub: python
no: 10
name: deepika
sub: python
'''
class Doctor:
    def __init__(self,no,name,spec):
        self.no=no
        self.name=name
        self.spec=spec
        print(self.no)
        print(self.name)
        print(self.spec)
        print('\n')
d=Doctor(1,'sachin','pediatric')

d1=Doctor(2,'veena','ent')
'''
o/p:
1
sachin
pediatric


2
veena
ent



'''
global_variable=40
class Test:
    class_variable=30
    def __init__(self,local_variable):
        self.instance_variable=20
        print(local_variable)
        print(self.instance_variable)
        print(Test.class_variable)
        print(global_variable)
one=Test(10)
'''
o/p: 10
20
30
40
'''
variable=40
class Assignment:
    variable=30
    def __init__(self,variable):
        print(variable)
        print(self.variable)
        print(Assignment.variable)
        print(globals()['variable'])
assign=Assignment(10)
'''
o/p: 10
30
30
40

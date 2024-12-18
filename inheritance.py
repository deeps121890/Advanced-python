'''
class Calac:
    def add(self):
        print('add')
    def sub(self):
        print('sub')
    def mul(self):
        print('mul')
one=Calac()
one.add()
one.sub()
one.mul()
class SciCalac(Calac):
    def sin(self):
        print('sin')
    def cos(self):
        print('cos')
one=SciCalac()
one.sin()
one.cos()
one.add()
one.sub()
one.mul()
'''
o/p:add
sub
mul
sin
cos
add
sub
mul


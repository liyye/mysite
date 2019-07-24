class Bird():
    def fiy(self):
        print('这是鸭子，会飞')

class Duck():
    def fiy(self):
        print('这是鸟，也会飞')

def fiyy(a):
    a.fiy()

b=Bird()
fiyy(b)
bb=Duck()
fiyy(bb)
















































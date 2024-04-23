"""
    crear una clase shape que reciba la x y la y 
    crear una clase rectangulo que hereda de la clase shape
    crear los correspondientes getter y setter para x e y
    https://docs.python.org/3/library/abc.html
"""

class Shape:
    def __init__(self,x,y) -> None:
        self.x =x
        self.y =y
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,x):
        self._x = x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,y):
        self._y= y

class Square(Shape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)        

square = Square(10,10)
print(square.x)
print(square.y)

class A:
    def __init__(self,x):
        self._x=x
class B:
    def __init__(self,y):        
        self._y = y

class C(A,B):
    def __init__(self, x,y):
        #super().__init__(x)
        
        A.__init__(self,x)
        B.__init__(self,y)

        #super(C,self).__init__(x)


c =C(10,5)
print(c._x)
print(c._y)

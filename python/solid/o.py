import uuid
from abc import ABC,abstractmethod


"""
 Crear un sistema que contenga una toolbar que a su vez tendrá
 figuras y colores

 las figuras permitidas son cuadrado y circulo
 los colores son black y white

 crear un canvas que permita 
    agregar figura
    elminar figura

Command pattern

    agregar add type color x y
    elminar remove id

"""

class Color:
    def __init__(self,r:int,g:int,b:int) -> None:
        self.r=r
        self.g=g
        self.b=b

class Shape(ABC):
    def __init__(self,x:int,y:int,color:Color) -> None:        
        super().__init__()
        self.x=x
        self.y = y
        self.color=color
        self.id = uuid.uuid4()   
class Rectangle(Shape):
    def __init__(self, x: int, y: int, color: Color) -> None:
        super().__init__(x, y, color)   
class Circle(Shape):
    def __init__(self, x: int, y: int, color: Color) -> None:
        super().__init__(x, y, color)
   
class ToolBar:
     def __init__(self) -> None:
         self._colors = {}
         self._shapes = {}
     def register_colors(self,key:str,color:Color):
         self._colors.update({key:color}) 
     def get_color(self,key:str)->Color:
         return self._colors.get(key,Color(0,0,0))
     def register_shapes(self,key:str,factory):    
        self._shapes.update({key:factory})
     def get_shape(self, key:str,*args)->Shape:
        return self._shapes.get(key)(*args) 
     


class Canvas:
    def __init__(self) -> None:
        self._shapes = []
    def add():
        pass
    def remove(str):
        pass    
    
class Application:
    def __init__(self,canvas,toolbar) -> None:
        pass
    def register_command():
        pass
    def run():
        pass



def createToolbar():
    toolbar = ToolBar()
    toolbar.register_colors("black", Color(0,0,0))
    toolbar.register_colors("white", Color(255,255,255))
    toolbar.register_shapes("circle", lambda *args:Circle(*args))
    toolbar.register_shapes("rectangle", lambda *args:Rectangle(*args))
    return toolbar
toolbar = createToolbar()
circle = toolbar.get_shape("circle", 0,10,toolbar.get_color("white"))

canvas = Canvas()
app = Application(canvas,toolbar)
app.run("add","circle", 0,10, "white")
app.run("remove", "")
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
    def __hash__(self) -> int:
        return hash(self.id)

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
        self._shapes = set()
    def add(self,shape:Shape):
        self._shapes.add(shape)
    def remove(str,id):
        pass    

class Command(ABC):
    def __init__(self,receiver:Canvas) -> None:
        super().__init__()
        self._receiver = receiver
    @abstractmethod
    def execute(self):
        pass

class AddCommand(Command):
    def __init__(self, receiver: Canvas,shape:Shape) -> None:        
        super().__init__(receiver)
        self._shape = shape
    def execute(self):
        self._receiver.add(self._shape)

class RemoveCommand(Command):
    def __init__(self, receiver:Canvas, id:uuid) -> None:        
        super().__init__(receiver)
        self._id = id 
    def execute(self):
        self._receiver.remove(id)

class FactoryCommad():
    @staticmethod
    def createAddCommand(toolbar:ToolBar,canvas:Canvas,*args):
        key,x,y,color =args
        command = AddCommand(canvas, toolbar.get_shape(key,x,y,toolbar.get_color(color)))
        return command
    @staticmethod
    def createRemoveCommnand(canvas, *args):
        id=args[0]   
        command = RemoveCommand(canvas,id)
        return command



def createToolbar():
    toolbar = ToolBar()
    toolbar.register_colors("black", Color(0,0,0))
    toolbar.register_colors("white", Color(255,255,255))
    toolbar.register_shapes("circle", lambda *args:Circle(*args))
    toolbar.register_shapes("rectangle", lambda *args:Rectangle(*args))
    return toolbar


class Application:
    def __init__(self,canvas,toolbar) -> None:
        self._commands = {}
    def register_command(self, key:str, factory):
        self._commands.update({key:factory})
    def run(self,*args):
        key,*newArgs = args
        command:Command = self._commands.get(key)(*newArgs)
        command.execute()


def createApp(canvas,toolbar):
    app = Application(canvas,toolbar)

    app.register_command("add", lambda *args:
                         FactoryCommad.createAddCommand(toolbar,canvas, *args))
    
    app.register_command("remove", 
                         lambda *args:
                         FactoryCommad.createRemoveCommnand(canvas,*args))
    
    return app
    
app = createApp(Canvas(), createToolbar())

app.run("add","circle", 0,10, "white")
app.run("remove", "1")
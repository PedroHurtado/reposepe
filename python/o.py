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

class ToolBar:
    """
        dictinary->Color
        dictionary->Shapes
        register_color()
        register_shape()
        get_color("black")
        get_shape("circulo", x, y, color)
    """
    pass
class Canvas:
    """
    solid(I)
    """
    pass
class Application:
    """
        Canvas
        ToolBar
    """
    pass
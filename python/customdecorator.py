"""
  1 crear una funcion que recibe como 1 args el fn
  2.crear y retornar una funcion con *args **kwargs
  3.invocar la funcion dentro de ella
  4.retornar la funcion
  https://refactoring.guru/design-patterns/decorator
"""
from functools import wraps
def decorator(fn):
    wraps(fn)
    def wrapper(*args,**kwargs):
        print('Before')
        result = fn(*args,**kwargs)
        print('After')
        return result
    return wrapper

def required(type:type): 

    def decorator(fn):
        wraps(fn)                
        def wrapper(*args,**kwargs):
            value = args[1]
            name = fn.__name__    
            if(value is None):
                raise TypeError(f'el {name} no puede ser nulo') 
            if not isinstance(value,type):
                raise TypeError(f"el {value} para {name} no es del tipo correcto. se requiere {type}") 
            return fn(*args,**kwargs)
        return wrapper
    return decorator

@decorator
def example(name):
    print(name)

class Foo:
    def __init__(self,name) -> None:
        self.name = name
        #self._name=name cualquier tipo de validacion tienes    
        #que duplicar la validación
    
    
    @property        
    def name(self):
        return self._name    
    
    @name.setter
    @required(str)
    def name(self,name):        
        self._name = name
    @name.deleter    
    def name(self):
        del self._name

try:
    foo = Foo("Hola")
    foo.name = 10;
    print(foo.name)
   
except TypeError as err:
    print(err)
except Exception as ex:
    print(ex)

example("Pedro")   #1
example("Pedro Hurtado")  #2
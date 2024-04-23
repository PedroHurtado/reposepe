try:
	1/0
except:
	print("error")
else:
	print("else")
finally:
	print("finally")
	
try:
	1/1
except:
	print("error")
else:
	print("else")
finally:
	print("finally")
"""
 excepción muda(antipatrón)
 se deben de controlar si puede ser en un punto común
 si algo no es correcto raise crear customException
 Exception

 try:
 except ExceptionSpecific:
 except Exception:

"""

class Foo:
    def __init__(self,name) -> None:
        self.name = name
        #self._name=name cualquier tipo de validacion tienes
        #que duplicar la validación
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if name is None:
            raise TypeError("name no puede ser nulo")
        if not  isinstance(name,str):
            raise TypeError("name tiene que ser string")
        self._name = name
    @name.deleter
    def name(self):
        del self._name

try:
    foo = Foo("Hola")
    foo.name = None
except TypeError as err:
    print(err)
except Exception as ex:
    print(ex)
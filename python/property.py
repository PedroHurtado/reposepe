"""
https://www.freecodecamp.org/espanol/news/python-decorador-property/
Crear una clase Foo con un atributo name y creamos
    getter
    setter
    deleter

    class Casa:

	def __init__(self, precio):
		self._precio = precio

	@property
	def precio(self):
		return self._precio
	
	@precio.setter
	def precio(self, precio_nuevo):
		if precio_nuevo > 0 and isinstance(precio_nuevo, float):
			self._precio = precio_nuevo
		else:
			print("Por favor ingrese un precio valido.")

	@precio.deleter
	def precio(self):
		del self._precio

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
        """
            valida que es string y no es none
        """
        self._name = name
    @name.deleter
    def name(self):
        del self._name

foo = Foo("Pedro Hurtado")
print(foo.name)
foo.name ="Pedro"
#foo._name nunca porque indicamos que es private
print(foo.name)
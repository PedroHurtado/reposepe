class Foo:
	name=''
	def __init__(self,name) -> None:
		self.name = name
	@classmethod
	def cl(cls,name):
		cls.name = name
	@staticmethod
	def static(age):		
		return age<=18
    

foo = Foo("Pedro")
print(foo.name) #Pedro
foo.static(18)
foo.cl("foo")  #''''

foo1 = Foo("Pedro Hurtado")
print(foo1.name) #Pedro Hurtado
foo1.cl("foo1") #''''



"""
crear la instancia de una clase con un metodo estatico y un class method
https://www.geeksforgeeks.org/class-method-vs-static-method-python/
"""

class Bar:
    def __init__(self,name) -> None:
        self.name = name
	
    @classmethod
    def create(cls,name):
        return cls(name)
    @staticmethod
    def createStatic(name):
        return Bar(name)
    
bar = Bar.create("Pedro")
print(bar.name) #pedro
bar1 = Bar.createStatic("Pedro1")
print(bar1.name) #pedro1
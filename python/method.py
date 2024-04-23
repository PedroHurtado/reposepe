class Foo:
    def instance(self):
        pass
    @classmethod
    def cl(cls):
        pass
    @staticmethod
    def static():
        pass

foo = Foo()
foo.cl()
foo.static()

"""
crear la instancia de una clase con un metodo estatico y un class method
"""
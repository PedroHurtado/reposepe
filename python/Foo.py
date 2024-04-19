class Foo:
    def __init__(self,id) -> None:
        self.id = id
        """
        implementar el codigo necesario para que las clases con id igual
        no se dupliquen en un set
        """


setter = set({Foo(5),Foo(5)})
print(len(setter)) #2

setter = set({1,1})
print(len(setter)) #1
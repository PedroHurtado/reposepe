class Foo:
    def __init__(self,id) -> None:
        self.id = id
        """
        implementar el codigo necesario para que las clases con id igual
        no se dupliquen en un set
        """
    def __eq__(self, value: object) -> bool:
        return self.id==value.id
    def __hash__(self) -> int:
        return hash(self.id)


print(Foo(5)==Foo(5))
setter = {Foo(5),Foo(5)}
print(len(setter)) #2

setter = {1,1}
print(len(setter)) #1
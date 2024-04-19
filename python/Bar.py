class Bar:
    def __init__(self,id:int,name:str) -> None:
        self.id =id
        self.name = name
    def __eq__(self, value: object) -> bool:  
        if isinstance(value, Bar):      
            return self.id == value.id and self.name == value.name
        return False
    def __hash__(self) -> int:
        return hash((self.id,self.name))

data = {None, Bar(1,"Pedro")}
print(data)

print(None == Bar(1,"Pedro")) # error si no comprobamos instance
print(Bar(1,"Pedro") == Bar(1,"Pedro")) # true
"""
un cliente se puede modificar,eliminar,leer y crear
un usuario solo se puede leer
"""

class Add:
    def add():
        pass
class Update:
    def update():
        pass
class Remove:
    def remove():
        pass
class Get:
    def get():
        pass

class Customer(Add,Update,Remove,Get):
    pass
class User(Get):
    pass

customer = Customer()
user = User()

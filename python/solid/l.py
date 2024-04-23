"""
   En el mundo de las aves existen pinguinon que 
   pesan 5 kg y aguilas que pesan 10 kg y vuelan a 100 km/hora
   crear las clases necesarias para representar pinguinos 
   y aguilas
   crear una funcion capaz de imprimir los pinguinos y las
   agilas y otra que solo imprima las aguilas

   Después crear una class Paloma que pesa 1 kg y vuela a 20 km/hora
"""

class Ave:
    def __init__(self,peso:int) -> None:
        self.peso = peso
class AveVoladora(Ave):
    def __init__(self, peso:int,velocidad:int) -> None:
        super().__init__(peso)
        self.velocidad = velocidad
class Aguila(AveVoladora):
    def __init__(self, peso:int, velocidad:int) -> None:
        super().__init__(peso,velocidad)
class Pinguino(Ave):
    def __init__(self, peso:int) -> None:
        super().__init__(peso)

def print_aves(ave:Ave,writer=print)->None:
    if not isinstance(ave,Ave):
        raise TypeError(f"el parametro no es del tipo {type(Ave)}")
    writer(ave)
def print_aves_voladoras(ave:AveVoladora, writer=print):
    if not isinstance(ave,AveVoladora):
        raise TypeError(f"el parametro no es del tipo {type(AveVoladora)}")
    writer(ave)

print_aves(Aguila(10,100))  #ok
print_aves(Pinguino(5))     #ok
print_aves_voladoras(Aguila(10,100)) #ok
print_aves_voladoras(Pinguino(10)) #error






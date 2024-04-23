"""
    escribir una funcion que imprima la fecha actual
    1. S
        1.1 Calcula la fecha actual
        1.2 Imprime
    2. D inyeccion de dependencias
"""
from datetime import date


#def actual_date():
#    Bad
#    print(date.today())

def print_date(date,writer):
    #Got
    writer(date)

actual_date = date.today()
print_date(actual_date,print)
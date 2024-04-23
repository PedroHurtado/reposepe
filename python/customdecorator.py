"""
  1 crear una funcion que recibe como 1 args el fn
  2.crear y retornar una funcion con *args **kwargs
  3.invocar la funcion dentro de ella
  4.retornar la funcion
  https://refactoring.guru/design-patterns/decorator
"""
from functools import wraps
def decorator(fn):
    wraps(fn)
    def wrapper(*args,**kwargs):
        print('Before')
        result = fn(*args,**kwargs)
        print('After')
        return result
    return wrapper

@decorator
def example(name):
    print(name)

example("Pedro")   #1
example("Pedro Hurtado")  #2
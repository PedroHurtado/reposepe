"""
    crear un fichero que contenga los valores con separador de linea
    1
    2
    3
    4
    5
    ...10
    leemos cada linea la convertimos a entero
    y escribimos un expresion generator escriba en un nuevo archivo
    los pares multiplicados por ellos mismo
    2->4
    4->16
    10->100
"""
import os
input =os.path.dirname(__file__)+ "\\input.txt"
output =os.path.dirname(__file__)+ "\\pares.txt"

def read_line_file(input:str):
    with open(input, "r") as fs:
        line = fs.readline()        
        while(line!=''):        
            yield int(line.strip())
            line = fs.readline()  

def new_line(v):
    return str(v) + '\n'

expression = (new_line(v*v) for v in read_line_file(input) if v%2==0)        

def write_file(output, expression):
    with open(output,"w") as w:        
        #w.writelines(expression)           
        for line in expression:
            w.write(line)
            


write_file(output, expression)


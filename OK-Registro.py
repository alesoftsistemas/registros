# Estructura de Datos y Algoritmos
# Facultad de Ciencias Exactas y Naturales
# Universidad Nacional de Catamarca
# Título: Ejemplo de REGISTROS 
# Descripción: Declarar una variable llamada empleado que tenga una estructura 
#              que permita almacenar el código, nombre y edad ingresados por el usuario.

# Definición de Clase 
class PERSONA():     
    def __init__(self):         
        self.codigo = 0         
        self.nombre = ""         
        self.edad   = 0  

# Carga de datos 
empleado        = PERSONA() 
empleado.codigo = input("Código: ") 
empleado.nombre = input("Nombre: ") 
empleado.edad   = input("Edad  : ") 

# Impresión de los datos
print("--------")  
print("Código: ", empleado.codigo)
print("Nombre: ", empleado.nombre)
print ("Edad: ", empleado.edad) 
print() 
input("Fin del Programa") 
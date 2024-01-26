#Funciones 

"""
Cuando escribimos muchas lineas de codigo una buena practica en la escritura de codigo es dividirlo en bloques 
ya que de esta manera hacemos codigo reutilizable

Las funciones son bloques de codigo que corren solo cuando se les invoca
Las funciones se definen una vez y se reutiliza 
Las funciones se utilizan para tener un codigo más manejable al dividirlo en bloques 
Las funciones hace que los codigos sean más faciles de mantener por el hecho de que esta segmentado

"""

#ejemplo
def my_function():
    print("Hola desde una función")

my_function() # Ejecuta el codigo que esta dentro de la funcion

#Recordemos que podemos pasar datos a las funciones a traves de parametros.
#Los parametros se definen dentro de los parentesis despues de definir el nombre de la funcion
#Podemos agregar cuantos parametros se desee, solo se debe de separar por comas


#Función con parametros
def print_fullname(Nombre):
    print(Nombre+ "Cabrera")

print_fullname("Carlos")

#En las funciones no es necesario definir los parametros pero se pueden especificar el tipo de parametro 
#esto es util para documentar el codigo ademas de nosotros tengamos la certeza de que ingresan los datos correctos a nuestra funcion 

#Funcion con el parametro defnido
def print_age(Edad: int):
    print("Edad: ", Edad)

print_age(24)


#Tambien podemos definir valores por default y este parametro se utilizara solo cuando la funcion sea llamda vacia 
def print_country(pais="España"):
    print("pais: ", pais)

print_country("México")
print_country()
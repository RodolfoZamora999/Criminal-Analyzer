from termcolor import colored
import os

#Ruta de la base de datos.
file = "database.pl"
#Inicia prolog con "data.pl" como base de conocimiento, 
#ejecuta "main" como objetivo y despues finaliza.
init_query_prolog = "swipl -f {0} -g main -t halt".format(file)


#Método de utilidad para resolver dependencias del proyecto.
def dependencies_resolution():
    os.system("pip install termcolor")
    os.system("clear")

#Método de utilidad para imprimir tablas con datos en consola.
def print_table(values: iter):
    max = 0
    for value in values:
        if len(value) > max:
            max = len(value)
    
    #Imprimir parte superior
    print( "+" + ("-" * (max + 2)) + "+")
    
    #Imprimir los valores de la tabla
    for value in values:
        if len(value) < max:
            diff = max - len(value)
            for add in range(diff):
                value += " "

        print("| ", value, " |", sep="")
    
    #Imprimir parte inferior
    print( "+" + ("-" * (max + 2)) + "+")


#Este método es responsable de cargar los datos a la base de conocimientos
def input_database():
    os.system("clear")
    print("Inserte las características del criminal.")
    print("Sintaxis: caracteristica:valor")
    print()

    values = []
    #Inicia la carga de datos
    while True:
        str_input = input("Insertar: ").lower().lstrip().rstrip().replace(" ", "_")
        
        if str_input == "complete" or str_input == "exit":
            os.system("clear")
            print("Valores que se almacenaran:")
            print_table(values)

            print("¿Desea guardarlos? 1:Sí 2:No")
            save = input("Insertar: ")

            if save == "1":
                print("Datos almacenados")
            elif save == "2":
                print("Nada")
            else:
                print("Inserta un opción correcta!")
            
            break

        if str_input.find(":") == -1:
            print("No olvides el ':' ")
            continue

        values.append(str_input)


def query_criminal():
    print("load")


#Método de entrada del programa
def main():
    #Se resuelven las dependencias
    dependencies_resolution()
    os.system("clear")
    os.system("color")
    print_table(["#"*40, "Bienvenidos a Criminal Analyzer 1.0", "#"*40])
    
    if os.path.exists(file):
        print(colored("Se ha detectado una base de datos existente.\n", "green"))
    else:
        print(colored("No se ha detectado una base de datos existente.\n", "red"))

    print("Por favor seleccione una de las siguientes opciones:")
    print("{0} Introducir datos\n{1} Hacer una consulta\n".format(colored("[1]", "green"), colored("[2]", "green")))
    select = input("{0} Selecciona una opción: ".format(colored("[-]", "blue")))
    if select == "1":
        input_database()
    elif select == "2":
        if os.path.exists(file):
            query_criminal()
        else:
            print("No se ha detectado una base de datos")
    else:
        print("Por favor seleccione una opción correcta")

#Punto de entrada del programa
if __name__ == "__main__":
    main()

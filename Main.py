from termcolor import colored
import os

#Ruta de la base de datos.
file = "database.pl"
#Inicia prolog con "data.pl" como base de conocimiento, 
#ejecuta "main" como objetivo y despues finaliza.
init_query_prolog = "swipl -f {0} -g main -t halt".format(file)

#Método de utilidad para imprimir tablas con datos en consola.
def print_table(values: iter, numerate: bool = False):
    max = 0
    for value in values:
        if len(value) > max:
            max = len(value)
        
    #Imprimir parte superior
    if numerate:
        count_values = len(values)
        add_v = 0
        if count_values < 10:
            add_v = 4
        elif count_values >= 10 and count_values < 100:
            add_v = 5 
        elif count_values >= 100 and count_values < 1000:
            add_v = 6 

        print( "+" + ("-" * (max + 2 + add_v)) + "+")
    else:
        print( "+" + ("-" * (max + 2)) + "+")
    
    #Imprimir los valores de la tabla
    cont_value = 0
    for value in values:
        cont_value += 1
        if len(value) < max:
            diff = max - len(value)
            for add in range(diff):
                value += " "

        if numerate:
            count_values = len(values)
            if count_values >= 10 and count_values < 100:
                if cont_value < 10:
                    value = value + " "   
            elif count_values >= 100 and count_values < 1000:
                if cont_value < 10:
                    value = value + "  "
                elif cont_value >= 10 and cont_value < 100:
                    value = value + " "

            value =  "[{0}] ".format(cont_value) + value

        print("| ", value, " |", sep="")

    #Imprimir parte inferior
    if numerate:
        count_values = len(values)
        add_v = 0
        if count_values < 10:
            add_v = 4
        elif count_values >= 10 and count_values < 100:
            add_v = 5 
        elif count_values >= 100 and count_values < 1000:
            add_v = 6 

        print( "+" + ("-" * (max + 2 + add_v)) + "+")
    else:
        print( "+" + ("-" * (max + 2)) + "+")


#Este método es responsable de cargar los datos a la base de conocimientos
def input_data():
    os.system("clear")
    print("Inserte las características del criminal.")
    print("Escriba {0} para finalizar la entrada de características.".format(colored("complete", "green")))
    print("{0}: caracteristica{1}valor\n".format(colored("Sintaxis", "yellow"), colored(":", "green")))

    #Inicia la carga de datos
    values = []
    while True:
        str_input = input("{0} Característica: ".format(colored("[-]", "blue"))).lower().lstrip().rstrip().replace(" ", "_")
        if str_input == "complete" or str_input == "exit":
            print("\nLas siguientes características se almacenarán en la base de conocimientos.")
            print_table(values, numerate=True)
            print("\n¿Confirma que desea almacenar estas características?")
            print("{0} Sí, almacenar datos.".format(colored("[1]", "green")))
            print("{0} No, seguir agregando características.".format(colored("[2]", "green")))
            print("{0} Cancelar e ignorar datos.\n".format(colored("[3]", "green")))
            
            while True:
                select = input("{0} Seleccione una opción: ".format(colored("[-]", "blue")))
                if select == "1":
                    #Almacenar los datos en la base de conocimiento.
                    print("Datos almacenados")
                    break
                elif select == "2":
                    #Seguir con la entrada de datos.
                    print("Nada")
                    break
                elif select == "3":
                    #Ignora los datos y regresa al inicio.
                    main()
                    break
                else:
                    print("Por favor seleccione una opción correcta, vuelva a intentarlo.\n")
            break

        if str_input.find(":") == -1:
            print("No olvides el ':' ")
            continue

        values.append(str_input)


def query_criminal():
    print("load")


#Método de entrada del programa
def main():
    os.system("clear")
    os.system("color")
    print_table(["#"*40, "Bienvenidos a Criminal Analyzer 0.1", "#"*40])
    
    if os.path.exists(file):
        print(colored("Se ha detectado una base de datos existente.\n", "green"))
    else:
        print(colored("No se ha detectado una base de datos existente.\n", "red"))

    print("Por favor seleccione una de las siguientes opciones:")
    print("{0} Introducir datos.\n{1} Hacer una consulta.\n{2} Salir.\n".format(colored("[1]", "green"), colored("[2]", "green"), colored("[3]", "green")))

    while True:
        select = input("{0} Seleccione una opción: ".format(colored("[-]", "blue")))
        if select == "1":
            input_data()
            break
        elif select == "2":
            if os.path.exists(file):
                query_criminal()
                break
            else:
                print("No se ha detectado una base de datos existente, por favor registre los datos primero.\n")
        elif select == "3":
            os.system("clear")
            exit()
        else:
            print("Por favor seleccione una opción correcta, vuelva a intentarlo.\n")
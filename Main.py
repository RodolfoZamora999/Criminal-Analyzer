from termcolor import colored
import os

#Ruta de la base de datos.
file = "database.pl"
temp_file = "query_file.temp"
swipl_goal = "es_criminal"
#Inicia prolog con "data.pl" como base de conocimiento, 
#ejecuta "es_criminal" como objetivo y despues finaliza.
init_query_prolog = "swipl -f {0} -g {1} -t halt".format(temp_file, swipl_goal)

#Método de utilidad para imprimir tablas con datos en consola.
def print_table(values: list, numerate: bool = False):
    #Verificar la cadena con mayor longitud.
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
    
    #Imprimir los valores de la lista en la tabla
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


#Método que almacena los datos en un fichero.
def save_data(values: list):
    with open(file, mode="w") as file_open:
        for value in values:
            tokens = value.split(":")
            temp = "{0}({1}).\n".format(tokens[0], tokens[1])
            file_open.write(temp)

        file_open.close()
        print(colored("\nDatos almacenados con éxito.", "green"))
        input("\nPresione Enter para continuar...")

        #Regresar al menu de inicio
        main()


#Método responsable de la recopilación de los datos que se almacenaran.
def input_data(values: list = None):
    os.system("clear")
    print("Inserte las características del criminal.")
    print("Escriba {0} para finalizar la entrada de características.".format(colored("complete", "green")))
    print("{0}: caracteristica{1}valor\n".format(colored("Sintaxis", "yellow"), colored(":", "green")))

    #Inicia la carga de datos
    if values is None:
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
                    save_data(values)
                    break
                elif select == "2":
                    #Seguir con la entrada de datos.
                    input_data(values)
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


#Método que almacena la consulta de manera temporal en un fichero.
def save_data_temp(file_data: str, input_values: list):
    prolog_query = ""
    for value in input_values:
        if not (input_values.index(value) + 1) == len(input_values):
              prolog_query += value + ", "
        else:
            prolog_query += value + " " 

    es_criminal = "Las características del sospechoso concuerdan un %100"
    es_criminal += " con las características de la base de conocimiento, por lo tanto, ¡Él es el culpable!"
    no_es_criminal = "Una o varias características del sospechoso no concuerdan con las características de"
    no_es_criminal += " la base de conocimiento, por lo tanto no lo podemos culpar del crimen."
    query_str = "es_criminal :- ({0} -> write(\"{1}\"); write(\"{2}\")).".format(prolog_query, es_criminal, no_es_criminal)

    with open(temp_file, mode="w") as file_open:
        file_open.write(file_data)
        file_open.write("\n")
        file_open.write(query_str)
        file_open.close()


#Método que recopila datos para hacer la consulta a prolog.
def query_criminal():
    os.system("clear")
    if not os.path.exists(file):
        print(colored("Error, la base de datos no existe.", "red"))
        main()
        return

    #Leer el fichero de la base de conocimiento
    with open(file, mode="r") as file_open:
        read_file = file_open.read()
        file_open.close()

    #Se filtran los datos de interes.
    list_values = read_file.split("\n")
    list_values.remove("")
    list_values_process = []
    for value in list_values:
        list_values_process.append(value.split("(")[0])

    #Inicia la captura de los datos del sospechoso
    print("Para hacer la consulta es necesario que ingrese los siguientes datos del sospechoso: ")
    print("Características totales a ingresar: {0}\n".format(colored(len(list_values_process), "yellow")))
    list_input_value = []
    for value in list_values_process:
        input_value = input("{0} Inserte {1}: ".format(colored("[-]", "blue"), value)).lower().lstrip().rstrip().replace(" ", "_")
        list_input_value.append("{0}({1})".format(value, input_value))
    
    #Se almacena la consulta
    save_data_temp(read_file, list_input_value)

    #Se hace la consulta en prolog
    input("\nTodo está preparado correctamente, ahora solo presione {0} para iniciar con la consulta.\n".format(colored("Enter", "yellow")))
    print(colored("En base a los resultados introducidos y la base de conocimientos se ha obtenido el siguiente resultado:", "yellow"))
    os.system(init_query_prolog)

    #Se elimina el archivo temporal
    os.remove(temp_file)
    
    #Más opciones
    print("\n\nSeleccione una opción para continuar:")
    print("{0} Realizar otra consulta.\n{1} Regresar al menú.\n{2} Salir del programa.\n".format(colored("[1]", "green"), colored("[2]", "green"), colored("[3]", "green")))
    while True:
        select = input("{0} Seleccione una opción: ".format(colored("[-]", "blue")))
        if select == "1":
            query_criminal()
        elif select == "2":
            main()
        elif select == "3":
            os.system("clear")
            exit()
        else:
            print("Por favor seleccione una opción correcta, vuelva a intentarlo.\n")


#Método de entrada del programa
def main():
    os.system("clear")
    print_table(["#"*40, "Bienvenidos a Criminal Analyzer 0.1", "#"*40])
    
    if os.path.exists(file):
        print(colored("Se ha detectado una base de datos existente.\n", "green"))
    else:
        print(colored("No se ha detectado una base de datos existente.\n", "red"))

    print("Por favor seleccione una de las siguientes opciones:")
    print("{0} Introducir datos.\n{1} Hacer una consulta.\n{2} Salir del programa.\n".format(colored("[1]", "green"), colored("[2]", "green"), colored("[3]", "green")))

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
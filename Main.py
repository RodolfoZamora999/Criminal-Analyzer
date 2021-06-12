import os

#
file = "database.pl"
#Inicia prolog con "data.pl" como base de conocimiento, 
#ejecuta "main" como objetivo y despues finaliza.
init_query_prolog = "swipl -f {0} -g main -t halt".format(file)

# Este método es responsable de cargar los datos a la base de conocimientos
def input_database():
    os.system("clear")
    print("Inserte los datos")
    print("caracteristica:valor")
    print()

    values = []
    #Inicia la carga de datos
    while True:
        str_input = input().lower().lstrip().rstrip().replace(" ", "_")
        
        if str_input == "complete" or str_input == "exit":
            os.system("clear")
            print("Valores que se almacenaran:")
            for value in values:
                print(value)


            print("¿Desea guardarlos? 1:Sí 2:No")
            

            
            break

        if str_input.find(":") == -1:
            print("No olvides el ':' ")
            continue

        values.append(str_input)

    

def query_criminal():
    print("load")



# Método de entrada del programa
def main():
    print("Welcome")
    print("1. Introducir datos 2. Consultar")

    #Entrada de los datos
    input_database()
    #Consultar caractériticas del criminal
   # query_criminal()
    #Ejecutar prolog
    #os.system(path)


if __name__ == "__main__":
    main()

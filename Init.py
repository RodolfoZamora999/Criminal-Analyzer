import os

#Se resuleven las dependencias del proyecto
def dependencies_resolution():
    os.system("pip install termcolor")
    os.system("clear")

#Activa el color de la terminal (si aplica)
def active_color_terminal():
    os.system("color")
    os.system("clear")

#Punto de entrada del programa
if __name__ == "__main__":
    dependencies_resolution()
    active_color_terminal()

    # Init program
    from Main import main
    main()

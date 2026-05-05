import os

import scripts.calificaciones as cal
import scripts.estatus as est
import scripts.reportes as rep

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m-----Sistema de Calificaciones-----\033[0m")
    print("a) Almacenar datos del alumno")
    print("b) Ver estatus del alumno")
    print("c) Extraer reporte")
    print("d) Terminar el programa")
    opcion = input(">> ")
    
    if opcion == "a":
        cal.init()
    elif opcion == "b":
        est.init()
    elif opcion == "c":
        rep.init()
    else:
        print("Fin del programa")
    
if __name__ == "__main__":
    menu()
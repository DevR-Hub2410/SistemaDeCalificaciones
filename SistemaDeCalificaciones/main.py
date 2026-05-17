import os

import scripts.calificaciones as cal
import scripts.estatus as est
import scripts.reportes as rep

import scripts.banner as banner

def menu():
    while True: # ciclo DO-UNTIL
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\033[32m{banner.splash1}\033[0m")
        print("\033[31mHecho por ByteStudio\033[0m")
        print("a) Almacenar datos del alumno")
        print("b) Ver estatus del alumno")
        print("c) Extraer reporte")
        print("d) Terminar el programa")
        opcion = input(">> ").lower()
        
        # Segun la opción elegida, se llama a distintos scripts
        if opcion == "a":
            cal.init()
        elif opcion == "b":
            est.init()
        elif opcion == "c":
            rep.init()
        elif opcion == "d":
            print("Fin del programa")
            break # Se sale del ciclo cuando se elige la opción d
        else:
            # Si se elige otra opción, se toma como no válida y se repite el ciclo.
            input("Opción no válida. Presione Enter para continuar...")

if __name__ == "__main__":
    menu()
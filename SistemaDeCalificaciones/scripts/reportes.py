import os
import scripts.calificaciones as cal

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    iniciarReporte()

def iniciarReporte():
    print("\033[34m-----Reporte final-----\033[0m")
    print(f"Alumnos registrados: {len(cal.materia)}") # Tamaño de el conjunto de [nombre y parciales]
    print(f"Total de aprobados: ")
    print(f"Total de reprobados: ")

    # Obtener los valores de materia
    for i in cal.materia:
        print(f"Alumno: \033[32m{i[0]}\033[0m") # i[0] es la parte de la lista donde se almaceno los nombres
        print(f"Calificaciones de parciales: ", end=" ")
        for j in i[1]: # i[1] son la lista de 5 parciales por alumno
            print(f"\033[34m{j[0]}\033[0m", end="   ") # j[0] va a recorrer parcial por parcial
        print("\n")
    
    input("\nPresiona Enter para volver al menú...")
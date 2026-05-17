import os
import scripts.calificaciones as cal
import matplotlib.pyplot as plt # Libreria para la gráfica

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Iniciar el reporte solo si hay alumnos registrados
    if cal.nombres[0] is None: 
        input("Primero debes registrar alumnos...")
        return
    iniciarReporte()
    # Obtener los datos generales para el reporte final
    promedioGeneral, sumaAprobados, sumaReprobados, maxima, minima, promedios = datosGenerales()

    # Llamar a la funcion finalReport con todos los datos obtenidos para mostrarlos
    finalReport(
        promedioGeneral,
        sumaAprobados,
        sumaReprobados,
        maxima,
        minima,
        promedios
    )

def iniciarReporte():
    print("\033[34m-----Reporte final-----\033[0m")
    # Obtener los valores de materia
    for i in cal.materia:
        print(f"Alumno: \033[32m{i[0]}\033[0m") # i[0] es la parte de la lista donde se almaceno los nombres
        print(f"Calificaciones de parciales: ", end=" ")
        for j in i[1]: # i[1] son la lista de 5 parciales por alumno
            print(f"\033[34m{j[0]}\033[0m", end="   ") # j[0] va a recorrer parcial por parcial
        print("\n")

def datosGenerales():
    # Variables para obtener resultados generales
    sumaPromedios = 0
    todasCalificaciones = []
    promedios = []
    sumaAprobados = 0
    sumaReprobados = 0

    print("\033[34m-----Promedio de cada alumno-----\033[0m")
    # Ciclo FOR para sacar el promedio de cada alumno y sumarlo
    for i in range(cal.rango): 
        promedio = sum(cal.calificaciones[i]) / 5
        promedios.append(promedio)
        print(f"{cal.nombres[i]} -> Promedio: {promedio:.2f}")
        sumaPromedios += promedio
        todasCalificaciones.extend(cal.calificaciones[i])
        # Selección simple y compuesta para contar el número de aprobados y reprobados
        if promedio >= 7:
            sumaAprobados += 1
        else:
            sumaReprobados += 1
    print("\n")

    # Sacar el promedio general de todos los alumnos
    promedioGeneral = sumaPromedios / cal.rango
    # Se escogen las calificaciones máxima y mínima de todas las calificaciones guardadas en un solo arreglo
    maxima = max(todasCalificaciones)
    minima = min(todasCalificaciones)
    # Datos generales guardados para usar en la función de impresión final
    return promedioGeneral, sumaAprobados, sumaReprobados, maxima, minima, promedios

def finalReport(promedioGeneral, sumaAprobados, sumaReprobados, maxima, minima, promedios):
    # Impresión de resultados unicos utilizando las variables obtenidas en la función anterior
    print("\033[34m-----Resultados Generales-----\033[0m")
    print(f"Promedio general: {promedioGeneral:.2f}")
    print(f"Alumnos registrados: {len(cal.materia)}") 
    print(f"Total de aprobados: {sumaAprobados}")
    print(f"Total de reprobados: {sumaReprobados}")
    print(f"Calificación máxima: {maxima}")
    print(f"Calificación mínima: {minima}")

    # Utilizando el arreglo de nombres y el de promedios se crea una gráfica de barras
    plt.bar(cal.nombres, promedios)
    plt.title("Promedio por alumno")
    plt.xlabel("Alumnos")
    plt.ylabel("Promedio")
    plt.ylim(0, 10)
    plt.show()

    input("\nPresiona Enter para volver al menú...")

import os
import scripts.calificaciones as cal

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m-----Busqueda de alumnos-----\033[0m")
    buscar_alumno()

def buscar_alumno():
    busqueda = input("Ingresa el nombre del alumno a buscar: ")
    encontrado = False
    i = 0
    
    # Ciclo WHILE para buscar al estudiante
    # Usamos cal.nombres para acceder a la lista del otro archivo
    while i < len(cal.nombres) and encontrado == False:
        if cal.nombres[i] is not None and cal.nombres[i].lower() == busqueda.lower():
            encontrado = True
            mostrar_estatus(i)
        i += 1
    
    if encontrado == False:
        print(f"'{busqueda}' no se encuentra en el sistema.")
    
    input("\nPresiona Enter para volver al menú...")

def mostrar_estatus(indice): # Recibir la variable i
    nombre = cal.nombres[indice]
    notas = cal.calificaciones[indice]
    
    suma_notas = 0
    for nota in notas: # Ciclo FOR para recorrer las materias 
        suma_notas += nota
    promedio = suma_notas / 5
    
    print(f"Resultados para: {nombre}")
    print(f"Calificaciones: {notas}")
    print(f"Promedio final: {promedio:.2f}")
    
    # Selección simple y compuesta para aprobado/reprobado
    if promedio >= 7:
        print("Estatus: \033[32mAPROBADO\033[0m")
    else:
        print("Estatus: \033[31mREPROBADO\033[0m")
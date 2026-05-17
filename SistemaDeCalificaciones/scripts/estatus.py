import os
import scripts.calificaciones as cal

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m-----Busqueda de alumnos-----\033[0m")
    buscar_alumno()

def buscar_alumno():
    # Pedir el nombre del alumno
    busqueda = input("Ingresa el nombre del alumno a buscar: ")
    encontrado = False
    i = 0
    
    # Ciclo WHILE para buscar al estudiante
    # Usamos cal.nombres para acceder a la lista del otro archivo
    while i < len(cal.nombres) and encontrado == False:
        # SI la la lista de los nombres no esta vacia y si el nombre de la busqueda es igual a alguno de la lista
        if cal.nombres[i] is not None and cal.nombres[i].lower() == busqueda.lower():
            encontrado = True
            mostrar_estatus(i) # Llevar el indice del alumno encontrado como parametro
        i += 1
    
    # Si al final de todo el ciclo while no se encuentra nada, se indica que no está
    if encontrado == False:
        print(f"'{busqueda}' no se encuentra en el sistema.")
    
    input("\nPresiona Enter para volver al menú...")

def mostrar_estatus(indice): # Recibir la variable i
    nombre = cal.nombres[indice]
    notas = cal.calificaciones[indice]
    
    suma_notas = 0
    for nota in notas: # Ciclo FOR para recorrer las materias 
        suma_notas += nota # Acumulador para sumar todas las notas del alumno
    promedio = suma_notas / 5 # Sacar promedio
    
    # Imprimir resultados
    print(f"Resultados para: {nombre}")
    print(f"Calificaciones: {notas}")
    print(f"Promedio final: {promedio:.2f}")

    # •	Selección múltiple (IF anidados) para asignar calificación
    if promedio >= 9.5:
        letra = "\033[32mA+\033[0m"
    elif promedio >= 9:
        letra = "\033[32mA\033[0m"
    elif promedio >= 8:
        letra = " \033[32mB\033[0m"
    elif promedio >= 7:
        letra = " \033[33mC\033[0m"
    else:
        letra = " \033[31mD\033[0m"
        
    print(f"Calificación del alumno: {letra}")
    
    # Selección simple y compuesta para aprobado/reprobado
    if promedio >= 7:
        print("Estatus: \033[32mAPROBADO\033[0m")
    else:
        print("Estatus: \033[31mREPROBADO\033[0m")
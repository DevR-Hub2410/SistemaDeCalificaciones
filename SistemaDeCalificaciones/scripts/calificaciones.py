import os

rango = 3 # Variable que es la cantidad de alumnos
nombres = [None for _ in range(rango)]
calificaciones = [[0 for _ in range(5)] for _ in range(rango)]

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m-----Registro de alumnos-----\033[0m")
    # LLamar a las funciones
    registrarAlumnos()
    registrarCalificaciones()

def registrarAlumnos(): # Funcion para registrar los alumnos
    for i in range(rango): # Ciclo para guardar los nombres en el arreglo de nombres
        nom = input(f"[{i+1}/{rango}] Ingresa el nombre del alumno: ") 
        nombres[i] = nom

def registrarCalificaciones(): # Funcion de registrar las calificaciones
    for i in range(rango): # Ciclo para ir por cada alumno
        print(f"\nRegistrando calificaciones para: {nombres[i]}") 
        for j in range(5): # Ciclo para pedir las cinco calificaciones de cada alumno
            calif = float(input(f"  Calificación {j+1}: "))
            calificaciones[i][j] = calif
    
    input("\nDatos almacenados correctamente. Presione Enter para volver al menú...")
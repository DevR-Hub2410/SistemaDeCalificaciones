import os

rango = 20 # Variable que es la cantidad de alumnos
nombres = [None for _ in range(rango)] # Vector
calificaciones = [[0 for _ in range(5)] for _ in range(rango)] # Matriz
# Materias (Arreglo tridimensional)
materia = []

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m-----Registro de alumnos-----\033[0m")
    # LLamar a las funciones
    registrarAlumnos()
    registrarCalificaciones()
    registrarMateria()

def registrarAlumnos(): # Funcion para registrar los alumnos
    for i in range(rango): # Ciclo para guardar los nombres en el arreglo de nombres
        nom = input(f"[{i+1}/{rango}] Ingresa el nombre del alumno: ") 
        nombres[i] = nom

def registrarCalificaciones(): # Funcion de registrar las calificaciones
    for i in range(rango): # Ciclo para ir por cada alumno
        print(f"\nRegistrando calificaciones para: {nombres[i]}") 
        for j in range(5): # Ciclo para pedir las cinco calificaciones de cada alumno
            calificaciones[i][j]=validarCalificaciones(j)
    input("\nDatos almacenados correctamente. Presione Enter para volver al menú...")

# Funcion para validar si la calificacion esta entre 0 y 10
def validarCalificaciones(materia):
    while True: # While que se seguira repitiendo hasta que se retorne un valor
        calif = float(input(f"  Calificación {materia+1}: ")) 
        if 0 <= calif <= 10:
            return calif # Retorna el valor y rompe el ciclo
        else:
            print("  \033[33mTiene que ser una calificación de entre 0 a 10\033[0m")

# Registra alumnos en una materia para que no se borren
def registrarMateria():
    for i in range(rango):
        parciales = [] # Va a recoger una cantidad de calificaciones de parciales
        for j in range(5):
            parciales.append([calificaciones[i][j]]) # Almacena todas las califs que se registraron
        materia.append([nombres[i], parciales]) # Se agrega todos los nombres y materias a una materia

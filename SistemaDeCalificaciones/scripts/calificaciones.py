import os

nombres = [None for _ in range(6)]
calificaciones = [[0 for _ in range(5)] for _ in range(6)]

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    registrarAlumnos()
    registrarCalificaciones()
    
def registrarAlumnos():
    for i in range(5):
        nom = input("Ingresa el nombre del alumno: ")
        nombres[i] = nom
        os.system('cls' if os.name == 'nt' else 'clear')
        
def registrarCalificaciones():
    for i in range(20):
        for j in range(5):
            calif = float(input(f"Ingresa la calificacion del alumno {nombres[i]}: "))
            calificaciones[i][j] = calif
            os.system('cls' if os.name == 'nt' else 'clear')
    # for i in calificaciones:
        # print(i, end=" ")
    print("Fin de la ejecucion")
nombres = [None for _ in range(20)]
calificaciones = [[0 for _ in range(20)] for _ in range(5)]

def init():
    registrarAlumnos()
    
def registrarAlumnos():
    for i in range(20):
        nom = input("Ingresa el nombre del alumno: ")
        nombres[i] = nom
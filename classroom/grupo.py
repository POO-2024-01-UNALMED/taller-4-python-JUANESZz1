from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas or []
        self.listadoAlumnos = estudiantes or []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos += lista

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}\nGrado {self.grado}"

if __name__ == "__main__":
    asignatura1 = Asignatura("Matematicas")
    asignatura2 = Asignatura("Castellano", "Salon 201")
    grupo1 = Grupo()

    print(asignatura1)
    print(grupo1)
    print(grupo1.grado)

    grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])

    grupo3 = Grupo()
    grupo4 = Grupo()
    grupo5 = Grupo()
    grupo3.agregarAlumno("Kelly")
    grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"])
    grupo5.agregarAlumno("Javier")

    print(grupo3.listadoAlumnos)
    print(grupo4.listadoAlumnos)
    print(grupo5.listadoAlumnos)

    grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles")
    print(len(grupo3._asignaturas))

    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)
    Grupo.asignarNombre()
    print(Grupo.grado)

from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Modelos.Estudiante import Estudiante
from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Repositorios.RepositorioInscripcion import RepositorioInscripcion
from tutorialFUP.Repositorios.RepositorioEstudiante import RepositorioEstudiante
from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInscripcion():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioMateria = RepositorioMateria()
        print("Creando Controlador")

    def index(self):
        print("Listar inscripciones")
        return self.repositorioInscripcion.findAll()

    def create(self, infoInscripcion, id_estudiante, id_materia):
        nuevaInscripcion = Inscripcion(infoInscripcion)
        elEstudiante = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        nuevaInscripcion.estudiante = elEstudiante
        nuevaInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return laInscripcion.__dict__

    def update(self, id, infoInscripcion, id_estudiante, id_materia):
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        laInscripcion.anio = infoInscripcion["año"]
        laInscripcion.semestre = infoInscripcion["semestre"]
        laInscripcion.notaFinal = infoInscripcion["nota_final"]
        elEstudiante = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        laInscripcion.estudiante = elEstudiante
        laInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(laInscripcion)

    def delete(self, id):
        print("Elimiando inscripcion con id ", id)
        return self.repositorioInscripcion.delete(id)
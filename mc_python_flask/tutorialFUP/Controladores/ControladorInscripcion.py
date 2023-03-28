from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Repositorios.RepositorioInscripcion import RepositorioInscripcion

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
        print("Creando Controlador")

    def index(self):
        print("Listar inscripciones")
        return self.repositorioInscripcion.findAll()

    def create(self, laInscripcion):
        print("Crear inscripcion")
        nuevaInscripcion = Inscripcion(laInscripcion)
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return laInscripcion.__dict__

    def update(self, id, laInscripcion):
        inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcionActual.codigo = laInscripcion["codigo-Materia"]
        inscripcionActual.nombre = laInscripcion["nombre"]
        inscripcionActual.horario = laInscripcion["horario"]
        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        print("Elimiando inscripcion con id ", id)
        return self.repositorioInscripcion.delete(id)

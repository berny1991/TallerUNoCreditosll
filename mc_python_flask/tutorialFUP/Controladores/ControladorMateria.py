from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria
from tutorialFUP.Repositorios.RepsotorioDepartamento import RepositorioDepartamento

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMateria():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento= RepositorioDepartamento()
        print("Creando Controlador")

    def index(self):
        print("Listar todas las materias")
        return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        nuevoMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)

    def show(self, id):
        elMateria = Materia(self.repositorioMateria.findById(id))
        return elMateria.__dict__

    def update(self, id, infoMateria):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        print("Elimiando materia con id ", id)
        return self.repositorioMateria.delete(id)

    """
       Relación departamento y materia
       """

    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)

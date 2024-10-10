from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    pass
class LibroError(Exception):
    """Clase base para excepciones relacionadas con libros."""
    pass

class LibroExistenteError(LibroError):
    """Excepción lanzada cuando se intenta agregar un libro ya existente en el catálogo."""
    def __init__(self, mensaje):
        super().__init__(mensaje)


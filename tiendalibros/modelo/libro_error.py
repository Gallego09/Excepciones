from tiendalibros.modelo.libro import Libro


class LibroError(Exception):
    def __init__(self, libro: Libro):
        self.libro = libro

class LibroError(Exception):
    """Clase base para excepciones relacionadas con libros."""
    pass

class LibroExistenteError(LibroError):
    """Excepción lanzada cuando se intenta agregar un libro ya existente en el catálogo."""
    def __init__(self, titulo: str, isbn: str):
        # Llama al método inicializador de la clase padre
        super().__init__(f"El libro con titulo {titulo} y ISBN: {isbn} ya existe en el catálogo")

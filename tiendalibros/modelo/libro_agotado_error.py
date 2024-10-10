from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    pass
class LibroError(Exception):
    """Clase base para excepciones relacionadas con libros."""
    pass

class LibroAgotadoError(LibroError):
    """Excepción lanzada cuando un libro no tiene existencias disponibles."""
    def __init__(self, titulo: str, isbn: str):
        # Atributos para el título y el ISBN del libro
        self.titulo = titulo
        self.isbn = isbn
        # Llama al método inicializador de la clase padre
        super().__init__(f"El libro con titulo {titulo} y ISBN: {isbn} está agotado")

    # Método especial para representar el objeto como una cadena de texto
    def __str__(self):
        return f"El libro con titulo {self.titulo} y ISBN: {self.isbn} está agotado"


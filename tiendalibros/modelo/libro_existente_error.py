from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

    pass
    # Defina metodo inicializador

    # Defina metodo especial
class LibroError(Exception):
    """Clase base para excepciones relacionadas con libros."""
    pass

class ExistenciasInsuficientesError(LibroError):
    """Excepción lanzada cuando las existencias de un libro son insuficientes para completar una compra."""
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int, existencias: int):
        # Atributos para el título, ISBN, cantidad a comprar y existencias disponibles
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias
        # Llama al método inicializador de la clase padre
        super().__init__(f"El libro con titulo {titulo} y ISBN: {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}")

    # Método especial para representar el objeto como una cadena de texto
    def __str__(self):
        return (f"El libro con titulo {self.titulo} y ISBN: {self.isbn} no tiene suficientes existencias "
                f"para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}")

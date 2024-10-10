class TiendaLibros:
    pass
    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
from libro import Libro
from carro_compra import CarroCompras
from excepciones import LibroExistenteError # type: ignore
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError # type: ignore

class TiendaLibros:
    # Defina los atributos catálogo y carrito. El catálogo será un diccionario con ISBN como llave y objetos Libro como valor.
    # El carrito será una instancia de la clase CarroCompras.
    def __init__(self):
        self.catalogo = {}  # Diccionario con ISBN como llave y objetos Libro como valor
        self.carrito = CarroCompras()  # Instancia de la clase CarroCompras

    # Defina el método adicionar_libro_a_catálogo que agregue un libro al catálogo.
    # Si el ISBN ya existe en el catálogo, se debe lanzar una excepción LibroExistenteError.
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        if isbn in self.catalogo:
            raise LibroExistenteError(f"El libro con titulo {self.catalogo[isbn].titulo} y ISBN: {isbn} ya existe en el catálogo")
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

from libro import Libro
from excepciones import LibroExistenteError # type: ignore

class TiendaLibros:
    def __init__(self):
        # Definimos los atributos catálogo (diccionario) y carrito (CarroCompras)
        self.catalogo = {}  # Diccionario con ISBN como llave y objetos Libro como valor
        self.carrito = CarroCompras()  # Instancia de la clase CarroCompras

    # Método adicionar_libro_a_catalogo que recibe los parámetros solicitados
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro:
        # Verificar si ya existe un libro en el catálogo con ese ISBN
        if isbn in self.catalogo:
            # Si ya existe, lanzamos la excepción LibroExistenteError
            raise LibroExistenteError(titulo, isbn)
        
        # Si no existe, creamos un nuevo objeto de la clase Libro
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        
        # Agregamos el objeto Libro al catálogo
        self.catalogo[isbn] = nuevo_libro
        
        # Retornamos el libro agregado
        return nuevo_libro
    
    from excepciones import LibroAgotadoError, ExistenciasInsuficientesError # type: ignore
from carro_compra import CarroCompras
from libro import Libro

class TiendaLibros:
    def __init__(self):
        # Inicializa el catálogo como un diccionario y el carrito como una instancia de CarroCompras
        self.catalogo = {}
        self.carrito = CarroCompras()

    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int):
        """Agrega un libro al carrito."""
        # Verifica si el libro está agotado
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        # Verifica si hay suficientes existencias
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)

        # Si todo está bien, agrega el libro al carrito
        item = self.carrito.agregar_item(libro, cantidad)

        # Disminuir las existencias del libro
        libro.existencias -= cantidad
        
        return item

    def retirar_item_de_carrito(self, isbn: str):
        """Elimina un libro del carrito utilizando su ISBN."""
        self.carrito.quitar_item(isbn)


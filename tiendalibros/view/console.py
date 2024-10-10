import sys

from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_existente_error import LibroAgotadoError, LibroExistenteError
from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras

    # Defina el metodo agregar_libro_a_carrito_de_compras

    # Defina el metodo adicionar_un_libro_a_catalogo

    from excepciones import LibroExistenteError, LibroAgotadoError, ExistenciasInsuficientesError # type: ignore
from tienda_libros import TiendaLibros

class UIConsola:
    def __init__(self):
        self.tienda_libros = TiendaLibros()

    def retirar_libro_de_carrito_de_compras(self):
        """Pide al usuario el ISBN del libro a retirar del carrito."""
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")
        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print(f"El libro con ISBN {isbn} ha sido retirado del carrito exitosamente.")
        except Exception as e:
            print(f"Error al retirar el libro del carrito: {str(e)}")

    def agregar_libro_a_carrito_de_compras(self):
        """Pide al usuario el ISBN y la cantidad del libro a agregar al carrito."""
        isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
        cantidad = int(input("Ingrese la cantidad de unidades del libro: "))
        
        try:
            libro = self.tienda_libros.catalogo[isbn]  # Buscar el libro en el catálogo
            self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)
            print(f"Se han agregado {cantidad} unidades del libro con ISBN {isbn} al carrito.")
        except LibroAgotadoError as e:
            print(f"Error: {str(e)}")
        except ExistenciasInsuficientesError as e:
            print(f"Error: {str(e)}")
        except KeyError:
            print(f"Error: No se encontró un libro con ISBN {isbn}.")
        except Exception as e:
            print(f"Error al agregar el libro al carrito: {str(e)}")

    def adicionar_un_libro_a_catalogo(self):
        """Pide al usuario los detalles del libro y lo añade al catálogo."""
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese la cantidad de existencias del libro: "))

        try:
            libro = self.tienda_libros.adicionar_libro_a_catálogo(isbn, titulo, precio, existencias)
            print(f"El libro '{libro.titulo}' ha sido añadido al catálogo exitosamente.")
        except LibroExistenteError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al añadir el libro al catálogo: {str(e)}")


import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError


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


    def retirar_libro_de_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro a retirar del carrito: ")
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("Libro retirado del carrito con éxito.")
        except LibroError as e:
            print("Error: ", str(e))

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro a agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            libro = self.tienda_libros.catalogo.get(isbn, None)
            if libro is None:
                print("El libro con ISBN {} no existe en el catálogo.".format(isbn))
                return
            self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)
            print("Libro agregado al carrito con éxito.")
        except ExistenciasInsuficientesError as e:
            print("Error: No hay suficientes unidades en existencia. ", str(e))
        except LibroAgotadoError as e:
            print("Error: El libro está agotado. ", str(e))
        except LibroError as e:
            print("Error: ", str(e))

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese la cantidad de unidades en existencia: "))
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado al catálogo con éxito.")
        except LibroExistenteError as e:
            print("Error: El libro ya existe en el catálogo. ", str(e))
        except LibroError as e:
            print("Error: ", str(e))
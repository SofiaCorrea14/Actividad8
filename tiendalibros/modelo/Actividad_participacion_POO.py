from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.carro_compra import CarroCompras

class LibroExistenteError(Exception):
    pass

class LibroAgotadoError(Exception):
    pass

class ExistenciasInsuficientesError(Exception):
    pass

class TiendaLibros: # Implemente la clase TiendaLibros
    def __init__(self):
        # Defina los atributos catálogo y carrito. 
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias): # Defina un método adicionar_libro_a_catálogo que reciba como parámetro el isbn, titulo, precio, existencias.
        if isbn in self.catalogo: # Verifique si ya existe un libro en el catálogo con ese isbn
            raise LibroExistenteError("El libro con el ISBN {} ya existe en el catálogo.".format(isbn)) # En caso de que ya exista debe lanzar una excepción LibroExistenteError.
        else:
            #En caso de que no exista, debe crea un objeto de la clase Libro con los datos recibidos por parámetro, agregar el objeto al catálogo y retornarlo. 
            libro = Libro(isbn, titulo, precio, existencias)
            self.catalogo[isbn] = libro
            return libro

    def agregar_libro_a_carrito(self, libro, cantidad): # Defina un método agregar_libro_a_carrito, reciba como parámetro el libro y la cantidad de unidades de ese libro agregar al carrito.
        if libro.existencias == 0: # Si el libro no tiene existencias.
            raise LibroAgotadoError("El libro '{}' está agotado.".format(libro.titulo)) # Lance una excepción LibroAgotadoError.
        if cantidad > libro.existencias: # Si no hay suficientes unidades del libro en existencias para cubrir la compra lance una excepción ExistenciasInsuficientesError.
            raise ExistenciasInsuficientesError("No hay suficientes unidades de '{}' en existencias.".format(libro.titulo))
        
        # Si no ocurren ninguno de los dos casos anteriores agregue el libro al carrito. 
        self.carrito.agregar_item(libro, cantidad)
        libro.existencias -= cantidad

    def retirar_item_de_carrito(self, isbn): # Defina un método retirar_item_de_carrito, reciba como parámetro el isbn del libro a eliminar del carrito.
        # En el cuerpo del método elimine el item del carrito llamando el método quitar_item del objeto carrito. 
        libro = self.catalogo.get(isbn, None)
        if libro is not None:
            self.carrito.quitar_item(isbn)
            # Incrementa las existencias del libro en el catálogo
            libro.existencias += 1

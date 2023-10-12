from tiendalibros.modelo.libro_error import LibroError
class LibroError(Exception):
    pass

class ExistenciasInsuficientesError(LibroError): # Cree un tipo de excepción ExistenciasInsuficientesError que herede de la excepción LibroError. 
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias): # Llame el método inicializador de la clase padre.
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar # Cree un atributo llamado cantidad_a_comprar, asignele un valor recibido por parámetro.
        self.existencias = existencias

    def __str__(self): # Defina un método especial para representar el objeto como una cadena de texto.
        return f"El libro con título '{self.titulo}' y ISBN: {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"
from tiendalibros.modelo.libro_error import LibroError
class LibroError(Exception):
    pass

class LibroAgotadoError(LibroError): # Cree un tipo de excepción LibroAgotadoError que herede de la excepción LibroError
    def __init__(self, titulo, isbn): #  En el método inicializador de la clase LibroAgotadoError llame el método inicializador de la clase padre.
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

# Defina un método especial para representar el objeto como una cadena de texto, de tal forma que la representación en cadena de texto.
    def __str__(self): 
        return f"El libro con título '{self.titulo}' y ISBN: {self.isbn} está agotado."

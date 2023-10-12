from tiendalibros.modelo.libro_error import LibroError

class LibroError(Exception):
    pass

class LibroExistenteError(LibroError): # Cree un tipo de excepción LibroExistenteError que herede de la excepción LibroError. 
    def __init__(self, titulo, isbn): # En el método inicializador de la clase LibroExistenteError llame el método inicializador de la clase padre. 
        super().__init__()
        self.titulo = titulo 
        self.isbn = isbn

    def __str__(self): # Defina un método especial para representar el objeto como una cadena de texto.
        return f"El libro con título '{self.titulo}' y ISBN: {self.isbn} ya existe en el catálogo."
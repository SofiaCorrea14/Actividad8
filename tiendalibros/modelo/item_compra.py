from tiendalibros.modelo.libro import Libro

class ItemCompra:
    def __init__(self, libro, cantidad): # Inicializador de la clase ItemCompra
        self.libro = libro # Atributo libro 
        self.cantidad = cantidad # Atributo cantidad de tipo Libro y int, respectivamente.

    def calcular_subtotal(self): # Defina un método llamado "calcular_subtotal"
        subtotal = self.libro.precio * self.cantidad # Calcule el subtotal multiplicando la cantidad por el precio del libro.
        return subtotal

from tiendalibros.modelo.item_compra import ItemCompra

class CarroCompras:
    def __init__(self): # Inicializador de la clase CarroCompras.
        self.items = [] # Inicializa la lista de items de compra como una lista vacía.

    def agregar_item(self, libro, cantidad): # Cree un método llamado "agregar_item".
        nuevo_item = ItemCompra(libro, cantidad) # Cree un objeto de la clase ItemCompra.
        self.items.append(nuevo_item) # La cantidad de unidades del libro a agregar.
        return nuevo_item # Se retorna el item creado y agregado.

    def calcular_total(self): # Cree el método calcular_total
        total = 0.0
        for item in self.items:
            total += item.calcular_subtotal() # Sume todos los subtotales de todos los item de la lista de items.
        return total # Retorne el total.

    def quitar_item(self, isbn): # Cree un método quitar_item, que reciba como parámetro un isbn.
        self.items = [item for item in self.items if item.libro.isbn != isbn] # Utilizando un list comprehension elimine de la lista items el item que contenga el libro con ese isbn. 
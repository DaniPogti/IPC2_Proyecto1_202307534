class NodoDato:
    def __init__(self, posx, posy, valor, nombre):
        self.posx = posx
        self.posy = posy
        self.valor = valor
        self.nombre = nombre
        self.fila = posx  # Assign the row number (posx) to the 'fila' attribute
        self.procesada = False  # Add this attribute to track if the row has been processed
        self.siguiente = None
        
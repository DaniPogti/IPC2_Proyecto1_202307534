class matriz:
    def __init__(self, nombre, n, m, datos):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.datos = datos
        
    def __str__(self):
        return f'MATRICES: {self.nombre} \nNum Fila: {self.n} \nNum Columna: {self.m}\n'

    
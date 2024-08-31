from ListaSimple import Lista_Enlazada_Simple

class Matriz:
    def __init__(self, n, m, nombre):
        self.n = n
        self.m = m
        self.nombre = nombre
        self.matriz_original = Lista_Enlazada_Simple(n, m, nombre)
        self.matriz_transformada = Lista_Enlazada_Simple(n, m, nombre)
        # Copia los valores iniciales en matriz_original
        self.copiarDatosIniciales()

    def copiarDatosIniciales(self):
        actual = self.matriz_original.cabeza
        while actual:
            valor = actual.valor
            self.matriz_transformada.insertar(actual.posx, actual.posy, valor, self.nombre)
            actual = actual.siguiente
            if actual == self.matriz_original.cabeza:
                break

    def MatrizPatrones(self):
        actual = self.matriz_transformada.cabeza
        if not actual:
            return
        while True:
            if actual.valor != 0:
                actual.valor = 1
            actual = actual.siguiente
            if actual == self.matriz_transformada.cabeza:
                break

    def obtenerValor(self, posx, posy):
        actual = self.matriz_transformada.cabeza
        while actual:
            if actual.posx == posx and actual.posy == posy:
                return actual.valor
            actual = actual.siguiente
            if actual == self.matriz_transformada.cabeza:
                break
        return 0

    def obtenerValorOriginal(self, posx, posy):
        actual = self.matriz_original.cabeza
        while actual:
            if actual.posx == posx and actual.posy == posy:
                return actual.valor
            actual = actual.siguiente
            if actual == self.matriz_original.cabeza:
                break
        return 0

    def sonFilasIdenticas(self, fila1, fila2):
        for j in range(1, self.m + 1):
            if self.obtenerValor(fila1, j) != self.obtenerValor(fila2, j):
                return False
        return True

    def formarTuplas(self):
        actual = self.matriz_transformada.cabeza
        tuplas = Lista_Enlazada_Simple(self.n, self.m, self.nombre)

        while actual:
            for j in range(1, self.m + 1):
                valor_original = self.obtenerValorOriginal(actual.posx, j)
                tupla = (valor_original,)
                tuplas.insertar(actual.posx, j, tupla, self.nombre)
            
            actual = actual.siguiente
            if actual == self.matriz_transformada.cabeza:
                break

        return tuplas

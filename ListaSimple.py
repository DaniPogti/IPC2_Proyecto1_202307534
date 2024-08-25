from datoNodo import NodoDato

class Lista_Enlazada_Simple:
    def __init__(self, n, m, nombre):
        self.cabeza = None
        self.n = int(n)
        self.m = int(m)
        self.nombre = nombre
        
    def insertar(self, posx, posy, valor):
        self.posx = posx 
        self.posy = posy
        self.valor = valor
        
        if posx > self.n or posy > self.m or posx < 1 or posy < 1:
            print(f"Fuera de rango en: x: {posx}, y: {posy}")
            return
            
        nodoNuevo = NodoDato(posx, posy, valor)
        if self.cabeza == None:
            self.cabeza = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
            
    def imprimir(self):
        print(f"Nombre de la Matriz: {self.nombre} | Con Filas N: {self.n} y Columnas M: {self.m}")
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                actual = self.cabeza
                encontrado = False
                while actual:
                    if actual.posx == i and actual.posy == j:
                        print("| ",actual.valor, end=" |")
                        encontrado = True
                        break
                    actual = actual.siguiente
                if not encontrado:
                    print("| ", 0, end=" |")
            print()
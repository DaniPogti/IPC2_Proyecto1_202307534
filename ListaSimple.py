from NODO import nodo
from datoNodo import NodoDato

class Lista_Enlazada_Simple:
    def __init__(self):
        self.cabeza = None
        
    def insertar(self, posx, posy, valor):
        self.posx = posx 
        self.posy = posy
        self.valor = valor
        nodoNuevo = NodoDato(posx, posy, valor)
        if self.cabeza == None:
            self.cabeza = nodoNuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo
            
    def imprimir(self):
        actual = self.cabeza
        while actual: 
            print(f"Posición: ({actual.posx}, {actual.posy})---- Valor: {actual.valor}")
            actual = actual.siguiente
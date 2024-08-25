from NodoMatrices import NodoMatriz
from ListaSimple import Lista_Enlazada_Simple

class ListaMatriz: 
    def __init__(self):
        self.cabeza = None
    
    def insertarmatrix(self, matriz):
        nodoNuevo = NodoMatriz(matriz)
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
        if self.cabeza == None:
            print("no hay ninguna matriz guardada")
            return
        actual = self.cabeza
        while True:
            #print(f"\nLa Matriz es: {actual.matriz.nombre}")
            actual.matriz.imprimir()
            actual = actual.siguiente
            if actual == self.cabeza:
                break
            
    def cambiarDatos(self):  # Método corregido
        actual = self.cabeza
        if not actual:
            return
        while True:
            actual.matriz.MatrizPatrones()  # Llamada correcta sin argumentos
            actual = actual.siguiente
            if actual == self.cabeza:
                break
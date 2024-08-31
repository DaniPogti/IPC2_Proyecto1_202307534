from NodoMatrices import NodoMatriz
from ListaSimple import Lista_Enlazada_Simple

class ListaMatriz: 
    def __init__(self):
        self.cabeza = None
        
    def matrizRepetida(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.matriz.nombre == nombre:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    def insertarmatrix(self, matriz, nombre):
        
        nodoNuevo = NodoMatriz(matriz, nombre)
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
            
    
    def procesar_matrices(self):
        actual = self.cabeza
        while actual:
            matriz = actual.matriz
            matriz.MatrizPatrones()  # Procesa la matriz para cambiar valores a 1 y 0
            print(f"Matriz procesada '{matriz.nombre}':")
            matriz.imprimir()  # Imprime la matriz procesada

            cabeza_resultado = matriz.sumar_filas_identicas()
            print(f"Matriz con filas idénticas sumadas '{matriz.nombre}':")
            matriz.imprimir_matriz_resultado(cabeza_resultado)
            
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
  
    
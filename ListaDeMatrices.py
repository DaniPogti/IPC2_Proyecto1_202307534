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
            
    
    def procesarMatrices(self):
        actual = self.cabeza
        try:
            while actual:
                matriz = actual.matriz

                matriz_copia = self.copiar_matriz(matriz)
                matriz_copia.MatrizPatrones()

                cabeza_resultado = matriz.sumarfR(matriz_copia)
                print(f"Matriz con filas idénticas sumadas '{matriz.nombre}':")
                matriz_copia.imprimir()
                matriz.imprimirResultado(cabeza_resultado)

                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        except: 
            print("error.... Existe una matriz errorea o ilegible")

            
    def copiar_matriz(self, matriz):
        
        copia = Lista_Enlazada_Simple(matriz.n, matriz.m, matriz.nombre)
        
        # Copia cada nodo de la matriz original a la nueva matriz
        actual = matriz.cabeza
        try:
            while True:
                copia.insertar(actual.posx, actual.posy, actual.valor, actual.nombre)
                actual = actual.siguiente
                if actual == matriz.cabeza:
                    break
            
            return copia 
        except:
            print("error.... Existe una matriz errorea o ilegible")   
    
    '''def generar_xml_matrices_reducidas(self, archivo_salida): #ya no se uso esto :(
        doc = Document()

        root = doc.createElement("Matrices")
        doc.appendChild(root)

        actual = self.cabeza
        while actual:
            matriz = actual.matriz
            matriz_copia = self.copiar_matriz(matriz)
            matriz_copia.MatrizPatrones()
            cabeza_resultado = matriz.sumarfR(matriz_copia)

            matriz_elemento = doc.createElement("Matriz")
            nombre_elemento = doc.createElement("Nombre")
            nombre_elemento.appendChild(doc.createTextNode(matriz.nombre))
            matriz_elemento.appendChild(nombre_elemento)
            
            filas_elemento = doc.createElement("Filas")
            fila_nodo = cabeza_resultado
            while fila_nodo:
                fila_elemento = doc.createElement("Fila")
                fila_elemento.setAttribute("numero", str(fila_nodo.fila))
                columna_elemento = doc.createElement("Columna")
                columna_elemento.setAttribute("numero", str(fila_nodo.columna))
                columna_elemento.appendChild(doc.createTextNode(str(fila_nodo.valor)))
                fila_elemento.appendChild(columna_elemento)
                filas_elemento.appendChild(fila_elemento)
                fila_nodo = fila_nodo.siguiente

            matriz_elemento.appendChild(filas_elemento)
            root.appendChild(matriz_elemento)

            actual = actual.siguiente
            if actual == self.cabeza:
                break

        with open(archivo_salida, 'w') as f:
            f.write(doc.toprettyxml(indent="  "))'''
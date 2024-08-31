from datoNodo import NodoDato
from NodoR import NodoMatrizResultado

class Lista_Enlazada_Simple: # la lista es circular pero le puse simple, mi error 
    def __init__(self, n, m, nombre): #atributos de n filas, m columnas y nombre de matriz
        self.cabeza = None
        self.n = int(n)
        self.m = int(m)
        self.nombre = nombre
        
    def insertar(self, posx, posy, valor, nombre): #insertar valores de x, y y valor de cada celda
        self.posx = posx 
        self.posy = posy
        self.valor = valor
        self.nombre = nombre
        
        if posx > self.n or posy > self.m or posx < 1 or posy < 1: #si X y Y pasan del rango de n y m, no agrega esos datos
            print(f"Dato fuera de rango: x: {posx}, y: {posy}, valor: {valor}, en matriz {self.nombre}")
            return
        
        elif self.n <= 0 or self.m <= 0: #si X y Y pasan del rango de n y m, no agrega esos datos
            print(f"Fuera de rango en: N {self.n}, M {self.m}")
            return
            
        nodoNuevo = NodoDato(posx, posy, valor, nombre) #crea un nuevo nodo con x, y valor
        if self.cabeza == None: #si la cabeza de la lista vacia
            self.cabeza = nodoNuevo # nuevo nodo que se conbierte en la cabeza
            nodoNuevo.siguiente = self.cabeza # apunta de regreso a la cabeza
        else: #si no esta vacia la lista
            actual = self.cabeza #se inicia puntero en la cabeza de la lista para iniciar a recorrer la lista
            #recorre la lista hasta toparse con el ultimo nodo, verificando que el ultimo nodo no sea la cabeza
            while actual.siguiente != self.cabeza: 
                actual = actual.siguiente #mueve el puntero al siguiente nodo
            actual.siguiente = nodoNuevo #cuando encuentra el ultimo nodo, apunte al nuevo nodo, y uñada uno nuevo
            nodoNuevo.siguiente = self.cabeza #apunta de nuevo a la cabeza
            
            
    def imprimir(self):
        if self.n <= 0 or self.m <= 0:
            print("**********************************************************************************")
            print(f"Matriz '{self.nombre}' no validad: N = {self.n}, M = {self.m}. Fuera de rango")
            print("**********************************************************************************")
            return
        print("============================================================================================")
        print(f"Nombre de la Matriz: {self.nombre} | Con Filas N: {self.n} y Columnas M: {self.m}")
        for i in range(1, self.n + 1):#recorre filas
            for j in range(1, self.m + 1):#recorre columnas
                actual = self.cabeza
                encontrado = False
                while actual:
                    if actual.posx == i and actual.posy == j: #si cordenada i,j es igual a x,y imprime
                        print("| ",actual.valor, end=" |")
                        encontrado = True 
                        break
                    actual = actual.siguiente #rompe y pase al siguiente
                if not encontrado: # ni no encuentra nada en i,j coloca un 0 en esa posicion
                    print("| ", 0, end=" |")
            print()
            actual = actual.siguiente
            if actual == self.cabeza:  # Si recorre la cabeza otra vez, termina el ciclo
                break
        print("============================================================================================")
            
    def MatrizPatrones(self):
        actual = self.cabeza #cabeza de lista 
        if not actual:
            return #si no hay nada retorna nada
        while True:
            if actual.valor != 0: #valores diferentes de 0 escribe un 1
                actual.valor = 1
            actual = actual.siguiente
            if actual == self.cabeza: #si recorre la cabeza otra vez termina el ciclo
                break
            
    def obtenerValor(self, posx, posy):
        actual = self.cabeza
        while actual:
            if actual.posx == posx and actual.posy == posy:
                return actual.valor
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return 0

    def sonFilasIdenticas(self, fila1, fila2):
        suma = 0
        for j in range(1, self.m + 1):
            valor1 = self.obtenerValor(fila1, j)
            valor2 = self.obtenerValor(fila2, j)
            if valor1 != valor2:
                return False, 0
            suma += valor1
        return True, suma
    
    def sumar_filas_identicas(self):
        # Crear la cabeza de la lista de nodos resultado
        cabeza_resultado = None
        ultimo_nodo = None
        
        # Recorre cada fila para encontrar filas idénticas y sumar los valores
        for fila1 in range(1, self.n + 1):
            for fila2 in range(fila1 + 1, self.n + 1):
                filas_identicas, suma = self.sonFilasIdenticas(fila1, fila2)
                if filas_identicas:
                    for columna in range(1, self.m + 1):
                        valor1 = self.obtenerValor(fila1, columna)
                        valor2 = self.obtenerValor(fila2, columna)
                        suma_valor = valor1 + valor2
                        nuevo_nodo = NodoMatrizResultado(fila1, columna, suma_valor)
                        
                        if cabeza_resultado is None:
                            cabeza_resultado = nuevo_nodo
                            ultimo_nodo = nuevo_nodo
                        else:
                            ultimo_nodo.siguiente = nuevo_nodo
                            ultimo_nodo = nuevo_nodo
                            
                    for columna in range(1, self.m + 1):
                        nodo = self.obtenerValor(fila2, columna)
                        if nodo:
                            nodo.valor = 0

        return cabeza_resultado

    def imprimir_matriz_resultado(self, cabeza_resultado):
        if cabeza_resultado is None:
            print("No hay resultados para mostrar.")
            return
        
        print("============================================================================================")
        print(f"Nombre de la Matriz: {self.nombre} | Con Filas N: {self.n} y Columnas M: {self.m}")

        for fila in range(1, self.n + 1):
            columna = 1
            while columna <= self.m:
                nodo = cabeza_resultado
                encontrado = False
                while nodo:
                    if nodo.fila == fila and nodo.columna == columna:
                        print("| ", nodo.valor, end=" |")
                        encontrado = True
                        break
                    nodo = nodo.siguiente
                
                if not encontrado:
                    print("| ", 0, end=" |")
                columna += 1
            print()
        print("============================================================================================")
            
       
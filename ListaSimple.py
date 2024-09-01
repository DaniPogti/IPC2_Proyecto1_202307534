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
    
    def sumar_filas_identicas(self, referencia):
        cabeza_resultado = None
        ultimo_nodo = None

        fila_actual = 1
        while fila_actual <= self.n:
            if referencia.esta_fila_procesada(fila_actual):
                fila_actual += 1
                continue  # Si la fila ya fue procesada, pasar a la siguiente

            fila_duplicada = False
            
            fila_comparada = fila_actual + 1
            while fila_comparada <= self.n:
                if not referencia.esta_fila_procesada(fila_comparada) and referencia.sonFilasIdenticas(fila_actual, fila_comparada):
                    fila_duplicada = True
                    
                    # Sumar las filas idénticas
                    for columna in range(1, self.m + 1):
                        valor_fila = self.obtenerValor(fila_actual, columna)
                        valor_fila_comparada = self.obtenerValor(fila_comparada, columna)
                        suma_valor = valor_fila + valor_fila_comparada

                        # Insertar el resultado en la lista resultante
                        nuevo_nodo = NodoMatrizResultado(fila_actual, columna, suma_valor)

                        if cabeza_resultado is None:
                            cabeza_resultado = nuevo_nodo
                            ultimo_nodo = nuevo_nodo
                        else:
                            ultimo_nodo.siguiente = nuevo_nodo
                            ultimo_nodo = nuevo_nodo
                    
                    # Marcar la fila duplicada como procesada
                    referencia.marcar_fila_como_procesada(fila_comparada)
                
                fila_comparada += 1

            # Si la fila no tenía duplicados o ya fue procesada, se mantiene tal cual
            if not fila_duplicada:
                for columna in range(1, self.m + 1):
                    valor = self.obtenerValor(fila_actual, columna)
                    nuevo_nodo = NodoMatrizResultado(fila_actual, columna, valor)
                    if cabeza_resultado is None:
                        cabeza_resultado = nuevo_nodo
                        ultimo_nodo = nuevo_nodo
                    else:
                        ultimo_nodo.siguiente = nuevo_nodo
                        ultimo_nodo = nuevo_nodo

            # Marcar la fila actual como procesada después de usarla
            referencia.marcar_fila_como_procesada(fila_actual)

            fila_actual += 1

        return cabeza_resultado

    def esta_fila_procesada(self, fila):
        nodo = self.cabeza
        while nodo:
            if nodo.fila == fila:
                return nodo.procesada
            nodo = nodo.siguiente
            if nodo == self.cabeza:  # Para listas circulares
                break
        return False

    def marcar_fila_como_procesada(self, fila):
        nodo = self.cabeza
        while nodo:
            if nodo.fila == fila:
                nodo.procesada = True
            nodo = nodo.siguiente
            if nodo == self.cabeza:  # Para listas circulares
                break


    def imprimir_matriz_resultado(self, cabeza_resultado):
        if cabeza_resultado is None:
            print("No hay resultados para mostrar.")
            return
        
        print("============================================================================================")
        print(f"!!!!!!Nombre de la Matriz Reducida!!!!!: {self.nombre} | Con Filas N: {self.n} y Columnas M: {self.m}")

        for fila in range(1, self.n + 1):
            for columna in range(1, self.m + 1):
                nodo = cabeza_resultado
                encontrado = False
                while nodo:
                    if nodo.fila == fila and nodo.columna == columna:
                        print("| ", nodo.valor, end=" |")
                        encontrado = True
                        break
                    nodo = nodo.siguiente
                
                if not encontrado:
                    # Retrieve the original value from the matrix and print it instead of 0
                    valor_original = self.obtenerValor(fila, columna)
                    print("| ", valor_original, end=" |")
            print()
        print("============================================================================================")

            
    def sumar_filas_identicas_referencia(self, referencia):
    # Crear la cabeza de la lista de nodos resultado
        cabeza_resultado = None
        ultimo_nodo = None

        fila_actual = 1  # Controla la fila actual que se está comparando

        while fila_actual <= self.n:
            # Marcar la fila actual para evitar re-procesarla
            referencia.marcar_fila_como_procesada(fila_actual)

            columna_actual = 1  # Itera por cada columna

            while columna_actual <= self.m:
                # Inicializar la suma para esta columna
                suma_valor = 0
                fila_a_sumar = fila_actual

                while fila_a_sumar <= self.n:
                    # Obtener si las filas son idénticas y la suma
                    son_identicas, suma_filas = referencia.sonFilasIdenticas(fila_actual, fila_a_sumar)
                    
                    if son_identicas:
                        # Sumar los valores de todas las filas idénticas
                        suma_valor += self.obtenerValor(fila_a_sumar, columna_actual)
                        referencia.marcar_fila_como_procesada(fila_a_sumar)  # Marcar fila como procesada

                    fila_a_sumar += 1

                # Crear un nuevo nodo para almacenar el resultado de la suma
                nuevo_nodo = NodoMatrizResultado(fila_actual, columna_actual, suma_valor)

                # Si es el primer nodo, se convierte en la cabeza de la lista
                if cabeza_resultado is None:
                    cabeza_resultado = nuevo_nodo
                    ultimo_nodo = nuevo_nodo
                else:
                    # Si no, se enlaza al final de la lista
                    ultimo_nodo.siguiente = nuevo_nodo
                    ultimo_nodo = nuevo_nodo

                columna_actual += 1

            fila_actual += 1

        return cabeza_resultado       
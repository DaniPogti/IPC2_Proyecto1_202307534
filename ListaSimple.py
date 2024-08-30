from datoNodo import NodoDato

class Lista_Enlazada_Simple: # la lista es circular pero le puse simple, mi error 
    def __init__(self, n, m, nombre): #atributos de n filas, m columnas y nombre de matriz
        self.cabeza = None
        self.n = int(n)
        self.m = int(m)
        self.nombre = nombre
        
    def insertar(self, posx, posy, valor): #insertar valores de x, y y valor de cada celda
        self.posx = posx 
        self.posy = posy
        self.valor = valor
        
        if posx > self.n or posy > self.m or posx < 1 or posy < 1: #si X y Y pasan del rango de n y m, no agrega esos datos
            print(f"Dato fuera de rango: x: {posx}, y: {posy}, valor: {valor}, en matriz {self.nombre}")
            return
        
        elif self.n <= 0 or self.m <= 0: #si X y Y pasan del rango de n y m, no agrega esos datos
            print(f"Fuera de rango en: N {self.n}, M {self.m}")
            return
            
        nodoNuevo = NodoDato(posx, posy, valor) #crea un nuevo nodo con x, y valor
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
            print(f"Matriz {self.nombre} no validad: N = {self.n}, M = {self.m}. No se almacena")
            print("____________________________________________________________________________________________")
            return
        print("____________________________________________________________________________________________")
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
        print("____________________________________________________________________________________________")
            
    def MatrizPatrones(self):
        actual = self.cabeza #cabeza de lista 
        if not actual:
            return #si no hay nada retorna nada
        while True:
            if actual.valor != 0: #valores diferentes de 0 escribe un 1
                actual.valor = 1
            actual = actual.siguiente
            if actual == self.cabeza: #si recorre la cabeza otra bez termina el ciclo
                break
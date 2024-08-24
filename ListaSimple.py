from NODO import nodo

class Lista_Enlazada_Simple:
    def __init__(self) :
        self.cabeza = None
        self.size = 0
        
    def insertar(self, dato):
        nodo_nuevo = nodo(dato) #se crea un nuevo nodo
        if self.cabeza == None: #si la lista esta vacia
            self.cabeza = nodo_nuevo #crea nuevo nodo
        else: #si ya existe un dato dentro de la lista
            actual = self.cabeza #obtener el primero de la lista
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nodo_nuevo
        self.size += 1
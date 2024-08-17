class Nodo:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        ''' 
        self.x = x
        self.y = y
        '''
        self.next = None
        
class Lista:
    def __init__(self):
        self.head = None
        
    def append(self, nombre, n, m):
        nuevoNodo = Nodo(nombre, n, m)
        #si la lista esta vacia el nuevo nodo sera la cabeza de la lista
        if self.head is None: 
            self.head = nuevoNodo
            nuevoNodo.next = self.head #apunta a el mismo para ser l nuevo nodo
        #si la lista no esta vacia recorre la lista y se posiciona como un nevo nodo
        else: 
            actual = self.head
            while actual.next != self.head:
                actual=actual.next #siguiente nodo para despues actualizar y colocarlo como nuevo
            actual.next = nuevoNodo
            nuevoNodo.next = self.head
    
    def display(self): #imprime los datos de la lista
        if self.head is None: # si lista estar vacia
            print("no hay nada pa")
            return
        
        
import xml.etree.ElementTree as ET 
from xml.dom import minidom # Importar librería minidom
from xml.dom.minidom import Document 
from ListaSimple import Lista_Enlazada_Simple
from ListaDeMatrices import ListaMatriz


def Menu(): #Crear el menu en consola 
    print('=========Menu Principal=========')
    print('1. Cargar Archivo')
    print('2. Procesar Archivo')
    print('3. Escribir Archivo de Salida')
    print('4. Mostrar datos del Estudiante')
    print('5. Generar Grafica')
    print('6. Salida')
    print('================================')
    
    opcion = int(input('Ingresar opcion: ')) # obtiene el dato en la consola
    return opcion

def LeerArchivo(rutaArchivo):
    doc = minidom.parse(rutaArchivo)
    root = doc.documentElement
    print(root.tagName)
    
    '''arbol = ET.parse(rutaArchivo) #parsea el archivo xml
    root = arbol.getroot() #obtiene la raiz matriz
    print(root.tag)#imprime la ruta de larchivo'''
    
    # Encontrar todos los elementos 'matriz'
    matrices = root.getElementsByTagName('matriz')
    
    Matriz = ListaMatriz()# contiene la lista enlazada de las Matrices
    
    
    '''for nombre_matriz in root.findall('matriz'): #iterar y busca segun la etiqueta de matriz en el xml
        nombreMatriz = nombre_matriz.get('nombre') #obtener el atributo nombre de la matriz
        nFila = int(nombre_matriz.get('n'))#obtener el atributo n fila de la matriz
        mColumna = int(nombre_matriz.get('m'))#obtener el atributo m cplumna de la matriz
        
        if Matriz.matrizRepetida(nombreMatriz):
            print(f"Matriz '{nombreMatriz}' Ya existe")
            continue'''
            
    for matriz in matrices:
        nombreMatriz = matriz.getAttribute('nombre')
        nFila = int(matriz.getAttribute('n'))
        mColumna = int(matriz.getAttribute('m'))
        
        if Matriz.matrizRepetida(nombreMatriz):
            print(f"Matriz '{nombreMatriz}' ya existe")
            continue   
        
        #imprimen, m y nombre de matriz leida
        #print(f"Procesando Matriz: {nombreMatriz}| Num de Filas: {nFila}, Num Columnas: {mColumna}")
        
        #envia n, m y nombre a lista enlazada que lo contendra en una varible
        lista = Lista_Enlazada_Simple(nFila, mColumna, nombreMatriz)
        
        #dentro de la busqueda de 'matriz' por cada matriz encontrada busca etiqueta de 'dato' que contiene X, Y y el valor
        '''for dato in nombre_matriz.findall('dato'): 
            x = int(dato.get('x')) # en varible x obtiene el atributo de 'x' dentro de 'dato' como entero
            y = int(dato.get('y')) # en varible y obtiene el atributo de 'y' dentro de 'dato' como entero
            valor = int(dato.text) # dentro de la etiqueta 'dato' obtiene el texto que se encuentra adentro de y lo amacena en valor
            #print(f"Insertando: x={x}, y={y}, valor={valor}") #imprimir para verificar que si obtenga los datos
            lista.insertar(x, y, valor, nombreMatriz) #lista contiene la lsita enlazada simple, manda los datos por el metodo insertar
            
        #print(f"Matriz: {nombreMatriz}") # imprime el nombre de la matriz leida
        Matriz.insertarmatrix(lista, nombre_matriz) #lista enlazada de matricecs inserta los datos leidos por la lista enlazada 'lista' 
        lista.imprimir()'''
        
        datos = matriz.getElementsByTagName('dato')
        for dato in datos:
            x = int(dato.getAttribute('x'))
            y = int(dato.getAttribute('y'))
            valor = int(dato.firstChild.nodeValue)
            lista.insertar(x, y, valor, nombreMatriz)
        
        Matriz.insertarmatrix(lista, nombreMatriz)
        lista.imprimir()
        
    print('Datos leídos con éxito con ElementTree')
    return Matriz #retorna matriz almacenada


def EscribirArchivoMD(cargada):
    
    if not cargada or not cargada.cabeza:
        print("No hay matrices cargadas para escribir en el archivo.")
        return
    
    # Crear un nuevo documento XML
    doc = Document()
    
    # Crear el elemento raíz <matrices>
    root = doc.createElement('matrices')
    doc.appendChild(root)
    
    # Recorrer las matrices en la lista enlazada circular
    actual = cargada.cabeza
    while True:
        # Crear el elemento <matriz> con sus atributos
        matriz_element = doc.createElement('matriz')
        matriz_element.setAttribute('nombre', actual.matriz.nombre)
        matriz_element.setAttribute('n', str(actual.matriz.n))
        matriz_element.setAttribute('m', str(actual.matriz.m))
        
        # Añadir los datos de la matriz al elemento <matriz>
        nodo_dato = actual.matriz.cabeza
        while True:
            dato_element = doc.createElement('dato')
            dato_element.setAttribute('x', str(nodo_dato.posx))
            dato_element.setAttribute('y', str(nodo_dato.posy))
            dato_text = doc.createTextNode(str(nodo_dato.valor))
            dato_element.appendChild(dato_text)
            matriz_element.appendChild(dato_element)
            
            nodo_dato = nodo_dato.siguiente
            if nodo_dato == actual.matriz.cabeza:
                break
        
        # Añadir la matriz al elemento raíz <matrices>
        root.appendChild(matriz_element)
        
        # Avanzar al siguiente nodo de la lista circular
        actual = actual.siguiente
        if actual == cargada.cabeza:
            break
    
    # Escribir el XML a un archivo
    with open("salida.xml", "w", encoding='UTF-8') as file:
        file.write(doc.toprettyxml(indent="  "))
    
    print("Archivo XML generado con éxito.")
    
        

if __name__ == '__main__':
    opcion = 0
    cargada = None
    while opcion != 6:
        opcion = Menu()
        
        if opcion == 1:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 1')
            rutaArchivo = input("Ingrese la ruta del archivo: ")
            
            cargada = LeerArchivo(rutaArchivo) #verifica que ya se cargaron datos
            
        elif opcion == 2:
            print('-------------------------------------------------------------')
            print()
            print('Procesando Matriz')
            print('Imprimiendo Matrices')
            if cargada:
                #toda vez exista algun archivo cargado
                print("Matrices originales////////////////////////////")
                cargada.imprimir() #imprimir originales
                print("Matrices Nuevas////////////////////////////////")
                cargada.procesar_matrices()  # Procesa e imprime las matrices
                
            else:
                print('No hay matrices cargadas.')
            
        elif opcion == 3:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 3')
            EscribirArchivoMD(cargada)
            
        elif opcion == 4:
            print('-------------------------------------------------------------')
            print('Nombre: Daniel Alejandro Portillo Garcia')
            print('Carnet: 202307534')
            print('IPC2 Proyecto 1 2024')
            pass
        elif opcion == 5:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 5')
            break
        elif opcion == 6:
            print('-------------------------------------------------------------')
            print('Adios :)')
            break
        else:
            print('-------------------------------------------------------------')
            print ('Ingrese una opcion valida del de u numero del 1 al 6')
            continue
        print('-------------------------------------------------------------')
import xml.etree.ElementTree as ET 
from xml.dom import minidom
from matrices import matriz
from datos import data
from ListaCircular import CircularLista
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
    arbol = ET.parse(rutaArchivo) #parsea el archivo xml
    root = arbol.getroot() #obtiene la raiz matriz
    print(root.tag)#imprime la ruta de larchivo
    
    Matriz = ListaMatriz()# contiene la lista enlazada de las Matrices
    
    
    for nombre_matriz in root.findall('matriz'): #iterar y busca segun la etiqueta de matriz en el xml
        nombreMatriz = nombre_matriz.get('nombre') #obtener el atributo nombre de la matriz
        nFila = int(nombre_matriz.get('n'))#obtener el atributo n fila de la matriz
        mColumna = int(nombre_matriz.get('m'))#obtener el atributo m cplumna de la matriz
        
        
        
        #imprimen, m y nombre de matriz leida
        #print(f"Procesando Matriz: {nombreMatriz}| Num de Filas: {nFila}, Num Columnas: {mColumna}")
        
        #envia n, m y nombre a lista enlazada que lo contendra en una varible
        lista = Lista_Enlazada_Simple(nFila, mColumna, nombreMatriz)
        
        #dentro de la busqueda de 'matriz' por cada matriz encontrada busca etiqueta de 'dato' que contiene X, Y y el valor
        for dato in nombre_matriz.findall('dato'): 
            x = int(dato.get('x')) # en varible x obtiene el atributo de 'x' dentro de 'dato' como entero
            y = int(dato.get('y')) # en varible y obtiene el atributo de 'y' dentro de 'dato' como entero
            valor = int(dato.text) # dentro de la etiqueta 'dato' obtiene el texto que se encuentra adentro de y lo amacena en valor
            #print(f"Insertando: x={x}, y={y}, valor={valor}") #imprimir para verificar que si obtenga los datos
            lista.insertar(x, y, valor) #lista contiene la lsita enlazada simple, manda los datos por el metodo insertar
            
        print(f"Matriz: {nombreMatriz}") # imprime el nombre de la matriz leida
        Matriz.insertarmatrix(lista) #lista enlazada de matricecs inserta los datos leidos por la lista enlazada 'lista' 
        lista.imprimir()
        
    print('Datos leídos con éxito con ElementTree')
    return Matriz #retorna matriz almacenada
        

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
            print('Se eligio la opcion 2')
            if cargada:
                #toda vez exista algun archivo cargado
                print("Matrices originales////////////////////////////")
                cargada.imprimir() #imprimir originales
                cargada.cambiarDatos()#cambia originales a 1 y 0
                print("Matrices Nuevas////////////////////////////////")
                cargada.imprimir()# imprime las cambiadas
                
            else:
                print('No hay matrices cargadas.')
            
        elif opcion == 3:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 3')
            pass
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
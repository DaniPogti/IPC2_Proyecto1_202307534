import xml.etree.ElementTree as ET 
from xml.dom import minidom
from matrices import matriz
from datos import data
from ListaCircular import CircularLista
from ListaSimple import Lista_Enlazada_Simple


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
    global lista
    arbol = ET.parse(rutaArchivo) #parsea el archivo xml
    root = arbol.getroot() #obtiene la raiz matriz
    print(root.tag)#imprime la ruta de larchivo
    
    
    for nombre_matriz in root.findall('matriz'):
        nombreMatriz = nombre_matriz.get('nombre') #obtener el atributo nombre de la matriz
        nFila = int(nombre_matriz.get('n'))#obtener el atributo n fila de la matriz
        mColumna = int(nombre_matriz.get('m'))#obtener el atributo m cplumna de la matriz
        
        print(f"Procesando Matriz: {nombreMatriz}| Num de Filas: {nFila}, Num Columnas: {mColumna}")
        
        lista = Lista_Enlazada_Simple(nFila, mColumna, nombreMatriz)
        
        for dato in nombre_matriz.findall('dato'):
            x = int(dato.get('x'))
            y = int(dato.get('y'))
            valor = int(dato.text)
            print(f"Insertando: x={x}, y={y}, valor={valor}")
            lista.insertar(x, y, valor)
            
        print(f"Matriz: {nombreMatriz}")
        
        lista.imprimir()
        
    print('Datos leídos con éxito con ElementTree')
        

if __name__ == '__main__':
    opcion = 0
    while opcion != 6:
        opcion = Menu()
        
        if opcion == 1:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 1')
            rutaArchivo = input("Ingrese la ruta del archivo: ")
            LeerArchivo(rutaArchivo)
            
        elif opcion == 2:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 2')
            lista.imprimir()
            pass
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
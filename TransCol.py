import math

filetimetable = open("transColText.txt","r")
#Fichero con el criptograma (escrito en una linea)
lines=filetimetable.readlines()
filetimetable.close()
filetimetable2 = open("1-1000.txt","r")
#Fichero con las 1000 palabras más comunes en ingles
lines2=filetimetable2.readlines()
filetimetable.close()
from itertools import product
import itertools
import numpy as np
import sys

n = len(sys.argv)
print("Total arguments passed:", n)

for xs in range(2,7):
#como vimos en teoria la distribución de las palabras estan sobretodo distribuidas entre 2 y 7

    #numCol = int(sys.argv[1])
    numCol = xs
    #numCol será el numero de caracteres de nuestra palabra clave

    aux = len(lines[0])
    #longitud de nuestro criptograma

    numFil = int(aux/numCol) + (aux%numCol > 0)
    #numFil es el número de filas de nuestra matriz

    blank = (numCol * numFil) - aux
    #caracteres que quedan sin rellenar

    mat = [0]*numCol
    for m in range(numCol):
        mat[m] = m
    #matriz auxiliar para permutar las columnas

    matrix = [[0]*numCol for i in range(numFil)]
    #matriz principal en la que colocamos nuestro criptograma

    for n in range(blank):
        matrix[numFil-1][numCol-1-n]= "1"
    #rellenamos los espacios en blanco con "1"

    b = set(itertools.permutations(mat))
    #b son las permutaciones de las columnas
    a = set(itertools.permutations(matrix[numFil-1][0:numCol], numCol))
    #a son las posibles permutaciones de las posiciones vacias

    a = list(a)
    b = list(b)
    order = []

    t = 0

    pow = ""
    numP = 0
    listaC = []
    listaR = []

    for i in a:
        #Recorremos las permutaciones de los espacios en blanco
        print("")
        print(t)
        print("----------")

        pos = 0
        matrix[numFil-1][0:(numCol)] = a[t]
        #vamos cambiando la ultima fila de la matriz por las permutaciones de a

        for let in lines:
            for j in range(numCol):
                for i in range(numFil):
                    if ((matrix[i][j]) != "1"):
                        matrix[i][j] = let[pos]
                        pos = pos + 1
        #rellenamos el array (dejando sin rellenar los huecos con "1")

        array1 = np.array(matrix)
        #hacemos uso de la libreria numpy

        for re in b:
            #Una vez tenemos una posible permutación de los huecos en blanco rotamos las columnas
            l = ""
            result = array1[:,re]
            for j in range(numFil):
                print(" " + ''.join(result[j]))
                l = l + ''.join(result[j])

            print(" " + l)
            print("+-+-+-+-+-+")
            overall = 0
            if sys.argv[1] in l: 
                #Buscamos la pista en las divisiones creadas
                numP = numP + 1
                pow = pow + l + "\n"
                listaR.append(l)
                order.append(re)
                for ne in lines2:
                    #Intentamos agregar más filtros para aumentar la precisión de nuestro programa el fichero 2
                    #contiene las 1000 palabras más comunes en inglés 
                    if ne[0:(len(ne)-2)] in l:
                        overall = overall + 1
                listaC.append(overall)
                #listaC contiene el numero de coincidencias de cada posible solución
        t = t + 1

    if(pow!=""):
        print("  Resultados encontrados:")
        #Aqui imprimimos todos los posibles resultados (contienen palabra en claro)
        print(" " + pow)
        print(listaC)
        print("\n")

    if (len(listaC) != 0):
        maxIndex = listaC.index(max(listaC))
        #Buscamos el resultado con más coincidencias con palabras en inglés

        j=0
        M=[]
        m = max(listaC)
        for i in listaC:
            if i==m:
                M.append(j)
            j+=1
        #Si más de uno tiene el mismo número de coincidencias sacamos los dos

        print("  Posible solución:  ")
        print(order)
        print("longitud de la palabra clave: " + str(xs))
        print("\n")
        for i in M:
            print(listaR[i])
        print("\n")
        sys.exit(0)
        #En caso de encontrar posibles soluciones salimos del programa
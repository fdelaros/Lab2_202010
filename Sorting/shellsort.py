"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """



import config as cf
from ADT import list as lt
from DataStructures import listnode as node


def shellSort(lst, lessfunction):
    """
    shellSort sort para una lista generica con un comparador establecido
    Args:
        lst:: List
            Lista sobre la cual se realizará el ordenamiento
        lessfunction:
            Funcion de comparación con la cual se organizaran los datos
    Return :: None
    """
    n = lt.size(lst)
    h = 1
    print("h=", h)
    while h < n//3:          # Se calcula el tamaño del primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1         # por ejemplo para n = 100, h toma un valor inicial de 40, 13 , 4, 1
        print("h=", h)
    while (h >= 1):
        print("Shell h: ", h)
        for i in range (h+1,n+1):  # posiciones validas para comparar con elementos a h-distancia a la izquierda
            j = i
            print("Shell i: ", i)
            while (j>=(h+1)) and lessfunction (lt.getElement(lst,j),lt.getElement(lst,j-h)):
                lt.exchange (lst, j, j-h)
                print("Shell Exchange: ", j, j-h)
                j -= h
        h //= 3              # h se decrementa en un tercio. cuando h es 1, se comporta como insertionsort
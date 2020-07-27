"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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

import config
from DataStructures import arraylist as alt
from DataStructures import singlelinkedlist as slt
from Sorting import selectionsort as sels
from Sorting import insertionsort as inss
from Sorting import shellsort as shes
from Sorting import mergesort as mers

"""
  Este módulo implementa el tipo abstracto de datos (TAD) lista. 
  Se puede implementar sobre una estructura de datos encadenada de forma sencilla o doble
"""

def newList (datastructure='SINGLE_LINKED'):
    """
    Crea una lista vacia
    """
    if (datastructure == "ARRAY_LIST"):
        lt = alt.newList()
    else:
        lt = slt.newList()
    return lt


def addFirst(lst, element):
    """
    Agrega un elemento en la primera posición de la lista
    Args:
        lst :: lista
            La lista a la cual se le añadirá el nuevo elemento
        element
            Elemento que será agregado a la lista que se pasa por parametro
    Return : None
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.addFirst (lst, element)
    else:
        slt.addFirst (lst, element)


def addLast(lst, element):
    """
    Agrega un elemento en la última posición de la lista
    Args:
        lst :: lista
            La lista a la cual se le añadirá el nuevo elemento
        element
            Elemento que será agregado a la lista que se pasa por parametro
    Return : None 
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.addLast (lst, element)
    else:
        slt.addLast (lst, element)


def isEmpty (lst):
    """
    Indica si la lista está vacía(True) o no (False)
    Args:
        lst
            Lista a evaluar
    Return: True en caso de que si, False en caso contrario
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.isEmpty(lst)
    else:
        return slt.isEmpty(lst)


def size(lst):
    """
    Informa el número de elementos almacenados en la lista
    Args:
        lst
            Lista a evaluar
    Return::int
        El numero de elementos dentro de la lista
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.size(lst)
    else:
        return slt.size(lst)


def firstElement (lst):
    """
    Retorna el primer elemento de la lista, sin eliminarlo.
    Args:
        lst
            Lista a evaluar
    Return::int
        El primer elemento dentro de la lista
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.firstElement (lst)
    else:
        return slt.firstElement (lst)



def lastElement (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo.
    Args:
        lst
            Lista a evaluar
    Return::int
        El último elemento dentro de la lista
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.lastElement(lst)
    else:
        return slt.lastElement(lst)

def lastElementIterative (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo.
    Args:
        lst
            Lista a evaluar
    Return::int
        El último elemento dentro de la lista
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.lastElementIterative(lst)
    else:
        return slt.lastElementIterative(lst)

def getElement (lst, pos):
    """
    Retorna el elemento en la posición pos de la lista.
    pos debe ser mayor que cero y menor o igual al tamaño de la lista
    la lista no esta vacia
    Args:
        lst
            Lista a evaluar
        pos
            posicion en la lista en la cual está el elemento
    Return::int
        El elemento dentro de la lista en la posición indicada

    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.getElement (lst, pos) 
    else:
        return slt.getElement (lst, pos) 



def deleteElement (lst, pos):
    """
    Elimina el elemento en la posición pos de la lista.
    pos debe ser mayor que cero y menor o igual al tamaño de la lista
    la lista no esta vacia
    Args:
        lst
            Lista a evaluar
        pos
            posicion en la lista en la cual está el elemento
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.deleteElement(lst, pos) 
    else:
        slt.deleteElement(lst, pos) 




def removeFirst (lst):
    """
    Remueve el primer elemento de la lista
    Args:
        lst
            Lista a evaluar
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.removeFirst (lst)
    else:
        slt.removeFirst (lst)




def removeLast (lst):
    """
    Remueve el último elemento de la lista
    Args:
        lst
            Lista a evaluar
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.removeLast (lst)
    else:
        slt.removeLast (lst)




def insertElement (lst, element, pos):
    """
    Inserta el elemento element en la posición pos de la lista.
    Args:
        lst
            Lista a evaluar
        element
            Elemento que se desea insertar en la lista
        pos::int
            Posición en la cual se desea agregar el elemento
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.insertElement (lst, element, pos)
    else:
        slt.insertElement (lst, element, pos)
    



def isPresent (lst, element, comparefunction):
    """
    Informa si el elemento element esta presente en la lista.
    Args:
        lst
            Lista a evaluar
        element
            Elemento que se desea insertar en la lista
        comparefuntion
            Función que permitirá identificar si el elemento está o no presente
    Return :: int
        La primera posición en la que se encuentra o cero (0) si no esta presente
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.isPresent (lst, element, comparefunction)
    else:
        return slt.isPresent (lst, element, comparefunction)




def exchange (lst, pos1, pos2):
    """
    Intercambia la informacion en las posiciones pos1 y pos2 de la lista
    Args:
        lst::
            Lista en la cual se realizaran los cambios
        pos1:: int
            posición del primer elemento que se desea cambiar
        pos2 :: int
            posición del segundo elemento que se desea cambiar
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.exchange (lst, pos1, pos2)
    else:
        slt.exchange (lst, pos1, pos2)




def changeInfo (lst, pos, element):
    """
    Reemplaza la información de la lista en la posicion pos, con el elemento element
    Args:
        lst
            Lista a evaluar
        pos
            posición en la que se desea modificar la informacion
        newInfo
            Información que será agregada en vez de la existente
    Return :: None
    """
    if (lst['type']=='ARRAY_LIST'):
        alt.changeInfo (lst, pos, element)
    else:
        slt.changeInfo (lst, pos, element)

def subList (lst, pos, numelem):
    """
    Retorna una sublista de la lista lst, partiendo de la posicion pos, con una longitud de numelem elementos
    """
    if (lst['type']=='ARRAY_LIST'):
        return alt.subList (lst, pos, numelem)
    else:
        return slt.subList (lst, pos, numelem)

def copy (lstSrc, lstDest, lo, hi):
    """
    copiar la sublista de lstSrc en el rango [lo, hi] a la lista lstDest en el mismo rango
    """
    if (lstSrc['type']=='ARRAY_LIST'):
        return alt.copy (lstSrc, lstDest, lo, hi)
    else:
        return slt.copy (lstSrc, lstDest, lo, hi)

        
def selectionSort(lst, compFunction):
    """
    Aplicar selection sort a la lista
    """
    sels.selectionSort (lst, compFunction)
    

def insertionSort(lst, lessfunction):
    """
    Aplicar insertion sort a la lista
    """
    inss.insertionSort (lst, lessfunction)


def shellSort(lst, lessfunction):
    """
    Aplicar shell sort a la lista
    """
    shes.shellSort (lst, lessfunction)

def mergeSort(lst, lessfunction):
    """
    Aplicar merge sort a la lista
    """
    mers.mergeSort (lst, lessfunction)

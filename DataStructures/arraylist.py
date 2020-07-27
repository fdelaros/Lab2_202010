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

"""
  Este módulo implementa una estructura de datos lineal, como un arreglo de apuntadores a 
  los nodos de la lista.
"""


def newList ():
    """
    Crea una lista vacia
    """
    new_list = {'elements':[], 'size':0, 'type':'ARRAY_LIST' }
    return (new_list)


def addFirst(lst, element):
    """
    Agrega un elemento en la primera posición de la lista
    Aumenta el tamaño de la lista en 1
    Args:
        lst :: lista
            La lista a la cual se le añadirá el nuevo elemento
        element
            Elemento que será agregado a la lista que se pasa por parametro
    Return : None    
    """
    try: 
        lst['elements'].insert (0,element)
        lst['size'] += 1
    except:
        print("Ocurrió un error al agregar el elemento a la lista")
    



def addLast(lst, element):
    """
    Agrega un elemento en la última posición de la lista
    Aumenta el tamaño de la lista en 1
     Args:
        lst :: lista
            La lista a la cual se le añadirá el nuevo elemento
        element
            Elemento que será agregado a la lista que se pasa por parametro
    Return : None    

    """
    try:
        lst['elements'].append (element)
        lst['size'] += 1
    except:
        print("Ocurrió un error al agregar el elemento a la lista")



def isEmpty (lst):
    """
    Indica si la lista está vacía
    Args:
        lst
            Lista a evaluar
    Return: True en caso de que si, False en caso contrario
    """
    return lst['size'] == 0


def size(lst):
    """
    Informa el número de elementos de la lista
    Args:
        lst
            Lista a evaluar
    Return::int
        El numero de elementos dentro de la lista
    """
    return lst['size'] 


def firstElement (lst):
    """
    Retorna el primer elemento de la lista, sin eliminarlo. La lista no puede ser vacía
    Args:
        lst
            Lista a evaluar
    Return::int
        El primer elemento dentro de la lista
    """
    return lst['elements'][0]



def lastElement (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo. La lista no puede ser vacía
    Args:
        lst
            Lista a evaluar
    Return::int
        El último elemento dentro de la lista
    """
    return lst['elements'][lst['size']-1]



def lastElementIterative (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo. La lista no puede ser vacía
    Args:
        lst
            Lista a evaluar
    Return::int
        El último elemento dentro de la lista
    """
    ultimo = None
    i = 0
    while i < lst['size']:
        ultimo = lst['elements'][i]
        i += 1
    return ultimo



def getElement (lst, pos):
    """
    Retorna el elemento en la posición pos de la lista sin eliminarlo
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
    return lst['elements'][pos-1]


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
    lst['elements'].pop(pos)
    lst['size'] -= 1    


def removeFirst (lst):
    """
    Remueve el primer elemento de la lista y lo retorna. La lista no puede ser vacía
    Args:
        lst
            Lista a evaluar
    """
    element = lst['elements'].pop(0)
    lst['size'] -= 1
    return element


def removeLast (lst):
    """
    Remueve el último elemento de la lista y lo retorna en caso de existir, de lo contrario retorna None
    Args:
        lst
            Lista a evaluar
    """
    element = lst['elements'].pop(lst['size']-1)
    lst['size'] -= 1
    return element

def insertElement (lst, element, pos):
    """
    Inserta el elemento element en la posición pos de la lista. pos debe ser menor o igual al tamaño de la lista. 
    Args:
        lst
            Lista a evaluar
        element
            Elemento que se desea insertar en la lista
        pos::int
            Posición en la cual se desea agregar el elemento
    """
    lst['elements'].insert (pos-1,element) 
    lst['size'] += 1


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
    if lst['size'] > 0:
        keyexist = False
        for keypos in range (1,size+1):
            if (comparefunction (element, lst['elements'][keypos-1])):
                keyexist = True
                break
        if keyexist:
            return keypos
    return 0   


def changeInfo (lst, pos, newinfo):
    """
    Cambia la informacion contenida en el nodo de la lista en la posicion pos
    Args:
        lst
            Lista a evaluar
        pos
            posición en la que se desea modificar la informacion
        newInfo
            Información que será agregada en vez de la existente
    Return :: None
    """
    lst['elements'][pos-1] = newinfo

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
    infopos1 = getElement (lst, pos1)
    infopos2 = getElement (lst, pos2)
    changeInfo (lst, pos1, infopos2)
    changeInfo (lst, pos2, infopos1)

def subList (lst, pos, numelem):
    """
    Retorna una sublista de la lista lst, partiendo de la posicion pos, con una longitud de numelem elementos
    """
    sublst = {'elements':[], 'size':0, 'type':'ARRAY_LIST' }
    elem = pos-1
    cont = 1
    while  cont <= numelem:
        sublst['elements'].append (lst['elements'][elem])
        sublst['size'] += 1
        elem += 1
        cont += 1
    return sublst

def copy (lstSource, lstDest, lo, hi):
    """
    copiar la sublista de lstSource en el rango [lo, hi] a la lista lstDest en el mismo rango
    """
    for pos in range(lo, hi+1):
        lstDest['elements'][pos-1] = lstSource['elements'][pos-1]

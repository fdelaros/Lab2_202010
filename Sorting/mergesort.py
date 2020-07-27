import config as cf
from ADT import list as lt
from DataStructures import listnode as node

def mergeSort (lst, lessfunction):
    lstaux = lt.subList (lst, 1, lt.size(lst))     #crear una lista auxiliar del mismo tamaNo y con el mismo contenido
    sort(lst, lstaux, lessfunction, 1, lt.size(lst))

def sort (lst, auxlst, lessfunction, lo, hi):
    """
    Ordena los elementos de la lista lst que se encuentren en el rango [lo, hi].
    lessfunction es la función de comparación entre los elementos de la lista.
    auxlst es una lista auxiliar de mismo tamaño que la lista original para ayudar al ordenamiento
    """
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    sort(lst, auxlst, lessfunction, lo, mid)        #ordenamiento mitad de lst en el rango [lo, mid] 
    sort(lst, auxlst, lessfunction, mid+1, hi)      #ordenamiento mitad de lst en el rango [mid+1, hi]
    merge(lst, auxlst, lessfunction,  lo, mid, hi)  #mezcla de las dos mitades ordenadas de lst 

def merge(lst, auxlst, lessfunction, lo, mid, hi):
    """
    ordenar el rango [lo, hi] en lst mezclando sus mitades ordenadas en los rangos [lo, mid] y [mid+1, hi]
    """
    if hi <= lo:
        return
    lt.copy(lst, auxlst, lo, hi)                    #copiar la sublista de lst en el rango [lo, hi] a la lista auxlst en el mismo rango
    i = lo                                          #recorre la midad ordenada en auxlist en el rango [lo, mid]
    j = mid+1                                       #recorre la midad ordenada en auxlist en el rango [mid+1, hi]
    
    for k in range(lo, hi+1):
        if i > mid:                                 #ya se pasaron los elementos de la mitad ordenada [lo, mid] a lst
            lt.changeInfo(lst, k, lt.getElement(auxlst,j))
            j += 1
        elif j > hi:                                #ya se pasaron los elementos de la mitad ordenada [mid+1, hi] a lst
            lt.changeInfo(lst, k, lt.getElement(auxlst,i))
            i += 1
        elif lessfunction(lt.getElement(auxlst,j), lt.getElement(auxlst,i)):    # auxlst[j] < auxlst[i]
            lt.changeInfo(lst, k, lt.getElement(auxlst,j))
            j += 1
        else:                                                                   # auxlst[i] <= auxlst[j]
            lt.changeInfo(lst, k, lt.getElement(auxlst,i))
            i += 1
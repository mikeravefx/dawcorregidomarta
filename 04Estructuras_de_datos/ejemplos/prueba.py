def crea_lista(posiciones: int) -> list:
    lista = []
    for i in range(posiciones):
        valor = int(input("Introduce un entero: "))
        lista.append(valor)
    return lista

# Crea una función que reciba una lista y la devuelva invertida
def invierte_lista(lista: list) -> list:
    """Invierte una lista

    Args:
        lista (list): La lista a invertir

    Returns:
        list: La lista invertida

    >>> invierte_lista([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> invierte_lista([])
    []
    >>> invierte_lista([1])
    [1]
    >>> invierte_lista(['a', 'b', 'c'])
    ['c', 'b', 'a']
    """
    return lista[::-1]

#lista = crea_lista(5)
#print(lista)
#print(invierte_lista(lista))
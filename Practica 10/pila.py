def insertar(lista, dato):
    lista.append (dato)#agregar al final

def borrar(lista):
    dato = lista.pop()
    return dato

def imprimir_pila(lista):
    lista.reverse()
    for x in lista:
        print (x)
    print()
    lista.reverse()

def main():
    pila = [0]
    insertar(pila, 1)
    insertar(pila,2)
    imprimir_pila(pila)
    print()
    print(borrar(pila))
    print(pila)



if __name__ == "__main__":
    main()

'''
Hacer unna cola. agregar de un lado y sacar del otro
'''

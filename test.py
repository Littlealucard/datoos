NUMERO=[]
opcion = ''
while opcion != '5':
    print("\nque operacion desea realizar")
    print("1. ver arreglo")
    print("2. modificar")
    print("3. eliminar")
    print("4. agregar")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        print(NUMERO)
    elif opcion == '2':
        if len(NUMERO) == 0:
            print("no hay elementos")
        else:
            print(NUMERO)
            for i, elemento in enumerate(NUMERO):
                print(f"{i+1}. {elemento}")
                indice = int(input("posicion actual")) - 1
                if indice >= 0 and indice < len(NUMERO):
                    nuevo_elemento = input("ingresa el nuevo valor")
                    NUMERO[indice] = nuevo_elemento
                    print("modificado con exito")
                else:
                    print("invalido")
    elif opcion == '3':
        print(f"que desea eliminar")
        if len(NUMERO) == 0:
            print("no hay elementos")
        else:
            print("elementos actuales")
            for i, elemento in enumerate(NUMERO):
                print(f"{i+1}. {elemento}")
                indice = int(input("ingresa el numero a eliminar")) - 1
                if indice >= 0 and indice <len(NUMERO):
                    del NUMERO[indice]
                    print("elemento eliminado")
                else:
                        print("invalido")
    elif opcion == '4':
        elemento = input("ingresa el dato")
        NUMERO.append(elemento)
        print(NUMERO)

    elif opcion == '5':
        print("abueno adios master :) ")
        break


Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

#Mostrar productos
def mostrar_productos():
    print("===============================================")
    print("Listado de Productos")
    print("===============================================")
    for id, producto in Productos.items():
        print(f"{id:<5}{producto:<15}{Precios[id]:<10}{Stock[id]:<10}")


#Opción 1]

def agregar_producto():
    while True:
        try:
            id = int(input("Digite el ID del producto: "))
            if id in Productos:
                print(f"El ID {id} ya existe. Por favor, ingrese un ID diferente.")
                continue
            break
        except ValueError:
            print("El ID debe ser un número entero. Inténtalo de nuevo.")

    producto = input("Digite el nombre del producto: ").strip()
    if not producto:
        print("El nombre del producto no puede estar vacío. Inténtalo de nuevo.")
        return

    while True:
        try:
            precio = float(input("Digite el precio del producto: "))
            break
        except ValueError:
            print("El precio debe ser un número flotante. Inténtalo de nuevo.")

    while True:
        try:
            stock = int(input("Digite el stock del producto: "))
            break
        except ValueError:
            print("El stock debe ser un número entero. Inténtalo de nuevo.")

    Productos[id] = producto
    Precios[id] = precio
    Stock[id] = stock

    print("Producto agregado exitosamente.")
    print()
    mostrar_productos()


#Opción [2]
def eliminar_producto():
    while True:
        try:
            id = int(input("Digite el ID del producto a eliminar: "))
            if id not in Productos:
                print(f"El ID {id} no existe. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("El ID debe ser un número entero. Inténtalo de nuevo.")

    del Productos[id]
    del Precios[id]
    del Stock[id]

    print("Producto eliminado exitosamente.")
    print()
    mostrar_productos()



#Opción [3]
def actualizar_producto():
    while True:
        try:
            id = int(input("Digite el ID del producto a actualizar: "))
            if id not in Productos:
                print(f"El ID {id} no existe. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("El ID debe ser un número entero. Inténtalo de nuevo.")

    producto = input("Digite el nombre del producto: ").strip()
    if not producto:
        print("El nombre del producto no puede estar vacío. Inténtalo de nuevo.")
        return

    while True:
        try:
            precio = float(input("Digite el precio del producto: "))
            break
        except ValueError:
            print("El precio debe ser un número flotante. Inténtalo de nuevo.")

    while True:
        try:
            stock = int(input("Digite el stock del producto: "))
            break
        except ValueError:
            print("El stock debe ser un número entero. Inténtalo de nuevo.")

    Productos[id] = producto
    Precios[id] = precio
    Stock[id] = stock

    print("Producto actualizado exitosamente.")
     

# Mostrar productos y opciones
mostrar_productos()
while True:
    print("===============================================")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Actualizar")
    print("4. Salir")
    opcion = int(input("Digite la opción: "))

    if opcion == 1:
        agregar_producto()

    elif opcion == 2:
        eliminar_producto()

    elif opcion == 3:
        actualizar_producto()

    elif opcion == 4:
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")
        print()

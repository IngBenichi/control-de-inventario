import json
import os
import flet as ft
op=0
Vnombre=[]
Vcodigo_barras=[]
Vprecio=[]
Vcantidad_stock=[]
def cargar_datos():
    if os.path.exists('inventario.json'):
        with open('inventario.json', 'r') as file:
            return json.load(file)
    return {"Vnombre": [], "Vcodigo_barras": [], "Vprecio": [], "Vcantidad_stock": []}

def guardar_datos(datos):
    with open('inventario.json', 'w') as file:
        json.dump(datos, file, indent=4)


def main(page: ft.Page):
    page.title = "Control de Inventario"
    page.window_width = 800
    page.window_height = 600
    
    nombre_input = ft.TextField(label="Nombre del Producto")
    codigo_barras_input = ft.TextField(label="Código de Barras", keyboard_type=ft.KeyboardType.NUMBER)
    precio_input = ft.TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER)
    cantidad_stock_input = ft.TextField(label="Cantidad de Stock", keyboard_type=ft.KeyboardType.NUMBER)
    resultado = ft.Text()
    def mostrar_mensaje(mensaje):
        page.snack_bar = ft.SnackBar(ft.Text(mensaje))
        page.snack_bar.open = True
        page.update()
    
    def agregar_producto(e):
        nombre = nombre_input.value
        try:
            precio = float(precio_input.value)
            codigo_barras = int(codigo_barras_input.value)
            cantidad_stock = int(cantidad_stock_input.value)
        
            if precio > 0 and codigo_barras > 0 and cantidad_stock > 0:
                Vnombre.append(nombre.lower())
                Vcodigo_barras.append(codigo_barras)
                Vprecio.append(precio)
                Vcantidad_stock.append(cantidad_stock)
                guardar_datos({"Vnombre": Vnombre, "Vcodigo_barras": Vcodigo_barras, "Vprecio": Vprecio, "Vcantidad_stock": Vcantidad_stock})
                mostrar_mensaje("Producto agregado exitosamente")
            else:
                mostrar_mensaje("Datos inválidos. Por favor, verifique los valores ingresados.")
        except ValueError:
            mostrar_mensaje("Por favor, ingrese valores numéricos válidos para el precio, código de barras y cantidad de stock.")
    
    def buscar_producto(e):
        nombre = nombre_input.value.lower()
        if nombre in Vnombre:
            producto = Vnombre.index(nombre)
            resultado.text = (
                f"Nombre del Producto: {Vnombre[producto]}\n"
                f"Precio del Producto: {Vprecio[producto]}\n"
                f"Código de barras del Producto: {Vcodigo_barras[producto]}\n"
                f"Stock del Producto: {Vcantidad_stock[producto]}"
            )
        else:
            resultado.text = "Producto no encontrado"
        page.update()
    
    def modificar_producto(e):
        nombre = nombre_input.value.lower()
        if nombre in Vnombre:
            producto = Vnombre.index(nombre)
            try:
                nuevo_precio = float(precio_input.value)
                nuevo_codigo_barras = int(codigo_barras_input.value)
                nueva_cantidad_stock = int(cantidad_stock_input.value)

                if nuevo_precio > 0 and nuevo_codigo_barras > 0 and nueva_cantidad_stock > 0:
                    Vnombre[producto] = nombre
                    Vprecio[producto] = nuevo_precio
                    Vcodigo_barras[producto] = nuevo_codigo_barras
                    Vcantidad_stock[producto] = nueva_cantidad_stock
                    guardar_datos({"Vnombre": Vnombre, "Vcodigo_barras": Vcodigo_barras, "Vprecio": Vprecio, "Vcantidad_stock": Vcantidad_stock})
                    mostrar_mensaje("Producto modificado exitosamente")
                else:
                    mostrar_mensaje("Datos inválidos. Por favor, verifique los valores ingresados.")
            except ValueError:
                mostrar_mensaje("Por favor, ingrese valores numéricos válidos para el precio, código de barras y cantidad de stock.")
        else:
            mostrar_mensaje("Producto no encontrado")

    def eliminar_producto(e):
        eliminar = [index for index, cantidad in enumerate(Vcantidad_stock) if cantidad == 0]
        if eliminar:
            for index in sorted(eliminar, reverse=True):
                del Vnombre[index]
                del Vcodigo_barras[index]
                del Vprecio[index]
                del Vcantidad_stock[index]
            guardar_datos({"Vnombre": Vnombre, "Vcodigo_barras": Vcodigo_barras, "Vprecio": Vprecio, "Vcantidad_stock": Vcantidad_stock})
            mostrar_mensaje("Productos eliminados exitosamente")
        else:
            mostrar_mensaje("No hay productos con stock igual a cero.")

    def salir(e):
        page.window_close()
    
    page.add(
        ft.Column([
            ft.Text("                                                             ********** CONTROL DE INVENTARIO **********"),
            nombre_input,
            codigo_barras_input,
            precio_input,
            cantidad_stock_input,
            ft.Row([
                ft.ElevatedButton("Agregar Producto", on_click=agregar_producto),
                ft.ElevatedButton("Buscar Producto", on_click=buscar_producto),
                ft.ElevatedButton("Modificar Producto", on_click=modificar_producto),
                ft.ElevatedButton("Eliminar Productos con Stock 0", on_click=eliminar_producto),
                ft.ElevatedButton("Salir", on_click=salir),
            ]),
            resultado,
        ])
    )
ft.app(target=main)

# Cargar los datos al iniciar el programa
datos = cargar_datos()
Vnombre = datos["Vnombre"]
Vcodigo_barras = datos["Vcodigo_barras"]
Vprecio = datos["Vprecio"]
Vcantidad_stock = datos["Vcantidad_stock"]

def input_numerico(prompt, tipo=float):
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico.")

op = 0

while(op != 5):
    print("\n********** CONTROL DE INVENTARIO **********")
    print("\nOpciones:")
    print("1. Agregar Producto")
    print("2. Buscar Producto")
    print("3. Modificar Productos")
    print("4. Eliminar Productos")
    print("5. salir\n")
    
    op = input_numerico("Ingrese la opción: \n", int)
    
    # AGREGAR PRODUCTO
    if(op == 1):
        nombre = input("Ingrese el nombre del producto: ")
        precio = input_numerico("Ingrese el precio del producto: ")
        if(precio > 0):
            codigo_barras = input_numerico("Ingrese el código de barras del producto: ", int)
            if(codigo_barras > 0):
                cantidad_stock = input_numerico("Ingrese cantidad de stock del producto: ", int)
                if(cantidad_stock > 0):
                    Vnombre.append(nombre.lower())
                    Vcodigo_barras.append(codigo_barras)
                    Vprecio.append(precio)
                    Vcantidad_stock.append(cantidad_stock)
                    print("\n***** Producto Agregado *****\n")
                else:
                    print("\n** Cantidad Invalida **")
                    print("***** ACCION CANCELADA *****")
            else:
                print("\n** Código Invalido **")
                print("***** ACCION CANCELADA *****")
        else:
            print("\n** Precio Invalido **")
            print("***** ACCION CANCELADA *****")
        guardar_datos({"Vnombre": Vnombre, "Vcodigo_barras": Vcodigo_barras, "Vprecio": Vprecio, "Vcantidad_stock": Vcantidad_stock})
    
    # BUSCAR PRODUCTO
    elif(op == 2):
        print("\n********** BUSCAR PRODUCTO **********\n")
        print("¿Cómo desea buscar el producto?")
        print("Opciones:")
        print("1. Nombre")
        print("2. Código de barras")
        print("3. Volver Atrás\n")
        opb = input_numerico("Ingrese la opción: \n", int)
        
        while(opb != 3):
            if(opb == 1):
                opbn = input("\nIngrese el nombre del producto: \n")
                if(opbn.lower() in Vnombre):
                    producto = Vnombre.index(opbn.lower())
                    print("\n************** PRODUCTO: **************")
                    print(f"Nombre del Producto: {Vnombre[producto]}")
                    print(f"Precio del Producto: {Vprecio[producto]}")
                    print(f"Código de barras del Producto: {Vcodigo_barras[producto]}")
                    print(f"Stock del Producto: {Vcantidad_stock[producto]}")
                    print("***************************************\n")
                else:
                    print("\n***** Producto no encontrado *****\n")
            elif(opb == 2):
                opbc = input_numerico("Ingrese el Código de barras del producto: \n", int)
                if(opbc in Vcodigo_barras):
                    producto = Vcodigo_barras.index(opbc)
                    print("\n************** PRODUCTO: **************")
                    print(f"Nombre del Producto: {Vnombre[producto]}")
                    print(f"Precio del Producto: {Vprecio[producto]}")
                    print(f"Código de barras del Producto: {Vcodigo_barras[producto]}")
                    print(f"Stock del Producto: {Vcantidad_stock[producto]}")
                    print("***************************************\n")
                else:
                    print("\n***** Producto no encontrado *****\n")
            else:
                print("\nOpción Invalida\n")
            print("¿Cómo desea buscar el producto?")
            print("Opciones:")
            print("1. Nombre")
            print("2. Código de barras")
            print("3. Volver Atrás\n")
            opb = input_numerico("Ingrese la opción: ", int)
    
    # MODIFICAR PRODUCTOS
    elif(op == 3):
        print("\n********** MODIFICAR PRODUCTO **********\n")
        print("1. Buscar Producto por Nombre")
        print("2. Buscar producto por código de barras")
        print("3. Volver Atras")
        opbm = input_numerico("\nIngrese la Opción:\n", int)
        
        if(opbm == 1 or opbm == 2):
            # modificar por Nombre
            if(opbm == 1):
                mop = input("Ingrese el nombre del producto:\n")
                if(mop.lower() in Vnombre):
                    print("\n***** Producto a Modificar Encontrado *****\n")
                    pmo = Vnombre.index(mop.lower())
                    print("¿Qué desea Modificar?")
                    print("1. Nombre")
                    print("2. Precio")
                    print("3. Código de barras")
                    print("4. Cantidad de stock")
                    print("5. Volver Atras")
                    mop2 = input_numerico("\nIngrese la Opción\n", int)
                    
                    while(mop2 != 5):
                        if(mop2 == 1):
                            nombre = input("Ingrese el nuevo nombre del producto: ")
                            Vnombre[pmo] = nombre.lower()
                            print("\n***** Producto Modificado *****\n")
                        elif(mop2 == 2):
                            precio = input_numerico("Ingrese el nuevo precio del producto: ")
                            if(precio > 0):
                                Vprecio[pmo] = precio
                                print("\n***** Producto Modificado *****\n")
                            else:
                                print("\n** Precio Invalido **")
                                print("***** ACCION CANCELADA *****")
                        elif(mop2 == 3):
                            codigo_barras = input_numerico("Ingrese el nuevo código de barras del producto: ", int)
                            if(codigo_barras > 0):
                                Vcodigo_barras[pmo] = codigo_barras
                                print("\n***** Producto Modificado *****\n")
                            else:
                                print("\n** Código Invalido **")
                                print("***** ACCION CANCELADA *****")
                        elif(mop2 == 4):
                            cantidad_stock = input_numerico("Ingrese la nueva cantidad de stock del producto: ", int)
                            if(cantidad_stock >= 0):
                                Vcantidad_stock[pmo] = cantidad_stock
                                print("\n***** Producto Modificado *****\n")
                            else:
                                print("\n** Cantidad Invalida **")
                                print("***** ACCION CANCELADA *****")
                        else:
                            print("Opción Invalida")
                        break
                else:
                    print("\n***** Producto no encontrado *****\n")
            # modificar por código de barras
            elif(opbm == 2):
                mop = input_numerico("Ingrese el código de barras del producto:\n", int)
                if(mop in Vcodigo_barras):
                    print("\n***** Producto a Modificar Encontrado *****\n")
                    pmo = Vcodigo_barras.index(mop)
                    print("¿Qué desea Modificar?")
                    print("1. Nombre")
                    print("2. Precio")
                    print("3. Código de barras")
                    print("4. Cantidad de stock")
                    print("5. Volver Atras")
                    mop2 = input_numerico("\nIngrese la Opción\n", int)
                    
                    while(mop2 != 5):
                        if(mop2 == 1):
                            nombre = input("Ingrese el nuevo nombre del producto: ")
                            Vnombre[pmo] = nombre.lower()
                            print("\n***** Producto Modificado *****\n")
                        elif(mop2 == 2):
                            precio = input_numerico("Ingrese el nuevo precio del producto: ")
                            if(precio > 0):
                                Vprecio[pmo] = precio
                                print("\n***** Producto Modificado *****\n")
                            else:
                                print("\n** Precio Invalido **")
                                print("***** ACCION CANCELADA *****")
                        elif(mop2 == 3):
                            codigo_barras = input_numerico("Ingrese el nuevo código de barras del producto: ", int)
                            if(codigo_barras > 0):
                                Vcodigo_barras[pmo] = codigo_barras
                                print("\n***** Producto Modificado *****\n")
                            else:
                                print("\n** Código Invalido **")
                                print("***** ACCION CANCELADA *****")
                        elif(mop2 == 4):
                            cantidad_stock = input_numerico("Ingrese la nueva cantidad de stock del producto: ", int)
                            if(cantidad_stock >= 0):
                                Vcantidad_stock[pmo] = cantidad_stock
                                print("\n***** Producto Modificado *****\n")
                            else:
                                print("\n** Cantidad Invalida **")
                                print("***** ACCION CANCELADA *****")
                        else:
                            print("Opción Invalida")
                        break
                else:
                    print("\n***** Producto no encontrado *****\n")
            guardar_datos({"Vnombre": Vnombre, "Vcodigo_barras": Vcodigo_barras, "Vprecio": Vprecio, "Vcantidad_stock": Vcantidad_stock})
        
    # ELIMINAR PRODUCTOS
    elif(op == 4):
        eliminar = []
        for index, cantidad in enumerate(Vcantidad_stock):
            if cantidad == 0:
                eliminar.append(index)
        if eliminar:
            print("\nLos siguientes productos tienen stock igual a cero y serán eliminados:")
            for index in eliminar:
                print(f"Nombre: {Vnombre[index]}")
                print(f"Código de barras: {Vcodigo_barras[index]}")
                print(f"Precio: {Vprecio[index]}\n")
            confirmacion = input("¿Está seguro de que desea eliminar estos productos? (si/no): \n")
            if(confirmacion.lower() == "si"):
                # Eliminar los productos de todas las listas
                for index in sorted(eliminar, reverse=True):
                    del Vnombre[index]
                    del Vcodigo_barras[index]
                    del Vprecio[index]
                    del Vcantidad_stock[index]
                print("\n***** Productos eliminados exitosamente *****\n")
            else:
                print("\n***** Eliminación cancelada *****\n")
        else:
            print("No hay productos con stock igual a cero.")
        guardar_datos({"Vnombre": Vnombre, "Vcodigo_barras": Vcodigo_barras, "Vprecio": Vprecio, "Vcantidad_stock": Vcantidad_stock})
    
    elif(op == 5):
        print("Hasta luego :)")

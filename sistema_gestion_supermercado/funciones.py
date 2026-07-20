"""
=========================================================
SISTEMA DE GESTIÓN DE SUPERMERCADO
=========================================================
"""
# =====================================================
# IMPORTACIONES
# =====================================================

import json
import os

from datetime import datetime

from datos import productos, CATEGORIAS

# =====================================================
# GUARDAR PRODUCTOS
# =====================================================

def guardar_productos():
    """
    Guarda todos los productos en un archivo JSON.
    """
    with open("productos.json", "w", encoding="utf-8") as archivo:
        json.dump(
            productos,
            archivo,
            indent=4,
            ensure_ascii=False
        )

# =====================================================
# CARGAR PRODUCTOS
# =====================================================

def cargar_productos():
    """
    Carga los productos desde productos.json.
    """
    if os.path.exists("productos.json"):
        with open("productos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            productos.clear()
            productos.extend(datos)

# =====================================================
# BUSCAR PRODUCTO (LAMBDA)
# =====================================================

def buscar_producto_codigo(codigo):
    """
    Busca un producto mediante su código.
    """
    return next(
        filter(
            lambda producto: producto["codigo"] == codigo,
            productos
        ),
        None
    )

# =====================================================
# VALIDAR PRECIO
# =====================================================

def validar_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio: $"))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            return precio
        except ValueError:
            print("Debe ingresar un número válido.")

# =====================================================
# VALIDAR STOCK
# =====================================================

def validar_stock():
    while True:
        try:
            stock = int(input("Ingrese el stock: "))
            if stock < 0:
                print("El stock no puede ser negativo.")
                continue
            return stock
        except ValueError:
            print("Debe ingresar un número entero.")

# =====================================================
# VALIDAR CATEGORÍA
# =====================================================

def validar_categoria():
    print("\nCategorías disponibles\n")
    for i, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{i}. {categoria}")
    while True:
        try:
            opcion = int(input("\nSeleccione una categoría: "))
            if 1 <= opcion <= len(CATEGORIAS):
                return CATEGORIAS[opcion - 1]
            print("Categoría incorrecta.")
        except ValueError:
            print("Debe ingresar un número.")

# =====================================================
# AGREGAR PRODUCTO
# =====================================================

def agregar_producto():

    print("\n" + "=" * 45)
    print("AGREGAR PRODUCTO")
    print("=" * 45)

    while True:

        codigo = input("Código: ").upper().strip()

        if codigo == "":

            print("Debe ingresar un código.")
            continue

        if buscar_producto_codigo(codigo):

            print("Ese código ya existe.")
            continue

        break

    while True:

        nombre = input("Nombre: ").title().strip()

        if nombre == "":

            print("Debe ingresar un nombre.")
            continue

        break

    categoria = validar_categoria()

    precio = validar_precio()

    stock = validar_stock()

    producto = {

        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "fecha_ingreso": datetime.now().strftime("%d-%m-%Y")
    }

    productos.append(producto)

    guardar_productos()

    print("\nProducto agregado correctamente.")

    input("\nPresione ENTER para continuar...")

# =====================================================
# MOSTRAR PRODUCTOS
# =====================================================

def mostrar_productos():

    print("\n" + "=" * 85)
    print("LISTA DE PRODUCTOS")
    print("=" * 85)

    if not productos:

        print("No existen productos registrados.")

        input("\nPresione ENTER para continuar...")
        return

    print(
        f"{'Código':<10}"
        f"{'Nombre':<20}"
        f"{'Categoría':<15}"
        f"{'Precio':<12}"
        f"{'Stock':<8}"
        f"{'Ingreso'}"
    )

    print("-" * 85)

    for producto in productos:

        print(
            f"{producto['codigo']:<10}"
            f"{producto['nombre']:<20}"
            f"{producto['categoria']:<15}"
            f"${producto['precio']:<11,.0f}"
            f"{producto['stock']:<8}"
            f"{producto['fecha_ingreso']}"
        )

    print("-" * 85)

    input("\nPresione ENTER para continuar...")

# =====================================================
# BUSCAR PRODUCTO
# =====================================================

def buscar_producto():

    print("\n" + "=" * 45)
    print("BUSCAR PRODUCTO")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")

        input("\nPresione ENTER para continuar...")
        return

    codigo = input("Ingrese el código: ").upper().strip()

    producto = buscar_producto_codigo(codigo)

    if producto is None:

        print("\nProducto no encontrado.")

    else:

        print("\nProducto encontrado\n")

        print(f"Código      : {producto['codigo']}")
        print(f"Nombre      : {producto['nombre']}")
        print(f"Categoría   : {producto['categoria']}")
        print(f"Precio      : ${producto['precio']:,.0f}")
        print(f"Stock       : {producto['stock']}")
        print(f"Fecha       : {producto['fecha_ingreso']}")

    input("\nPresione ENTER para continuar...")

# =====================================================
# ACTUALIZAR STOCK
# =====================================================

def actualizar_stock():

    print("\n" + "=" * 45)
    print("ACTUALIZAR STOCK")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")

        input("\nPresione ENTER para continuar...")
        return

    codigo = input("Ingrese el código: ").upper().strip()

    producto = buscar_producto_codigo(codigo)

    if producto is None:

        print("\nProducto no encontrado.")

        input("\nPresione ENTER para continuar...")
        return

    print(f"\nProducto : {producto['nombre']}")
    print(f"Stock actual : {producto['stock']}")

    nuevo_stock = validar_stock()

    producto["stock"] = nuevo_stock

    guardar_productos()

    print("\nStock actualizado correctamente.")

    input("\nPresione ENTER para continuar...")    

# =====================================================
# ELIMINAR PRODUCTO
# =====================================================

def eliminar_producto():

    print("\n" + "=" * 45)
    print("ELIMINAR PRODUCTO")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")
        input("\nPresione ENTER para continuar...")
        return

    codigo = input("Ingrese el código del producto: ").upper().strip()

    producto = buscar_producto_codigo(codigo)

    if producto is None:

        print("\nProducto no encontrado.")
        input("\nPresione ENTER para continuar...")
        return

    print("\nProducto encontrado")
    print(f"Código : {producto['codigo']}")
    print(f"Nombre : {producto['nombre']}")

    respuesta = input("\n¿Desea eliminar este producto? (S/N): ").upper()

    if respuesta == "S":

        productos.remove(producto)

        guardar_productos()

        print("\nProducto eliminado correctamente.")

    else:

        print("\nOperación cancelada.")

    input("\nPresione ENTER para continuar...")

# =====================================================
# APLICAR DESCUENTO
# =====================================================

def aplicar_descuento():

    print("\n" + "=" * 45)
    print("APLICAR DESCUENTO")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")
        input("\nPresione ENTER para continuar...")
        return

    codigo = input("Ingrese el código del producto: ").upper().strip()

    producto = buscar_producto_codigo(codigo)

    if producto is None:

        print("\nProducto no encontrado.")
        input("\nPresione ENTER para continuar...")
        return

    print(f"\nProducto : {producto['nombre']}")
    print(f"Precio actual : ${producto['precio']:,.0f}")

    while True:
        try:
            descuento = float(input("Ingrese el descuento (%): "))

            if descuento < 0 or descuento > 100:

                print("Ingrese un porcentaje entre 0 y 100.")
                continue
            break
        except ValueError:

            print("Debe ingresar un número.")

    producto["precio"] = round(

        producto["precio"] * (1 - descuento / 100),

        2
    )

    guardar_productos()

    print(f"\nNuevo precio: ${producto['precio']:,.0f}")

    input("\nPresione ENTER para continuar...")

# =====================================================
# ORDENAR PRODUCTOS
# =====================================================

def ordenar_productos():

    print("\n" + "=" * 45)
    print("PRODUCTOS ORDENADOS")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")

        input("\nPresione ENTER para continuar...")
        return

    productos_ordenados = sorted(

        productos,

        key=lambda producto: producto["nombre"]
    )
    print(
        f"{'Código':<10}"
        f"{'Nombre':<20}"
        f"{'Categoría':<15}"
        f"{'Precio':<12}"
        f"{'Stock'}"
    )

    print("-" * 75)

    for producto in productos_ordenados:

        print(
            f"{producto['codigo']:<10}"
            f"{producto['nombre']:<20}"
            f"{producto['categoria']:<15}"
            f"${producto['precio']:<11,.0f}"
            f"{producto['stock']}"
        )

    input("\nPresione ENTER para continuar...")

# =====================================================
# MOSTRAR CATEGORÍAS
# =====================================================

def mostrar_categorias():

    print("\n" + "=" * 45)
    print("CATEGORÍAS REGISTRADAS")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")

        input("\nPresione ENTER para continuar...")
        return

    categorias = set(

        map(

            lambda producto: producto["categoria"],

            productos
        )
    )

    for categoria in sorted(categorias):

        print(f"- {categoria}")

    input("\nPresione ENTER para continuar...")

# =====================================================
# FUNCIÓN RECURSIVA
# =====================================================

def calcular_total_recursivo(lista_productos, indice):

    """
    Calcula el valor total del inventario utilizando
    recursividad.
    """

    # Caso base

    if indice >= len(lista_productos):

        return 0

    subtotal = (

        lista_productos[indice]["precio"]

        * lista_productos[indice]["stock"]

    )

    return subtotal + calcular_total_recursivo(

        lista_productos,

        indice + 1

    )

# =====================================================
# VALOR TOTAL DEL INVENTARIO
# =====================================================

def total_inventario():

    print("\n" + "=" * 45)
    print("VALOR TOTAL DEL INVENTARIO")
    print("=" * 45)

    if not productos:

        print("No existen productos registrados.")

        input("\nPresione ENTER para continuar...")
        return

    total = calcular_total_recursivo(productos, 0)

    print(f"\nCantidad de productos : {len(productos)}")
    print(f"Valor total inventario : ${total:,.0f}")

    input("\nPresione ENTER para continuar...")
"""
=========================================================
SISTEMA DE GESTIÓN DE SUPERMERCADO
=========================================================
"""
from funciones import (
    cargar_productos,
    agregar_producto,
    mostrar_productos,
    buscar_producto,
    actualizar_stock,
    eliminar_producto,
    aplicar_descuento,
    ordenar_productos,
    mostrar_categorias,
    total_inventario
)

# =====================================================
# MENÚ PRINCIPAL
# =====================================================

def mostrar_menu():

    print("\n" + "=" * 50)
    print("     SISTEMA DE GESTIÓN DE SUPERMERCADO")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar stock")
    print("5. Eliminar producto")
    print("6. Aplicar descuento")
    print("7. Ordenar productos")
    print("8. Mostrar categorías")
    print("9. Valor total del inventario")
    print("10. Salir")

# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

def main():

    # Cargar los productos guardados
    cargar_productos()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            aplicar_descuento()
        elif opcion == "7":
            ordenar_productos()
        elif opcion == "8":
            mostrar_categorias()
        elif opcion == "9":
            total_inventario()
        elif opcion == "10":
            print("\nGracias por utilizar el sistema de gestión de inventario del supermercado.")
            print("Hasta pronto.")
            break

        else:

            print("\nOpción inválida.")
            input("\nPresione ENTER para continuar...")

# =====================================================
# EJECUCIÓN DEL PROGRAMA
# =====================================================

if __name__ == "__main__":

    main()


# TP Integrador Repetitivas - Condicionales y Secuenciales
# Alumno: Marcelo David Kacerovsky
# DNI: 37.043.673
# Ejercicio 1: Caja del Kiosco


while not (customer := input("Cliente: ").strip()).isalpha():
    print("Ingrese un nombre valido")

while not (products := input("Cantidad de productos: ").strip()).isdigit() or products == "0":
    print("Ingrese un valor valido")


print(f"Cliente: {customer}")
print(f"Cantidad de productos: {products}")


total = 0
discounts = 0


for i in range(int(products)):
    print(f"Producto {i + 1}:")

    while not (price := input("\tPrecio: ").strip()).isdigit() or price == "0":
        print("\tIngrese un valor valido")

    while (discount := input("\tDescuento (S/N): ").strip().upper()) != "S" and discount != "N":
        print("\tIngrese un valor valido (S o N)")

    price = int(price)
    total += price
    if discount == "S":
        discounts += price * .1


print(f"Total sin descuentos: ${total:.2f}")
print(f"Total con descuentos: ${(total - discounts):.2f}")
print(f"Ahorro: ${discounts:.2f}")
print(f"Promedio por producto: ${(total - discounts) / int(products):.2f}")

# TP Integrador Repetitivas - Condicionales y Secuenciales
# Alumno: Marcelo David Kacerovsky
# DNI: 37.043.673
# Ejercicio 2: Acceso al Campus y Menú Seguro


STUDENT = "alumno"
PASSWORD = "python123"
attempts = 1

user = None
password = None


while attempts < 4 and (user != STUDENT and password != PASSWORD):
    if attempts != 1:
        print("Error: credenciales inválidas.")

    user = input(f"Intento {attempts}/3 - Usuario: ").strip()
    password = input(f"Clave: ").strip()
    attempts += 1


if attempts < 4:
    print("Acceso concedido.")
    option = None

    while option != "4":
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir\n")
        option = input("Opción: ").strip()

        match option:
            case "1":
                print("Inscripto\n")
            case "2":
                new_password = input("Nueva clave: ").strip()
                if len(new_password) < 6:
                    print("Error: mínimo 6 caracteres.\n")
                else:
                    password = new_password
                    print("Clave actualizada.\n")
            case "3":
                print("Cada error es una oportunidad para aprender algo nuevo.\n")
            case "4":
                break
            case _:
                print("Error: opción fuera de rango.\n")

else:
    print("Cuenta bloqueada")

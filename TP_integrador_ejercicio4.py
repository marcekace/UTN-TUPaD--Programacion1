# TP Integrador Repetitivas - Condicionales y Secuenciales
# Alumno: Marcelo David Kacerovsky
# DNI: 37.043.673
# Ejercicio 4 — “Escape Room: La Bóveda”
from random import randint


energy = 100
time = 12
open_locks = 0
alarm = False
partial_code = ""
force_lock = 0


while not (user := input("Nombre del Agente: ").strip().title()).isalpha():
    print("Error: nombre inválido.")


print(f"\nBienvenido {user}\n")
option = None
prev_option = None

while option != "4":
    if open_locks == 3:
        print("Victoria")
        break
    elif energy <= 0 or time <= 0:
        print("Derrota")
        break
    elif alarm is True and time <= 3:
        print("Derrota (Sistema Bloqueado)")
        break

    print("-" * 80)
    print(f"\nEnergia: {energy}\nTiempo: {time}\nCerraduras abiertas: {open_locks}")
    print("\n1. Forzar cerradura (costo: -20 energía, -2 tiempo)\n2. Hackear panel (costo: -10 energía, -3 tiempo)\n3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)\n4. Salir\n")
    print("-" * 80)
    option = input("Opción: ").strip()

    match option:
        case "1":
            energy -= 20
            time -= 2

            if prev_option == "1" or prev_option is None:
                force_lock += 1

            if force_lock == 3:
                alarm = not alarm
                print("Alarma activada")
            elif alarm is False and energy < 40:
                print(alarm)
                while (prompt := input("Ingrese un numero (1 - 3): ").strip()) != "1" and prompt != "2" and prompt != "3":
                    print("Ingrese una opción valida.")

                if prompt == "3":
                    alarm = not alarm
                    print("Alarma activada")

            if alarm is False and force_lock < 3:
                open_locks += 1
                print("Cerradura abierta")
        case "2":
            energy -= 10
            time -= 3
            force_lock = 0

            print("Hackeando panel... ")
            print("Obteniendo  codigos: ", end="")

            for _ in range (4):
                char = chr(randint(65, 90))
                print(char, end="")
                partial_code += char

            print(f"\nCodigo Parcial: {partial_code}")

            if len(partial_code) >= 8:
                open_locks += 1
                print("Cerradura abierta")
        case "3":
            energy += 15
            time -= 1
            force_lock = 0

            if alarm:
                energy += 10

            if energy > 100:
                energy = 100
        case "4":
            break
        case _:
            print("Error: opción inválida.\n")

    prev_option = option

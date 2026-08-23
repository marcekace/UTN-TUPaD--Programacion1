# TP Integrador Repetitivas - Condicionales y Secuenciales
# Alumno: Marcelo David Kacerovsky
# DNI: 37.043.673
# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

while not (user := input("Nombre del Gladiador: ").strip().title()).isalpha():
    print("Error: Solo se permiten letras.")

print("-" * 60)
print(f"BIENVENIDO A LA ARENA {user}".center(60))
print("-" * 60)

life = 100
enemy = 100
potions = 3
attack = 15
enemy_attack = 12
user_turn = True

option = None


while life > 0 and enemy > 0:
    print("\n")
    print("=" * 60)
    print("INICIO DEL COMBATE".center(60))
    print("=" * 60)
    print(f"{user} (HP: {life}) vs Enemigo (HP: {enemy}) | Pociones: {potions}\nElige acción:")
    print("1. Ataque Pesado\n2. Ráfaga veloz\n3. Curar")
    print("-" * 60)
    print("\n")
    option = input(">> ").strip()

    match option:
        case "1":
            damage = attack
            if enemy < 20:
                damage *= 1.5

            enemy -= damage
            user_turn = not user_turn
            print(f"¡Atacaste al enemigo por {damage} puntos de daño!")
        case "2":
            print("¡Inicias una ráfaga de golpes!")

            for _ in range(3):
                enemy -= 5
                print("> Golpe conectado por 5 de daño")

            user_turn = not user_turn
        case "3":
            if potions > 0:
                life += 30
                potions -= 1
                if life > 100:
                    life = 100
            else:
                print("No quedan pociones!")

            user_turn = not user_turn
        case _:
            print("Error: Ingrese un número válido.n")

    if user_turn is False:
        life -= enemy_attack
        user_turn = not user_turn
        print(f"¡El enemigo te atacó por {enemy_attack} puntos de daño!")

if life > 0:
    print(f"¡VICTORIA! {user} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

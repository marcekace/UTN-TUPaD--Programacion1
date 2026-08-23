# TP Integrador Repetitivas - Condicionales y Secuenciales
# Alumno: Marcelo David Kacerovsky
# DNI: 37.043.673
# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”


monday = "0,0,0,0"
tuesday = "0,0,0"


while not (user := input("Nombre del operador: ").strip().title()).isalpha():
    print("Error: operador inválido.")


print(f"Acceso concedido.\nBienvenido {user}\n")
option = None

while option != "5":
    print("\n1. Reservar turno\n2. Cancelar turno (por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema\n")
    option = input("Opción: ").strip()

    match option:
        case "1":
            day = input("Elija el día (1 = Lunes, 2 = Martes): ").strip()

            if day != "1" and day != "2":
                print("Error: opción inválida.\n")
            else:
                date = monday if day == "1" else tuesday

                while not (patient := input("Nombre del paciente: ").strip().title()).isalpha():
                    print("Ingrese un nombre válido.")

                if patient in date or date.count("0") == 0:
                    print("El paciente ya posee cita o se alcanzo el maximo de turnos para este dia\n.")
                else:
                    if day == "1":
                        monday = date.replace("0", patient, 1)
                    else:
                        tuesday = date.replace("0", patient, 1)
                    print(f"Paciente {patient} agendado con exito.\n")
        case "2":
            day = input("Elija el día (1 = Lunes, 2 = Martes): ").strip()

            if day != "1" and day != "2":
                print("Error: opción inválida.\n")
            else:
                date = monday if day == "1" else tuesday

                while not (patient := input("Nombre del paciente: ").strip().title()).isalpha():
                    print("Ingrese un nombre válido.")

                if patient in date:
                    if day == "1":
                        monday = date.replace(patient, "0")
                    else:
                        tuesday = date.replace(patient, "0")
                    print(f"Turno del paciente {patient} cancelado con exito.")
                else:
                    print(f"El paciente {patient} no posee un turno para el dia seleccionado.\n")                        
        case "3":
            day = input("Elija el día (1 = Lunes, 2 = Martes): ").strip()

            if day != "1" and day != "2":
                print("Error: opción inválida.\n")
            else:
                date = monday if day == "1" else tuesday
                counter = 1
                flag = True

                for c in date:
                    if c == ",":
                        counter += 1
                        if not flag:
                            flag = not flag
                    elif c == "0":
                        print(f"\n\tTurno {counter} libre", end="")
                    else:
                        if flag:
                            print(f"\n\tTurno {counter} ", end="")
                            flag = not flag
                        print(c, end="")
                print("\n")                
        case "4":
            dates = f"{monday}|{tuesday}"
            print("-" * 30)
            print("RESUMEN GENERAL".center(30))
            print("-" * 30)
            print("\n")
            print("LUNES".center(30))
            counter = 1
            flag = True

            for c in dates:
                if c == ",":
                    counter += 1
                    if not flag:
                        flag = not flag
                elif c == "|":
                    print("\n")
                    print("MARTES".center(30))    
                elif c == "0":
                    print(f"\nTurno {counter}:\tlibre", end="")
                else:
                    if flag:
                        print(f"\nTurno {counter}:\t", end="")
                        flag = not flag
                    print(c, end="")
            print("\n")
            print("-" * 30)
            print("-" * 30)
        case "5":
            break
        case _:
            print("Error: opción inválida.\n")

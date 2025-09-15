# Un instituto de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día, DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
#Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el programa le mostrará el porcentaje de aprobados.
#Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.
#Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.


fecha=input("Ingrese la fecha en formato 'dia DD/MM': ")

fecha_verdad=fecha.split()
if len(fecha_verdad) !=2:
    print("Formato Incorrecto.")
else:
    dia_semana=fecha_verdad[0].capitalize()
    fecha=fecha_verdad[1].split("/")

    if len(fecha) !=2:
        print("Formato Incorrecto")
    else:
        dia_num=int(fecha[0])
        mes=int(fecha[1])

        if dia_num < 1 or dia_num > 31 or mes < 1 or mes > 12:
            print("Hubo en error en la fecha.")
        else:
            if dia_semana == "Lunes":
                print("Nivel Inicial")
                examenes=input("Hubo examenes? (si/no): ").capitalize()
                if examenes == "Si":
                    aprobados =int(input("Cantidad de alumnos aprobados: "))
                    desaprobados=int(input("Cantidad de alumnos desaprobados: "))
                    total=aprobados+desaprobados
                    if total > 0:
                        print(f"Porcentaje de aprobados {(aprobados*100)/total:.2f}%")
            elif dia_semana == "Martes":
                print("Nivel Intermedio")
                examenes=input("Hubo examenes? (si/no): ").capitalize()
                if examenes == "Si":
                    aprobados =int(input("Cantidad de alumnos aprobados: "))
                    desaprobados=int(input("Cantidad de alumnos desaprobados: "))
                    total=aprobados+desaprobados
                    if total > 0:
                        print(f"Porcentaje de aprobados {(aprobados*100)/total:.2f}%")
            elif dia_semana == "Miercoles":
                print("Nivel Avanzado")
                examenes=input("Hubo examenes? (si/no): ").capitalize()
                if examenes == "Si":
                    aprobados =int(input("Cantidad de alumnos aprobados: "))
                    desaprobados=int(input("Cantidad de alumnos desaprobados: "))
                    total=aprobados+desaprobados
                    if total > 0:
                        print(f"Porcentaje de aprobados {(aprobados*100)/total:.2f}%")
            elif dia_semana == "Jueves":
                print("Practica Hablada")
                asistencia=float(input("Porcentaje de asistencias: "))
                if asistencia > 50:
                    print("Asistio la mayoria.")
                else:
                    print("No asistio la mayoria.")
            elif dia_semana == "Viernes":
                print("Ingles para viajeros")
                if dia_num == 1 and (mes == 1 or mes == 7):
                    print("Comienzo de nuevo ciclo")
                    alumnos=int(input("Cantidad de alumnos del nuevo ciclo: "))
                    arancel=float(input("Arancel por alumno $"))
                    print(f"Ingreso total:${alumnos*arancel:.2f}")
            else:
                print("El dia ingresado no es valido.")


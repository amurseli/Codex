import matplotlib.pyplot as plt
import csv

NEW_DATA = "chart.csv"
CODEX = "codex.csv"

def validar_opcion(minimo: int, maximo: int) -> int:
    opcion = int(input("Ingrese un numero de opcion: "))
    while not opcion in range(minimo, maximo + 1):
        print("Error. Intentelo nuevamente.")
        opcion = int(input("Ingrese un numero de opcion: "))
    
    return int(opcion)

def plot_voice(x:list, y:list) -> None:

    plt.figure(figsize = (10,10))
    plt.bar(x,y)
    plt.xlabel('Fecha')
    plt.ylabel('Minutos')
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show()

def string_to_int(list_: list) -> None:
    for i in range(len(list_)):
        list_[i] = int(list_[i])

def save_codex(dates:list, minutes:list) -> None:
    with open(CODEX,'a',encoding='utf-8-sig') as writef:
        write = csv.writer(writef, delimiter=";")

        for i in range(len(dates)):
            write.writerow([dates[i],minutes[i]])

def main () -> None:
    x=[]
    y=[]
    continuar = True

    with open(NEW_DATA,'r',encoding='utf-8-sig') as readf:
        plots = csv.reader(readf, delimiter=';')
        next(plots,None)
        for row in plots:
            x.append(row[0])
            y.append(row[1])
    string_to_int(y)
    
    while continuar:
        print(
            """ 
            1) Abrir el "Codex".
            2) Crear un archivo.
            3) Subir un archivo.
            4) Descargar un archivo.
            5) Sincronizar.
            6) Generar carpetas de una evaluacion.
            7) Actualizar entregas de alumnos vía mail.
            8) Salir. 
            """)
        
        opcion = validar_opcion(1, 8)
        if opcion == 1:
            plot_voice(x,y)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            print("Saliendo del programa")
            continuar = False 

    save_codex(x,y)

main()
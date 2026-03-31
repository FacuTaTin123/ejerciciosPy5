'''6- Administrador de tareas:
Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
Muestra la lista de tareas agregadas.
Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.
'''

def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada=False):
    nueva_tarea = {"Descripcion": tarea, "Fecha limite": fecha_limite, "Prioridad": prioridad}
    tareas.append(nueva_tarea)
    print("Se agrego la tarea")
    
    completada = False

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")
            if tarea.get("completada", False):
                print("Estado: Completada")
                    
def marcar_completada(lista_tareas):
    completar = int(input('que indice de tarea desea marcar como completada: '))
    if 0 <= completar < len(lista_tareas):
        lista_tareas[completar]['completada'] = True
        print('la tarea ha sido marcada como completada')
    else:
        print('error')

if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("descripción de la tarea: ")
            fecha_limite_nueva = input("fecha limite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            mostrar_tareas(lista_tareas)

        elif opcion == "3":
            break
        
        elif opcion == "4":
            marcar_completada(lista_tareas)
            
        elif opcion == "5":
            break
        
        else:
            print("\nnono asi no\nasi(1,2,3,4,5)\n")

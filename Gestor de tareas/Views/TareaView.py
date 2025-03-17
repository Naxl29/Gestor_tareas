from colorama import Fore, Style
import random

class VistaTarea:
    @staticmethod
    def mostrar_menu():
        print(Fore.CYAN + "\n--- Gestor de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Ver Tareas")
        print("3. Actualizar Estado de Tarea")
        print("4. Eliminar Tarea")
        print("5. Agregar Etiqueta")
        print("6. Salir")

    @staticmethod
    def obtener_datos_tarea():
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        return titulo, descripcion

    @staticmethod
    def mostrar_tareas(tareas):
        if tareas:
            print(Fore.CYAN + "--- Lista de Tareas ---" + Style.RESET_ALL)
            for tarea in tareas:
                print(f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Estado: {tarea[3]}")
        else:
            print(Fore.RED + "No hay tareas registradas." + Style.RESET_ALL)
    
    @staticmethod
    def mostrar_tareas_etiquetas(tareas):
        colores_disponibles = [
            Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, 
            Fore.CYAN, Fore.WHITE, Fore.BLACK, Fore.LIGHTBLACK_EX,
            Fore.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX
        ]
        
        if tareas:
            print(Fore.CYAN + "--- Lista de Tareas ---" + Style.RESET_ALL)
            for tarea in tareas:
                etiquetas = tarea[4].split(",")  
                etiquetas_coloreadas = []
                
                for etiqueta in etiquetas:
                    color = random.choice(colores_disponibles)
                    etiquetas_coloreadas.append(f"{color}{etiqueta.strip()}{Style.RESET_ALL}")
                
                print(f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Estado: {tarea[3]}, Etiquetas: {', '.join(etiquetas_coloreadas)}")
        else:
            print(Fore.RED + "No hay tareas registradas." + Style.RESET_ALL)

    @staticmethod
    def mostrar_etiquetas(etiquetas):
        if etiquetas:
            print(Fore.CYAN + "--- Lista de Etiquetas ---" + Style.RESET_ALL)
            for etiqueta in etiquetas:
                print(f"ID: {etiqueta[0]}, Nombre: {etiqueta[1]}")
        else:
            print(Fore.RED + "No hay etiquetas registradas." + Style.RESET_ALL)   

    @staticmethod
    def obtener_id_tarea():
        return int(input("Ingrese el ID de la tarea: ")) 

    @staticmethod
    def obtener_nuevo_estado():
        return input("Ingrese el nuevo estado (pendiente/completada): ").strip().lower()

    @staticmethod
    def obtener_id_etiqueta(): 
        return int(input("Ingrese el ID de la etiqueta: "))

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"\n{mensaje}")
    
    @staticmethod
    def agg_etiqueta():
        return input("¿Desea agregar una etiqueta? (si/no): ").strip().lower()
        
    @staticmethod
    def ver_t_e():
        return input("¿Desea ver las tareas con etiquetas? (si/no): ").strip().lower()    
    




    
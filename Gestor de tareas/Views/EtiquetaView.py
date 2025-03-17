from colorama import Fore, Style

class VistaEtiqueta:
    @staticmethod
    def menu():
        print(Fore.CYAN + "\n--- Gestor de Tareas ---")
        print("1. Crear Etiqueta")
        print("2. Ver Etiquetas")
        print("3. Modificar Etiqueta")
        print("4. Eliminar Etiqueta")
        print("5. Salir")

    @staticmethod
    def datos_etiqueta():
        nombre = input("Ingrese el nombre de la etiqueta: ")
        return nombre

    @staticmethod
    def mostrar_etiquetas(etiquetas):
        if etiquetas:
            print(Fore.CYAN + "--- Lista de Etiquetas ---" + Style.RESET_ALL)
            for etiqueta in etiquetas:
                print(f"ID: {etiqueta[0]}, Nombre: {etiqueta[1]}")
        else:
            print(Fore.RED + "No hay etiquetas registradas." + Style.RESET_ALL)

    @staticmethod
    def obtener_id_etiqueta(): 
        return int(input("Ingrese el ID de la etiqueta: "))
    
    @staticmethod
    def nuevo_nombre():
        return input("Ingrese el nuevo nombre: ")


    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"\n{mensaje}")



from Models.Tarea import ModeloTarea
from Views.TareaView import VistaTarea
from Controllers.TareaController import ControladorTarea
from Models.Etiqueta import ModeloEtiqueta
from Views.EtiquetaView import VistaEtiqueta
from Controllers.EtiquetaController import ControladorEtiqueta 
from colorama import Fore, Style
import sys

if __name__ == "__main__":
    modelo_t = ModeloTarea()
    vista_t = VistaTarea()
    controlador_t = ControladorTarea(modelo_t, vista_t)
    modelo_e = ModeloEtiqueta()
    vista_e = VistaEtiqueta
    controlador_e = ControladorEtiqueta(modelo_e, vista_e)
while True:
    print(Fore.CYAN + "\n--- Gestor de Tareas ---")
    print("1. Tareas")
    print("2. Etiquetas")
    print("3. Salir")
    opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)

    if opcion == "1":
        controlador_t.ejecutar_t()
    elif opcion == "2":
        controlador_e.ejecutar_e()
    elif opcion == "3":
        print(Fore.CYAN + "Saliendo del gestor de tareas. ¡Hasta pronto!")
        sys.exit(0)
    else:
        print(Fore.RED + "Opción no válida. Intente de nuevo.")


from colorama import Fore, Style

class ControladorTarea:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_t(self):
        self.modelo.crear_tabla()
        while True:
            self.vista.mostrar_menu()
            opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)

            match opcion:
                case '1':
                    titulo, descripcion = self.vista.obtener_datos_tarea()
                    if not titulo.strip():
                        print(Fore.RED + "¡No se pudo agregar la tarea, campos incompletos!" + Style.RESET_ALL)
                        self.ejecutar_t()
                    else:
                        self.modelo.agregar_tarea(titulo, descripcion)
                    while True:
                        res = self.vista.agg_etiqueta()
                        if res == "si":
                            id_tarea = self.modelo.ultimo_id()
                            
                            etiquetas = self.modelo.ver_etiquetas()
                            self.vista.mostrar_etiquetas(etiquetas)
                            ids_etiquetas = [etiqueta[0] for etiqueta in etiquetas]
                            while True:
                                try:
                                    id_etiqueta = self.vista.obtener_id_etiqueta()
                                    if id_etiqueta in ids_etiquetas:
                                                if etiquetas:
                                                    self.modelo.agregar_etiqueta(id_tarea, id_etiqueta)
                                                    self.vista.mostrar_mensaje(Fore.GREEN + "Etiqueta agregada correctamente")
                                                    break
                                    else:
                                        print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)        
                                except ValueError:
                                    print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                            break
                        elif res == "no":
                            self.vista.mostrar_mensaje(Fore.GREEN + "¡Tarea agregada correctamente!")
                            break
                        else:
                            self.vista.mostrar_mensaje(Fore.RED + "¡Opción incorrecta!" + Style.RESET_ALL)
                case '2':
                    while True:
                        op = self.vista.ver_t_e()
                        if op == "si":
                            tareas = self.modelo.obtener_tareas_etiquetas()
                            self.vista.mostrar_tareas_etiquetas(tareas)
                            break
                        elif op == "no":
                            tareas = self.modelo.obtener_tareas()
                            self.vista.mostrar_tareas(tareas)
                            break
                        else:
                            self.vista.mostrar_mensaje(Fore.RED + "¡Opción incorrecta!" + Style.RESET_ALL)
                case '3':   
                    while True:
                        op = self.vista.ver_t_e()
                        if op == "si":
                            tareas = self.modelo.obtener_tareas_etiquetas()
                            self.vista.mostrar_tareas_etiquetas(tareas)
                            break
                        elif op == "no":
                            tareas = self.modelo.obtener_tareas()
                            self.vista.mostrar_tareas(tareas)
                            break
                        else:
                            self.vista.mostrar_mensaje(Fore.RED + "¡Opción incorrecta!" + Style.RESET_ALL)
                    ids_tareas = [tarea[0] for tarea in tareas]
                    while True:
                        try:
                            id_tarea = self.vista.obtener_id_tarea()
                            if id_tarea in ids_tareas:
                                if tareas:
                                    while True:
                                        nuevo_estado = self.vista.obtener_nuevo_estado()
                                        if nuevo_estado in ["pendiente", "completada"]:
                                            self.modelo.actualizar_tarea(id_tarea, nuevo_estado)
                                            self.vista.mostrar_mensaje(Fore.GREEN + "¡Estado de la tarea actualizado!")
                                            break
                                        else:
                                            print(Fore.RED + "¡Opción incorrecta!" + Style.RESET_ALL)
                                    break
                                else:
                                    self.ejecutar_t()
                            else:
                                print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)
                        except ValueError:
                            print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                case '4':
                    while True:
                        op = self.vista.ver_t_e()
                        if op == "si":
                            tareas = self.modelo.obtener_tareas_etiquetas()
                            self.vista.mostrar_tareas_etiquetas(tareas)
                            break
                        elif op == "no":
                            tareas = self.modelo.obtener_tareas()
                            self.vista.mostrar_tareas(tareas)
                            break
                        else:
                            self.vista.mostrar_mensaje(Fore.RED + "¡Opción incorrecta!" + Style.RESET_ALL)
                    ids_tareas = [tarea[0] for tarea in tareas]

                    try:
                        id_tarea = self.vista.obtener_id_tarea()
                        if id_tarea in ids_tareas:
                            if tareas:
                                self.modelo.eliminar_tarea(id_tarea)
                                self.vista.mostrar_mensaje(Fore.GREEN + "¡Tarea eliminada correctamente!")
                            else:
                                self.ejecutar_t
                        else:
                            print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                case '5':
                    while True:
                        op = self.vista.ver_t_e()
                        if op == "si":
                            tareas = self.modelo.obtener_tareas_etiquetas()
                            self.vista.mostrar_tareas_etiquetas(tareas)
                            break
                        elif op == "no":
                            tareas = self.modelo.obtener_tareas()
                            self.vista.mostrar_tareas(tareas)
                            break
                        else:
                            self.vista.mostrar_mensaje(Fore.RED + "¡Opción incorrecta!" + Style.RESET_ALL)
                    ids_tareas = [tarea[0] for tarea in tareas]
                    while True:
                        try:
                            id_tarea = self.vista.obtener_id_tarea()
                            if id_tarea in ids_tareas:
                                if tareas:
                                    etiquetas = self.modelo.ver_etiquetas()
                                    self.vista.mostrar_etiquetas(etiquetas)
                                    ids_etiquetas = [etiqueta[0] for etiqueta in etiquetas]
                                    while True:
                                        try:
                                            id_etiqueta = self.vista.obtener_id_etiqueta()
                                            if id_etiqueta in ids_etiquetas:
                                                    if etiquetas:
                                                        self.modelo.agregar_etiqueta(id_tarea, id_etiqueta)
                                                        self.vista.mostrar_mensaje(Fore.GREEN + "Etiqueta agregada correctamente")
                                                        break
                                            else:
                                                print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)        
                                        except ValueError:
                                            print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                                    break
                                else:
                                    print(Fore.RED + "No hay tareas disponibles." + Style.RESET_ALL)
                                    break 
                            else:
                                print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)        
                        except ValueError:
                            print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                case '6':
                    self.vista.mostrar_mensaje(Fore.BLUE + "Regresando al menú principal...")
                    break
                case _:
                    self.vista.mostrar_mensaje(Fore.RED + "Opción no válida. Por favor, intente de nuevo.")


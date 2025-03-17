from colorama import Fore, Style

class ControladorEtiqueta:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_e(self):
        while True:
            self.vista.menu()
            opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)

            match opcion:
                case '1':
                    nombre = self.vista.datos_etiqueta()
                    self.modelo.crear_etiqueta(nombre)
                    self.vista.mostrar_mensaje(Fore.GREEN + "¡Etiqueta agregada correctamente!")
                case '2':
                    etiquetas = self.modelo.ver_etiquetas()
                    self.vista.mostrar_etiquetas(etiquetas)
                case '3':
                    etiquetas = self.modelo.ver_etiquetas()
                    self.vista.mostrar_etiquetas(etiquetas)
                    ids_etiquetas = [etiqueta[0] for etiqueta in etiquetas]
                    while True:
                        try:
                            id_etiqueta = self.vista.obtener_id_etiqueta()
                            if id_etiqueta in ids_etiquetas:
                                if etiquetas:
                                    nuevo_nombre = self.vista.nuevo_nombre()
                                    self.modelo.actualizar_etiqueta(id_etiqueta, nuevo_nombre)
                                    self.vista.mostrar_mensaje(Fore.GREEN + "¡Etiqueta actualizada!")
                                    break
                                else:
                                    self.ejecutar_e
                            else:
                                print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)
                        except ValueError:
                            print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                case '4':
                    etiquetas = self.modelo.ver_etiquetas()
                    self.vista.mostrar_etiquetas(etiquetas)
                    ids_etiquetas = [etiqueta[0] for etiqueta in etiquetas]
                    try:
                        id_etiqueta = self.vista.obtener_id_etiqueta()
                        if id_etiqueta in ids_etiquetas:
                            if etiquetas:
                                self.modelo.eliminar_etiqueta(id_etiqueta)
                                self.vista.mostrar_mensaje(Fore.GREEN + "¡Etiqueta eliminada correctamente!")
                            else:
                                self.ejecutar_e
                        else:
                            print(Fore.RED + "Error: ID fuera de rango." + Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
                case '5':
                    self.vista.mostrar_mensaje(Fore.BLUE + "Regresando al menú principal... ")
                    return
                case _:
                    self.vista.mostrar_mensaje(Fore.RED + "Opción no válida. Por favor, intente de nuevo.")    
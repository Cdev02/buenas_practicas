import validador as Validador

class Request:
    def __init__(self):
        self.validador = Validador()

    def solicitud(self, datos):
        if self.validador.validar_datos(datos):
            print("Solicitud realizada")
        else:
            print("Datos inválidos")
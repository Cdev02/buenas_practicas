import request as Request

class Usuario:
    def __init__(self, id_usuario, nombre, contraseña, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol
        self.request = Request()

    def solicitud(self, datos):
        if self.request.validar_datos(datos):
            print(f"Solicitud realizada por {self.nombre}")
        else:
            print("Datos inválidos")
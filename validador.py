import cache as Cache

class Validador:
    def __init__(self):
        self.cache = Cache()

    # Verificar si los datos son válidos
    def validar_datos(self, datos):
        if datos is None or len(datos) == 0:
            return False
        return True

    # Autenticar al usuario
    def autenticar(self, usuario, contraseña):
        if usuario == "admin" and contraseña == "password":
            return True
        return False
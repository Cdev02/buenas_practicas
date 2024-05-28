class Cache:
    def __init__(self):
        self.data = {}

    # Verificar si la clave existe en la cache
    def validar(self, key):
        if key in self.data:
            return True
        return False

    # Almacenar la respuesta en la cache
    def almacenar_resp(self, key, value):
        self.data[key] = value

    # Actualizar la respuesta en la cache
    def act_resp(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value
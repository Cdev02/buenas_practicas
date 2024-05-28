class Orden:
    def __init__(self, id_orden, id_usuario, fecha_orden, estado, productos, direccion):
        self.id_orden = id_orden
        self.id_usuario = id_usuario
        self.fecha_orden = fecha_orden
        self.estado = estado
        self.productos = productos
        self.direccion = direccion

    def crear_orden(self):
        print(f"Orden {self.id_orden} creada")

    def eliminar_orden(self):
        print(f"Orden {self.id_orden} eliminada")

    def editar_orden(self, nuevos_productos):
        self.productos = nuevos_productos
        print(f"Orden {self.id_orden} editada")
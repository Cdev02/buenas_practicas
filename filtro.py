import validador as Validador

class Filtro:
    def __init__(self):
        self.validador = Validador()

    def validar(self, ip):
        # Verificar si la IP es válida
        if ip.startswith("192.168."):
            return True
        return False

    def verificar_ip(self, ip):
        # Verificar si la IP está bloqueada
        if ip in ["192.168.1.100", "192.168.1.200"]:
            return False
        return True

    def bloquear_ip(self, ip):
        # Bloquear la IP
        print(f"IP {ip} bloqueada")
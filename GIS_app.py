from abc import ABC, abstractmethod
from typing import List


class Nodo(ABC):
    def __init__(self, estado_comun):
        self.estado_comun = estado_comun

    @abstractmethod
    def accept(self, visitor):
        pass


class Grafo:
    def __init__(self):
        self.nodos = []

    def add_nodo(self, nodo):
        self.nodos.append(nodo)

    def accept(self, visitor):
        for nodo in self.nodos:
            nodo.accept(visitor)


class Enlace:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino


class Visitor(ABC):
    @abstractmethod
    def visit_ciudad(self, ciudad):
        pass

    @abstractmethod
    def visit_industria(self, industria):
        pass

    @abstractmethod
    def visit_lugar_turismo(self, lugar_turismo):
        pass


class XMLExporter(Visitor):
    def __init__(self):
        self.xml = ""

    def visit_ciudad(self, ciudad):
        self.xml += f"<ciudad>\n"
        self.xml += f"  <nombre>{ciudad.estado_especifico['nombre']}</nombre>\n"
        self.xml += f"  <poblacion>{ciudad.estado_especifico['poblacion']}</poblacion>\n"
        self.xml += f"</ciudad>\n"

    def visit_industria(self, industria):
        self.xml += f"<industria>\n"
        self.xml += f"  <nombre>{industria.estado_especifico['nombre']}</nombre>\n"
        self.xml += f"  <empleados>{industria.estado_especifico['empleados']}</empleados>\n"
        self.xml += f"</industria>\n"

    def visit_lugar_turismo(self, lugar_turismo):
        self.xml += f"<lugar_turismo>\n"
        self.xml += f"  <nombre>{lugar_turismo.estado_especifico['nombre']}</nombre>\n"
        self.xml += f"  <tipo>{lugar_turismo.estado_especifico['tipo']}</tipo>\n"
        self.xml += f"</lugar_turismo>\n"

    def get_xml(self):
        return self.xml


class Ciudad(Nodo):
    def __init__(self, estado_comun, estado_especifico):
        super().__init__(estado_comun)
        self.estado_especifico = estado_especifico

    def accept(self, visitor):
        visitor.visit_ciudad(self)


class Industria(Nodo):
    def __init__(self, estado_comun, estado_especifico):
        super().__init__(estado_comun)
        self.estado_especifico = estado_especifico

    def accept(self, visitor):
        visitor.visit_industria(self)


class LugarTurismo(Nodo):
    def __init__(self, estado_comun, estado_especifico):
        super().__init__(estado_comun)
        self.estado_especifico = estado_especifico

    def accept(self, visitor):
        visitor.visit_lugar_turismo(self)


# Crear un grafo con nodos de diferentes tipos
grafo = Grafo()
grafo.add_nodo(
    Ciudad("Estado común", {"nombre": "Madrid", "poblacion": 3200000}))
grafo.add_nodo(Industria("Estado común", {
               "nombre": "Fábrica de coches", "empleados": 5000}))
grafo.add_nodo(LugarTurismo("Estado común", {
               "nombre": "Parque de atracciones", "tipo": "Diversión"}))

# Crear un objeto Visitor que imprime la información de los nodos en formato XML
exporter = XMLExporter()

# Aceptar el objeto Visitor en el grafo
grafo.accept(exporter)

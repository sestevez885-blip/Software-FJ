"""
Módulo de Entidades para Software FJ.
Contiene la clase abstracta base y la clase Cliente con validaciones robustas.
"""

from abc import ABC, abstractmethod
from excepciones import ClienteNoValidoError

class EntidadBase(ABC):
    """Clase abstracta que representa entidades generales del sistema."""
    
    def __init__(self, identificador: str):
        self._identificador = identificador

    @property
    def identificador(self) -> str:
        """Permite acceder al identificador de forma segura (Encapsulación)."""
        return self._identificador

    @abstractmethod
    def obtener_detalles(self) -> str:
        """Método abstracto que las clases hijas deben implementar obligatoriamente."""
        pass


class Cliente(EntidadBase):
    """Clase que representa a un cliente de Software FJ con validaciones estrictas."""
    
    def __init__(self, identificador: str, nombre: str, correo: str, telefono: str):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ClienteNoValidoError("El nombre del cliente no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        if not valor or "@" not in valor or "." not in valor:
            raise ClienteNoValidoError(f"El correo '{valor}' no es válido.")
        self._correo = valor.strip()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not valor or not valor.isdigit() or len(valor) < 7:
            raise ClienteNoValidoError("El teléfono debe contener al menos 7 dígitos numéricos.")
        self._telefono = valor.strip()

    def obtener_detalles(self) -> str:
        """Retorna una cadena con la información detallada del cliente."""
        return f"Cliente [ID: {self._identificador}] - Nombre: {self._nombre}, Correo: {self._correo}, Teléfono: {self._telefono}"

    def __str__(self):
        return self.obtener_detalles()
"""
Módulo de Servicios para Software FJ.
Define la clase abstracta Servicio y tres servicios especializados, 
aplicando polimorfismo, herencia y métodos sobrecargados.
"""

from abc import abstractmethod
from entidades import EntidadBase
from excepciones import ServicioNoDisponibleError

class Servicio(EntidadBase):
    """Clase abstracta que representa un servicio ofrecido por Software FJ."""
    
    def __init__(self, identificador: str, nombre_servicio: str, costo_base: float, disponible: bool = True):
        super().__init__(identificador)
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base
        self.disponible = disponible

    @property
    def costo_base(self) -> float:
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor: float):
        if valor < 0:
            raise ValueError("El costo base no puede ser negativo.")
        self._costo_base = float(valor)

    def verificar_disponibilidad(self):
        """Verifica si el servicio está activo y disponible."""
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre_servicio}' no se encuentra disponible actualmente.")
        return True

    @abstractmethod
    def calcular_costo(self) -> float:
        """Método abstracto para calcular el costo que será sobrescrito en las clases hijas."""
        pass

    @abstractmethod
    def obtener_detalles(self) -> str:
        pass


class ReservaSala(Servicio):
    """Servicio especializado para reserva de salas."""
    
    def __init__(self, identificador: str, nombre_servicio: str, costo_base: float, capacidad_personas: int, disponible: bool = True):
        super().__init__(identificador, nombre_servicio, costo_base, disponible)
        self.capacidad_personas = capacidad_personas

    # Demostración de sobrecarga de métodos: acepta parámetros opcionales (impuesto y descuento)
    def calcular_costo(self, impuesto: float = 0.19, descuento: float = 0.0) -> float:
        """Calcula el costo total de la sala aplicando opcionalmente impuestos y descuentos."""
        self.verificar_disponibilidad()
        costo_con_impuesto = self.costo_base * (1 + impuesto)
        costo_final = costo_con_impuesto * (1 - descuento)
        return round(costo_final, 2)

    def obtener_detalles(self) -> str:
        return f"Reserva de Sala [ID: {self._identificador}] - Nombre: {self.nombre_servicio}, Capacidad: {self.capacidad_personas} personas, Costo Base: ${self.costo_base}"


class AlquilerEquipo(Servicio):
    """Servicio especializado para alquiler de equipos tecnológicos."""
    
    def __init__(self, identificador: str, nombre_servicio: str, costo_base: float, numero_serial: str, disponible: bool = True):
        super().__init__(identificador, nombre_servicio, costo_base, disponible)
        self.numero_serial = numero_serial

    def calcular_costo(self, horas: int = 1, recargo_urgente: float = 0.0) -> float:
        """Calcula el costo del alquiler de equipos en función de las horas y un recargo opcional."""
        self.verificar_disponibilidad()
        costo_total = (self.costo_base * horas) + recargo_urgente
        return round(costo_total, 2)

    def obtener_detalles(self) -> str:
        return f"Alquiler de Equipo [ID: {self._identificador}] - Equipo: {self.nombre_servicio}, Serial: {self.numero_serial}, Costo/Hora: ${self.costo_base}"


class AsesoriaEspecializada(Servicio):
    """Servicio especializado para asesorías técnicas profesionales."""
    
    def __init__(self, identificador: str, nombre_servicio: str, costo_base: float, area_especialidad: str, disponible: bool = True):
        super().__init__(identificador, nombre_servicio, costo_base, disponible)
        self.area_especialidad = area_especialidad

    def calcular_costo(self, complejidad_factor: float = 1.0) -> float:
        """Calcula el costo de la asesoría aplicando un factor de complejidad opcional."""
        self.verificar_disponibilidad()
        return round(self.costo_base * complejidad_factor, 2)

    def obtener_detalles(self) -> str:
        return f"Asesoría Especializada [ID: {self._identificador}] - Tema: {self.nombre_servicio}, Área: {self.area_especialidad}, Costo Base: ${self.costo_base}"
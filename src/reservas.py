"""
Módulo de Reservas para Software FJ.
Gestiona la relación entre clientes y servicios, controlando estados y excepciones.
"""

from entidades import Cliente
from servicios import Servicio
from excepciones import ErrorReservaError

class Reserva:
    """Clase que representa una reserva de un servicio por parte de un cliente."""
    
    id_contador = 1  # Autoincremental para generar códigos únicos de reserva

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion_horas: int = 1):
        self.id_reserva = f"RES-{Reserva.id_contador:03d}"
        Reserva.id_contador += 1
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente"  # Estados: Pendiente, Confirmada, Cancelada

    @property
    def duracion_horas(self) -> int:
        return self._duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, valor: int):
        if valor <= 0:
            raise ErrorReservaError("La duración de la reserva debe ser mayor a 0 horas.")
        self._duracion_horas = int(valor)

    def confirmar_reserva(self):
        """Confirma la reserva aplicando manejo avanzado de excepciones y bloques try/except/else/finally."""
        print(f"\n[Proceso] Intentando confirmar reserva {self.id_reserva}...")
        try:
            # Validamos disponibilidad del servicio
            self.servicio.verificar_disponibilidad()
            
            if self.estado == "Confirmada":
                raise ErrorReservaError(f"La reserva {self.id_reserva} ya se encuentra confirmada previamente.")
            if self.estado == "Cancelada":
                raise ErrorReservaError(f"No se puede confirmar la reserva {self.id_reserva} porque está cancelada.")
                
        except ErrorReservaError as e:
            # Capturamos errores de negocio de reserva
            print(f"-> [Error de Reserva controlado]: {e}")
            raise  # Encadenamiento de excepciones si es necesario
        else:
            # Se ejecuta si no hubo excepciones
            self.estado = "Confirmada"
            print(f"-> ¡Éxito! Reserva {self.id_reserva} confirmada correctamente.")
        finally:
            # Se ejecuta siempre, ideal para logs o cierres
            print(f"-> [Log interno]: Finalizó intento de confirmación para {self.id_reserva}. Estado actual: {self.estado}")

    def cancelar_reserva(self):
        """Cancela una reserva existente de forma segura."""
        if self.estado == "Cancelada":
            print(f"-> Aviso: La reserva {self.id_reserva} ya estaba cancelada.")
            return
        self.estado = "Cancelada"
        print(f"-> Reserva {self.id_reserva} cancelada exitosamente.")

    def obtener_resumen(self) -> str:
        """Retorna un resumen detallado de la reserva."""
        return (
            f"Reserva ID: {self.id_reserva} | Estado: {self.estado} | "
            f"Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre_servicio} | "
            f"Duración: {self.duracion_horas}h"
        )

    def __str__(self):
        return self.obtener_resumen()
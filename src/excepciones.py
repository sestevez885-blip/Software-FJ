"""
Módulo de Excepciones Personalizadas para Software FJ.
Define errores específicos del dominio para un manejo robusto de excepciones.
"""

class SoftwareFJError(Exception):
    """Clase base para todas las excepciones personalizadas del sistema."""
    def __init__(self, mensaje="Ocurrió un error general en el sistema Software FJ"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ClienteNoValidoError(SoftwareFJError):
    """Se lanza cuando los datos de un cliente no cumplen con las validaciones."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando se intenta solicitar un servicio inactivo o inexistente."""
    pass


class ErrorReservaError(SoftwareFJError):
    """Se lanza cuando ocurre un fallo al procesar, confirmar o cancelar una reserva."""
    pass
"""
Módulo Sistema para Software FJ.
Coordina las colecciones en memoria de clientes, servicios y reservas,
e implementa un sistema robusto de registro en archivos de log.
"""

import os
from datetime import datetime
from entidades import Cliente
from servicios import Servicio
from reservas import Reserva
from excepciones import SoftwareFJError

class SistemaSoftwareFJ:
    """Clase central que gestiona las operaciones de Software FJ sin bases de datos."""
    
    def __init__(self, ruta_log: str = "logs/sistema.log"):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.ruta_log = ruta_log
        self._inicializar_directorio_logs()

    def _inicializar_directorio_logs(self):
        """Crea la carpeta y el archivo de logs si no existen."""
        directorio = os.path.dirname(self.ruta_log)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        # Creamos el archivo de log inicial si no existe
        if not os.path.exists(self.ruta_log):
            with open(self.ruta_log, "w", encoding="utf-8") as f:
                f.write(f"--- INICIO DE LOGS SOFTWARE FJ - {datetime.now()} ---\n")

    def registrar_log(self, tipo: str, mensaje: str):
        """Registra un evento o error en el archivo de logs con marca de tiempo."""
        marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entrada_log = f"[{marca_tiempo}] [{tipo.upper()}] {mensaje}\n"
        try:
            with open(self.ruta_log, "a", encoding="utf-8") as f:
                f.write(entrada_log)
        except Exception as e:
            print(f"Error crítico escribiendo en el archivo de log: {e}")

    def agregar_cliente(self, cliente: Cliente):
        """Agrega un cliente a la lista interna tras validarlo."""
        try:
            self.clientes.append(cliente)
            self.registrar_log("INFO", f"Cliente agregado exitosamente: {cliente.nombre} (ID: {cliente.identificador})")
            print(f"[Sistema] Cliente registrado: {cliente.nombre}")
        except Exception as e:
            self.registrar_log("ERROR", f"Fallo al agregar cliente: {e}")
            raise

    def agregar_servicio(self, servicio: Servicio):
        """Agrega un servicio especializado a la lista interna."""
        try:
            self.servicios.append(servicio)
            self.registrar_log("INFO", f"Servicio agregado exitosamente: {servicio.nombre_servicio} (ID: {servicio.identificador})")
            print(f"[Sistema] Servicio registrado: {servicio.nombre_servicio}")
        except Exception as e:
            self.registrar_log("ERROR", f"Fallo al agregar servicio: {e}")
            raise

    def crear_reserva(self, cliente: Cliente, servicio: Servicio, duracion: int) -> Reserva:
        """Crea una reserva vinculando cliente y servicio, controlando excepciones."""
        try:
            reserva = Reserva(cliente, servicio, duracion)
            self.reservas.append(reserva)
            self.registrar_log("INFO", f"Reserva creada correctamente: ID {reserva.id_reserva}")
            print(f"[Sistema] Reserva creada con éxito: {reserva.id_reserva}")
            return reserva
        except SoftwareFJError as se:
            self.registrar_log("ADVERTENCIA", f"Error de negocio al crear reserva: {se}")
            print(f"[Sistema Advertencia]: {se}")
            raise
        except Exception as e:
            self.registrar_log("ERROR", f"Error inesperado al crear reserva: {e}")
            print(f"[Sistema Error Inesperado]: {e}")
            raise
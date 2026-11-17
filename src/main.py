"""
Módulo Principal (main.py) para Software FJ.
Ejecuta la simulación de las 10 operaciones requeridas por el docente,
probando casos exitosos, errores controlados, excepciones personalizadas
y bloques try/except/else/finally.
"""

from sistema import SistemaSoftwareFJ
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from excepciones import ClienteNoValidoError, ServicioNoDisponibleError, ErrorReservaError

def ejecutar_simulacion():
    print("=" * 70)
    print(" INICIANDO SIMULACIÓN - SISTEMA INTEGRAL DE GESTIÓN (SOFTWARE FJ)")
    print("=" * 70)
    
    # Inicializamos nuestro sistema sin base de datos
    sistema = SistemaSoftwareFJ()
    
    print("\n--- FASE 1: REGISTRO DE CLIENTES (Válidos e Inválidos) ---")
    
    # Operación 1: Registro válido de cliente
    try:
        c1 = Cliente("C001", "Carlos Pérez", "carlos.perez@email.com", "3001234567")
        sistema.agregar_cliente(c1)
    except Exception as e:
        print(f"Error capturado: {e}")

    # Operación 2: Registro inválido de cliente (Correo incorrecto - Dispara excepción)
    try:
        print("\n[Intento] Registrando cliente con correo inválido...")
        c_invalido = Cliente("C002", "Ana Gómez", "correo_sin_arroba.com", "3109876543")
        sistema.agregar_cliente(c_invalido)
    except ClienteNoValidoError as e:
        print(f"-> [Excepción controlada con éxito]: {e}")
        sistema.registrar_log("ADVERTENCIA", f"Intento fallido de cliente: {e}")

    # Operación 3: Registro válido de segundo cliente
    try:
        c2 = Cliente("C003", "María Rodríguez", "maria.rodriguez@email.com", "3201112233")
        sistema.agregar_cliente(c2)
    except Exception as e:
        print(f"Error capturado: {e}")


    print("\n--- FASE 2: REGISTRO DE SERVICIOS ESPECIALIZADOS ---")
    
    # Operación 4: Crear servicio de Sala de Reuniones (hereda de Servicio)
    try:
        sala = ReservaSala("S001", "Sala Ejecutiva Alpha", 150000.0, capacidad_personas=10, disponible=True)
        sistema.agregar_servicio(sala)
    except Exception as e:
        print(f"Error: {e}")

    # Operación 5: Crear servicio de Alquiler de Equipo tecnológico
    try:
        equipo = AlquilerEquipo("S002", "Servidor Portátil de Pruebas", 45000.0, numero_serial="SN-998877", disponible=True)
        sistema.agregar_servicio(equipo)
    except Exception as e:
        print(f"Error: {e}")

    # Operación 6: Crear servicio de Asesoría Especializada (Inactivo para probar errores)
    try:
        asesoria = AsesoriaEspecializada("S003", "Arquitectura de Software POO", 200000.0, area_especialidad="Desarrollo", disponible=False)
        sistema.agregar_servicio(asesoria)
    except Exception as e:
        print(f"Error: {e}")


    print("\n--- FASE 3: CREACIÓN Y GESTIÓN DE RESERVAS Y EXCEPCIONES ---")

    # Operación 7: Reserva válida de sala con cálculo de costo sobrecargado (impuesto y descuento)
    try:
        print("\n[Operación] Creando reserva de Sala para Carlos...")
        reserva1 = sistema.crear_reserva(c1, sala, duracion=3)
        costo_final = sala.calcular_costo(impuesto=0.19, descuento=0.10)
        print(f"-> Costo calculado con sobrecarga (Impuesto + Descuento): ${costo_final:,.2f}")
        reserva1.confirmar_reserva()
    except Exception as e:
        print(f"Error en reserva 1: {e}")

    # Operación 8: Intentar confirmar la misma reserva otra vez (Prueba try/except/else/finally y control de duplicidad)
    try:
        print("\n[Operación] Intentando confirmar nuevamente la misma reserva (debe fallar y controlarse):")
        reserva1.confirmar_reserva()
    except ErrorReservaError as e:
        print(f"-> [Control de excepción de negocio verificado]: {e}")

    # Operación 9: Reserva fallida por intentar usar un servicio NO disponible (Asesoría inactiva)
    try:
        print("\n[Operación] Intentando reservar un servicio inactivo (Asesoría):")
        reserva_fallida = sistema.crear_reserva(c2, asesoria, duracion=2)
        reserva_fallida.confirmar_reserva()
    except (ServicioNoDisponibleError, ErrorReservaError) as e:
        print(f"-> [Excepción capturada correctamente por servicio no disponible]: {e}")
        sistema.registrar_log("ADVERTENCIA", f"Intento de reserva sobre servicio inactivo bloqueado: {e}")

    # Operación 10: Alquiler de equipo con cálculo de costo por horas y recargo urgente
    try:
        print("\n[Operación] Creando reserva y alquiler de equipo tecnológico para María...")
        reserva2 = sistema.crear_reserva(c2, equipo, duracion=5)
        costo_equipo = equipo.calcular_costo(horas=5, recargo_urgente=20000.0)
        print(f"-> Costo total del alquiler de equipo (con horas y recargo): ${costo_equipo:,.2f}")
        reserva2.confirmar_reserva()
    except Exception as e:
        print(f"Error en reserva 2: {e}")

    print("\n" + "=" * 70)
    print(" RESUMEN FINAL DEL SISTEMA (10 OPERACIONES COMPLETADAS)")
    print("=" * 70)
    print(f"Total Clientes registrados: {len(sistema.clientes)}")
    print(f"Total Servicios registrados: {len(sistema.servicios)}")
    print(f"Total Reservas gestionadas: {len(sistema.reservas)}")
    print("\nEstado de las reservas:")
    for r in sistema.reservas:
        print(f" - {r}")
        
    print("\n¡Simulación finalizada con éxito! Revise el archivo 'logs/sistema.log' para ver el registro detallado.")
    print("=" * 70)

if __name__ == "__main__":
    ejecutar_simulacion()
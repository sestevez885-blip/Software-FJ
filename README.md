# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

##  Descripción del Proyecto
Sistema orientado a objetos desarrollado en **Python** para la empresa **Software FJ**, diseñado para gestionar clientes, servicios especializados (salas, alquiler de equipos y asesorías) y reservas. 

El proyecto demuestra una arquitectura modular sin uso de motores de bases de datos, utilizando estructuras de memoria (listas y objetos) y almacenamiento persistente en archivos para el registro de eventos y errores (**logging**).

---

##  Características Técnicas
- **Programación Orientada a Objetos (POO):**
  - **Abstracción:** Uso de la clase abstracta `EntidadBase` y la clase abstracta `Servicio` mediante el módulo `abc`.
  - **Encapsulación:** Atributos protegidos con propiedades (`@property` y `@setter`) para validación estricta de datos personales.
  - **Herencia y Polimorfismo:** Especializaciones de servicio (`ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`) que redefinen la lógica de costo y detalles.
  - **Sobrecarga de Métodos:** Variantes parametrizadas para cálculo de costos con impuestos, descuentos, horas y recargos.
- **Manejo Avanzado de Excepciones:**
  - Jerarquía de excepciones personalizadas (`SoftwareFJError`, `ClienteNoValidoError`, `ServicioNoDisponibleError`, `ErrorReservaError`).
  - Bloques estructurados `try / except / else / finally`.
  - Registro automatizado de trazas y eventos en `logs/sistema.log`.

---

##  Estructura del Proyecto
```text
Software-FJ/
│
├── docs/
│   └── documentacion.md
├── logs/
│   └── sistema.log          # Registro de eventos y errores generados en ejecución
├── src/
│   ├── entidades.py         # Clase EntidadBase y Cliente
│   ├── excepciones.py       # Excepciones personalizadas del dominio
│   ├── main.py              # Script principal con la simulación de 10 operaciones
│   ├── reservas.py          # Clase Reserva y lógica de confirmación/cancelación
│   ├── servicios.py         # Clase abstracta Servicio y sus 3 especializaciones
│   └── sistema.py           # Gestor central de colecciones y registrador de logs
├── .gitignore
└── README.md
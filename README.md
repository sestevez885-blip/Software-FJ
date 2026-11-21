<img width="4032" height="1173" alt="image" src="https://github.com/user-attachments/assets/3197a0a3-0a8e-4d25-8e9a-315f00e59800" />
<img width="4032" height="1935" alt="image" src="https://github.com/user-attachments/assets/ff97fbb4-de40-47d1-8bbb-2bbf80021baf" />
<img width="4032" height="1806" alt="image" src="https://github.com/user-attachments/assets/b509804d-a7fd-40b6-90e4-395dbb1e4971" />
<img width="3875" height="2268" alt="image" src="https://github.com/user-attachments/assets/ef5ebae6-144b-4c30-9f44-d855111c50bc" />
<img width="2050" height="2268" alt="image" src="https://github.com/user-attachments/assets/f7ef3d00-aeaf-48bd-8b3c-938c458a72b4" />
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

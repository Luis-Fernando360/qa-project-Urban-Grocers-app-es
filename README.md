# Proyecto Sprint 7 Urban Grocers - Pruebas de API

# 

# \# Descripción del proyecto

Automatización de pruebas para la aplicación web Urban Grocers, enfocado en validar flujos críticos del negocio como la creación de kits y el envío de solicitudes, asegurando la calidad y estabilidad del sistema.

# \# Objetivo

Automatizar pruebas funcionales para:

Reducir pruebas manuales repetitivas

Detectar defectos tempranos

Garantizar flujos clave del usuario

# 

# \# Documentación

- Fuente: \[apiDoc de Urban Grocers]

- Detalles de los endpoints, parámetros y respuestas.

# 

# \# Tecnologías utilizadas

- Python

- Selenium Web Driver

- Pytest

- Web Driver Manager

- Page Objet Model (POM)

- Requests

# 

# \# Casos de prueba automatizados

- Creación de kits con nombre válido

- Envío de solicitudes

- Validación de elementos visibles

- Manejo de esperas explícitas

- Control de errores comunes de UI

#

# \# Ejecución del Proyecto

\# Instalación

 1\. Clonar el repositorio:

 &nbsp;  ```bash

 &nbsp;  git clone https://github.com/tu-usuario/urban-grocers-api-tests.git

 2\. Ejecutar pruebas:

Pytest

# Estructura del Proyecto

\- tests/      -> Casos de prueba
\- pages/      -> Lógica de interacción con la UI
\- data/       -> Datos de prueba
\- config/     -> Configuración del entorno


# 

# \# Bugs encontrados

# 1\. BUG 1 — La API acepta nombre vacío:

\- Entrada: {"name": ""}

\- Resultado esperado: 400 Bad Request

\- Resultado real: 201 Created

\- Severidad: Media

\- Descripción: El servidor permite crear kits sin nombre, lo cual no debería ser válido.

# 2\.BUG 2 — La API acepta nombres mayores a 511 caracteres:

\- Entrada: {"name": "a" * 512}

\- Resultado esperado: 400 Bad Request

\- Resultado real: 201 Created

\- Severidad: Alta

\- Descripción: El servidor no valida la longitud máxima permitida.

# 3\. BUG 3 — La API devuelve 500 cuando falta el campo name:

\- Entrada: {}

\- Resultado esperado: 400 Bad Request

\- Resultado real: 500 Internal Server Error

\- Severidad: Crítica

\- Descripción: El servidor se rompe al recibir un JSON sin el parámetro obligatorio.

# 4\. BUG 4 — La API acepta valores no string:

\- Entrada: {"name": 123}

\- Resultado esperado: 400 Bad Request

\- Resultado real: 201 Created

\- Severidad: Media

\- Descripción: El servidor no valida el tipo de dato del parámetro name.

#

# \# Autor

# Luis Fernando López Gutiérrez
# QA Automation Engineer

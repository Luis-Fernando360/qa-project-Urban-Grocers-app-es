# \# Proyecto Urban Grocers - Pruebas de API

# 

# \## Descripción

# Este proyecto contiene pruebas automatizadas para la API de Urban Grocers. Las pruebas están diseñadas para validar los endpoints principales, asegurar la correcta integración del sistema y detectar posibles errores antes de su despliegue en producción.

# 

# \## Documentación

# \- Fuente: \[apiDoc de Urban Grocers]

# \- Detalles de los endpoints, parámetros y respuestas.

# 

# \## Tecnologías utilizadas

# \- Python

# \- Pytest

# \- Requests

# 

# \## Instalación

# 1\. Clonar el repositorio:

# &nbsp;  ```bash

# &nbsp;  git clone https://github.com/tu-usuario/urban-grocers-api-tests.git

# 

# \## Bugs encontrados

# 1\. BUG 1 — La API acepta nombre vacío:

# \- Entrada: {"name": ""}

# \- Resultado esperado: 400 Bad Request

# \- Resultado real: 201 Created

# \- Severidad: Media

# \- Descripción: El servidor permite crear kits sin nombre, lo cual no debería ser válido.

# 2\.BUG 2 — La API acepta nombres mayores a 511 caracteres:

# \- Entrada: {"name": "a" * 512}

# \- Resultado esperado: 400 Bad Request

# \- Resultado real: 201 Created

# \- Severidad: Alta

# \- Descripción: El servidor no valida la longitud máxima permitida.

# 3\. BUG 3 — La API devuelve 500 cuando falta el campo name:

# \- Entrada: {}

# \- Resultado esperado: 400 Bad Request

# \- Resultado real: 500 Internal Server Error

# \- Severidad: Crítica

# \- Descripción: El servidor se rompe al recibir un JSON sin el parámetro obligatorio.

# 4\. BUG 4 — La API acepta valores no string:

# \- Entrada: {"name": 123}

# \- Resultado esperado: 400 Bad Request

# \- Resultado real: 201 Created

# \- Severidad: Media

# \- Descripción: El servidor no valida el tipo de dato del parámetro name.

#

# \## Autor

# Luis Fernando López Gtz

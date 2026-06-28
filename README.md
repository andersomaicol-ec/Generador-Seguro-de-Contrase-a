                                                Generador Seguro de Contraseñas en Python



# Integrante

* Michael Shiguango



# Objetivo del sistema

Desarrollar una aplicación en Python que permita generar contraseñas seguras y personalizadas, brindando al usuario la posibilidad de seleccionar la longitud y los tipos de caracteres que desea incluir. El sistema incorpora validaciones para evitar errores de entrada, utiliza mecanismos de generación criptográficamente seguros mediante la librería **secrets** y evalúa el nivel de seguridad de la contraseña generada.



# Descripción de funcionalidades

El sistema permite:

* Solicitar la longitud de la contraseña.
* Validar que la longitud ingresada sea un número entero.
* Exigir una longitud mínima de **8 caracteres** para garantizar una contraseña más segura.
* Permitir seleccionar el uso de:

  * Letras mayúsculas.
  * Letras minúsculas.
  * Números.
  * Símbolos.
* Validar que las respuestas ingresadas sean únicamente **"s"** o **"n"**.
* Solicitar nuevamente la configuración cuando el usuario no selecciona ningún tipo de carácter.
* Garantizar que la contraseña contenga al menos un carácter de cada tipo seleccionado.
* Generar contraseñas utilizando la librería **secrets**, recomendada para aplicaciones relacionadas con la seguridad informática.
* Mostrar un resumen de la configuración seleccionada por el usuario.
* Evaluar el nivel de seguridad de la contraseña generada (Débil, Media, Fuerte o Muy Fuerte).
* Mostrar recomendaciones para mejorar la seguridad cuando sea necesario.
* Permitir generar nuevas contraseñas sin necesidad de reiniciar el programa.



# Tecnologías utilizadas

* Python 3
* Librería `secrets`
* Librería `string`
* Visual Studio Code
* GitHub



# Cronograma del proyecto

| Semana | Actividad desarrollada                                                                                                                                                                                                                                                    | Resultado obtenido                                                           |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **1**  | Análisis del problema, definición del objetivo del sistema e investigación sobre buenas prácticas para la creación de contraseñas seguras.                                                                                                                                | Se definió el alcance y los requerimientos del proyecto.                     |
| **2**  | Diseño de la solución mediante diagramas de casos de uso, arquitectura del sistema y análisis del funcionamiento del software.                                                                                                                                            | Diagramas terminados y diseño lógico definido.                               |
| **3**  | Configuración del entorno de desarrollo (Python, Visual Studio Code y GitHub). Creación del repositorio y estructura inicial del proyecto.                                                                                                                                | Entorno de desarrollo preparado y repositorio configurado.                   |
| **4**  | Desarrollo de la primera versión del programa. Implementación de la entrada de datos y validación de la longitud de la contraseña para aceptar únicamente valores numéricos.                                                                                              | Primera versión funcional del sistema.                                       |
| **5**  | Implementación de la selección de mayúsculas, minúsculas, números y símbolos. Incorporación de validaciones para las respuestas (s/n) y control para evitar que el usuario continúe sin seleccionar al menos un tipo de carácter.                                         | Sistema más robusto y con mejor manejo de errores.                           |
| **6**  | Optimización del algoritmo reemplazando la librería **random** por **secrets**. Se implementó una longitud mínima de 8 caracteres y se garantizó que la contraseña contenga al menos un carácter de cada tipo seleccionado.                                               | Contraseñas más seguras siguiendo buenas prácticas de seguridad informática. |
| **7**  | Incorporación del resumen de configuración, evaluación automática del nivel de seguridad de la contraseña, recomendaciones para el usuario y opción para generar nuevas contraseñas sin reiniciar el programa. Elaboración del diagrama de flujo y corrección de errores. | Sistema optimizado, más intuitivo y completamente funcional.                 |
| **8**  | Elaboración del README, revisión general del proyecto, pruebas finales, grabación de videos explicativos y entrega del proyecto.                                                                                                                                          | Proyecto completamente documentado, probado y listo para su presentación.    |



# Fecha

Junio de 2026



# Informe Final

## Introducción

La seguridad informática representa uno de los aspectos más importantes en la protección de la información digital. Una contraseña segura disminuye significativamente el riesgo de accesos no autorizados y protege la información personal de los usuarios.

Con este proyecto se desarrolló un **Generador Seguro de Contraseñas** utilizando Python, aplicando conceptos de programación estructurada, validación de datos, estructuras condicionales, ciclos repetitivos y generación criptográficamente segura mediante la librería **secrets**.


## Descripción del problema

Actualmente muchas personas utilizan contraseñas cortas, repetidas o fáciles de adivinar, lo que incrementa considerablemente el riesgo de sufrir ataques informáticos o accesos no autorizados.

Ante esta problemática se desarrolló un sistema capaz de generar contraseñas robustas, personalizadas y seguras, incorporando validaciones para evitar errores de entrada y ofreciendo recomendaciones sobre el nivel de seguridad de cada contraseña generada.



## Relación con los contenidos de la asignatura

Durante el desarrollo del proyecto se aplicaron los conocimientos adquiridos en la asignatura, entre ellos:

* Variables.
* Tipos de datos.
* Entrada y salida de información.
* Estructuras condicionales.
* Ciclos repetitivos.
* Validación de datos.
* Manejo de librerías en Python.
* Buenas prácticas de programación.
* Diagramas de flujo.
* Diagramas de casos de uso.
* Arquitectura del sistema.
* Documentación de software.
* Uso de GitHub para el control del proyecto.



## Explicación del sistema desarrollado

El sistema inicia solicitando al usuario la longitud de la contraseña y verifica que el valor ingresado sea un número entero con una longitud mínima de ocho caracteres.

Posteriormente solicita seleccionar los tipos de caracteres que desea utilizar: letras mayúsculas, letras minúsculas, números y símbolos. Además, valida que las respuestas sean únicamente **"s"** o **"n"** y obliga al usuario a seleccionar al menos un tipo de carácter para continuar.

Una vez validadas todas las opciones, el programa construye el conjunto de caracteres disponibles y garantiza que la contraseña contenga al menos un carácter de cada tipo seleccionado.

La generación de la contraseña se realiza mediante la librería **secrets**, especializada en la creación de valores aleatorios para aplicaciones relacionadas con la seguridad informática.

Finalmente, el sistema presenta un resumen de la configuración seleccionada, muestra la contraseña generada, evalúa automáticamente su nivel de seguridad (Débil, Media, Fuerte o Muy Fuerte), ofrece recomendaciones al usuario y permite generar nuevas contraseñas sin necesidad de reiniciar la aplicación.



## Reflexión sobre el impacto de la tecnología

El desarrollo de este proyecto permitió comprender la importancia de aplicar buenas prácticas de programación para resolver problemas relacionados con la seguridad informática.

Además de fortalecer conocimientos sobre Python, estructuras de control, validación de datos y documentación técnica, el proyecto permitió conocer la importancia de utilizar herramientas especializadas como la librería **secrets**, la cual ofrece un mayor nivel de seguridad que otros métodos tradicionales de generación aleatoria.

Este tipo de aplicaciones demuestra cómo la tecnología puede contribuir a proteger la información personal de los usuarios, promoviendo el uso de contraseñas robustas y reduciendo los riesgos asociados a vulnerabilidades de seguridad digital.

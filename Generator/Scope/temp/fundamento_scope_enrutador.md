# Fundamento del Scope como enrutador

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

Este documento explica el diseño. La [especificación del Scope](especificacion_scope.md) contiene las responsabilidades y criterios necesarios para construir el prototipo.

## Problema de diseño

El Scope debe orientar el trabajo en un proyecto sin acumular todos los procedimientos especializados. Si mezcla contexto, restricciones y pasos de cada disciplina, su mantenimiento exige cambiar el mismo archivo por motivos distintos.

## Elección: separar gobierno y especialización

El Scope establece el contexto, las reglas locales y la selección de capacidades. Las skills desarrollan los procedimientos. Se conserva el término enrutador para describir esa selección; no implica un servicio ejecutable ni un agente independiente.

| Sección del Scope | Razón de su existencia |
| --- | --- |
| A. Contexto y alcance del proyecto | Permite comprender el objetivo y sus límites antes de seleccionar una capacidad. |
| B. Reglas y límites de actuación | Ubica las convenciones, autorizaciones y resolución de conflictos. |
| C. Selección y uso de skills | Separa la elección de capacidades de sus procedimientos y contempla ausencias y dependencias. |
| D. Cambios de gobernanza | Define cómo mantener las reglas sin confundir una instrucción de protección con un control técnico. |

## Alternativas y tradeoffs

| Alternativa | Ventaja | Limitación |
| --- | --- | --- |
| Un Scope con todos los procedimientos | Lectura concentrada en un archivo. | Mezcla responsabilidades y crece con cada especialidad. |
| Solo skills sin contexto local | Cada procedimiento conserva su independencia. | Falta una ubicación clara para reglas y límites comunes del proyecto. |
| Scope como enrutador y skills especializadas — elegida | Mantiene separadas las responsabilidades y facilita reutilizar procedimientos. | Requiere descripciones útiles, referencias verificables y tratamiento de dependencias. |

El patrón no garantiza ausencia de errores, seguridad técnica ni compatibilidad universal. Es una elección de organización cuyo resultado debe comprobarse contra la especificación. El alcance actual termina en el diseño del Scope; la construcción de skills corresponde a la siguiente etapa.

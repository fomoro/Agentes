# Plantillas de mapa y pendientes

- Actualizado: el 2026-09-17 08:44
- Rol de ejecución: diseñador de skills y arquitecto de soluciones e integraciones
- Autor: Sam (Asistente IA del Sr. Wolfan)

## Uso

Sustituye los marcadores con información del proyecto. Resuelve la cabecera desde la gobernanza del destino; no copies la firma de esta referencia. Conserva títulos y columnas acordados por el usuario. Omite secciones no aplicables y no generes filas de relleno.

Mantén solo los identificadores utilizados. Explica una vez que los servicios son lógicos y propuestos; identifica en la fila correspondiente cualquier excepción a ese estado general. Si una relación necesita evidencia adicional, incorpora una referencia breve en la celda pertinente o una columna de fuente cuando resulte más claro.

## Mapa preliminar

```markdown
# Mapa preliminar de integraciones [sistemas]

[Cabecera según la gobernanza vigente]

## Objetivo y alcance

### Objetivo
[Relacionar las capacidades de negocio, los contratos disponibles y las responsabilidades de integración para comprender la solución que se estimará.]

### Alcance
[Precisar fase, sistemas, interacciones y límites. Indicar el carácter lógico de los servicios y qué decisiones sobre implementación quedan abiertas.]

## Identificación utilizada

| Identificador | Significado | Ejemplo |
| --- | --- | --- |
| [Tipo de ID utilizado] | [Qué representa] | [Ejemplo del mapa] |

## Contratos de interfaces disponibles

| # | Sistema responsable | Contrato | Para qué sirve | Capacidades relacionadas | Fuente |
| --- | --- | --- | --- | --- | --- |
| 1 | [Sistema] | [Nombre documentado] | [Propósito] | [IDs funcionales] | [Enlace verificado] |

## Capacidades atendidas principalmente por [sistema]

| # | ID | Capacidad | Razón arquitectónica |
| --- | --- | --- | --- |
| 1 | [ID funcional] | [Nombre vigente o propuesta identificada] | [Cómo se atiende dentro del sistema] |

## Capacidades que requieren integración

| # | ID de capacidad | Capacidad | Dirección | Contrato o mecanismo | Responsabilidad de integración |
| --- | --- | --- | --- | --- | --- |
| 1 | [ID funcional] | [Nombre vigente o propuesta identificada] | [Origen → Destino] | [Documentado o Por definir] | [ID — Nombre lógico] |

### Alcance de las responsabilidades de integración

| Responsabilidad de integración | Sistema que la atiende | Aclaración de alcance |
| --- | --- | --- |
| [ID — Nombre lógico] | [Sistema o asignación propuesta] | [Información de negocio, resultado y límite útil para evitar confusión] |

### Tramos de integración, cuando se requieran

| # | Responsabilidad de integración | Origen | Destino | Qué inicia el intercambio | Información y resultado esperado |
| --- | --- | --- | --- | --- | --- |
| 1 | [Mismo ID — Nombre lógico] | [Sistema] | [Sistema] | [Solicitud, evento o condición] | [Contenido de negocio y resultado de este tramo] |
```

Adapta el número de cuadros a los sistemas e interacciones necesarios. No exijas un intermediario ni tres sistemas. Omite el cuadro de tramos cuando repita una relación directa ya clara; úsalo para explicar intermediación, distribución a varios destinos o secuencias que la matriz no aclare. Repetir un ID en distintos tramos expresa continuidad de la responsabilidad lógica, no prueba que una sola interfaz física cubra todos los tramos. Si un tramo requiere otra responsabilidad, justifícala antes de crear un identificador distinto.

## Registro separado de pendientes

```markdown
# Pendientes de integración [sistemas]

[Cabecera según la gobernanza vigente]

## Pendientes de arquitectura para estimación

| # | Relacionado con | Pendiente | Con quién confirmar |
| --- | --- | --- | --- |
| 1 | [Responsabilidad o dependencia] | [Decisión que afecta el alcance o el esfuerzo] | [Interlocutor] |

## Pendientes de arquitectura detallada

| # | Relacionado con | Pendiente | Con quién confirmar |
| --- | --- | --- | --- |
| 1 | [Servicio o contrato] | [Definición técnica por resolver] | [Interlocutor] |

## Pendientes funcionales

| # | Relacionado con | Pendiente | Con quién confirmar |
| --- | --- | --- | --- |
| 1 | [Capacidad o proceso] | [Regla, significado o resultado por confirmar] | [Interlocutor] |
```

Si ya existe un registro autorizado, actualízalo en lugar de crear otro. Si la solicitud excluye la creación de un archivo de pendientes, comunica las brechas en la entrega sin ampliar el conjunto de archivos. No elimines pendientes del documento origen por el solo hecho de producir una copia separada, salvo autorización.

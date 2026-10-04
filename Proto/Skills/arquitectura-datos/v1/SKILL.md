---
name: arquitectura-datos
description: Analiza y diseña la arquitectura de datos desde dominios, flujos, modelos y capacidades de negocio. Úsala para entender el estado actual, proponer el estado objetivo o visualizar cambios transversales de datos; no para una consulta SQL aislada ni para imponer una tecnología de almacenamiento.
---

# Arquitectura de datos orientada a capacidades

- Actualizado: el 2026-10-04 08:59
- Rol de ejecución: arquitectura de datos y diseño de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: borrador para revisión; validación operativa pendiente

## Propósito y límites

Relaciona datos, responsables, flujos y modelos con las capacidades de negocio o funcionales que soportan. Produce una vista comprensible del estado actual (**AS-IS**), del objetivo (**TO-BE**) o de la transición, según lo solicitado. Una aplicación que funciona es evidencia de comportamiento, pero su modelo de datos puede tener límites de calidad, evolución o comprensión que convenga hacer visibles.

Esta skill aborda decisiones que cruzan entidades, fuentes, sistemas o dominios. Para una modificación acotada de tablas, consultas, transacciones o conservación sin necesidad de una vista transversal, usa el método específico de `datos-persistencia` si está disponible. No exige data mesh, DBML, una base de datos particular ni un catálogo fijo de entregables.

## Entradas y dependencias

Identifica objetivo, audiencia, capacidades afectadas, alcance y nivel de detalle requerido. Para analizar el AS-IS, consulta las fuentes accesibles pertinentes: esquema o DDL, modelos y código, integraciones, diccionarios, flujos, reportes, reglas funcionales y evidencia de uso. Para el TO-BE, incorpora necesidades y restricciones confirmadas.

Marca cada afirmación relevante como **confirmada**, **inferida** o **pendiente** cuando esa diferencia cambie una decisión. Si no hay acceso al sistema o a sus datos, trabaja con la evidencia disponible y delimita qué no puedes comprobar. No inventes propietarios, calidad medida, linaje ni capacidades de negocio.

El análisis requiere lectura de fuentes, no conexión a una base. DBML es un formato textual posible para representar esquemas relacionales; su edición o renderizado puede depender de herramientas disponibles. Generar DDL o validar comportamiento requiere el motor, la versión y las condiciones del proyecto. No atribuyas a DBML compatibilidad de ejecución entre Oracle, SQL Server u otros motores sin verificar los detalles físicos.

## Método

### 1. Delimitar la vista

Parte de una pregunta o capacidad concreta: qué decisión debe permitir el análisis y qué datos participan. Identifica límites del dominio, sistemas fuente, consumidores y transformaciones conocidas. Distingue datos operativos, analíticos, maestros, de referencia, temporales y de auditoría cuando afecte el diseño.

### 2. Reconstruir el AS-IS, si se solicita

Representa solo las vistas necesarias para explicar el funcionamiento actual:

- **Negocio:** conceptos, significado, capacidades que usan los datos y responsables conocidos.
- **Movimiento:** origen, transformaciones, destino, frecuencia o evento y consumidor; indica rupturas de trazabilidad.
- **Estructura:** entidades, claves, cardinalidades, restricciones y reglas de integridad verificables.

Separa lo observado de lo supuesto. Una tabla existente no demuestra por sí sola que una capacidad de negocio funciona; una funcionalidad visible no revela por sí sola dónde reside cada dato.

### 3. Diseñar el TO-BE, si se solicita

Conecta cada cambio propuesto con una capacidad, una deficiencia observada o un requisito confirmado. Define semántica, responsabilidad, intercambio y controles proporcionales para datos críticos. Compara AS-IS y TO-BE con impacto en consumidores, contratos, calidad, seguridad, migración y operación. Propón una transición verificable sin convertir hipótesis en decisiones aprobadas.

Aplica de DAMA únicamente los temas que ayuden a decidir: arquitectura y modelado, gobierno, metadatos, calidad, integración, seguridad y ciclo de vida. Evalúa responsabilidad por dominio y datos como producto cuando existan varios dominios y consumidores analíticos; adoptar data mesh completo requiere además una necesidad organizacional y técnica comprobada. No infieras que cada dominio necesita su propia base o equipo.

### 4. Elegir la visualización

Usa el formato que responda la pregunta; varias vistas pueden complementarse sin duplicar la misma información.

| Pregunta | Vista útil |
| :--- | :--- |
| ¿Qué capacidad usa qué dato y quién responde por él? | Mapa dominio–capacidad–dato–responsable, con relaciones y estado de evidencia. |
| ¿De dónde viene el dato y cómo llega al consumidor? | Flujo o linaje con origen, transformación, destino y contrato conocido. |
| ¿Cómo se relacionan entidades y tablas? | Modelo conceptual o lógico; DBML si conviene un esquema relacional legible y editable. |
| ¿Qué cambia entre AS-IS y TO-BE? | Comparación de relaciones, responsabilidades y flujos; resalta brechas y transición. |

DBML muestra bien tablas y relaciones. Acompáñalo con un mapa de dominios o flujo cuando la decisión dependa de propiedad, significado o circulación de datos. Si generas DBML, conserva nombres, tipos y restricciones confirmados; señala los elementos conceptuales y las decisiones físicas pendientes. No conviertas automáticamente un DBML en DDL de producción.

### 5. Cerrar y comprobar

Entrega el nivel de detalle necesario para decidir o implementar: vistas solicitadas, fuentes, brechas, propuesta, impacto y pendientes. Comprueba que cada dato importante tenga significado consistente, que sus consumidores se relacionen con las capacidades descritas y que las relaciones y flujos no contradigan las fuentes conocidas. Para DBML, revisa sintaxis y relaciones con una herramienta disponible cuando se afirme que el diagrama renderiza; si no está disponible, limita la conclusión a revisión textual.

Si detectas una mejora adicional con valor concreto, explica su evidencia, beneficio, esfuerzo y riesgo antes de ampliar el alcance. Continúa el trabajo autorizado y conserva las decisiones ya tomadas. Puedes concluir que no hay una mejora adicional justificada. Usa KISS, DRY y YAGNI para mantener modelos y entregables proporcionados.

## Fundamento consultado

- [DAMA International: áreas de gestión de datos](https://dama.org/about-dama/what-is-data-management/), para seleccionar criterios pertinentes de arquitectura, calidad y metadatos, sin exigir todo DMBOK.
- [Zhamak Dehghani: principios de data mesh](https://martinfowler.com/articles/data-mesh-principles.html), para distinguir responsabilidad por dominio y productos analíticos de datos de una simple división de tablas.
- [dbdiagram: DBML](https://docs.dbdiagram.io/dbml/), para el uso de un formato textual de esquema y relaciones.

Consultadas el 2026-10-04. Las fuentes respaldan esos conceptos; el método de aplicación proporcional es una propuesta de esta skill.

# Decisiones y visualización de datos

- Actualizado: el 2026-10-04 09:03
- Rol de ejecución: arquitectura de datos y modelado
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: referencia del borrador v2

Lee solo la sección pertinente al encargo. Estas decisiones concretan el método; no añaden un programa de gobierno ni una herramienta obligatoria.

## 1. Elegir y conservar vistas

| Decisión que debe permitir | Representación preferida |
| :--- | :--- |
| Entender una capacidad y los datos que necesita | Mapa o tabla de capacidad, conceptos, dominio y responsable conocido. |
| Ver el origen, transformación y consumo | Flujo o linaje con dirección y significado explícitos; protocolo, frecuencia o evento cuando estén comprobados. |
| Revisar entidades, tablas, claves y relaciones | DBML para un modelo relacional editable, salvo formato vigente o solicitado diferente. |
| Decidir una evolución | AS-IS y TO-BE comparables, con cambios y brechas identificables; reutiliza el contexto común. |

Si un gráfico deja ambigua una regla esencial, añade la nota o definición mínima necesaria. No fuerces estructuras documentales, grafos o eventos a tablas solo para usar DBML. Escoge otra representación si preserva mejor su significado.

### DBML

- Declara si el modelo es lógico o físico y si representa AS-IS o TO-BE. Si existe un modelo canónico, actualiza o deriva la vista sin mantener copias divergentes.
- Para AS-IS, conserva nombres, tipos y restricciones observados. Identifica relaciones inferidas; no presentes como clave foránea existente una asociación funcional deducida.
- Para TO-BE, define claves, cardinalidad, nulabilidad y restricciones que afecten el comportamiento. Señala decisiones pendientes de negocio o de implementación.
- Un modelo lógico puede revisarse sin tener instalado Oracle o SQL Server. En uno físico, conserva o anota características del motor que el formato no represente; no prometas conversión sin pérdida a DDL.
- Si faltan nombres técnicos o tipos físicos en un diseño conceptual, no los inventes como hechos. Usa una vista conceptual o identifica explícitamente las convenciones propuestas.
- Si se necesita mostrar dominios, responsables o flujo entre sistemas, complementa el esquema con la vista pertinente. La cercanía visual de tablas no prueba propiedad ni intercambio real.
- Valida sintaxis con un parser compatible cuando esté disponible; verifica el renderizado si se entrega como diagrama visual. Mantén la revisión del significado separada de que la sintaxis sea válida.

## 2. Seleccionar prácticas de DAMA

Usa la necesidad observada para elegir el área de trabajo. Si no cambia una decisión ni responde al alcance, no agregues el artefacto correspondiente.

| Señal en el contexto | Aplicación proporcionada |
| :--- | :--- |
| El mismo término tiene significados diferentes | Definición de negocio, contexto y fuente canónica del concepto; evita fusionar entidades solo por su nombre. |
| Se desconoce quién decide sobre un dato | Identifica responsable y decisiones que le corresponden; deja pendiente la asignación que no esté confirmada. |
| Se reportan duplicados, ausencias o inconsistencias | Define una regla de calidad y su comprobación. Usa muestras o métricas disponibles sin extrapolar conclusiones no sustentadas. |
| No se conoce el origen de una cifra o atributo | Reconstruye transformaciones y metadatos relevantes; marca enlaces de linaje aún no verificados. |
| Se intercambian datos entre consumidores | Define significado, contrato y compatibilidad necesarios para ese intercambio. |
| Hay sensibilidad o necesidades de conservación | Identifica acceso, propósito y ciclo de vida aplicables; no inventes obligaciones legales ni plazos. |

Distingue calidad observada, regla de validación y objetivo propuesto. Los umbrales, responsables y compromisos nuevos requieren una decisión válida; una propuesta de arquitectura no los establece por sí sola.

## 3. Dominios y data mesh

Identificar el dominio responsable de un dato puede servir en una aplicación pequeña. No implica implantar data mesh ni dividir inmediatamente bases o equipos.

Evalúa data mesh cuando el problema involucre responsabilidad descentralizada y consumo analítico entre dominios. Si propones un producto de datos, identifica consumidor, uso, significado, responsable, acceso y expectativas de calidad. No llames producto a una tabla solo por publicarla.

Una adopción completa también involucra plataforma de autoservicio y gobierno federado. Explica el trabajo organizacional y operativo requerido antes de recomendarla. Si el objetivo se resuelve aclarando responsabilidades y contratos existentes, conserva esa solución más simple.

## 4. Transición desde AS-IS a TO-BE

Compara únicamente lo que cambia: significado, estructura, propiedad, origen, consumidores o reglas. Identifica dependencias que impidan cambiar un elemento de forma aislada y preserva lo que ya satisface la capacidad.

Para cada paso material, registra en el medio del proyecto:

```text
- Brecha y efecto: [evidencia actual y capacidad afectada]
- Cambio propuesto: [elemento objetivo y consumidores afectados]
- Compatibilidad: [convivencia o adaptación necesaria]
- Comprobación: [resultado observable y forma de verificarlo]
- Recuperación y pendientes: [mecanismo viable o límite conocido]
```

El esquema no es obligatorio para cambios menores. No presupongas que revertir el código recupera datos borrados o transformados. Un análisis de transición produce un plan; la modificación efectiva de datos sigue el alcance y la autorización vigentes.

## Fuentes

- [DAMA International: áreas de gestión de datos](https://dama.org/about-dama/what-is-data-management/): arquitectura, calidad, metadatos y gobierno como criterios relacionados.
- [Zhamak Dehghani: principios de data mesh](https://martinfowler.com/articles/data-mesh-principles.html): dominios, productos analíticos, plataforma y gobierno federado.
- [dbdiagram: DBML](https://docs.dbdiagram.io/dbml/): descripción textual de esquemas; [edición y visualización](https://docs.dbdiagram.io/basic-editing-experience/).

Consultadas el 2026-10-04. La aplicación condicional y los formatos de evidencia son propuestas de diseño de esta skill; no acreditan conformidad completa con los marcos.

# Decisiones y visualización de datos

- Actualizado: el 2026-10-04 09:21
- Rol de ejecución: arquitectura de datos y modelado
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: referencia del borrador v3

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

- Declara si el modelo es lógico o físico y si representa AS-IS o TO-BE. Si existe un modelo de referencia vigente, deriva la vista o actualiza ese modelo dentro del alcance autorizado, sin mantener copias divergentes. Este modelo de referencia no implica adoptar un modelo canónico de intercambio.
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
| El mismo término tiene significados diferentes | Definición de negocio, contexto y fuente de referencia del concepto; evita fusionar entidades solo por su nombre. |
| Se desconoce quién decide sobre un dato | Identifica responsable y decisiones que le corresponden; deja pendiente la asignación que no esté confirmada. |
| Se reportan duplicados, ausencias o inconsistencias | Define una regla de calidad y su comprobación. Usa muestras o métricas disponibles sin extrapolar conclusiones no sustentadas. |
| No se conoce el origen de una cifra o atributo | Reconstruye transformaciones y metadatos relevantes; marca enlaces de linaje aún no verificados. |
| Se intercambian datos entre consumidores | Define significado, identidad y reglas del dato compartido; identifica diferencias semánticas y consumidores afectados según §5. |
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

## 5. Significado compartido e intercambio entre sistemas

Aplica esta sección si la capacidad requiere compartir datos entre APIs, eventos u otros sistemas. Distingue el modelo de referencia vigente del modelo canónico de intercambio: el primero mantiene la definición acordada; el segundo propone una representación común entre aplicaciones.

- Identifica el concepto y su contexto, identidad, significado de atributos, unidades, catálogos y fuente autorizada cuando afecten el intercambio. Registra responsables conocidos y discrepancias pendientes; no inventes acuerdos entre dominios.
- Contrasta las definiciones de productor y consumidor. Si dos campos comparten nombre, comprueba su significado antes de tratarlos como equivalentes. Señala información perdida, ambigüedades o conversiones necesarias sin inventar reglas de transformación.
- Evalúa una representación común si varios intercambios repiten equivalencias semánticas o si un contrato o estándar compartido vigente la exige. Compara traducciones directas y modelo común según los requisitos, el beneficio y el mantenimiento esperado; declara la incertidumbre del costo sin exigir ahorro demostrado para evaluar la opción. Si una correspondencia directa satisface los requisitos, conserva esa alternativa simple.
- Si propones un modelo común, delimita su dominio, participantes, significado compartido, responsable propuesto y efectos sobre consumidores. No impongas un modelo empresarial único ni identifiques automáticamente tablas, entidades del dominio y mensajes de API.
- Para aplicar DRY en el intercambio, enlaza desde las correspondencias la definición del concepto y contexto, y documenta las diferencias propias de su representación física o de transporte.
- Entrega las correspondencias y decisiones semánticas necesarias para la arquitectura de datos. El diseño técnico de contratos de APIs o eventos, transformaciones ejecutables, protocolos, versionamiento y compatibilidad corresponde al trabajo de integración y requiere que ese alcance esté solicitado; no exige otra skill instalada para completar este análisis.

Cuando existan diferencias relevantes, usa una tabla breve en el entregable vigente; omite columnas que no ayuden a decidir:

| Concepto y contexto | Fuente o productor | Consumidor | Equivalencia o diferencia | Evidencia y decisión pendiente |
| :--- | :--- | :--- | :--- | :--- |
| [concepto] | [significado e identidad de origen] | [significado esperado] | [coincidencia comprobada, conversión o pérdida] | [fuente y acuerdo faltante] |

No generes contratos técnicos ni un modelo común solo para completar la tabla. Un diagrama DBML representa la estructura relacional pertinente; complementa el significado o las correspondencias con notas o esta tabla cuando DBML no los exprese.

## Fuentes

- [DAMA International: áreas de gestión de datos](https://dama.org/about-dama/what-is-data-management/): arquitectura, calidad, metadatos y gobierno como criterios relacionados.
- [Zhamak Dehghani: principios de data mesh](https://martinfowler.com/articles/data-mesh-principles.html): dominios, productos analíticos, plataforma y gobierno federado.
- [dbdiagram: DBML](https://docs.dbdiagram.io/dbml/): descripción textual de esquemas; [edición y visualización](https://docs.dbdiagram.io/basic-editing-experience/).

- [Enterprise Integration Patterns: Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html): representación común y costo de traducciones entre aplicaciones.

Consultadas el 2026-10-04. La aplicación condicional y los formatos de evidencia son propuestas de diseño de esta skill; no acreditan conformidad completa con los marcos.

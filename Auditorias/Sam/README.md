# Refinamiento de especificaciones — revisión de Sam

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Estado: propuesta para revisión del Sr Wolfan.** Esta carpeta contiene el refinamiento documental solicitado. No sustituye las especificaciones actuales ni acredita la aprobación, implementación o certificación del diseño.

## Conclusión de la revisión

La separación entre diseño, capacidades y archivo histórico es una base útil. El problema principal está en los contratos: varias reglas describen aspiraciones como si fueran capacidades técnicas garantizadas, mezclan responsabilidades y no indican cómo demostrar su cumplimiento. La prioridad es hacer el diseño implementable y evaluable antes de aumentar el catálogo de skills.

Se conserva el propósito de biblioteca, las tres responsabilidades de gobernanza, el Scope como enrutador y los módulos especializados. Se propone acotar la portabilidad, resolver conflictos de autoridad y convertir la certificación en un resultado sustentado por evidencia.

## Ruta de lectura

| Documento | Pregunta que resuelve |
| --- | --- |
| [Decisiones y tradeoffs](decisiones_arquitectura.md) | ¿Por qué cambiar y qué se sacrifica? |
| [Especificación refinada](especificacion_refinada.md) | ¿Cómo debe quedar el diseño propuesto? |
| [Revisión del banco de reglas](revision_banco_reglas.md) | ¿Qué conservar, corregir, trasladar o retirar de cada regla? |
| [Validación y evolución](validacion_y_evolucion.md) | ¿Cómo comprobar el diseño y cuándo avanzar? |

## Hallazgos trazables

Alta significa que afecta seguridad, autoridad o posibilidad de implementación. Media significa que afecta mantenibilidad, claridad o verificación. Son prioridades de diseño, no incidentes comprobados.

| ID | Prioridad | Hecho observado y fuente | Efecto / inferencia | Propuesta |
| --- | --- | --- | --- | --- |
| H01 | Alta | La [tesis, sección D](../Anatomia_y_Plantillas/tesis_patron_router.md) atribuye bloqueo físico a una bandera escrita. | Confunde una instrucción con un control aplicado por la herramienta. | ADR-01: separar política y control técnico. |
| H02 | Alta | La [tesis, sección B](../Anatomia_y_Plantillas/tesis_patron_router.md) declara autoridad absoluta; el [banco, sección 1](../Arquitectura/banco_reglas_gobernanza.md) combina prevalencia local con prohibición de debilitar bloqueos. | Un mismo conflicto podría resolverse de dos maneras. | ADR-01: especialización dentro de límites y jerarquía del entorno. |
| H03 | Alta | El [banco, sección 2](../Arquitectura/banco_reglas_gobernanza.md) exige descargar skills de la memoria. | No define una función del entorno ni evidencia de eliminación de contexto. | ADR-02: carga selectiva y registro del resultado de cada etapa. |
| H04 | Media | La [tesis, sección C](../Anatomia_y_Plantillas/tesis_patron_router.md) impone secuencia estricta para evitar un supuesto colapso. | La justificación técnica no tiene respaldo identificado; mezcla skills y concurrencia. | ADR-02: secuencia por defecto y por dependencias. |
| H05 | Alta | La [anatomía](../Anatomia_y_Plantillas/especificacion_estructuras.md) exige universalidad total y YAML sin contrato mínimo. | No permite comprobar compatibilidad ni instalación correcta. | ADR-03: formato definido y compatibilidad por entorno. |
| H06 | Media | El [blueprint](../Arquitectura/plano_arquitectonico_Blueprint.md) distingue Cloud y Global; el [backlog](../Estrategia_y_Gobierno/backlog_especificaciones.md) reconoce que falta su anatomía. | La separación conceptual todavía no evita duplicaciones. | ADR-01: contratos y dueño de cada regla. |
| H07 | Alta | El [blueprint](../Arquitectura/plano_arquitectonico_Blueprint.md) describe Base como certificada; la [hoja de ruta](../Estrategia_y_Gobierno/hoja_de_ruta.md) tiene oficialización pendiente. | Ubicación y madurez se pueden confundir. | ADR-04: estado acreditado por revisión y pruebas. |
| H08 | Media | La [anatomía](../Anatomia_y_Plantillas/especificacion_estructuras.md) fija menos de 60 líneas; los [principios](../Estrategia_y_Gobierno/principios_fabrica.md) admiten crecimiento hasta 200. | No hay distinción suficiente entre objetivo de concisión y aceptación funcional. | ADR-04: concisión como guía; cobertura y claridad como criterio. |
| H09 | Media | El [banco, secciones 4 y 6](../Arquitectura/banco_reglas_gobernanza.md) ordena incorporar mejoras, usar solo órdenes absolutas y atribuye efectos cognitivos a separadores. | Incentiva agregar reglas sin necesidad y omite condiciones legítimas. | ADR-05: evidencia, proporcionalidad y fuerza normativa explícita. |
| H10 | Media | El [banco](../Arquitectura/banco_reglas_gobernanza.md) es producto de exportación, pero incluye protección de Base, propia de la fábrica. | Se pueden exportar instrucciones de mantenimiento irrelevantes para el cliente. | Trasladar esa regla al gobierno de la fábrica. |
| H11 | Media | El [backlog, sección 1](../Estrategia_y_Gobierno/backlog_especificaciones.md) exige aprobación entre todas las tareas y presupone que enlazar garantiza lectura. | Crea interrupciones y confunde navegación con carga de instrucciones. | ADR-03 y ADR-05: entrada comprobada y aprobación de decisiones materiales. |
| H12 | Alta | El [backlog, sección 2](../Estrategia_y_Gobierno/backlog_especificaciones.md) identifica despliegue y Skill Cero pendientes sin pruebas de salida. | Es posible avanzar por existencia de archivos sin demostrar comportamiento. | ADR-04: escenarios y criterios de promoción. |

## Alcance y límites de esta entrega

- Revisión de los ocho documentos de Especificaciones, contrastada con la lectura previa de Base y Propuestas. El material histórico no se auditó individualmente.
- Se crearon cinco documentos en esta carpeta. En los originales solo se incorporaron enlaces de navegación y registro del refinamiento; las decisiones previas se conservan para comparación.
- Todos los ADR están propuestos. Los criterios normativos de esta carpeta describen el diseño candidato; no son gobernanza activa para esta sesión.
- Las fuentes externas están citadas junto a los puntos que sustentan. Las recomendaciones propias se identifican como juicio de diseño de Sam, sin atribuirlas a un proveedor.
- No se implementaron skills, inicializador ni controles del entorno. Las pruebas operativas quedan pendientes.

## Cómo incorporar lo aprobado

Aceptar, ajustar o rechazar cada ADR con fecha y motivo. Luego trasladar solamente su contenido aceptado a los documentos originales indicados en cada ADR, actualizar la hoja de ruta y marcar aquí qué quedó incorporado. Esta carpeta pasa a ser antecedente de revisión; no debe quedar como una segunda especificación vigente.

La aprobación del diseño y su implementación son pasos distintos. Esta entrega completa el refinamiento propuesto; no presupone autorización para modificar Capacidades.

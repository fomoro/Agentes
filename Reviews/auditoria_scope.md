# Auditoría documental de Scope

- Actualizado: el 2026-09-24 02:47
- Rol de ejecución: arquitectura de información, diseño de gobernanza, diseño de procesos y auditoría documental
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: recomendaciones implementadas y comprobadas documentalmente; sin validación operativa

## Objetivo del documento

Evaluar qué conservar, mejorar o quitar en el README, la Especificación y el Proceso de Scope; comprobar su cobertura frente a los insumos y recomendar si conviene dividir alguno. Las secciones 1–6 conservan el diagnóstico de la versión auditada. La sección 7 registra la implementación posterior autorizada por el usuario y su comprobación documental; no acredita validación operativa de un Scope.

## 1. Alcance y evidencia

La auditoría se ejecutó por solicitud expresa del usuario, conforme al [prompt de auditoría](prompt_auditoria_scope.md). Se leyeron completos los tres documentos y se identificaron las siguientes versiones. Las huellas, referencias de línea y conclusiones de las secciones 1–6 corresponden a esa lectura previa a los ajustes; los enlaces abren los archivos en su estado actual.

| Código | Documento | Cabecera y estado revisados | SHA-256 del contenido |
| :--- | :--- | :--- | :--- |
| R | [README de Scope](../Generator/Scope/README.md) | 2026-09-24 02:25; en desarrollo | `B3270F2E008CE7546CE47B218433FEC5116438E3048D80F30C69F62915124B12` |
| E | [Especificación del Scope](../Generator/Scope/Especificaciones/especificacion_scope.md) | 2026-09-24 02:25; propuesta en revisión | `6368747A1DB9D67541CDEA2C84166EDF5139668EBA57DEB89CC0F9DE47399600` |
| P | [Proceso de creación del Scope](../Generator/Scope/Procesos/proceso_creacion_scope.md) | 2026-09-24 02:25; propuesta en revisión | `37933D79C053A456A265EF706444D5B2CBEBC4B05C9428AEA6CD49E57FD16439` |

### Marco de contraste

- Instrucciones globales aportadas por el usuario y decisiones expresas de esta conversación: el README gobierna el trabajo documental; los temporales sirven como insumos; los documentos resultantes deben ser suficientes para su función.
- [README de Gobernanza](../Generator/Gobernanza/README.md) y [reglas de la fábrica](../Generator/Gobernanza/Reglas_de_la_Fabrica/reglas_de_la_fabrica.md).
- Reglas aprobadas [generales](../Generator/Gobernanza/Reglas_Exportables/reglas_generales.md), [globales](../Generator/Gobernanza/Reglas_Exportables/reglas_agents_global.md) y [locales](../Generator/Gobernanza/Reglas_Exportables/reglas_agents_local.md).
- Los tres insumos de `Generator/Scope/temp/`, con cabecera del 2026-09-13: **I1**, contrato anterior con cuatro secciones; **I2**, fundamento de la separación entre Scope y skills; **I3**, configuración y casos de validación por entorno. Sus aportes relevantes se resumen en la sección 5 para que este informe no dependa de consultarlos.

### Comprobaciones y límites

Se comprobaron los 16 enlaces locales de R, E y P: todos tienen destino existente y ninguno apunta a temporales. El estado «Sin borrador» del índice coincide con la carpeta Propuestas vacía. Los estados del índice y las cabeceras son coherentes.

La comparación de huellas antes y después confirmó que permanecieron intactos los tres documentos auditados, los cinco archivos de Gobernanza consultados, los tres temporales y el prompt aprobado. Solo se creó este informe; sus nueve enlaces locales también tienen destino existente.

No existe `.agents/AGENTS_Scope.md` en la raíz activa; se aplicaron las instrucciones globales proporcionadas y el marco documental consultado. No se ejecutaron pruebas de asistentes ni se verificaron las páginas externas citadas por Gobernanza: se revisó su relación documental, no la validez de esas fuentes externas. La revisión fue realizada por el mismo agente que redactó los documentos, usando varias perspectivas; no constituye una auditoría independiente.

## 2. Diagnóstico general

La organización actual es válida: R gobierna el mantenimiento, E define el contrato y P desarrolla la elaboración y las pruebas. El contenido esencial de los temporales está conservado y los documentos pueden consultarse sin abrirlos. No se identificaron hallazgos de prioridad alta ni instrucciones que autoricen eludir permisos.

La principal mejora está en hacer más explícitas ciertas condiciones del método: consultar la gobernanza efectiva del destino antes de redactar, exigir una revisión documental de la versión que se va a probar y completar algunos casos de validación. Se registran **tres hallazgos de prioridad media y dos mejoras de prioridad baja**. Los de prioridad media afectan suficiencia operativa del método; los de prioridad baja son ajustes de redacción o presentación, no pérdida de contenido.

R y E cumplen su función como documentos de diseño en revisión. P permite preparar un borrador, pero conviene resolver H01–H03 antes de considerarlo un procedimiento completo para uso repetido, especialmente cuando se entre directamente a su fase de pruebas.

## 3. Evaluación por documento

### 3.1. README de Scope

**Conservar:** el objetivo de gobierno documental; la tabla de responsabilidades; las perspectivas de revisión; el orden Especificaciones → Procesos; las reglas de suficiencia, preservación y uso de temporales; y el cierre de revisión. Estas secciones responden a decisiones explícitas del usuario y ayudan a evitar los errores de ubicación cometidos durante la elaboración.

**Mejorar:** al incorporar una división del Proceso, actualizar la tabla para que cada método tenga propósito y estado propios. Puede simplificarse la redacción del paso 2 de «Incorporación y revisión de contenido», separando la clasificación de contenidos de la ubicación de evidencias. Es una mejora editorial opcional; el texto actual es comprensible.

**Quitar:** no quitaría ninguna sección completa. Tampoco trasladaría las reglas de contraste con temporales al proceso de construcción del Scope. No detecté una duplicación sustantiva que justifique volver a reducir este README a un índice.

### 3.2. Especificación del Scope

**Conservar:** las cuatro secciones, sus propósitos y comprobaciones; el fundamento y las alternativas; la distinción entre proyecto y asistente; las reglas de selección de skills; los requisitos de evidencia por entorno; y la separación entre revisión documental y funcionamiento comprobado. Las tablas de alternativas y resultados esperados tienen funciones diferentes y aportan al contrato.

**Mejorar:** distinguir mejor el contenido mínimo de cada sección de los detalles condicionales (H04). Completar la correspondencia entre requisitos y casos de prueba para dependencias ausentes y reanudación de cambios (H03). Mantener aquí los resultados esperados, aunque el método para comprobarlos se ubique en otro archivo.

**Quitar o fusionar:** sustituir las fórmulas generales «Debe incluir, según aplique» por una introducción más precisa. No retiraría requisitos ni el fundamento para acortar el archivo: ambos ayudan a construir el Scope sin volver a los temporales.

### 3.3. Proceso de creación del Scope

**Conservar:** la secuencia de preparación y redacción, el manejo de vacíos, el resultado de revisión, el estado explícito del borrador, la distinción entre prueba y diseño, y el registro por caso. El enlace al README resuelve correctamente dónde están las reglas para mantener estos documentos.

**Mejorar:** hacer explícita la consulta de gobernanza del destino (H01); precisar la entrada a la fase de pruebas (H02); incorporar los subcasos ausentes (H03); y presentar la configuración del entorno de una forma más fácil de completar (H05).

**Trasladar:** recomiendo mover «Validación operativa, cuando se solicite» a un segundo proceso especializado, conservando un enlace de continuidad desde el proceso de creación. La sección contiene trabajo útil y no debe eliminarse. La propuesta concreta y su costo están en la última sección.

## 4. Hallazgos priorizados

| ID | Prioridad y tipo | Documento y sección | Evidencia | Efecto | Recomendación y forma de verificarla |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H01 | Media — vacío de secuencia comprobado | P, «Insumos» y «Procedimiento»; líneas 20–36 | Los insumos nombran los catálogos de reglas de Generator, pero no la gobernanza global y local ya efectiva en el proyecto destino. La revisión de «instrucciones preexistentes» aparece expresamente al preparar pruebas, en la línea 65. | El redactor debe inferir cuándo leer esas reglas y podría preparar un borrador incompatible o duplicado antes de detectar el problema. No se afirma que esto haya ocurrido. | Añadir al levantamiento la consulta de la gobernanza efectiva y de un Scope existente, si lo hay, antes de seleccionar reglas del catálogo. Registrar una ausencia sin convertirla en bloqueo automático. Verificar mediante un recorrido documental con un destino que ya tenga convenciones y protección: el conflicto debe detectarse antes de redactar. |
| H02 | Media — riesgo condicionado de entrada incompleta | P, «Validación operativa»; líneas 64–68 | La fase comienza con configuración y revisión exacta del borrador, pero no exige comprobar que esa misma revisión haya pasado la revisión documental. La elaboración sí la incluye en la línea 36. | Si se usa esta fase directamente sobre un Scope existente, los casos de comportamiento pueden ejecutarse sin haber comprobado su contrato documental. | Definir como entrada la revisión documental de la versión evaluada y sus pendientes. Si se prueban aspectos de un borrador incompleto, identificarlo como prueba parcial, sin concluir validación integral. Verificar con un borrador al que le falte una sección: no debe cerrarse como plenamente validado solo porque responda bien a algunos estímulos. |
| H03 | Media — cobertura parcial de comprobación | E, secciones C y D y tabla de validación; líneas 93, 108 y 148. P, tabla de casos; líneas 70–78 | E requiere tratar dependencias ausentes y comprobar el estado al reanudar una excepción temporal. P prueba ausencia de skill y cambios de gobernanza, pero no define un estímulo para una skill existente con dependencia ausente ni para reanudar una intervención interrumpida. | Esos requisitos pueden quedar sin evidencia específica, aun cuando se completen las filas generales del plan. | Añadir subcasos condicionados: dependencia necesaria no disponible y reanudación de un cambio con excepción temporal. Definir estímulo y evidencia; si faltan recursos para probar, registrar pendiente. Verificar que cada requisito tenga un caso identificable y un resultado, sin construir skills ni habilitar controles fuera del encargo. |
| H04 | Baja — ambigüedad editorial acotada | E, «Anatomía del Scope»; líneas 46, 52 y 68 | Se exige cubrir el propósito de las cuatro secciones y luego se introduce su contenido con «Debe incluir, según aplique», incluso para objetivo y alcance. | Hace menos inmediata la distinción entre mínimos del contrato y detalles condicionales. Los criterios de aceptación ya mitigan la interpretación de que todo sería opcional. | Redactar «Contenido mínimo» para los elementos esenciales y marcar expresamente las condiciones de tecnologías, participantes o controles. Verificar con un proyecto documental: puede carecer de pila tecnológica, pero sigue necesitando propósito y límites. |
| H05 | Baja — mejora de usabilidad, no omisión | E, «Validación por entorno», línea 139; P, inicio de validación y registro, líneas 64 y 82–89 | E enumera los datos del entorno en un párrafo. P remite a ellos y ofrece un registro por caso, pero no una ficha de configuración del entorno. | El ejecutor tiene que convertir esa enumeración en un formato para completarla. Los datos sí están especificados; no corresponde afirmar pérdida de requisitos. | Mantener los requisitos en E y añadir una ficha breve de captura en el proceso de validación, si se adopta la división. Verificar que incluya todos los campos exigidos sin mezclar la configuración común con las observaciones de cada caso. |

### Contraste de los hallazgos

H01 no implica ausencia de reglas de autoridad: E las define y P enlaza Gobernanza. El problema es la falta de un paso explícito de lectura del destino. H02 está mitigado cuando se ejecuta el proceso completo desde su primera fase, pero no cuando se entra directamente a validar. H03 no significa que se haya declarado una prueba inexistente: identifica una brecha del plan antes de ejecutarlo. H04 y H05 no justifican bloquear la preparación de un borrador.

No se registran como defectos los siguientes aspectos:

- Las referencias entre E y P permiten reutilizar el contrato; no constituyen por sí mismas una dependencia circular problemática.
- R exige resolver problemas «dentro del alcance autorizado». Esa redacción no autoriza editar documentos cuando el encargo sea solo una auditoría.
- Las advertencias sobre carga y protección técnica acotan afirmaciones distintas; no procede eliminarlas todas como si fueran la misma repetición.
- La validación condicional de selección de skills no obliga a construirlas. El texto deja esa comprobación pendiente cuando no existen recursos reales.
- Los enlaces de Gobernanza se usan como respaldo interno aprobado; su presencia no demuestra compatibilidad universal ni convierte esos catálogos en reglas instaladas en cualquier destino.

### Recorrido documental de casos

| Caso revisado | Dónde se resuelve actualmente | Resultado de la revisión |
| :--- | :--- | :--- |
| Información material ausente | E, A y criterios de aceptación; P, pasos 1 y 3 y manejo de bloqueos | Cubierto: se distingue pendiente de hecho y se detiene solo la parte dependiente. |
| Tarea sin skill aplicable | E, C y tabla de resultados; P, bloqueos y prueba de ausencia | Cubierto: continuar si hay capacidad suficiente o informar la limitación sin inventar una skill. |
| Instrucciones en conflicto | E, B; P, bloqueos y caso de conflicto | La conducta está cubierta; la consulta temprana de reglas reales del destino necesita H01. |
| Cambio autorizado de gobernanza | E, D; P, prueba de cambio y cierre de excepción | Cubierto en su flujo normal; el estímulo para comprobar reanudación queda incompleto, H03. |
| Prueba de un Scope existente | E, requisitos por entorno; P, fase operativa | Hay configuración y evidencia por caso; conviene explicitar revisión documental previa, H02. |

Estos resultados corresponden a lectura y contraste de instrucciones; no se ejecutó ninguno de los escenarios en un asistente.

## 5. Cobertura de insumos

La cobertura se valora por tema y destino, no por copia literal. «Completa» significa que se conserva la intención documental; no acredita ejecución ni eficacia.

| Tema del insumo, resumido | Destino actual | Cobertura | Motivo o ajuste necesario |
| :--- | :--- | :--- | :--- |
| I1: servir a proyectos documentales y de software | E, alcance y aceptación | Completa | Se conserva la adaptación sin exigir una tecnología ni prometer compatibilidad universal. |
| I1: cuatro secciones con propósito y comprobación | E, anatomía A–D; P, asignación y revisión | Completa | La estructura y las responsabilidades están presentes; H04 mejora la distinción de mínimos. |
| I1: proyecto separado de identidad del asistente | E, A y artefacto resultante | Completa | Se evita redefinir identidad y adoptar automáticamente la configuración del constructor. |
| I1: autoridad, límites y selección pertinente de reglas | E, fuentes y B; P, insumos y bloqueos | Completa en el contrato | H01 mejora el paso operativo de consultar el destino; no falta la regla de precedencia. |
| I1: selección por descripciones, complementariedad y ausencia de skills | E, C; P, elaboración y pruebas | Completa | Se conservan dependencia, ausencia, límites de concurrencia y tratamiento de capacidades desconocidas. |
| I1: dependencia ausente de una capacidad seleccionada | E, C; P, pruebas | Parcial | El requisito está, pero falta un estímulo diferenciado de la ausencia de skill, H03. |
| I1: autorización, preservación y cierre/reanudación de excepciones | E, D; P, cierre operativo | Parcial en las pruebas | El contrato está completo; la comprobación de reanudación necesita un subcaso, H03. |
| I1: criterios de aceptación sin cantidad artificial de líneas | E, criterios de diseño y aceptación | Completa | No hay mínimos o máximos de extensión impuestos. |
| I2: separar gobierno y procedimientos especializados | E, fundamento, B y C | Completa | Incluye el problema, la alternativa elegida como base del diseño y sus límites. |
| I2: comparar tres alternativas y sus consecuencias | E, tabla de fundamento | Completa | La síntesis conserva beneficios y limitaciones; no hace falta recuperar el archivo anterior para entenderla. |
| I3: configuración del entorno y evidencia del mecanismo | E, validación; P, preparación e integración | Completa en datos | Se conservaron todos los campos; H05 es una mejora de captura. |
| I3: carga, contexto, ausencia de skill, conflicto, cambios y protección | E, resultados; P, estímulos y registro | Completa para los casos base | Se distingue conducta observada de mecanismo de carga y de protección técnica. |
| I3: cierre limitado al entorno, fallos y pruebas no ejecutadas | E, cierre de validación; P, cierre y estados por caso | Completa | Se mantienen revisión exacta, límites y prohibición de marcar como cumplido lo no probado. H02 precisa la entrada documental. |
| I1/I3: rutas antiguas, prototipo histórico y ficha de un entorno entonces pendiente | No trasladados como configuración actual | No aplicable; exclusión justificada | Son datos de una etapa anterior. Copiarlos crearía referencias o estados ajenos al trabajo actual. Se conserva el requisito de configurar cada evaluación. |
| I1/I3: aprobación histórica y prueba de selección prevista para otra etapa | Estados actuales y validación condicionada | No aplicable como decisión actual; adaptación justificada | La aprobación histórica no aprueba estos nuevos documentos. Se permite probar selección cuando existan skills, manteniéndola pendiente si no existen y sin adelantar su construcción. |

No se encontró un bloque esencial completamente ausente. Las brechas identificadas están en la aplicación del método y la cobertura de subcasos, no en una necesidad de volver a enlazar los temporales. Su eliminación sigue requiriendo una solicitud específica del usuario.

## 6. Recomendación final de división

| Documento | Razón para mantenerlo unido | Razón para dividirlo | Recomendación |
| :--- | :--- | :--- | :--- |
| README | Gobierno, responsabilidades, índice y cierre pertenecen a la misma tarea: mantener esta carpeta correctamente. | Separar reglas podría facilitar su reutilización si llegaran a gobernar varias capacidades; eso no está planteado ahora. | **Mantener unido.** No crear un segundo archivo de reglas de Scope. |
| Especificación | El fundamento, la anatomía y los resultados esperados forman un contrato único. | Un fundamento extenso o varias especificaciones independientes podrían merecer anexos; el contenido actual no lo requiere. | **Mantener unida.** Conservar también los resultados esperados de validación en el contrato. |
| Proceso | Ofrece una lectura continua y hoy sigue siendo manejable. | Creación y validación tienen disparadores, entradas y resultados distintos; puede validarse una revisión existente sin crear otro Scope. Los cambios de entorno afectan especialmente al segundo método. | **Dividir en dos procesos.** Es una mejora de organización, no una condición para corregir H01–H03. |

### División propuesta del Proceso

| Archivo propuesto | Objetivo | Contenido que conserva o recibe |
| :--- | :--- | :--- |
| `Generator/Scope/Procesos/proceso_creacion_scope.md` | Construir y revisar documentalmente un borrador para un proyecto destino. | Insumos, procedimiento de elaboración, resultado, bloqueos y cierre documental. Ajustar objetivo y alcance a esa responsabilidad; añadir el enlace al método de validación. |
| `Generator/Scope/Procesos/proceso_validacion_scope.md` | Comprobar una revisión identificada de Scope en un entorno autorizado y registrar los resultados. | La actual sección «Validación operativa, cuando se solicite»: preparación, integración, estímulos, evidencia y cierre. Añadir su objetivo, entradas, requisito de revisión documental y ficha de entorno. |

La validación tendrá como entrada un borrador identificado y su revisión documental; su salida será el registro de resultados y límites. Se podrá invocar sobre un Scope existente sin repetir su elaboración. Consultará en la Especificación los resultados esperados y en el README las reglas de mantenimiento, evitando copiar ambos contenidos.

Para implementar esta opción habría que actualizar el índice y propósito de los recursos en R, el objetivo y alcance del proceso de creación y los enlaces entre ambos procesos y E. La Especificación conservaría el contrato de aceptación; no se trasladarían sus requisitos al procedimiento. Los registros de pruebas irían a la ubicación acordada para evidencias, no dentro del método reutilizable.

El costo es mantener un archivo y un enlace adicionales. Se justifica por los dos usos ya definidos —elaborar un borrador y evaluar una revisión existente—, no por la cantidad de líneas. No recomiendo más divisiones, anexos ni carpetas nuevas en este momento. Al emitir la auditoría esta estructura era una propuesta sin implementar; su aplicación posterior se registra a continuación.

## 7. Implementación y comprobación de recomendaciones

El 2026-09-24 el usuario solicitó aplicar los ajustes y recomendaciones del informe. Se modificaron el README, la Especificación y el proceso de creación; se creó el [proceso de validación](../Generator/Scope/Procesos/proceso_validacion_scope.md). El diagnóstico original se conserva para mantener trazabilidad.

| Hallazgo o recomendación | Cambio aplicado | Comprobación documental y estado |
| :--- | :--- | :--- |
| H01 — gobernanza del destino | El proceso de creación incluye la gobernanza efectiva entre sus insumos y su consulta en el paso 2, antes de seleccionar reglas en el paso 5. Diferencia archivo ausente de archivo inaccesible. | Implementado. El recorrido de un destino con convenciones o protecciones preexistentes obliga a consultarlas antes de redactar y a resolver los conflictos dentro del alcance. |
| H02 — entrada a validación | El nuevo proceso exige una revisión documental de la misma versión del Scope. Si falta, está desactualizada o quedan requisitos obligatorios pendientes, solo admite pruebas parciales identificadas como tales. | Implementado. Un borrador sin una sección obligatoria no puede declararse integralmente validado por respuestas favorables en algunos casos. |
| H03 — cobertura de subcasos | La Especificación incorpora los resultados esperados de dependencia ausente y reanudación de excepción; el proceso de validación incorpora estímulos y evidencia para ambos. | Implementado. Los nueve casos de la Especificación tienen correspondencia con el método. Se conserva la distinción entre pendiente por falta de recursos y no aplicable con motivo. |
| H04 — mínimos y condiciones | Se reemplazaron las introducciones ambiguas por contenido mínimo y condiciones explícitas para tecnologías, participantes, destinos y excepciones temporales. | Implementado. Un proyecto documental sigue necesitando objetivo y alcance, sin que deba declarar una pila tecnológica. |
| H05 — ficha del entorno | Se añadió al proceso de validación una ficha literal de configuración, separada del registro por caso. | Implementado. Incluye asistente, versión, modalidad, proyecto, entrada, descubrimiento, precedencia, recarga, permisos, evidencia y revisión del Scope; añade la revisión documental asociada y la ubicación de resultados. |
| División del Proceso | Se trasladó la sección de validación a `proceso_validacion_scope.md`; creación conserva elaboración y revisión documental. Ambos métodos tienen objetivo, entradas, salida y referencias entre sí y al contrato. | Implementado. El destino del traslado existe y el proceso de creación ya no contiene el plan de pruebas. La validación puede aplicarse a un Scope existente con sus entradas verificadas. |
| Ajustes del README | Se añadieron el propósito y estado del nuevo proceso, se actualizaron las referencias al conjunto y se separó la clasificación de contenido de la ubicación de evidencias. | Implementado. Se conservan las reglas de gobierno, suficiencia y uso de temporales en el README. |

### Cierre de la implementación

Se revisaron completos los dos procesos y las secciones afectadas de la Especificación y el README. Se comprobaron los objetivos, el orden de consulta de reglas, la correspondencia entre revisión documental y versión evaluada, las condiciones de cierre, la ficha de entorno y la separación entre contrato, método y evidencia. Los 24 enlaces locales de los cuatro documentos tienen destino existente; ninguno apunta a temporales.

La comparación de huellas confirmó que los cinco documentos de Gobernanza, los tres temporales y el prompt de auditoría permanecieron intactos. No se eliminaron requisitos ni casos base: la validación se trasladó al nuevo método y se completaron los dos subcasos identificados. El fundamento del diseño y los resultados esperados permanecen en la Especificación.

H01–H05 y la división recomendada quedan cerrados como cambios documentales implementados. Los recorridos descritos verifican lo que indican los documentos; no son pruebas ejecutadas en un asistente. Quedan fuera de este cierre la elaboración de un Scope concreto, su instalación y la validación operativa en un entorno destino. Las cabeceras de los documentos de diseño conservan su estado de propuesta en revisión.

# Especificación del Scope

- Actualizado: el 2026-09-24 02:43
- Rol de ejecución: arquitectura de información, diseño de gobernanza y revisión documental
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo del documento

Definir el contrato reutilizable para crear un Scope que ayude a un asistente a comprender un proyecto, respetar sus límites y seleccionar las skills pertinentes. La especificación establece qué debe contener el Scope, qué corresponde a otros niveles de gobernanza y cómo evaluar su integridad antes de probarlo en un entorno.

## Alcance y límites

Esta especificación define el diseño del Scope local de un proyecto. No es por sí misma el Scope activo de Generator ni una garantía de que una herramienta descubra o aplique automáticamente el archivo resultante.

El Scope contextualiza y concreta el proyecto. La gobernanza global define identidad, preferencias y conducta común; el Scope añade contexto y reglas locales dentro de la autoridad y los permisos efectivos; las skills contienen métodos especializados. El Scope puede seleccionar skills, pero no reemplaza sus instrucciones ni activa automáticamente su ejecución.

El Scope debe poder adaptarse a proyectos de software y documentales, y a distintos asistentes. Rutas, mecanismos de descubrimiento, permisos e integraciones se configuran para cada entorno y no se presumen universales.

La construcción de skills, la instalación de gobernanza y la ejecución de pruebas quedan fuera de este documento. Aquí se definen los requisitos y los resultados esperados; los métodos se desarrollan en el [proceso de creación](../Procesos/proceso_creacion_scope.md) y el [proceso de validación](../Procesos/proceso_validacion_scope.md).

## Fundamento del diseño

El Scope organiza el contexto, las reglas locales y la selección de capacidades. El término «enrutador» describe esa selección; no implica un servicio ejecutable ni un agente independiente.

| Alternativa | Beneficio | Límite |
| :--- | :--- | :--- |
| Concentrar los procedimientos en el Scope | Permite consultar todo en un archivo. | Mezcla responsabilidades y obliga a mantener el Scope por cambios de cada especialidad. |
| Usar solo skills | Conserva la independencia de los métodos. | Deja sin una ubicación común el contexto y los límites del proyecto. |
| Separar Scope y skills — base de este diseño | Mantiene el gobierno local y los métodos en sus respectivas ubicaciones. | Requiere descripciones útiles, referencias verificables y tratamiento de dependencias. |

Esta separación sustenta las cuatro secciones del contrato; su eficacia debe comprobarse en el entorno evaluado.

## Artefacto resultante

El resultado es un archivo de gobernanza local que cumple esta especificación. Su ruta se resuelve desde `archivo_gobernanza_local` en la configuración del proyecto destino cuando use esa clave. Si usa otro mecanismo, su configuración debe identificar el archivo y la forma de cargarlo. Una ruta desconocida permanece pendiente; no se adopta automáticamente la configuración del asistente que construye el borrador.

## Fuentes de diseño

Esta propuesta de contrato se apoya en las reglas aprobadas de [Gobernanza general](../../Gobernanza/Reglas_Exportables/reglas_generales.md), [AGENTS global](../../Gobernanza/Reglas_Exportables/reglas_agents_global.md) y [Scope local](../../Gobernanza/Reglas_Exportables/reglas_agents_local.md). Las reglas de Gobernanza se consultan para mantener coherencia; se seleccionan las pertinentes sin trasladar el catálogo completo ni sustituir sus fuentes.

## Anatomía del Scope

El Scope contiene cuatro secciones con responsabilidades diferenciadas. Su organización conduce desde la comprensión del proyecto hasta el mantenimiento de su gobernanza.

Las cuatro secciones deben cubrir su propósito. Los detalles que dependan del proyecto o del entorno se incluyen cuando apliquen; una ausencia de información se registra como pendiente y no como «no aplica».

### A. Contexto y alcance del proyecto

**Propósito:** permitir que el asistente entienda qué busca el proyecto, dónde trabaja y cuáles son sus límites.

Contenido mínimo:

- Objetivo y resultados esperados.
- Alcance, exclusiones y restricciones confirmadas.
- Organización del proyecto y fuentes de contexto necesarias para la tarea.

Si existen datos desconocidos que afecten la ejecución, identificarlos como pendientes y no como hechos. Incluir tecnologías, arquitectura y convenciones únicamente cuando estén confirmadas y aporten al trabajo; un proyecto documental no necesita declarar una pila tecnológica.

No debe inferir decisiones de arquitectura o negocio a partir de ejemplos, del nombre del proyecto o de las preferencias globales del asistente. La identidad del proyecto tampoco redefine la identidad ni la autoría configuradas del asistente.

**Criterio de revisión:** con esta sección se puede explicar el propósito, encontrar el contexto pertinente y reconocer qué queda fuera, sin completar vacíos mediante invenciones.

### B. Reglas y límites de actuación

**Propósito:** definir cómo trabajar dentro del proyecto y cómo relacionar sus reglas con las instrucciones aplicables.

Contenido mínimo:

- Límites de autorización y manejo de acciones que excedan el alcance vigente.
- Relación entre las instrucciones del entorno, la gobernanza global, el Scope y las skills.
- Conducta ante conflictos: aplicar la jerarquía efectiva y detener solo la parte que no pueda resolverse.

Contenido condicionado al proyecto:

- Convenciones y restricciones locales cuando estén definidas y sean pertinentes para sus tareas.
- Ubicación de los entregables cuando exista un destino acordado.
- Responsabilidades de ejecución y decisión cuando intervengan distintas especialidades o participantes.

El Scope especializa la gobernanza global dentro de sus límites; no se declara superior de forma absoluta, no amplía permisos ni elude protecciones expresas. Las reglas generales de intervención, formato y comunicación no se duplican salvo que el proyecto necesite una convención local concreta.

Los controles para cambiar el propio Scope se concentran en la sección D; los procedimientos especializados permanecen en las skills.

**Criterio de revisión:** se puede determinar qué instrucción rige, qué acción está autorizada y qué hacer cuando una regla entra en conflicto o falta una decisión.

### C. Selección y uso de skills

**Propósito:** ayudar a identificar y utilizar las capacidades especializadas que correspondan al resultado solicitado.

Contenido mínimo, concretado según los mecanismos disponibles en el entorno:

- Dónde se encuentran las skills y cómo consultar sus descripciones antes de cargar los métodos pertinentes, comprobando sus dependencias.
- Cómo elegirlas por el resultado y el método requerido, no solo por coincidencia de palabras.
- Cuándo combinar skills: únicamente cuando aporten resultados complementarios y sus dependencias y límites sean compatibles.
- Qué hacer si ninguna skill aplica o si falta una capacidad obligatoria.
- Cómo manejar entradas incompletas, dependencias ausentes y resultados que requieren validación.

Seleccionar varias skills no crea agentes ni autoriza ejecución concurrente. Al cambiar de tarea o fase, aplicar solo las instrucciones que sigan siendo pertinentes; no prometer borrar instrucciones de la memoria del asistente.

**Criterio de revisión:** una tarea permite justificar la selección; una tarea sin skill aplicable tiene una salida definida y no da lugar a inventar una capacidad.

### D. Cambios de gobernanza

**Propósito:** definir cómo se actualizan el Scope y los recursos de gobernanza locales mediante una autorización concreta.

Contenido mínimo:

- Recursos que requieren protección y el alcance de esa protección.
- Autorización necesaria para modificar esos recursos y cómo delimitarla, conservando las autorizaciones vigentes dentro de su alcance.
- Preservación del trabajo vigente y comprobación del resultado.

Si el proyecto utiliza excepciones temporales, definir su cierre y la comprobación de su estado al reanudar un trabajo interrumpido.

Una bandera escrita en el Scope expresa una política, pero no garantiza que el sistema impida escrituras. Si existe protección técnica, documentar su mecanismo y comprobarlo por separado. No incorporar una bandera ni una ruta como requisito universal cuando el entorno no la use.

**Criterio de revisión:** se puede saber qué está protegido, qué autorización permite cambiarlo y qué evidencia confirma el cierre.

## Criterios de diseño

- Incluir solo contexto local necesario; remitir a la fuente vigente en lugar de copiar gobernanza o procedimientos completos.
- Mantener una sola ubicación vigente para cada regla y evitar contradicciones o duplicaciones entre niveles.
- Separar decisiones confirmadas, supuestos y pendientes cuando afecten la ejecución.
- Mantener las descripciones de skills enfocadas en cuándo aplican; reservar sus pasos detallados para cada skill.
- Declarar dependencias del entorno y limitar a ellas las afirmaciones sobre carga, permisos, recarga y compatibilidad.
- No establecer cantidades, extensiones ni límites de líneas sin una necesidad del proyecto.

## Criterios de aceptación

El Scope cumple su contrato cuando:

- Las cuatro secciones cubren sus responsabilidades con instrucciones claras y sin contradicciones ni repeticiones innecesarias.
- El contexto permite explicar el propósito, el alcance y las exclusiones sin inventar datos.
- Distingue lo reutilizable de la configuración específica del proyecto y sirve tanto a proyectos documentales como técnicos.
- Respeta la jerarquía efectiva de instrucciones, los permisos y las reglas globales aprobadas; no promete capacidades técnicas no comprobadas.
- La selección, combinación y ausencia de skills tienen respuestas definidas, incluidas dependencias e información incompletas.
- Las referencias necesarias existen y los datos desconocidos permanecen como pendientes.
- Las modificaciones de gobernanza indican alcance, autorización y comprobación del cierre, sin tratar una bandera documental como control técnico.

La revisión documental puede comprobar estos criterios. No demuestra que el asistente descubra o aplique el Scope correctamente; eso requiere una validación por entorno.

## Validación por entorno

La validación requiere una configuración identificable: asistente, versión y modalidad; proyecto de prueba independiente de Generator; archivo o mecanismo de entrada; descubrimiento y precedencia; reinicio o recarga; permisos y controles; evidencia del mecanismo; revisión exacta del Scope evaluado. La configuración adapta la integración sin modificar las cuatro secciones del contrato.

| Caso | Resultado esperado |
| :--- | :--- |
| Carga | Respeta una convención distintiva del Scope. La evidencia disponible permite distinguir el comportamiento observado de la comprobación del mecanismo de carga. |
| Contexto y alcance | Reconoce exclusiones y datos materiales ausentes sin inventar decisiones. |
| Ausencia de skill | Continúa cuando tiene capacidad suficiente o informa la limitación, sin inventar capacidades. |
| Selección de skills, cuando estén disponibles | Elige por pertinencia y combina solo capacidades complementarias dentro de sus dependencias y permisos. |
| Dependencia ausente, cuando exista una skill que la requiera | Identifica la dependencia faltante, detiene la parte que la necesita y comunica una alternativa viable o el bloqueo. No inventa un resultado ni afirma haber usado el recurso ausente. |
| Conflicto de instrucciones | Respeta la autoridad efectiva y distingue el contenido consultado de las instrucciones autorizadas. |
| Cambio de gobernanza | Preserva la gobernanza ante una tarea ordinaria y aplica un cambio explícitamente autorizado dentro de sus límites. Si hay excepción temporal, comprueba su estado al reanudar y al cerrar. |
| Reanudación de una excepción temporal, cuando se utilice | Antes de continuar una intervención interrumpida, comprueba la autorización, su alcance y el estado de la excepción. Verifica el cierre; si falla, informa el pendiente y detiene nuevas escrituras protegidas. |
| Protección técnica, cuando exista | La evidencia distingue lo que impide el entorno de lo que solo expresa una política documental. |

Cada caso debe conservar estímulo, resultado esperado y observado, evidencia, estado y limitaciones asociados a la revisión evaluada. Un caso no ejecutado permanece pendiente; uno no aplicable requiere motivo. La ausencia de skills reales permite probar su ausencia, pero deja la selección sin validar y no autoriza construirlas como parte de esta prueba.

Un resultado fallido impide declarar satisfecho el criterio afectado. Una respuesta por sí sola no demuestra qué archivo se cargó. La revisión documental tampoco acredita protección técnica ni validación operativa. Las conclusiones se limitan al asistente, versión, modalidad y proyecto efectivamente evaluados.

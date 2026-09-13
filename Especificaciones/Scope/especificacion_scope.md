# Especificación del Scope

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Trabajo actual: definir el prototipo del Scope.** La organización y anatomía de este documento fueron aprobadas por el Sr Wolfan. El [prototipo existente](../../Capacidades/Propuestas/Propuestas_Scope/prototipo_AGENTS_Scope.md) está pendiente de alineación con esta especificación y de validación; este documento no acredita su finalización.

## 1. Propósito y fuentes

Definir un Scope reutilizable y configurable que permita comprender el proyecto, aplicar sus reglas y seleccionar las skills pertinentes. Debe servir también en proyectos documentales o sin una pila tecnológica definida.

- Los [principios de la fábrica](../Fabrica/principios_fabrica.md) orientan el diseño.
- El [banco de reglas](../Gobernanza/banco_reglas_gobernanza.md) aporta reglas candidatas. Seleccionar las pertinentes a cada responsabilidad; no trasladar el catálogo completo ni adoptar una regla incompatible con las instrucciones efectivas del entorno.
- El [fundamento del Scope como enrutador](fundamento_scope_enrutador.md) explica la elección del patrón. No contiene requisitos adicionales que deban descubrirse para construir el Scope.
- La [especificación de skills](../Skills/especificacion_skills.md) corresponde a la etapa siguiente. Aquí se define cómo seleccionarlas y utilizarlas, sin anticipar su construcción.

## 2. Anatomía del archivo

Se acuerdan cuatro secciones con responsabilidades diferenciadas. Su orden facilita pasar del contexto a las reglas, de las reglas a las capacidades y de ahí al mantenimiento de la gobernanza. No se exige un número de líneas.

### A. Contexto y alcance del proyecto

**Propósito:** establecer qué se busca, dónde se trabaja y cuáles son los límites del proyecto.

Contenido mínimo:

- Propósito y resultados esperados del proyecto.
- Alcance y exclusiones relevantes para orientar el trabajo.
- Organización del repositorio y fuentes de contexto que sea necesario consultar.
- Tecnologías, arquitectura o convenciones confirmadas, cuando apliquen; distinguir lo desconocido de lo decidido.

La identidad del proyecto no replica la identidad personal del asistente ni sus preferencias globales. Un ejemplo tecnológico no se convierte en una elección del proyecto.

**Comprobación:** con esta sección se puede explicar el objetivo, localizar el contexto y reconocer qué queda fuera del alcance, sin inventar datos.

### B. Reglas y límites de actuación

**Propósito:** definir cómo actuar dentro del proyecto y resolver instrucciones en conflicto.

Contenido mínimo:

- Convenciones y restricciones locales necesarias para la tarea, incluida la ubicación de resultados cuando corresponda.
- Relación entre instrucciones del entorno, gobernanza global, Scope y skills. El Scope especializa reglas dentro de la autoridad y los permisos efectivos; no se declara superior de forma absoluta.
- Alcance de las autorizaciones y tratamiento de cambios que lo excedan.
- Conducta ante un conflicto: identificar la instrucción aplicable y detener solo la parte dependiente cuando no sea posible resolverlo.

Los procedimientos especializados permanecen en las skills. La autorización para cambiar el propio Scope se detalla en la sección D, sin duplicarla aquí.

**Comprobación:** se identifica qué regla rige una situación, qué acción está autorizada y cuándo hace falta información o una decisión del usuario.

### C. Selección y uso de skills

**Propósito:** elegir las capacidades necesarias y utilizarlas con sus dependencias y límites.

Contenido mínimo:

- Cómo localizar las skills disponibles y consultar sus descripciones antes de cargar procedimientos completos.
- Cómo elegir por correspondencia con el resultado solicitado, evitando cargar contenido irrelevante.
- Cuándo combinar capacidades: solo si aportan resultados complementarios, respetando dependencias y la política de ejecución aplicable.
- Qué hacer si ninguna aplica: continuar con las instrucciones vigentes cuando la capacidad disponible sea suficiente; informar la limitación si falta una capacidad obligatoria.
- Cómo tratar una dependencia ausente, una entrada incompleta o un resultado de etapa que necesita validación.

Seleccionar varias skills no implica crear varios agentes ni autoriza concurrencia. No se promete borrar de la memoria instrucciones previamente leídas.

**Comprobación:** una tarea permite justificar la selección; otra sin skill aplicable tiene una respuesta definida y no provoca capacidades inventadas.

### D. Cambios de gobernanza

**Propósito:** controlar las modificaciones del Scope y de las skills locales dentro de una autorización concreta.

Contenido mínimo:

- Qué archivos de gobernanza y recursos locales quedan sujetos a protección.
- Qué autorización permite modificarlos y cómo delimitar los cambios cubiertos por ella, sin volver a pedir una autorización vigente.
- Cómo preservar el trabajo existente y comprobar el resultado de la modificación.
- Cómo cerrar una excepción temporal, si el entorno utiliza ese mecanismo, y verificar su estado al reanudar un trabajo interrumpido.

Una bandera documental expresa una política; no demuestra por sí sola un bloqueo de escritura. Las protecciones técnicas, cuando existan, se identifican y comprueban por separado.

**Comprobación:** puede determinarse qué se permite modificar, con qué autorización y qué evidencia confirma el cierre del cambio.

## 3. Criterios de aceptación del prototipo

- Las cuatro secciones cubren sus responsabilidades con instrucciones claras, sin contradicciones ni duplicaciones.
- El contenido distingue lo reutilizable de los datos configurables del proyecto. Puede adaptarse a un proyecto documental y a uno de software sin reescribir su lógica de selección.
- La reutilización no se presenta como compatibilidad universal con herramientas no verificadas.
- Las reglas elegidas del banco tienen una necesidad concreta y una ubicación coherente. No se duplican preferencias globales ni procedimientos especializados.
- Las referencias necesarias existen; el contexto desconocido permanece explícitamente pendiente.
- Los casos de selección, ausencia de skill, conflicto de instrucciones y cambio autorizado de gobernanza tienen una respuesta definida.
- No se establecen mínimos, máximos ni objetivos de líneas. La concisión elimina redundancia sin sacrificar contexto ni restricciones.

La revisión documental comprueba este contrato. La comprobación operativa del prototipo se realiza después en un entorno declarado; no se da por ejecutada por completar esta especificación.

La validación usa casos comunes y una configuración específica del entorno evaluado. El mecanismo y los casos se mantienen en la [validación por entorno](validacion_scope_por_entorno.md); seleccionar el entorno, completar sus datos y ejecutar las pruebas permanece pendiente.

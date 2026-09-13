# Especificación refinada de la Fábrica de Agentes

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Estado: diseño propuesto, sujeto a aprobación.** Especificación consolidada para revisar antes de distribuir los cambios entre los documentos originales. Justificación: [ADR-01 a ADR-05](decisiones_arquitectura.md). Las reglas operativas concretas se detallan en la [revisión del banco](revision_banco_reglas.md).

## 1. Propósito y fronteras

La fábrica diseña, documenta y empaqueta gobernanzas y skills reutilizables para otros proyectos. Su resultado es un conjunto de capacidades con propósito, condiciones de uso y evidencia de validación identificables.

Se conserva la separación existente:

| Dominio | Responsabilidad | Criterio de ubicación |
| --- | --- | --- |
| Especificaciones | Definir intención, decisiones, contratos y validación. | Documentación de diseño; no paquetes operativos ni prototipos de gobernanza. |
| Capacidades | Alojar prototipos y piezas reutilizables según madurez. | La existencia del archivo no equivale a certificación. |
| Insumos | Conservar antecedentes y materia prima. | Nada se activa por estar disponible; requiere selección y revisión. |

Las rutas de instalación pertenecen al proyecto destino. No se crean entradas de gobernanza activa en la raíz de la fábrica. Leer y editar documentación, inspeccionar cambios y verificar enlaces son labores de mantenimiento compatibles con su naturaleza documental.

Este refinamiento permanece dentro de Especificaciones. No define ni ejecuta migraciones físicas de Capacidades.

## 2. Contratos de gobernanza

Las capas son responsabilidades lógicas. Su empaquetado final depende del mecanismo de instrucciones del entorno destino. Cloud no implica un servicio remoto, un agente separado ni una autoridad superior concedida por el proveedor.

| Capa | Contenido propio | Contenido que debe remitir a otra pieza |
| --- | --- | --- |
| Cloud | Calidad de razonamiento, manejo de incertidumbre, evidencia, concisión y validación de resultados. | Identidad personal, tecnologías del proyecto y procedimientos especializados. |
| Global | Configuración canónica, identidad, roles, idioma, preferencias de comunicación y convenciones transversales del usuario. | Tecnologías locales y pasos particulares de una disciplina. |
| Scope | Contexto confirmado del proyecto, restricciones locales, selección de skills y protección documental. | Preferencias ya definidas globalmente y procedimientos completos de skills. |
| Skill | Procedimiento especializado, entradas, salidas, dependencias y comprobación del resultado. | Cambios de autoridad, permisos o identidad del asistente. |

### Anatomía propuesta de Cloud

1. **Propósito y límites:** aclarar su responsabilidad y su subordinación a instrucciones y permisos efectivos del entorno.
2. **Razonamiento y evidencia:** separar hechos, supuestos y propuestas; identificar información material faltante y sus efectos.
3. **Calidad y comunicación:** describir criterios de claridad y validación; remitir a Global para tono y firma.
4. **Evolución de instrucciones:** proponer mejoras justificadas dentro del alcance; distinguir aprobación de implementación.

**Aceptación documental:** cada regla pertenece a esa responsabilidad, las afirmaciones técnicas tienen fuente o se presentan como hipótesis y no se replica la configuración canónica.

### Anatomía propuesta de Global

1. **Configuración canónica:** una fuente para los datos configurables; referencias resueltas y manejo explícito de ausencias o ciclos.
2. **Identidad y preferencias:** roles por necesidad, idioma y estilo solicitados, sin exigir declarar roles en cada mensaje.
3. **Convenciones transversales:** nombres, firma y formato cuando correspondan al entregable.
4. **Relación con el proyecto:** mecanismo declarado de localización del Scope y tratamiento de su ausencia según la integración elegida.

**Aceptación documental:** las preferencias se pueden cambiar en un único lugar; no se presupone tecnología local ni se promete descubrir un archivo que el entorno no carga.

### Anatomía propuesta de Scope

Se conservan las cuatro secciones actuales:

| Sección | Contenido mínimo | Verificación |
| --- | --- | --- |
| A. Identidad y contexto | Propósito del proyecto, alcance, restricciones confirmadas y referencias relevantes. Tecnología solo si corresponde y se conoce. | Los hechos son trazables; lo desconocido no aparece como decisión. |
| B. Precedencia y jerarquía | Límites del entorno, especialización permitida y resolución de conflictos con skills. | Una regla local no amplía permisos ni invalida una restricción superior. |
| C. Motor de selección | Descubrimiento, elección, ausencia de skill, dependencias y resultado esperado. | La elección se explica por la tarea y puede comprobarse. |
| D. Protección de gobernanza | Cambios sujetos a autorización y distinción entre política escrita y control técnico disponible. | Se identifica qué protección existe y cómo se verifica. |

**Aceptación documental:** las cuatro responsabilidades están cubiertas sin duplicar procedimientos. Menos de 60 líneas se mantiene como objetivo orientativo para la base; excederlo exige explicar la necesidad, no comprimir texto hasta perder claridad. La versión configurada puede crecer con restricciones reales del proyecto.

## 3. Autoridad y autorización

- El entorno determina la jerarquía efectiva de instrucciones y los permisos. La integración debe documentarlos; la fábrica no los redefine mediante una frase.
- Dentro del margen permitido, Scope especializa las convenciones del proyecto. Una skill complementa esas reglas y no amplía autorizaciones.
- Ante un conflicto, identificar las instrucciones afectadas y aplicar la autoridad efectiva. No descartar una skill completa por una instrucción separable que no debe seguirse; detener la parte dependiente si el conflicto impide un resultado correcto.
- La orden de modificar un artefacto se evalúa por su alcance. Una bandera escrita no sustituye autorización humana ni acredita un bloqueo del sistema de archivos.
- Una excepción autorizada se limita a los archivos y cambios acordados. Si existe un estado temporal de protección, restaurarlo y verificarlo al terminar. Si la ejecución se interrumpe, comprobarlo al reanudar; no presumir que se restauró.
- Las referencias, ejemplos e insumos aportan contenido; no se convierten automáticamente en instrucciones con autoridad.

## 4. Contrato mínimo de skill

Un skill es un módulo de instrucciones especializadas. Puede incluir herramientas ejecutables, pero no necesita código ni representa por sí mismo un agente autónomo.

El contrato de empaquetado toma como referencia [Agent Skills](https://agentskills.io/specification): carpeta con `SKILL.md`, metadatos YAML con nombre y descripción; el nombre coincide con la carpeta. Se comprueban las restricciones del formato al empaquetar. Referencias, scripts y recursos se incorporan cuando son necesarios. Los ejemplos son una convención permitida del proyecto, no una obligación universal. Las dependencias del entorno se declaran y no se confunden con portabilidad total.

El siguiente contrato operativo es una propuesta propia de la fábrica:

| Elemento | Requisito de diseño |
| --- | --- |
| Activación | Explicar qué tarea resuelve y en qué casos no aplica. |
| Entradas | Identificar la información requerida, la opcional y la respuesta ante ausencias materiales. |
| Procedimiento | Dar pasos suficientes para el resultado; remitir detalles extensos a recursos concretos. |
| Salida | Definir el artefacto o respuesta, destino cuando corresponda y condiciones de aceptación. |
| Dependencias | Declarar herramientas, acceso a red, archivos o capacidades necesarias; distinguir requisitos de opciones. |
| Límites | Respetar el alcance y las autorizaciones; no cambiar gobernanza por iniciativa propia. |
| Verificación | Incluir un caso normal, uno con información insuficiente y uno fuera de alcance. |

Una skill sin scripts puede ser válida. Una skill con dependencias externas puede ser reutilizable si las declara y verifica; no se etiqueta como autocontenida si necesita recursos no incluidos.

## 5. Selección y flujo

1. Comprender el resultado solicitado y las restricciones aplicables.
2. Consultar descripciones disponibles, evitando cargar indiscriminadamente todos los procedimientos.
3. Elegir solo las skills necesarias. Cargar sus referencias cuando el procedimiento o la tarea las requiera.
4. Si ninguna aplica, trabajar con las instrucciones vigentes cuando sea suficiente. Si una capacidad requerida falta, informar la limitación sin inventarla.
5. Ordenar etapas por dependencias. Mantener secuencia por defecto; seleccionar varias skills no autoriza delegar ni ejecutar agentes concurrentes.
6. Al cerrar una etapa, conservar resultado, evidencia, supuestos y pendientes necesarios para la siguiente. Validar sus entradas antes de usarlas.
7. Dejar de usar instrucciones que ya no aplican; no afirmar que fueron borradas del contexto ni que hubo un ahorro cuantificado sin medición.

## 6. Integración y despliegue: contrato previo a la implementación

La primera integración se describe mediante una ficha con: entorno y versión o fecha verificada, entrada reconocida, ubicación de los documentos, mecanismo de carga, precedencia, permisos disponibles y evidencia de prueba. Un entorno sin ficha validada queda como no verificado.

El inicializador futuro tiene este contrato mínimo:

| Aspecto | Resultado requerido |
| --- | --- |
| Entrada | Destino explícito, revisión de capacidades elegida y ficha de integración aplicable. |
| Prevalidación | Resolver destino, detectar archivos existentes y comprobar compatibilidad antes de escribir. |
| Plan de cambios | Mostrar archivos que se crearían o cambiarían y diferencias en contenido existente. |
| Conflictos | Conservar personalizaciones; una sustitución requiere estar cubierta por la autorización. |
| Repetición | Con la misma entrada y destino sin cambios, no duplicar archivos ni reglas. |
| Fallo parcial | Informar operaciones completadas y pendientes; permitir recuperar la revisión previa sin borrar trabajo ajeno. |
| Salida | Registro de revisión instalada, archivos afectados y comprobación de carga. |

La selección de herramienta, implementación del inicializador y ejecución de estas comprobaciones están pendientes. No se exige Git como propiedad universal: si la primera integración lo requiere, debe declararlo.

## 7. Calidad, evidencia y evolución

Obligatorio identifica límites o aceptación indispensable; recomendado admite una excepción justificada; opcional depende de la necesidad. Una regla condicional puede ser precisa si define condición, acción y resultado.

Las mejoras se justifican por un problema concreto. La opinión técnica propia se identifica como propuesta de Sam; las afirmaciones externas citan una fuente verificable. El nombre de un proveedor no constituye evidencia.

Se usan enlaces para navegación, no como prueba de activación automática. Los criterios de promoción y los escenarios operativos se mantienen únicamente en el [plan de validación](validacion_y_evolucion.md), evitando duplicar su estado en varios documentos.

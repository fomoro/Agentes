# Reglas de la fábrica

- Actualizado: el 2026-09-24 20:19
- Rol de ejecución: arquitectura de gobernanza de agentes y arquitectura de información
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: aprobado

## Objetivo

Establecer las reglas con las que Generator diseña, revisa y prepara agentes, scopes y skills reutilizables. Estas reglas gobiernan el trabajo de la fábrica; no se copian automáticamente a los proyectos destino. Las especificaciones definen el contrato de cada capacidad y los procesos describen cómo construirla y validarla.

## 1. Alcance y autoridad de Generator

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Límite de la fábrica** | Separar el diseño y la preparación de una capacidad de su instalación o ejecución en un proyecto destino. No declarar disponible una capacidad que solo esté especificada. | Propuesta del agente IA |
| **Aislamiento del destino** | Conservar los borradores de gobernanza del destino en las ubicaciones de diseño; no instalarlos como gobernanza activa de la fábrica. Resolver sus rutas desde el proyecto destino y probarlos en un proyecto independiente cuando esté autorizado. | Propuesta del agente IA |
| **Destino explícito** | Antes de incorporar una regla, identificar si gobierna Generator, el AGENTS global, el Scope local o una skill. Ubicarla en una sola fuente vigente y referenciarla cuando otro documento la necesite. | Propuesta del agente IA |

## 2. Custodia de fuentes

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Fuentes vigentes y antecedentes** | Identificar la fuente vigente de cada decisión y distinguirla de insumos, auditorías y propuestas históricas. No promover un antecedente a regla aprobada por el solo hecho de citarlo. | Propuesta del agente IA |
| **Cobertura de insumos** | Cuando se solicite incorporar o contrastar insumos, leer completos los pertinentes y los documentos destino. Incorporar cada elemento relevante o justificar su exclusión; el resultado debe cumplir su función sin consultar archivos temporales. | Propuesta del agente IA |
| **Trazabilidad útil** | En «Origen / referencia», usar «Propuesta del agente IA» para formulaciones propias o un enlace «Referencia externa» a documentación oficial de OpenAI consultada que respalde el criterio. Atribuir solo el respaldo comprobado; no inventar procedencias. Mantener la regla agnóstica: la referencia no crea dependencia del proveedor ni acredita funcionamiento en todos los entornos. | Propuesta del agente IA |

## 3. Diseño y mantenimiento de reglas y especificaciones

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Abstracción** | Al diseñar agentes y skills, priorizar principios y reglas reutilizables sobre componentes específicos de un proyecto, salvo cuando ese detalle sea necesario para aplicar la capacidad. | Propuesta del agente IA |
| **Especialización** | Incorporar una regla a una skill solo cuando sea específica de su método, estable y reutilizable; mantener las reglas generales en la gobernanza correspondiente. | Propuesta del agente IA |
| **Contrato y método** | Ubicar requisitos, fundamento y criterios de aceptación en Especificaciones; pasos, decisiones operativas y formatos de evidencia en Procesos. Revisar el contrato antes de contrastarlo con sus procesos. | Propuesta del agente IA |
| **Traslado de reglas** | Al trasladar, fusionar o retirar reglas, identificar la regla y sus secciones de origen y destino por su propósito, conservar la intención y registrar motivo y resultado. No decidir la ubicación por el número, título o archivo de origen. | Propuesta del agente IA |
| **Contrato de la capacidad** | Antes de diseñar un agente o una skill, definir el objetivo, las entradas, el resultado esperado, los límites y las condiciones para detenerse o solicitar información. | [Referencia externa](https://developers.openai.com/plugins/build/skills) |
| **Activación diferenciada** | Describir cuándo corresponde usar una skill y cuándo no. Evitar descripciones tan amplias que compitan con otras skills o activen un método irrelevante. | [Referencia externa](https://developers.openai.com/plugins/build/skills) |
| **Dependencias declaradas** | Identificar herramientas, datos, permisos y recursos necesarios para usar una capacidad. No afirmar portabilidad o funcionamiento en un entorno cuyas dependencias no se hayan comprobado. | Propuesta del agente IA |
| **Agnosticidad controlada** | Mantener el núcleo de reglas y responsabilidades independiente de proveedor o herramienta cuando sea viable; aislar y justificar las dependencias específicas en la configuración o el recurso correspondiente. | Propuesta del agente IA |
| **Estructura** | Separar los temas con títulos o divisores cuando faciliten localizar las reglas. | [Referencia externa](https://developers.openai.com/api/docs/guides/prompt-engineering#message-formatting-with-markdown-and-xml) |
| **Fuerza normativa** | Indicar explícitamente qué debe hacer el agente, qué debe evitar y cuándo aplica la instrucción. Reservar términos absolutos como «siempre», «nunca» y «debe» para requisitos que realmente los exijan. | [Referencia externa](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Referencia externa](https://developers.openai.com/api/docs/guides/voice-prompting) |

## 4. Gestión de propuestas y decisiones

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Estado explícito** | Distinguir propuesta, decisión confirmada, prototipo y capacidad validada. No inferir aprobación del diseño completo a partir de un cambio documental o una prueba parcial. | Propuesta del agente IA |
| **Pendientes concretos** | Mantener los vacíos y decisiones sin resolver en el backlog o registro acordado; no rellenarlos con supuestos en una regla exportable. | Propuesta del agente IA |
| **Borradores y evidencias** | Reservar Propuestas para borradores concretos y guardar los resultados de pruebas en la ubicación acordada para evidencias, separados de los métodos reutilizables. | Propuesta del agente IA |

## 5. Validación y promoción de resultados

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Revisión documental** | Contrastar cada documento con su objetivo y después comprobar la coherencia del conjunto: destino, alcance, referencias, estados, contradicciones, duplicaciones y rutas. Informar qué se comprobó y qué queda pendiente. | Propuesta del agente IA |
| **Prueba representativa** | Antes de considerar operativa una capacidad, probar casos que deban activarla, casos que no, entradas incompletas y límites relevantes en un entorno declarado. | [Referencia externa](https://developers.openai.com/plugins/build/skills) |
| **Promoción verificable** | Exportar como lista para uso solo una capacidad cuyo contenido, dependencias y resultado se hayan comprobado según sus criterios de aceptación. Informar qué validación se hizo y qué queda pendiente. | Propuesta del agente IA |

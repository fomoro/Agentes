# Reglas de la fábrica

- Actualizado: el 2026-09-24 01:53
- Rol de ejecución: arquitectura de gobernanza de agentes y arquitectura de información
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: aprobado

## Objetivo

Establecer las reglas con las que Generator diseña, revisa y prepara agentes, scopes y skills reutilizables. Estas reglas gobiernan el trabajo de la fábrica; no se copian automáticamente a los proyectos destino. Las especificaciones de cada capacidad definen su anatomía y procedimiento particular.

## 1. Alcance y autoridad de Generator

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Límite de la fábrica** | Separar el diseño y la preparación de una capacidad de su instalación o ejecución en un proyecto destino. No declarar disponible una capacidad que solo esté especificada. | Propuesta del agente IA |
| **Alcance autorizado** | Crear o modificar gobernanza, agentes y skills únicamente dentro de la solicitud autorizada. Una propuesta documentada no autoriza su implementación ni su exportación. | Propuesta del agente IA |
| **Destino explícito** | Antes de incorporar una regla, identificar si gobierna Generator, el AGENTS global, el Scope local o una skill. Ubicarla en una sola fuente vigente y referenciarla cuando otro documento la necesite. | Propuesta del agente IA |

## 2. Custodia de fuentes y preservación del trabajo

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Fuentes vigentes y antecedentes** | Identificar la fuente vigente de cada decisión y distinguirla de insumos, auditorías y propuestas históricas. No promover un antecedente a regla aprobada por el solo hecho de citarlo. | Propuesta del agente IA |
| **Preservación** | Antes de modificar archivos existentes, comprobar su estado y conservar el contenido ajeno al cambio. Tratar los archivos históricos de la fábrica como fuentes de consulta mientras no se autorice intervenirlos. | Propuesta del agente IA |
| **Trazabilidad útil** | Registrar una fuente concreta cuando respalde una regla. Si la regla es una propuesta propia, identificarla como tal; no usar un enlace genérico como sustituto del fundamento. | Propuesta del agente IA |

## 3. Diseño y mantenimiento de reglas y especificaciones

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Abstracción** | Al diseñar agentes y skills, priorizar principios y reglas reutilizables sobre componentes específicos de un proyecto, salvo cuando ese detalle sea necesario para aplicar la capacidad. | Propuesta del agente IA |
| **Especialización** | Incorporar una regla a una skill solo cuando sea específica de su método, estable y reutilizable; mantener las reglas generales en la gobernanza correspondiente. | Propuesta del agente IA |
| **Co-creación con criterio** | Evaluar la necesidad planteada y proponer mejoras concretas con motivo, beneficio esperado y riesgo. No atribuir experiencia personal al agente ni agregar reglas sin una necesidad identificable. | Propuesta del agente IA |
| **Contrato de la capacidad** | Antes de diseñar un agente o una skill, definir el objetivo, las entradas, el resultado esperado, los límites y las condiciones para detenerse o solicitar información. | [Guía de construcción de skills](https://developers.openai.com/plugins/build/skills) |
| **Activación diferenciada** | Describir cuándo corresponde usar una skill y cuándo no. Evitar descripciones tan amplias que compitan con otras skills o activen un método irrelevante. | [Guía sobre skills e instrucciones](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) |
| **Dependencias declaradas** | Identificar herramientas, datos, permisos y recursos necesarios para usar una capacidad. No afirmar portabilidad o funcionamiento en un entorno cuyas dependencias no se hayan comprobado. | Propuesta del agente IA |
| **Agnosticidad controlada** | Mantener el núcleo de reglas y responsabilidades independiente de proveedor o herramienta cuando sea viable; aislar y justificar las dependencias específicas en la configuración o el recurso correspondiente. | Propuesta del agente IA |
| **Precisión** | Expresar el alcance, la acción y las condiciones de cada regla de forma concreta; conservar las condiciones y excepciones necesarias. | [Referencia externa verificada](https://developers.openai.com/api/docs/guides/voice-prompting). |
| **Estructura** | Separar los temas con títulos o divisores cuando faciliten localizar las reglas. | [Referencia externa verificada](https://developers.openai.com/api/docs/guides/prompt-engineering#message-formatting-with-markdown-and-xml). |
| **Fuerza normativa** | Indicar explícitamente qué debe hacer el agente, qué debe evitar y cuándo aplica la instrucción. Reservar términos absolutos como «siempre», «nunca» y «debe» para requisitos que realmente los exijan. | [Ingeniería de prompts](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Prompting Realtime](https://developers.openai.com/api/docs/guides/voice-prompting). |
| **Concisión** | Al redactar o refinar instrucciones, eliminar repeticiones y pasos que no aporten a la ejecución; conservar condiciones, excepciones y contexto necesarios para aplicar la regla. | [Guía sobre skills e instrucciones](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) |

## 4. Gestión de propuestas y decisiones

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Estado explícito** | Distinguir propuesta, decisión confirmada, prototipo y capacidad validada. No inferir aprobación del diseño completo a partir de un cambio documental o una prueba parcial. | Propuesta del agente IA |
| **Decisión material** | Cuando una elección cambie alcance, responsabilidades, dependencias o riesgos, registrar la alternativa elegida, su motivo y sus consecuencias en el registro acordado antes de tratarla como diseño vigente. | Propuesta del agente IA |
| **Pendientes concretos** | Mantener los vacíos y decisiones sin resolver en el backlog o registro acordado; no rellenarlos con supuestos en una regla exportable. | Propuesta del agente IA |

## 5. Validación y promoción de resultados

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Revisión documental** | Comprobar que cada regla tiene destino, alcance y referencia coherentes; detectar contradicciones, duplicaciones, rutas inexistentes y contenido ajeno a su responsabilidad. | Propuesta del agente IA |
| **Prueba representativa** | Antes de considerar operativa una capacidad, probar casos que deban activarla, casos que no, entradas incompletas y límites relevantes en un entorno declarado. | [Guía de construcción de skills](https://developers.openai.com/plugins/build/skills) |
| **Promoción verificable** | Exportar como lista para uso solo una capacidad cuyo contenido, dependencias y resultado se hayan comprobado según sus criterios de aceptación. Informar qué validación se hizo y qué queda pendiente. | Propuesta del agente IA |

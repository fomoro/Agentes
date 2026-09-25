# Auditoría integral de Generator

- Actualizado: el 2026-09-24 20:23
- Rol de ejecución: auditoría documental, arquitectura de información y diseño de procesos
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: auditoría ejecutada y ajustes documentales aplicados; validación operativa pendiente

## Objetivo

Determinar si `C:\Dev\Agentes\Generator` tiene el conjunto mínimo, coherente y útil de documentos para empezar a usar la fábrica. La auditoría debe evaluar **cada archivo**, sus relaciones y los vacíos reales; no justificar documentos por el trabajo invertido en crearlos.

## Instrucciones para ejecutar la auditoría

Actúa como revisor crítico, incluso de documentos que hayas redactado. Antes de evaluarlos, consulta la gobernanza global vigente del asistente, el [README principal](../README.md) y las [reglas de Generator](../Generator/.rules/Reglas_Operacion.md). Aplica sus límites sin copiarlos al informe.

1. Inventaría recursivamente `Generator`, incluidas las carpetas ocultas y las carpetas vacías. Lee **completo** cada archivo vigente. Identifica su ruta, revisión o fecha y estado. Consulta insumos históricos solo cuando ayuden a comprobar cobertura; no los trates como reglas vigentes ni exijas consultarlos para usar el resultado.
2. Evalúa cada archivo frente a su objetivo: ¿qué decisión o tarea permite cumplir?, ¿qué contenido es imprescindible?, ¿qué sobra, se repite o pertenece a otro lugar? Para cada uno recomienda **conservar, simplificar, fusionar, trasladar o retirar**, con evidencia y efecto. No fuerces cambios cuando el archivo ya cumple su función.
3. Comprueba el conjunto: autoridad y separación entre reglas internas de Generator, reglas exportables, Global, Local y Skills; relación entre especificaciones y procesos; referencias y rutas existentes; estados de aprobación; dependencias del entorno; suficiencia sin temporales. No trates la ausencia de un archivo como defecto sin explicar qué función necesaria queda descubierta.
4. Aplica KISS y YAGNI: cuestiona cada README, tabla, plantilla, sección y control adicional. Conserva únicamente lo que ayude a decidir, construir, usar o verificar. Usa responsabilidad única y dependencias claras como criterios de diseño; no fuerces los demás principios SOLID sobre documentos si no aportan una decisión concreta.
5. Revisa **cada fila** de `Origen / referencia` en los archivos de reglas. El valor esperado es `Propuesta del agente IA` para una formulación propia o un enlace etiquetado `Referencia externa` a documentación oficial de OpenAI que realmente respalde el criterio. Verifica cada cita: su procedencia no convierte la regla en dependiente del proveedor. Señala valores distintos, citas que no sustentan el texto y procedencias inciertas; no inventes fuentes ni reclasifiques antecedentes como propuestas propias sin evidencia.
6. Distingue revisión documental, prototipo, validación operativa y preparación para exportar. Concluye si Generator puede empezar a usarse, con qué alcance y qué impide cerrar esta etapa. No declares probada una capacidad por tener especificación o proceso.

## Informe requerido

Cuando se ejecute este encargo, agrega el informe **en este mismo archivo**, en una sección nueva titulada `## Resultado de la auditoría`. No crees otro documento en `Reviews` ni modifiques `Generator` durante la auditoría.

El informe debe contener:

- **Alcance y evidencia:** fecha de revisión, archivos leídos, fuentes consultadas y limitaciones.
- **Evaluación archivo por archivo:** tabla con ruta, función, valor real, problema comprobado —si existe—, recomendación y motivo. Incluir todos los archivos inventariados; registrar aparte las carpetas vacías que afecten el diseño.
- **Hallazgos transversales:** solo contradicciones, duplicaciones, dependencias o vacíos respaldados por rutas y secciones concretas. Distinguir defecto, riesgo y preferencia editorial.
- **Cambios mínimos recomendados:** ordenados por impacto; indicar qué se conserva, simplifica, fusiona, traslada o retira, y las referencias que habría que actualizar. Son propuestas, no autorización para ejecutarlas.
- **Veredicto:** `Listo para uso acotado`, `Listo con pendientes no bloqueantes` o `No listo`; explicar el alcance del veredicto y los bloqueos. No confundir este veredicto documental con validación operativa o exportación.

## Cierre de la revisión

- [x] Cada archivo fue evaluado frente a una función concreta; las especificaciones definen contratos y los procesos permiten ejecutar su función propia.
- [x] El contenido pertinente de los insumos está cubierto o su exclusión está justificada; los documentos vigentes no dependen de archivos temporales.
- [x] Se verificaron referencias, rutas y respaldo real de las fuentes externas.
- [x] Se informaron duplicaciones, estados, pendientes, límites de comprobación y un veredicto sustentado, sin proponer estructura por costumbre.

Deja sin marcar cualquier punto no comprobado e indica qué faltó. El resultado de la auditoría no aprueba automáticamente sus recomendaciones.

## Resultado de la auditoría

Los hallazgos y recuentos siguientes describen el estado anterior a los ajustes. Su aplicación, autorizada por el usuario, se registra al final de este documento.

### Veredicto y alcance

**Listo para uso acotado:** hay documentación suficiente para elaborar un primer Scope y una primera skill, utilizando la gobernanza global ya disponible y declarando el entorno destino. Para cerrar la base documental conviene resolver los ajustes de fuentes, aislamiento y registro de entorno indicados abajo. La producción de un AGENTS global propio y la validación operativa del conjunto siguen pendientes.

La estructura principal tiene sentido. El exceso se concentra en reglas generales repetidas y en el README de Local. Recomiendo reducir esos contenidos y conservar la separación entre especificación, creación y validación: responden a preguntas distintas y permiten validar una capacidad existente sin reconstruirla.

Se leyeron completos los **11 archivos** actuales de `Generator`, incluidas sus carpetas ocultas, el README principal y la gobernanza global vigente del asistente. Se revisaron **59 reglas**, **27 enlaces internos** y las **7 páginas externas distintas** citadas por 12 reglas. Los 27 enlaces internos resuelven a destinos existentes. Los cuatro catálogos de reglas declaran estado aprobado; los otros siete documentos declaran propuesta en revisión. Esta auditoría no cambia esos estados.

La revisión corresponde al 2026-09-24. Se registraron huellas SHA-256 de los archivos para comprobar que el informe corresponde al contenido leído. No se ejecutaron skills, instalaron archivos ni probaron mecanismos de carga. La ausencia de `.agents/AGENTS_Scope.md` en esta fábrica no se considera un defecto: existen gobernanza global y un punto de entrada documental en el README principal.

### Evaluación archivo por archivo

Las rutas de esta tabla son relativas a `Generator`. Las horas identifican la revisión declarada en la cabecera; todas corresponden al 2026-09-24.

| Archivo y revisión | Función y valor | Problema o límite comprobado | Recomendación |
| :--- | :--- | :--- | :--- |
| [.rules/Reglas_Operacion.md](../Generator/.rules/Reglas_Operacion.md) · 19:52 | Define cómo trabaja la fábrica y distingue diseño, pruebas y exportación. | Repite conducta de la gobernanza global; la regla de aislamiento es ambigua; el criterio de procedencia permite más valores que los acordados. | **Simplificar.** Conservar criterios propios de la fábrica y corregir H1–H3. |
| [Agents/.rules/reglas_generales.md](../Generator/Agents/.rules/reglas_generales.md) · 01:55 | Catálogo reutilizable de comportamiento para los productos. | Cinco referencias usan etiquetas distintas de la acordada; una tiene respaldo indirecto. | **Conservar y ajustar referencias.** Su parecido con la gobernanza del asistente constructor no lo vuelve inútil: sirve a otros destinos. |
| [Agents/.rules/reglas_agents_global.md](../Generator/Agents/.rules/reglas_agents_global.md) · 01:55 | Define configuración, precedencia, autoría y preferencias globales exportables. | «Ubicación Estricta» es una regla general de entrega, sin particularidad del AGENTS global. No constituye por sí solo un AGENTS global terminado. | **Conservar y trasladar** esa fila al catálogo general, verificando unicidad; mantener las otras cinco reglas. |
| [Agents/.rules/reglas_agents_local.md](../Generator/Agents/.rules/reglas_agents_local.md) · 01:55 | Aporta contexto local, protección opcional y selección de skills. | El título fija una ruta que el objetivo correctamente declara adaptable. Las reglas de bandera son condicionales, no requisitos universales. | **Conservar.** Un título como «Reglas de gobernanza local» sería más coherente; ajuste editorial, no bloqueo. |
| `Agents/Local/README.md` · 19:39 · retirado tras la auditoría | Resume responsabilidades y tres criterios de mantenimiento. | Suficiencia y agnosticidad ya están en las reglas de la fábrica; los otros documentos explican sus funciones. Su única regla exclusiva exige mantener este mismo README. | **Retirar.** Actualizar primero los dos enlaces que lo usan; no crear un sustituto. |
| [Agents/Local/Especificaciones/especificacion_scope.md](../Generator/Agents/Local/Especificaciones/especificacion_scope.md) · 19:39 | Define las cuatro secciones del Scope y los resultados que deben poder comprobarse. | Repite límites y criterios entre anatomía, diseño, aceptación y cierre. El detalle de la ficha de entorno también aparece en el proceso. | **Simplificar manteniendo un archivo.** Conservar anatomía y resultados esperados; dejar la ficha y el registro operativo en el proceso. |
| [Agents/Local/Procesos/proceso_creacion_scope.md](../Generator/Agents/Local/Procesos/proceso_creacion_scope.md) · 19:39 | Permite reunir contexto, construir el borrador y revisarlo. | «Manejo de decisiones y bloqueos» reitera gobernanza general; el cierre repite parte de los pasos 7 y 8. | **Simplificar.** Integrar las condiciones de parada en el paso pertinente y conservar una sola comprobación de cierre. |
| [Agents/Local/Procesos/proceso_validacion_scope.md](../Generator/Agents/Local/Procesos/proceso_validacion_scope.md) · 19:39 | Permite comprobar un Scope existente por entorno y conservar evidencia. | Reitera varias veces los límites de aprobación y validación. El enlace al README añade una dependencia prescindible. | **Conservar separado y recortar repeticiones.** La ficha, los estímulos y el registro por caso aportan valor. |
| [Agents/Skills/Especificaciones/especificacion_skills.md](../Generator/Agents/Skills/Especificaciones/especificacion_skills.md) · 19:34 | Contrato compacto de propósito, activación, entradas, método, dependencias y salida. | El empaquetado queda deliberadamente condicionado al destino; todavía no hay un paquete concreto evaluado. | **Conservar.** Es suficiente para diseñar la primera skill; concretar su formato al construirla, sin añadir un manual de plataforma anticipado. |
| [Agents/Skills/Procesos/proceso_creacion_skill.md](../Generator/Agents/Skills/Procesos/proceso_creacion_skill.md) · 19:34 | Define una secuencia corta desde la necesidad hasta el borrador revisado. | No presenta un defecto estructural que justifique más documentación. | **Conservar.** El contrato compartido evita repetir la especificación. |
| [Agents/Skills/Procesos/proceso_validacion_skill.md](../Generator/Agents/Skills/Procesos/proceso_validacion_skill.md) · 19:34 | Define casos, evidencia y conclusión de una prueba operativa. | Identifica asistente y modalidad, pero omite versión del asistente/modelo y ubicación del entorno de prueba; dificulta reproducir o comparar resultados. | **Ajustar** el registro del paso 1, sin crear otra plantilla o archivo. |

Las carpetas vacías `Agents/Local/Propuestas` y `Agents/Skills/Propuestas` son destinos definidos de trabajo; pueden conservarse sin README. `Agents/Global` representa una capacidad todavía no desarrollada. Su ausencia de archivos limita la oferta de la fábrica, pero no impide probar Local y Skills bajo una gobernanza global existente. No recomiendo llenar esa carpeta por simetría.

### Hallazgos transversales

**H1 · Media · Inconsistencia de procedencia.** «Trazabilidad útil», en `Reglas_Operacion.md`, admite documentos internos y fuentes externas genéricas. El criterio acordado para estos catálogos es `Propuesta del agente IA` o un enlace `Referencia externa` a documentación oficial de OpenAI. Las 12 filas con fuentes externas incumplen la etiqueta exacta; los enlaces existen, pero accesibilidad y respaldo no son equivalentes. Ajustar la regla canónica y las celdas correspondientes. La tabla de fuentes siguiente precisa el respaldo encontrado; no hace falta añadir esta política a otro README.

**H2 · Media · Aislamiento redactado como prohibición de construcción.** La frase «No crear en la fábrica archivos de activación destinados al cliente» puede impedir generar esos mismos archivos en las carpetas de propuestas, actividad que los procesos autorizan. El objetivo útil es impedir su activación accidental. Redacción mínima propuesta: «Conservar los borradores de gobernanza del destino en las ubicaciones de diseño; no instalarlos como gobernanza activa de la fábrica. Resolver sus rutas desde el proyecto destino». Mantener las pruebas en un entorno identificado e independiente cuando corresponda.

**H3 · Media · Repetición entre gobierno del asistente y gobierno de la fábrica.** `Alcance autorizado`, `Preservación`, `Co-creación con criterio`, `Precisión`, `Concisión` y `Decisión material` repiten criterios ya presentes en las secciones 3–5 y 7 de la gobernanza global consultada. El README principal ya ordena consultarla. En las reglas internas, conservar solo el complemento específico que cada fila aporte; retirar el resto. En cambio, los catálogos exportables tienen una función de producto y deben conservar su base general: el entorno cliente puede no disponer de la configuración de este asistente. Esta distinción evita borrar contenido útil por una comparación puramente textual.

**H4 · Media · Evidencia de skills con entorno insuficientemente identificado.** El paso 1 de `proceso_validacion_skill.md` no pide la versión del asistente/modelo ni la ubicación del proyecto de prueba. El proceso de Scope sí registra versión, modalidad y proyecto. Añadir esos datos al registro de Skills y dejar como pendiente el dato que el entorno no permita conocer. Esto permite limitar correctamente las conclusiones, sin imponer un sistema de versiones nuevo.

**H5 · Baja · Mantenimiento documental sobredimensionado en Local.** Su README no contiene una convención local irreemplazable. Las tres reglas se resuelven en `Reglas_Operacion.md`: «Cobertura de insumos», «Contrato y método» y «Agnosticidad controlada». Retirarlo requiere ajustar los enlaces de los dos procesos, ambos en «Alcance». En la especificación, reducir los avisos reiterados sobre validación y autoridad. La tabla de resultados esperados de la especificación y la tabla de estímulos del proceso no son duplicados completos: conservar esa separación útil.

**H6 · Baja · Regla general ubicada en catálogo especializado.** «Ubicación Estricta», en `reglas_agents_global.md`, aplica a cualquier entrega. Trasladarla a `reglas_generales.md` permite que el catálogo global se concentre en su configuración y relación con otros niveles. El destino existe; el traslado sigue siendo una propuesta.

### Revisión de Origen / referencia

Se revisaron las 59 filas: 28 de fábrica, 15 generales, 6 globales y 10 locales. **47** declaran `Propuesta del agente IA`; cumplen el formato acordado y no alegan respaldo externo. Esa etiqueta informa procedencia, no demuestra aprobación ni funcionamiento. Las otras **12** se contrastaron con su fuente oficial. En todas corresponde normalizar el texto visible a `Referencia externa` si se conserva la cita.

| Catálogo y regla | Fuente consultada | Respaldo encontrado y tratamiento recomendado |
| :--- | :--- | :--- |
| Fábrica · Contrato de la capacidad | [Referencia externa](https://developers.openai.com/plugins/build/skills) | «Define the workflow boundary» respalda entradas, pasos, salida y condiciones de parada de una skill. Extender ese contrato a agentes es una decisión de diseño de la fábrica, no una garantía de la fuente. |
| Fábrica · Activación diferenciada | [Referencia externa](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | «Better skills» respalda delimitar los disparadores y evitar descripciones demasiado amplias. Es una publicación oficial del blog; si se exige estrictamente un manual, «Write SKILL.md» de la guía de construcción también respalda el criterio. |
| Fábrica · Precisión | [Referencia externa](https://developers.openai.com/api/docs/guides/voice-prompting) | «General Tips» y «Avoid literal instruction traps» respaldan precisión y alcance explícito. El contexto original es Realtime; no demuestra rendimiento universal de la regla. |
| Fábrica · Estructura | [Referencia externa](https://developers.openai.com/api/docs/guides/prompt-engineering#message-formatting-with-markdown-and-xml) | La sección enlazada respalda títulos, listas y límites lógicos entre contenidos. Conservar la cita sin afirmar garantías de obediencia. |
| Fábrica · Fuerza normativa | [Referencia externa](https://developers.openai.com/api/docs/guides/prompt-engineering) y [Referencia externa](https://developers.openai.com/api/docs/guides/voice-prompting) | La primera respalda instrucciones explícitas; «Avoid literal instruction traps» de la segunda respalda reservar restricciones absolutas para requisitos reales. |
| Fábrica · Concisión | [Referencia externa](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Respalda revisar instrucciones innecesarias y descripciones excesivas. La formulación agnóstica es una adaptación; el documento también advierte diferencias entre modelos. |
| Fábrica · Prueba representativa | [Referencia externa](https://developers.openai.com/plugins/build/skills) | «Test the skill» incluye activación, no activación, entradas incompletas y casos límite. Respaldo directo del criterio central. |
| Generales · Mínimo alcance de intervención | [Referencia externa](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | «Editing constraints» respalda preservar cambios ajenos. La condición de pedir una ampliación solo cuando sea indispensable es elaboración del proyecto; la cita no respalda toda la regla por sí sola. |
| Generales · Separar contenido de instrucciones | [Referencia externa](https://developers.openai.com/api/docs/guides/agent-builder-safety) | «Prompt injections» y «Don’t use untrusted variables in developer messages» respaldan impedir que datos externos adquieran autoridad indebida. Conservar el principio sin importar las políticas particulares de Agent Builder. |
| Generales · Verificar antes de afirmar ejecución | [Referencia externa](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | La guía promueve verificación y cierre honesto de pendientes, pero no sustenta de forma específica la clasificación propuesta/intentada/confirmada ni la comprobación antes de repetir un efecto ambiguo. Usar `Propuesta del agente IA` para esta formulación propia, o aportar un pasaje más directo antes de mantener atribución externa. |
| Generales · Comprobar el estado antes de modificar | [Referencia externa](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | «Editing constraints» respalda releer cambios y preservarlos. La aclaración sobre ausencia de bloqueo de concurrencia es precisión propia; no atribuirla al texto externo. |
| Generales · Preferir acciones recuperables | [Referencia externa](https://learn.chatgpt.com/docs/codex/cli) | «Start your first task» propone puntos de recuperación con Git. Respalda recuperación; proporcionalidad y alternativas fuera de Git son adaptación del proyecto. |

Una adaptación puede conservar una referencia que respalde su criterio central. No necesita copiar literalmente la fuente, pero tampoco atribuirle las condiciones añadidas por la fábrica. Las dos reglas citadas como ejemplo por el usuario —Contrato y Concisión— tienen respaldo útil; el nombre visible de sus enlaces debe normalizarse y su redacción interna debe seguir siendo agnóstica.

### Cobertura, estados y límites

Los seis temas del antecedente «Principios de la fábrica», leído completo anteriormente en esta conversación, están cubiertos: co-creación, separación de destino, fuente vigente, agnosticidad, reutilización y calidad proporcional. Se contrastaron con las reglas actuales. Sus nombres antiguos de carpetas, exigencia de backlog/hoja de ruta y prohibición general de carpetas ocultas se excluyen porque no corresponden a la organización vigente o exceden el problema real de activación. El archivo temporal ya no está en su ruta al ejecutar esta auditoría; no se afirma haber releído una versión nueva ni haber contrastado todos los temporales del proyecto.

No se encontraron enlaces desde Generator a temporales. Las referencias mutuas entre especificación y procesos sirven para navegar y no forman, por sí solas, una dependencia circular de ejecución. No se requiere otro README, una plantilla por carpeta, una nueva capa de gobernanza ni dividir más documentos.

Las cabeceras aprobadas y las propuestas se conservaron como evidencia del estado actual. Crear o revisar un documento no equivale a aprobarlo. Tras los ajustes que se decidan, la adopción del conjunto debe registrarse una sola vez con alcance claro; esta auditoría no exige aprobaciones por cada paso de construcción.

### Cambios mínimos recomendados

1. Corregir en los archivos existentes la ambigüedad de aislamiento, la política de procedencia y las 12 etiquetas externas. Resolver el respaldo indirecto de «Verificar antes de afirmar ejecución» según la tabla anterior.
2. Completar la identificación del entorno en la validación de Skills. No hace falta otro archivo.
3. Retirar el README de Local después de actualizar sus dos referencias; depurar las reglas internas que repiten la gobernanza global y los párrafos reiterados de Local. Trasladar «Ubicación Estricta» al catálogo general.
4. Conservar los seis documentos de especificación y procesos de Local y Skills. Empezar con un caso concreto de cada uno bajo la gobernanza global existente y usar sus pruebas para detectar necesidades reales. Desarrollar Global cuando se decida producir ese artefacto, no para llenar una carpeta.

El primer uso documental puede comenzar con el alcance indicado. La validación operativa y la exportación requieren evidencia del caso concreto; no se obtienen aprobando este informe.

## Aplicación de los ajustes

Ejecutada el 2026-09-24 por solicitud del usuario. Se conservaron el informe original como diagnóstico y los seis documentos de especificación, creación y validación; no se añadieron archivos.

| Hallazgo | Cambio aplicado |
| :--- | :--- |
| H1 · Procedencia | Se corrigió «Trazabilidad útil» y se normalizaron los enlaces conservados como «Referencia externa». «Verificar antes de afirmar ejecución» quedó como «Propuesta del agente IA». «Activación diferenciada» cita ahora el manual oficial de construcción de skills, cuyo respaldo se comprobó en la auditoría. |
| H2 · Aislamiento | Se permitió conservar borradores del destino en la fábrica sin activarlos como su gobernanza; se mantuvo la separación del proyecto de prueba. |
| H3 · Repetición | Se retiraron de las reglas internas las seis filas identificadas en H3: su conducta ya está cubierta por la gobernanza global, que el README principal exige consultar. No se eliminaron reglas equivalentes de los catálogos exportables, porque sirven a otros destinos. |
| H4 · Entorno | El proceso de validación de Skills registra versión, modelo y ubicación del proyecto de prueba; los datos desconocidos limitan las conclusiones que dependan de ellos. |
| H5 · Local | Se retiró su README y se actualizaron los dos enlaces entrantes. La especificación conserva anatomía y resultados esperados; la ficha y el registro quedan en validación. Se redujeron criterios repetidos, avisos y el cierre de creación. |
| H6 · Ubicación | «Ubicación Estricta» se trasladó, sin cambiar su contenido, del catálogo global a la sección 3 del catálogo general. Se verificó una sola aparición. |

También se cambió el título del catálogo local a «Reglas de gobernanza local». No se modificaron el README principal, las propuestas ni las carpetas ajenas al alcance. El README retirado no estaba versionado en su ruta vigente y no se creó una copia de recuperación.

### Comprobación y cierre

- Generator contiene **10 documentos** y **53 reglas**: 22 internas, 16 generales, 5 globales y 10 locales.
- Las **44** procedencias propias y las **9** filas con referencias externas cumplen el formato acordado. Se conserva el contraste de fuentes realizado en esta auditoría; no se atribuye una nueva comprobación web a esta edición.
- Los **23 enlaces internos** de Generator resuelven a destinos existentes. No quedan dependencias del README retirado ni enlaces a temporales; `Reviews` conserva un solo archivo.
- Se mantuvieron los estados previos: cuatro catálogos aprobados y seis documentos en revisión. La autorización de estos ajustes no se presentó como aprobación integral de los diseños.

**Cierre documental de los hallazgos H1–H6: completado.** Se mantiene el veredicto **Listo para uso acotado**. Quedan para el siguiente encargo la construcción y prueba de un primer caso concreto; no se instalaron capacidades, no se ejecutaron pruebas operativas ni se habilitó la exportación como producto validado.

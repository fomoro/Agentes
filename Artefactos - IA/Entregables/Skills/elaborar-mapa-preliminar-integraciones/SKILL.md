---
name: elaborar-mapa-preliminar-integraciones
description: Crear o refinar mapas preliminares de integración para arquitectura de solución en fase de estimación, aplicables a distintos procesos de negocio y sistemas. Relaciona capacidades, contratos y responsabilidades mediante una primera versión autónoma y revisión conjunta. No sustituye el diseño detallado ni la evaluación completa de reutilización de interfaces.
---

# Elaborar un mapa preliminar de integraciones

- Actualizado: el 2026-09-17 08:44
- Rol de ejecución: diseñador de skills, arquitecto de soluciones e integraciones y analista de procesos de negocio
- Autor: Sam (Asistente IA del Sr. Wolfan)

## 1. Resultado y límites

Entrega un mapa que permita a Negocio y Tecnología comprender qué capacidades necesitan intercambiar información, qué responsabilidad corresponde a cada sistema y qué falta confirmar para estimar la solución. Conserva los pendientes separados del mapa, según la ubicación acordada.

Aplica el método a cualquier proceso de negocio y conjunto de sistemas. Obtén las reglas, actores, términos, especialistas y restricciones de las fuentes del proyecto. No presupongas un proveedor externo, un portal, un intermediario, un sistema central ni un mecanismo de integración determinado.

Prepara una primera versión completa, sustentada y revisada dentro del alcance solicitado. Después refínala con el usuario, aportando criterio y señalando decisiones abiertas. No conviertas una propuesta o un supuesto en una decisión confirmada.

Aplica el Scope y la gobernanza efectiva del proyecto. Esta skill aporta el método de elaboración; no cambia permisos, identidad, ubicaciones ni reglas locales. Resuelve la firma del entregable desde la configuración vigente, sin copiar el autor de este paquete.

El paquete contiene instrucciones Markdown y plantillas internas; no requiere scripts ni proveedores específicos. Su uso requiere acceso a los insumos del proyecto y un medio autorizado para leer y editar documentos. Estar guardado en una carpeta no acredita instalación automática ni validación en todos los asistentes.

## 2. Entradas y responsabilidades

Localiza las entradas con las rutas del proyecto destino; no presupongas nombres de carpetas ni sistemas:

| Entrada | Uso |
| --- | --- |
| Gobernanza y Scope aplicables | Determinar alcance, especialidades, ubicación y firma. |
| Catálogo de capacidades vigente | Mantener significado, identificadores y trazabilidad de las necesidades. |
| Documentación de los sistemas y contratos de interfaces disponibles | Identificar intercambios documentados y evidencia de cobertura, tanto interna como externa. |
| Decisiones del usuario | Reconocer exigencias acordadas y alternativas descartadas. |
| Mapa existente, si se está revisando | Preservar contenido y ediciones recientes del usuario. |
| Catálogo de integraciones o servicios, si está disponible y es pertinente | Reconocer candidatas sin deducir cobertura por su nombre. |

Si falta una entrada que cambia el propósito o los límites, solicita ese dato y continúa el trabajo independiente. Si falta el contrato de una responsabilidad identificada, conserva la propuesta y formula el pendiente; no inventes campos ni elimines la necesidad por falta de documentación.

Si no existe un catálogo formal de capacidades, deriva una lista provisional de las necesidades documentadas y márcala para validación. Conserva los identificadores existentes; si hacen falta nuevos, usa la convención local o declara una convención propuesta. No exijas prefijos de un caso anterior ni conviertas la creación del catálogo en un proyecto adicional.

Asume responsabilidades complementarias de arquitectura de soluciones, análisis funcional del dominio, arquitectura de integraciones y revisión documental. Selecciona la especialidad funcional a partir del proceso y sus fuentes; consulta a quienes conocen sus reglas cuando falte evidencia. Los roles no otorgan autoridad para aprobar reglas ni atribuyen experiencia personal.

## 3. Seleccionar el momento de trabajo

- Si el usuario solicita crear el mapa, ejecuta el momento 1 sin pedir aprobación por cada frase. Usa el propósito acordado; si está incompleto, aclara solo lo que determine el resultado.
- Si el usuario solicita revisar, comparar o discutir una sección, ejecuta el momento 2 sobre esa sección. Una consulta de opinión no autoriza por sí sola a editar el archivo.
- Si existe una instrucción de trabajar paso a paso, conserva ese ritmo durante la revisión. No la conviertas en obligación de consultar cada decisión editorial durante una nueva elaboración autónoma expresamente solicitada.

## 4. Momento 1: elaborar una primera versión autónoma

### Paso 1. Fijar propósito, fase y evidencia

1. Redacta la pregunta que debe responder el mapa y delimita los sistemas e interacciones incluidos.
2. Declara que se trata de arquitectura para estimación y que los servicios son responsabilidades lógicas propuestas, cuando ese sea su estado. No fijes por ello el número ni el mecanismo de las interfaces físicas.
3. Contrasta capacidades, fuentes y decisiones. Distingue comportamiento documentado, requerimiento acordado, propuesta y pendiente de confirmar.
4. Registra las contradicciones que cambien la interpretación. Una decisión de exigir una capacidad no demuestra que un sistema o un servicio existente ya la implemente.
5. Si dos documentos usan nombres distintos para la misma capacidad, conserva el ID y señala la equivalencia o la discrepancia. No alteres silenciosamente la fuente funcional.

### Paso 2. Recorrer los escenarios de negocio

Para cada capacidad, identifica quién actúa, qué necesita lograr, qué sistema la atiende y cuál es el resultado esperado. Distingue acciones de pantalla, reglas de negocio, consultas, notificaciones y tratamientos internos.

Deriva los escenarios del proceso real: recorrido principal, variantes, excepciones y actividades automáticas que afecten el alcance. Sigue cada escenario hasta su resultado de negocio y el último sistema implicado. Recibir una notificación no demuestra que el sistema destino haya completado el procesamiento esperado.

Antes de proponer un servicio, identifica quién inicia el intercambio, hacia quién, cuándo, para qué y con qué información de negocio. Describe la información necesaria sin inventar nombres de campos técnicos.

### Paso 3. Proponer solo los servicios justificados

- Separa capacidad de negocio y servicio. Buscar, seleccionar o mostrar datos ya recibidos puede resolverse dentro de un sistema sin otra integración.
- Antes de agregar una interfaz, comprueba si falta una consulta, decisión, notificación o registro entre sistemas que los intercambios previstos no cubren.
- Asigna a cada servicio lógico una responsabilidad coherente. Permite que apoye varias capacidades cuando comparten esa responsabilidad; no agrupes funciones sin relación ni dupliques servicios por cada variante de pantalla.
- Separa responsabilidades internas de un sistema de las interfaces necesarias para comunicarse con él. No inventes una API por cada tratamiento interno.
- Usa nombres con verbo, objeto y contexto necesario. Comprueba que se entiendan sin leer la descripción.
- Conserva un ID estable y un único nombre por servicio lógico en todos los cuadros. La numeración de filas solo cuenta elementos.
- Registra contratos de interfaces por su nombre real y con su fuente. Si no está disponible, indica «Por definir» y concreta qué debe solicitarse al equipo responsable.
- No conviertas cada intercambio en una API. Usa el mecanismo documentado o acordado, como solicitud/respuesta, evento o archivo; si se desconoce, deja su definición pendiente. No añadas mecanismos por catálogo.
- No determines reutilización, adaptación o creación por semejanza de nombres. Si la decisión requiere operaciones o campos no disponibles, identifica la evidencia faltante para el análisis posterior.

### Paso 4. Construir los cuadros y comprobar el recorrido

1. Separa las capacidades atendidas principalmente dentro de un sistema de las que requieren interacción con otros.
2. Representa cada tramo necesario sin forzar que todas las capacidades pasen por todos los sistemas.
3. Usa la dirección para indicar quién inicia la solicitud o envía la notificación. Distingue ese inicio de la respuesta de regreso.
4. Comprueba que el verbo del extremo corresponda a la flecha. Si un sistema inicia la petición de un reporte, no describas su responsabilidad únicamente como «recibir».
5. Si una capacidad tiene una variante de integración, identifica su condición; no conviertas una alternativa en una decisión adoptada.
6. Verifica que el dato recibido por un sistema no se describa automáticamente como visible para una persona. Registra qué uso falta acordar.
7. Si el intercambio es automático, identifica el evento o condición que lo inicia. Si existe intermediación, documenta sus tramos; si no existe, representa la conexión directa. Respeta las restricciones confirmadas del proyecto.

### Paso 5. Organizar el documento y los pendientes

Lee [references/plantillas.md](references/plantillas.md) y úsalo para redactar el mapa y el registro de pendientes. Adapta sistemas y secciones al proyecto; evita añadir columnas o párrafos que repitan lo ya visible.

Clasifica cada pendiente por la decisión necesaria:

| Categoría | Qué falta resolver |
| --- | --- |
| Arquitectura para estimación | Una responsabilidad, dependencia, alternativa o brecha que afecta la comprensión de la solución y su esfuerzo. |
| Arquitectura detallada | La definición de operaciones, datos, contratos, seguridad, errores, monitoreo o comportamiento técnico. |
| Funcional | El significado de un dato, una regla de negocio, el resultado esperado o quién realiza una actividad del proceso. |

Una pregunta funcional puede afectar la estimación; mantenla en una ubicación principal e indica su efecto si cambia el alcance. Mencionar una API no convierte una pregunta en técnica.

Solicita muestras o escenarios concretos cuando ayuden a resolver una duda. Separa el contenido de negocio de la definición técnica cuando requieran decisiones distintas. Formula pendientes de frecuencia, entrega o confirmación solo cuando sean relevantes para el intercambio; no los copies por analogía con otro proyecto.

La selección preliminar de candidatas puede ser necesaria para estimar; no la aplaces automáticamente hasta el diseño detallado. Reserva la confirmación de cobertura para la evidencia suficiente. «Con quién confirmar» identifica al interlocutor, no una asignación aceptada.

### Paso 6. Revisar antes de entregar

Lee [references/criterios-y-casos.md](references/criterios-y-casos.md) y corrige las inconsistencias detectadas en el alcance autorizado. Verifica vínculos desde la carpeta real del resultado y aplica la firma vigente.

Entrega el archivo con una explicación breve de su alcance y de las decisiones abiertas. No traslades al usuario defectos básicos de nombres, estructura o coherencia que puedas resolver con la evidencia disponible.

## 5. Momento 2: refinar mediante revisión conjunta

1. Relee la sección vigente antes de modificarla e incorpora las ediciones recientes del usuario.
2. Explica qué está cubierto, qué falta y por qué importa. Si revisas un documento anterior, distingue contenido útil, duplicado, superado y ajeno al propósito.
3. Presenta una propuesta concreta de fila o sección cuando falte una decisión del usuario. Aporta criterio si detectas contradicciones; no aceptes automáticamente ni agregues contenido para demostrar iniciativa.
4. Aplica los cambios acordados cuando exista autorización. No repitas una aprobación ya concedida ni amplíes el cambio a documentos excluidos.
5. Revisa todas las apariciones afectadas dentro del documento autorizado: ID, nombre, dirección, alcance y pendientes. Si hay repercusiones en otros archivos, infórmalas sin asumir autorización para editarlos.
6. Conserva explícita la diferencia entre aprobar una propuesta de arquitectura y demostrar la capacidad técnica de los sistemas.
7. Cierra con el ajuste realizado y cualquier decisión que siga abierta. Mantén el documento ligero y evita repetir en prosa sus cuadros.

## 6. Aceptación del resultado

El mapa queda listo para revisión cuando cada responsabilidad tiene sustento o estado propuesto visible; las capacidades están trazadas; los nombres, direcciones y cuadros son consistentes; y los pendientes tienen una pregunta concreta e interlocutor.

La revisión documental no confirma implementaciones ni equivale al cierre de las decisiones de negocio. La aprobación del diseño y las comprobaciones operativas se registran conforme a la gobernanza del proyecto.

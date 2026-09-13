# Decisiones de arquitectura y tradeoffs

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Estado: ADR-01, ADR-02, ADR-03 y ADR-05 propuestos; ADR-04 con incorporación parcial sobre extensión documental. Aprobador: Sr Wolfan.** El retiro de cuotas de líneas responde a su solicitud; no implica aceptación del resto del ADR-04. Los identificadores de hallazgos y cambios incorporados se resuelven en el [diagnóstico](README.md). El diseño resultante está en la [especificación refinada](especificacion_refinada.md).

## ADR-01 — Separar responsabilidades, autoridad y controles

**Contexto:** H01, H02 y H06. Las tres capas son útiles como responsabilidades, pero un archivo local no adquiere autoridad absoluta por declararla. Tampoco una bandera documental demuestra un bloqueo de escritura.

**Decisión propuesta:** conservar Cloud, Global y Scope como capas lógicas. Cloud concentra calidad de razonamiento; Global, identidad y preferencias transversales; Scope, contexto y reglas del proyecto. La precedencia efectiva y los permisos corresponden al entorno de ejecución. Scope especializa preferencias cuando está permitido; ningún skill amplía autorizaciones. La protección documental se acompaña de controles verificables cuando el entorno los permita.

| Alternativa | Beneficio | Costo o limitación |
| --- | --- | --- |
| Scope con autoridad absoluta | Regla muy simple de leer. | No resuelve límites externos y contradice bloqueos superiores. |
| Un único archivo para todo | Reduce puntos de carga. | Mezcla mantenimiento de identidad, proyecto y operación. |
| Tres responsabilidades y adaptación al entorno — recomendada | Permite reutilizar sin fingir una jerarquía universal. | Requiere documentar el mecanismo de carga y los conflictos del entorno elegido. |

**Por qué:** hace explícito qué controla cada pieza y evita prometer seguridad que la documentación no demuestra. Es juicio de diseño de Sam; no se presenta como garantía de un modelo.

**Riesgo controlado:** si solo existe una instrucción de protección, se declara protección documental. No se certifica aislamiento técnico sin una prueba del control externo. No se introduce un motor de permisos propio.

**Acción siguiente y aceptación:** revisar responsabilidades y ejecutar V01, V02 y V06 del [plan](validacion_y_evolucion.md) cuando exista un entorno de prueba autorizado.

**Documentos afectados al incorporar:** blueprint, anatomía y banco de reglas. Revisar también la tesis para eliminar autoridad absoluta y bloqueo físico atribuido al texto.

**Reconsiderar si:** la herramienta destino exige otro empaquetado; las responsabilidades pueden mantenerse aunque cambien los archivos físicos.

## ADR-02 — Enrutar por necesidad y dependencias

**Contexto:** H03 y H04. Descargar instrucciones ya leídas y evitar un supuesto colapso mediante secuencia son garantías sin mecanismo especificado.

**Decisión propuesta:** descubrir capacidades por su descripción, cargar las necesarias y registrar el resultado útil al cambiar de etapa. Mantener ejecución secuencial por defecto y obligatoria cuando haya dependencia. La selección de varias skills no implica crear varios agentes; cualquier delegación requiere habilitación aplicable. No introducir concurrencia en esta iteración.

| Alternativa | Beneficio | Costo o limitación |
| --- | --- | --- |
| Cargar todas las skills | Toda la información queda disponible desde el inicio. | Incorpora instrucciones irrelevantes y aumenta conflictos potenciales. |
| Secuencia universal como garantía cognitiva | Facilita seguir un único flujo. | Su explicación actual no es verificable y fuerza pasos innecesarios. |
| Selección progresiva y dependencia explícita — recomendada | Reduce material irrelevante y conserva trazabilidad entre etapas. | Exige entradas y salidas claras; el ahorro real debe medirse. |

**Por qué:** reemplaza metáforas de memoria por acciones observables. La especificación pública de Agent Skills describe carga progresiva de metadatos, instrucciones y recursos; eso no prueba que se borre contexto previamente cargado. [Fuente primaria](https://agentskills.io/specification).

**Riesgo controlado:** una salida de etapa es insumo sujeto a validación, no verdad incuestionable. Si falta una capacidad obligatoria, se reporta el impedimento; el trabajo independiente puede continuar.

**Acción siguiente y aceptación:** usar V03, V04 y V05. Solo considerar concurrencia futura con una necesidad demostrada y tareas independientes.

**Documentos afectados al incorporar:** tesis, anatomía y banco de reglas.

**Reconsiderar si:** una carga representativa demuestra que la secuencia es un cuello de botella material y el entorno admite coordinación verificable.

## ADR-03 — Portabilidad declarada y comprobada

**Contexto:** H05 y H11. Universalidad de contenido, formato de paquete y carga automática son propiedades diferentes.

**Decisión propuesta:** adoptar un contrato mínimo de skill y mantener separada una ficha de integración por entorno. Comenzar validando un entorno; declarar otro compatible solo después de comprobarlo. Un enlace desde el README asegura navegación documental, no activación automática.

| Alternativa | Beneficio | Costo o limitación |
| --- | --- | --- |
| Declarar universalidad por usar Markdown | No requiere adaptación inicial. | No demuestra dónde ni cómo se leen las instrucciones. |
| Diseñar todo para una sola herramienta | Facilita la primera integración. | Acopla reglas de dominio con detalles del proveedor. |
| Núcleo común y ficha de integración — recomendada | Mantiene reutilización y hace explícitos los límites. | Añade una verificación por entorno, sin construir adaptadores anticipadamente. |

**Por qué:** GitHub documenta diferencias de soporte de instrucciones entre sus propias superficies. Inferencia de diseño: el nombre de un archivo no basta para acreditar carga en cualquier herramienta. [Fuente primaria](https://docs.github.com/en/copilot/reference/custom-instructions-support).

**Riesgo controlado:** no se crea un framework de adaptadores. La primera ficha puede ser una tabla que indique producto, versión o fecha de verificación, entrada, ubicación, precedencia y evidencia.

**Acción siguiente y aceptación:** elegir el primer entorno cuando comience la POC y ejecutar V01, V07 y V10. La elección permanece pendiente; esta revisión no la inventa.

**Documentos afectados al incorporar:** anatomía, blueprint y backlog de despliegue.

**Reconsiderar si:** el proyecto decide atender exclusivamente una herramienta, manteniendo documentadas las dependencias.

## ADR-04 — Promover por evidencia y no por ubicación

**Contexto:** H07, H08 y H12. Carpeta, longitud y existencia de archivos no prueban que un diseño funcione.

**Decisión propuesta:** distinguir propuesta, aprobación de diseño, validación operativa y disponibilidad para uso. Exigir un resultado observable por capacidad, pruebas representativas y registro de limitaciones antes de certificarla.

**Ajuste incorporado el 2026-09-12:** eliminar mínimos, máximos y objetivos de líneas del Scope. Se evalúan cobertura de responsabilidades, claridad, ausencia de contradicciones y duplicaciones, y ubicación adecuada del detalle. Solicitado por el Sr Wolfan; el resto de este ADR sigue propuesto.

**Corrección de criterio:** la cifra de 60 líneas provenía de la anatomía original. No se encontró una justificación documentada. Sam la mantuvo inicialmente como orientación; esta revisión retira también esa recomendación. No se sustituye por otra cifra.

| Alternativa de extensión | Beneficio | Tradeoff |
| --- | --- | --- |
| Límite numérico obligatorio | Fácil de contar. | Puede forzar omisiones o compresión y no demuestra calidad. |
| Cifra orientativa | Permite excepciones. | Mantiene un objetivo sin fundamento que condiciona la redacción. |
| Criterios de contenido sin cuota — incorporada | Ajusta la extensión al problema y conserva lo necesario. | Requiere revisar redundancia y responsabilidades en vez de contar líneas. |

| Alternativa | Beneficio | Costo o limitación |
| --- | --- | --- |
| Certificar por carpeta y longitud | Comprobación muy barata. | Puede aceptar un archivo corto, incompleto o inoperante. |
| Evaluación exhaustiva multientorno antes del primer skill | Amplia cobertura inicial. | Retrasa aprender con un caso real y multiplica trabajo prematuro. |
| POC pequeña y promoción con evidencia — recomendada | Detecta fallas importantes con inversión acotada. | No permite extrapolar el resultado a entornos no probados. |

**Por qué:** el primer skill debe validar el contrato del conjunto, no inaugurar un catálogo grande. Es juicio de diseño de Sam basado en los vacíos declarados por el proyecto.

**Riesgo controlado:** un diseño puede aprobarse antes de implementarse, pero queda marcado como no validado operativamente. La palabra certificado requiere entorno, revisión y resultados identificables.

**Acción siguiente y aceptación:** adoptar las etapas y escenarios del [plan](validacion_y_evolucion.md). No marcar pruebas como ejecutadas por haberlas documentado.

**Documentos afectados al incorporar:** hoja de ruta, backlog, blueprint y criterios de aceptación de la anatomía.

**Reconsiderar si:** los riesgos del primer caso requieren controles adicionales; ampliar las pruebas por riesgo, no por número de documentos.

## ADR-05 — Reglas proporcionales, verificables y con origen

**Contexto:** H09, H10 y H11. El catálogo mezcla obligaciones, preferencias, prácticas de fábrica y afirmaciones sin fuente comprobable.

**Decisión propuesta:** cada regla tiene un dueño, una condición de aplicación y un resultado verificable. Diferenciar obligatorio, recomendado y opcional. Identificar las propuestas propias y respaldar afirmaciones externas con una fuente concreta. Solicitar aprobación de cambios estructurales o ampliaciones de alcance, aprovechando la autorización ya concedida para el trabajo acordado.

| Alternativa | Beneficio | Costo o limitación |
| --- | --- | --- |
| Convertir todas las frases en prohibiciones | Produce uniformidad superficial. | Oculta excepciones necesarias y multiplica conflictos. |
| Mantener solo principios generales | Documentación breve. | Deja sin resolver conductas críticas. |
| Normas según riesgo y condición — recomendada | Conserva límites claros y margen para tareas distintas. | Requiere decidir qué merece ser obligatorio. |

**Por qué:** RFC 2119 distingue requisitos, recomendaciones y opciones, y pide moderación al imponer mandatos. Se adopta esa distinción como criterio editorial local, sin reclamar conformidad normativa de esta fábrica con un protocolo IETF. [Fuente primaria](https://www.rfc-editor.org/info/rfc2119/).

**Riesgo controlado:** la proporcionalidad no debilita permisos ni autorizaciones. Los separadores se usan para legibilidad; no se les atribuye reinicio de atención ni prevención garantizada de errores.

**Acción siguiente y aceptación:** revisar las 37 reglas con su [disposición propuesta](revision_banco_reglas.md), comprobar V08 y V09 y decidir los ADR como conjunto o individualmente.

**Documentos afectados al incorporar:** principios, banco de reglas y borradores del backlog.

**Reconsiderar si:** una regla flexible produce ambigüedad comprobada; precisar su condición y evidencia antes de volverla absoluta.

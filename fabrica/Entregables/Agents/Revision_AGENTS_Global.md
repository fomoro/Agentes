# Revisión de conservación de la gobernanza global

- Actualizado: el 2026-09-18 10:32
- Rol de ejecución: Arquitecto de IA e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr. Wolfan)

Se contrasta el [original](../../../Insumos/Agents/Base/AGENTS_Global.md) con el [refinado](AGENTS_Global_Refinado.md). Este registro documenta la revisión; no agrega instrucciones al asistente.

## Criterio aplicado

La independencia de una plataforma o proyecto no exige eliminar principios ni preferencias personales. Se conservan los principios explícitos; las reglas de disciplina indican cuándo aplican. Se retiran de la base las recetas que fuerzan una implementación concreta, con justificación y sin atribuirles un traslado inexistente.

## Correspondencia con el original

| Regla o grupo original | Resultado | Ubicación y razón |
| :--- | :--- | :--- |
| Configuración única, referencias entre claves y consulta de valores | Conservado y precisado | §1: conserva los cuatro valores del archivo original y detecta ciclos y errores. |
| Nunca imprimir claves o marcadores | Mejorado | §1: los permite en configuraciones, plantillas y diagnósticos; exige resolverlos en salidas finales. |
| Asistente principal del Sr Wolfan | Conservado con distribución | §2 identifica al asistente desde la configuración; §6 conserva la relación personal en la firma vigente. |
| Catálogo de trece roles, incluidos Notion y recaudo | Retirado por decisión aprobada | §2 selecciona responsabilidades sin catálogo cerrado. No se trasladaron roles a skills. |
| Selección automática, prioridad específica, combinación y declaración de roles | Conservado | §2: responsabilidades según la tarea, sin credenciales ni permisos implícitos. |
| Enfoque pragmático y orientado a resultados | Recuperado explícitamente | §3, Enfoque. |
| Comunicación ejecutiva, tuteo bogotano, sin emojis ni muletillas | Recuperado | §3 fija el principio; §6 expresa la preferencia personal y sus excepciones por contexto. |
| Veracidad, hechos, supuestos, inferencias, riesgos y pendientes | Recuperado y precisado | §3: aplica cuando afecten el resultado o cambie una decisión. |
| KISS, YAGNI, DRY, Least Surprise y evitar sobreingeniería | Recuperado literalmente en intención | §3, Simplicidad: los cuatro principios quedan nombrados. |
| Aplicabilidad de roles, marcos, formatos y gobierno | Conservado | §3: utilidad o exigencia obligatoria del contexto. |
| Qué, por qué, riesgo y acción siguiente | Conservado y ampliado | §3 conserva el principio; §5 lo implementa con plantilla y estado de decisión. No presume que un riesgo ya está controlado. |
| Utilidad, simplicidad y trazabilidad suficiente | Recuperado y centralizado | §5, Validación y cierre, conserva los tres criterios explícitos; §3 mantiene el principio por referencia. |
| Precedencia específica sobre general y especialización local | Precisado | §3: respeta autoridad efectiva, permisos y protecciones expresas. |
| Skills sin ampliación de autoridad o permisos | Conservado y ampliado | §3: tratamiento de conflictos; §7: selección y uso. |
| Aclarar información material, asumir incertidumbre menor y no repetir confirmaciones | Conservado | §4, Intención, alcance y autorización. |
| Análisis consultivo y ejecución por solicitud | Conservado y precisado | §4: una solicitud de implementación autoriza el código necesario; una consulta conceptual no lo hace automáticamente. |
| Plan previo: alcance, responsabilidades, dependencias, riesgos y estrategia | Recuperado y centralizado | §5, Proporcionalidad, incluye los cinco elementos y validación; §4, Software y código, remite a esa regla. |
| Soluciones completas, sin fragmentos inconexos | Recuperado | §4, Coherencia del trabajo; limitado al alcance solicitado. |
| SOLID, Demeter, ADP; Feature Envy, Magic Values y estado mutable | Recuperado y precisado | §4: SOLID y Demeter se aplican según responsabilidades y dependencias, evitando abstracciones sin necesidad en el alcance. ADP se expresa como «evita dependencias cíclicas entre módulos o paquetes, tanto directas como indirectas». Feature Envy, Magic Values y estado mutable innecesario se conservan en una regla aparte de Software y código. |
| Guard clauses y DTO/Record | Recuperado | §4: preferencia condicionada a menor complejidad y compatibilidad con el lenguaje y diseño. |
| Clases menores a 400 líneas y métodos menores a 30 | Conservado como heurística con valores actualizados | §4: la versión vigente usa clases menores a 500 líneas y métodos menores a 40. Se mantienen como referencias de revisión, sin rechazo automático ni fragmentación artificial. |
| Comparación: inconsistencias, contradicciones, exceso de detalle y vacíos | Recuperado completo | §4, Coherencia del trabajo. |
| Cambios: qué cambió, qué se mantuvo, qué se hizo bien y efectos | Recuperado | §6, Entregables; se comunica cuando aporta a evaluar el cambio. |
| Guías con regla práctica, ruta, pasos, ejemplo y lista de verificación | Recuperado | §6, Presentación; se incluyen las partes necesarias. |
| No convertir supuestos en decisiones | Conservado | §3, Criterio; §5 distingue propuesta y confirmación. |
| Nombres significativos, término consistente, evitar ambigüedad y responsabilidades ficticias | Recuperado completo | §4, Coherencia del trabajo. |
| Claridad sobre brevedad | Recuperado explícitamente | §4, Coherencia del trabajo. |
| Caso de Estudio, POC, MVP, Piloto y Proyecto Formal | Recuperado | §5: referencias cuando ayudan a decidir y el proyecto no define otras; no son una secuencia obligatoria. |
| Arquitectura de estimación, detallada y evaluación | Recuperado | §5: selección por resultado requerido. |
| ADR para decisiones estructurales, difíciles de revertir o transversales | Recuperado | §5: registro equivalente permitido; no exige un archivo adicional. |
| TOGAF pragmático para capacidades, dominios, objetivo y transición | Recuperado | §5: condicionado a valor, sin imponer todos sus artefactos. |
| Markdown y prioridad del formato solicitado | Recuperado explícitamente | §6, Presentación. |
| WhatsApp y Teams: continuidad, 220 caracteres y Pregunta: Respuesta | Recuperado y aclarado | §6: límite flexible; Pregunta: Respuesta aplica al responder, sin fabricar respuestas al preguntar. |
| Correo: asunto, cuerpo, brevedad y cortesía | Conservado | §6, Presentación. |
| Visualizaciones útiles y sugerencia de Mermaid | Recuperado | §6: Mermaid es una opción si el destino lo admite. |
| Bloques de código reservados para sintaxis | Conservado | §6, Presentación. |
| Receta MVP HTML: mobile-first, Bootstrap CDN, Hero → Valor → CTA único y código embebido | Retirada de la base | Impone decisiones de interfaz e implementación que no corresponden a todo MVP. Sigue disponible en el original; no fue trasladada a una skill. |
| C4: inicio obligatorio flowchart TD y subgraph solo como frontera | Retirado de la base | Convención de representación concreta. Sigue en el original; no fue trasladada. |
| C4: elementos obligatorios del nivel 2 y conexiones del nivel 3 | Retirado como receta fija | Debe definirse y validarse en el método de diagramación aplicable. §6 exige respetar la semántica elegida; no reproduce la receta ni afirma equivalencia completa. |
| Relaciones con protocolos relevantes | Conservado con generalización | §6: identifica interfaces y protocolos con evidencia, sin imponer una lista cerrada. |
| Solicitud exclusivamente C4: solo diagrama | Conservado y ampliado | §6: aplica a cualquier solicitud exclusivamente de diagrama. |
| Firma en lista, actualización sin duplicar, exclusión de conversación rutinaria | Conservado y actualizado | §6: incorpora la instrucción vigente de fecha y hora y «Asistente IA del Sr. Wolfan»; protege formatos incompatibles con la cabecera. |
| Consultar Scope antes de actuar, cargar solo skills pertinentes y continuar si faltan rutas | Conservado y precisado | §7 distingue ausencia de archivo de imposibilidad de lectura. |
| No inventar skills, reglas o comportamientos ausentes | Conservado | §3 exige evidencia; §7 prohíbe inventar skills o capacidades. |
| Modificar gobernanza solo por solicitud y con controles locales | Conservado y centralizado | §4 establece solicitud explícita y controles aplicables, sin desactivarlos; §7 remite a esa autorización. |
| Revalidar ante cambio de proyecto o evidencia de cambios | Conservado | §7, Contexto del proyecto. |
| Roles y skills no implican delegación concurrente automática | Recuperado explícitamente | §7; §4 condiciona el uso de agentes a autorización, entorno y tarea verificable. |

## Mejoras del refinado que se conservan

- Comprobación del estado antes de modificar, respeto del trabajo previo y preferencia por recuperación verificable.
- Verificación antes de repetir acciones con resultados ambiguos y reintentos justificados por evidencia.
- Distinción entre información e instrucciones; conflictos limitados a la parte del trabajo afectada.
- Cierre basado en evidencia y criterios de aceptación, sin afirmar éxito con requisitos pendientes.
- Revisión de gobernanza con conservación de intención y destinos comprobados para traslados.

## Depuración de repeticiones

| Tema | Regla principal | Referencias y condiciones conservadas |
| :--- | :--- | :--- |
| Autorización | §4, Intención, alcance y autorización | §1 y §7 remiten a ella. Incluye continuidad de permisos, cambios de gobernanza y su configuración, skills, acciones destructivas y ausencia de aprobaciones por etiquetas. La solicitud explícita para configuración se refiere a la gobernanza; no agrega una aprobación para configurar aplicaciones dentro de una implementación autorizada. §3 conserva la jerarquía de autoridad, que cumple una función distinta. |
| Proporcionalidad | §5, Proporcionalidad | §4 remite para planificar software. Una sola regla dimensiona planificación, documentación, revisión y comprobaciones; conserva controles obligatorios y planificación de cambios relevantes. |
| Validación | §5, Validación y cierre | §3 remite como principio, §4 al completar una ejecución y §6 al comunicar el cierre. §7 agrega referencias, configuración y coherencia como comprobaciones específicas. |

Se conservan las comprobaciones previas a editar o reintentar, los criterios técnicos y las condiciones particulares de iniciativas y arquitectura. No son repeticiones del cierre: regulan decisiones o momentos distintos. Las referencias a secciones son breves y no requieren consultar este registro para ejecutar la gobernanza.

## Precisiones de la revisión completa

- La plantilla de decisiones se activa cuando el efecto en alcance, costo, riesgo o dirección es material, en coherencia con el principio de Decisiones.
- Si no existe un registro acordado, la decisión material se documenta en la respuesta o entregable correspondiente. Para arquitectura se conserva la regla específica de ADR.
- Los valores vigentes de 500 líneas por clase y 40 por método se conservan; la tabla de correspondencia identifica la diferencia frente a los valores originales.

## Límites y verificación

- No se crearon ni modificaron skills ni gobernanza local. Ninguna retirada figura como traslado realizado.
- El archivo original se conserva. La configuración de la propuesta mantiene la identidad que ya contenía el original; Sam firma como autor de esta revisión, no como cambio de esa configuración.
- Se mantienen siete secciones principales y la eliminación aprobada del catálogo de roles.
- La revisión comprueba cobertura textual y coherencia de instrucciones; no constituye una prueba de obediencia en ejecución de un modelo.

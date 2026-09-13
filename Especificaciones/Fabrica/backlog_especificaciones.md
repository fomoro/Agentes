# Backlog de especificaciones

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

El backlog conserva únicamente pendientes con una condición de cierre y una síntesis de asuntos resueltos. El trabajo actual es el prototipo del Scope. Los documentos de Auditorías permanecen como contexto histórico, sin tareas obligatorias de actualización.

## 1. Pendientes del Scope

| Pendiente | Qué falta | Condición de cierre |
| --- | --- | --- |
| Alinear el prototipo | Aplicar la anatomía y seleccionar reglas coherentes del banco. | Prototipo revisado contra la [especificación](../Scope/especificacion_scope.md). |
| Concretar el proyecto de prueba | Elegir una carpeta destino independiente de la fábrica y registrar versión de Codex y permisos. | Ficha de [validación local](../Scope/validacion_scope_codex_local.md) completada. |
| Validar el comportamiento | Ejecutar los casos de carga, conflicto, ausencia de skill y modificación de gobernanza. | Resultados observados y limitaciones registrados; no basta con definir los casos. |
| Revisar las reglas heredadas antes de seleccionarlas | El banco conserva reglas anteriores sobre autoridad absoluta, descarga de memoria y estilos obligatorios. | Las reglas elegidas para el prototipo respetan el contrato actual y no introducen contradicciones. No exige reescribir todo el banco. |

## 2. Vacíos de diseño pendientes

| Tema | Estado real | Próxima decisión o condición de cierre |
| --- | --- | --- |
| Global y Cloud | Fuera del foco actual; su anatomía completa no está resuelta en Especificaciones. | Determinar si se requieren como entregables propios después del Scope. No bloquea definir sus límites de interacción actuales. |
| Inicializador | Pendiente para despliegue posterior. La primera prueba puede prepararse manualmente. | Definir entradas, conflictos, repetición y recuperación antes de implementarlo; no es requisito del prototipo. |
| Skill Cero | Etapa 2, pendiente. No es un vacío de anatomía del Scope. | Elegir un caso y construir un módulo después de cerrar el primer entregable. |
| Trazabilidad histórica del banco | Las cinco reglas recientes tienen fuentes OpenAI verificadas; las otras atribuciones no se han auditado individualmente. | Identificar la fuente concreta de las reglas heredadas que se decida utilizar. |

Autoridad y protección dejaron de ser un vacío de diseño: están especificadas en B y D del Scope. Su comprobación operativa sigue pendiente en la sección 1. Compatibilidad se acotó a Codex local por elección del Sr Wolfan; falta validarla, no volver a elegir el entorno.

## 3. Resuelto en diseño

| Asunto | Resultado y fuente vigente |
| --- | --- |
| Mezcla de principios transversales y particulares | [Principios de fábrica](principios_fabrica.md) transversales; anatomía y enrutamiento en Scope; empaquetado en skills. |
| Organización y nombres | [Estructura del repositorio](estructura_repositorio.md) contrastada con carpetas existentes; títulos y nombres alineados. |
| Anatomía del Scope | Cuatro responsabilidades y criterios en la [especificación](../Scope/especificacion_scope.md), sin cuotas de líneas ni universalidad garantizada. |
| Autoridad y protección documental | Límites del entorno y autorización explícita en secciones B y D del Scope; sin atribuir un bloqueo físico al texto. |
| Primer entorno y diseño de comprobación | Codex en proyecto local, seleccionado por el usuario; mecanismo y escenarios en [validación local](../Scope/validacion_scope_codex_local.md). |
| Co-creación y cinco reglas nuevas | Incorporadas al banco; atribución de las cinco como adaptaciones de recomendaciones oficiales de OpenAI. |

## 4. Borradores anteriores y cierre

- Co-creación: el criterio transversal ya está resuelto en los principios; su eventual incorporación a Cloud depende de retomar esa capa.
- Auditoría por lenguaje binario y separadores: no se adopta como criterio de calidad. La claridad y la comprobación del resultado están definidas en los principios; las formulaciones heredadas del banco se revisan al seleccionarlas.
- Documentos sin referencias: navegación resuelta en el README y comprobación de enlaces. La carga efectiva se valida aparte; un enlace no prueba activación.
- Aprobación entre cada subtarea: no se exige para trabajo ya autorizado. Se mantiene la decisión humana sobre cambios materiales y cierre del entregable.
- Retrospectiva: después de validar Scope y skills, incorporar aquí únicamente fallos o vacíos nuevos con condición de cierre. No genera un registro adicional en Auditorías.

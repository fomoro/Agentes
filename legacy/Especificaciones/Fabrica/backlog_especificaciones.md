# Backlog de especificaciones

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

El backlog contiene únicamente trabajo pendiente con una condición de cierre. El foco actual es el prototipo del Scope. Los documentos de Auditorías permanecen como contexto histórico, sin tareas obligatorias de actualización.

## 1. Pendientes del Scope

| Pendiente | Qué falta | Condición de cierre |
| --- | --- | --- |
| Alinear el prototipo | Aplicar la anatomía y seleccionar reglas coherentes del banco. | Prototipo revisado contra la [especificación](../Scope/especificacion_scope.md). |
| Concretar el proyecto de prueba | Elegir el asistente y una carpeta destino independiente; documentar su mecanismo de carga y sus controles. | [Validación por entorno](../Scope/validacion_scope_por_entorno.md) completada con evidencia. |
| Validar el comportamiento | Ejecutar los casos de carga, conflicto, ausencia de skill y modificación de gobernanza. | Resultados observados y limitaciones registrados; no basta con definir los casos. |
| Revisar las reglas heredadas antes de seleccionarlas | El banco conserva reglas anteriores sobre autoridad absoluta, descarga de memoria y estilos obligatorios. | Las reglas elegidas para el prototipo respetan el contrato actual y no introducen contradicciones. No exige reescribir todo el banco. |

## 2. Pendientes posteriores

| Pendiente | Cuándo abordarlo | Condición de cierre |
| --- | --- | --- |
| Definir Global y Cloud | Después de cerrar el Scope, si se confirma que deben mantenerse como entregables propios. | Responsabilidad, contenido, relación con el Scope y criterios de aceptación definidos. |
| Diseñar el inicializador | Después de validar manualmente el Scope en un proyecto destino. | Entradas, conflictos, repetición, recuperación y resultado esperado especificados antes de implementarlo. |
| Construir el Skill Cero | Etapa 2, después de cerrar el primer entregable. | Caso seleccionado, módulo construido y validado contra la especificación de skills. |
| Completar la trazabilidad del banco | Antes de incorporar al prototipo una regla heredada cuya procedencia sea relevante para decidir. | Fuente concreta identificada o regla marcada explícitamente como criterio interno sin respaldo externo verificado. |
| Ejecutar la retrospectiva | Después de validar el Scope y las skills. | Fallos o vacíos nuevos incorporados al backlog con responsable lógico y condición de cierre. |

## 3. Criterios de gestión

- Retirar una entrada cuando su condición de cierre esté cumplida; el backlog no conserva historial de asuntos resueltos.
- Registrar el resultado vigente en la especificación que corresponda, sin trasladarlo a otro documento solo para conservar memoria del cambio.
- Añadir un pendiente únicamente cuando describa una acción futura concreta y una condición verificable de cierre.
- Mantener separados el foco actual y las etapas posteriores. Un pendiente posterior no bloquea el Scope salvo que sea una dependencia explícita.
- No tratar borradores, auditorías o ideas descartadas como trabajo pendiente. Si una decisión cambia, formular la nueva acción necesaria en lugar de conservar su discusión histórica.

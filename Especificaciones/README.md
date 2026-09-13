# Especificaciones de la Fábrica de Agentes

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

## Trabajo actual: prototipo del Scope

La fábrica tiene dos entregables principales: primero el Scope y después las skills. Estamos en el primero. La anatomía está definida; queda alinear y validar el prototipo existente.

Ruta de lectura:

1. [Principios de la fábrica](Fabrica/principios_fabrica.md): criterios de diseño y trabajo.
2. [Especificación del Scope](Scope/especificacion_scope.md): contenido, responsabilidades y aceptación.
3. [Banco de reglas](Gobernanza/banco_reglas_gobernanza.md): seleccionar únicamente lo pertinente al Scope.
4. [Prototipo existente](../Capacidades/Propuestas/Propuestas_Scope/prototipo_AGENTS_Scope.md): pieza pendiente de alineación con la especificación actual.

El [fundamento del Scope como enrutador](Scope/fundamento_scope_enrutador.md) es una explicación complementaria del diseño. La [validación en Codex local](Scope/validacion_scope_codex_local.md) define cómo comprobar el prototipo en el primer entorno elegido; todavía no se han ejecutado las pruebas.

## Organización por propósito

| Carpeta | Responsabilidad | Documentos |
| --- | --- | --- |
| Fabrica | Diseño y gestión de la propia fábrica. | [Principios](Fabrica/principios_fabrica.md), [estructura del repositorio](Fabrica/estructura_repositorio.md), [hoja de ruta](Fabrica/hoja_de_ruta.md) y [backlog](Fabrica/backlog_especificaciones.md). |
| Gobernanza | Reglas compartidas disponibles para seleccionar. | [Banco de reglas](Gobernanza/banco_reglas_gobernanza.md). |
| Scope | Primer entregable: contrato del Scope. | [Especificación](Scope/especificacion_scope.md), [fundamento del Scope como enrutador](Scope/fundamento_scope_enrutador.md) y [validación en Codex local](Scope/validacion_scope_codex_local.md). |
| Skills | Segundo entregable: capacidades especializadas. | [Especificación de skills](Skills/especificacion_skills.md), reservada para la siguiente etapa. |

Las especificaciones contienen diseño; los prototipos y paquetes se mantienen en Capacidades. Auditorías se conserva como contexto histórico y no requiere actualizaciones durante el trabajo actual. Sus referencias reflejan la organización existente cuando se escribió.

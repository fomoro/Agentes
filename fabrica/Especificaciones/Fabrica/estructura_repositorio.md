# Estructura del repositorio

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

Este documento describe las carpetas, su contenido y su estado observado. No pretende ser una arquitectura completa de ejecución. La anatomía del producto se mantiene en la [especificación del Scope](../Scope/especificacion_scope.md).

## 1. Carpetas principales

| Carpeta | Propósito | Regla de ubicación |
| --- | --- | --- |
| Especificaciones | Diseño y criterios para construir. | Documentos de referencia vigentes; no prototipos operativos. |
| Capacidades | Gobernanzas y módulos reutilizables. | Piezas y prototipos; estar en una carpeta no acredita certificación. |
| Insumos | Material histórico y fuentes de rescate. | Antecedentes que requieren selección antes de reutilizarse. |
| Auditorias | Contexto de revisiones anteriores. | Se conserva intacta por instrucción del usuario; no requiere nuevos registros. |

## 2. Organización de Especificaciones

| Carpeta | Contenido |
| --- | --- |
| Fabrica | Principios transversales, estructura del repositorio, hoja de ruta y backlog. |
| Gobernanza | Banco de reglas compartido, del cual se selecciona lo pertinente. |
| Scope | Especificación, fundamento del enrutador y validación local del primer entregable. |
| Skills | Especificación reservada para el segundo entregable. |

El [README](../README.md) ofrece la ruta de lectura. Los principios particulares de cada entregable se mantienen en su especificación, no se duplican en los principios de la fábrica.

## 3. Estado observado de Capacidades

Inspección del 2026-09-13. No se modificó esta carpeta.

| Ruta | Estado observado | Interpretación |
| --- | --- | --- |
| Base | Contiene archivos Global, Cloud y Scope; Scope está vacío. | No se puede afirmar que la gobernanza esté terminada por su ubicación. |
| Propuestas/Propuestas_Scope | Contiene el prototipo del Scope. | Pendiente de alineación con la especificación actual. |
| Propuestas/Propuestas_Cloud y Propuestas/Propuestas_Global | Carpetas sin archivos. | No hay prototipos disponibles allí en esta revisión. |
| Propuestas/Propuestas_Skills | Carpeta sin archivos. | Construcción de skills pendiente. |
| Especificas | Carpeta sin archivos. | Su uso no está definido para el trabajo actual; no se le asigna una función por inferencia. |

Las carpetas de prueba y de capacidades activas aparecían en el plano anterior, pero no existen en el estado inspeccionado. No son requisito del prototipo actual; su eventual creación depende de definir y necesitar ese ciclo de publicación.

## 4. Nombres y referencias

- Usar nombres que describan el propósito real y coincidan semánticamente con el título.
- Mantener enlaces relativos entre documentos vigentes y comprobarlos después de mover o renombrar archivos.
- Los enlaces de Auditorías son históricos y pueden conservar ubicaciones anteriores; no se actualizan como parte del mantenimiento actual.

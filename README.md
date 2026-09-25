# Fábrica de Agentes Locales

> **Actualizado:** 2026-09-24
> **Rol de ejecución:** Arquitecto de información
> **Autor:** Jeff (Asistente IA del Sr. Wolfan)

## 1. Objetivo

Entorno para estructurar, estandarizar y empaquetar enrutadores inteligentes (`AGENTS_Scope.md`) y sus herramientas (`SKILL.md`), listos para instalarse en proyectos destino.

## 2. Estructura de la Fábrica

El repositorio está organizado según el flujo de producción:

- **`Input\`**: Fuentes, referencias y materiales de entrada.
- **`Generator\`**: Línea de ensamblaje con los planos y manuales de construcción.
  - **`.rules\`**: Reglas internas de operación para la fábrica.
  - **`Agents\`**: Laboratorio de diseño del producto final.
    - `.rules\`: Reglas de comportamiento exportables.
    - `Global\`: Define el **Agente Global** (comportamiento universal y marco de responsabilidades).
    - `Local\`: Define el **Agente Local** (`AGENTS_Scope.md`). Es el enrutador que evalúa la orden y selecciona el skill.
    - `Skills\`: Herramientas, plantillas y paso a paso técnico (`SKILL.md`) para ejecutar la tarea.
- **`Proto\` y `Reviews\`**: Entornos para pruebas de concepto y auditorías.
- **`Export\`**: Productos terminados y listos para instalarse en el proyecto del cliente.

## 3. Extensiones recomendadas

- [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme/blob/main/README.md): `Ctrl+Shift+P` → `Material Icons: Activate Icon Theme`.
- [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf): `Ctrl+Shift+P` → `Markdown PDF: Export (pdf)`.

## 4. Trabajo documental en este proyecto

Antes de crear o modificar documentos, consulta la gobernanza global vigente del asistente y las [reglas de Generator](Generator/.rules/Reglas_Operacion.md). Comprueba qué contenido ya tiene una fuente vigente; edita solo esa fuente y crea otro archivo únicamente si cumple una función distinta. Escribe lo necesario para decidir, ejecutar o verificar, sin repetir instrucciones generales.

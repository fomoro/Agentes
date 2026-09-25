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
    - `Local\`: Define el **Agente Local** (`AGENTS_Scope.md`). Es el enrutador que evalúa la orden y selecciona el skill.
    - `Skills\`: Manual de trabajo para el asistente.
      - `Especificaciones\`: Define la estructura obligatoria del skill.
      - `Procesos\`: Paso a paso para construir el skill y guía para validarlo en entorno controlado.
- **`Proto\`**: Borradores y pruebas de concepto de agentes y skills, organizados en `Global\`, `Local\` y `Skills\`.
- **`Reviews\`**: Auditorías.
- **`Export\`**: Productos terminados y listos para instalarse en el proyecto del cliente.

## 3. Uso de la Fábrica

- **Diseñar un Skill:** Sigue el [plantilla de creación](Proto\Skills\_PLANTILLA_SKILL.md).

## 4. Extensiones recomendadas

- [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme/blob/main/README.md): `Ctrl+Shift+P` → `Material Icons: Activate Icon Theme`.
- [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf): `Ctrl+Shift+P` → `Markdown PDF: Export (pdf)`.

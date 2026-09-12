# Gobernanza local: Agentes especializados

## 1. Propósito

Este archivo identifica los agentes especializados disponibles en el proyecto y establece las reglas comunes para seleccionarlos y coordinarlos. Cada agente delega su ejecución detallada en las skills y referencias que le correspondan.

Cuando se incorpore un nuevo agente, debe registrarse en la sección **Agentes especializados del proyecto** con su responsabilidad, ámbito y skill principal.

**Autor de entregables:** Sam

Este campo es la fuente canónica del nombre de autor que deben usar las skills del proyecto. Su valor puede cambiar sin modificar las skills.

## 2. Precedencia y Gobernanza Local

La gobernanza local complementa las reglas globales y prevalece únicamente cuando define una instrucción más específica para este proyecto o una de sus carpetas.

Al trabajar sobre una carpeta:

1. Identifica el agente responsable según este archivo.
2. Aplica sus responsabilidades y criterios de salida.
3. Consulta en `skills/` únicamente las skills relevantes para la tarea.
4. Mantén las reglas globales que no entren en conflicto con la gobernanza local.

Ante solapamiento entre agentes, prioriza el más específico al contexto de la tarea. Combina agentes o skills únicamente cuando sus responsabilidades sean complementarias.

## 3. Agentes Especializados del Proyecto

- **Agente 1: Diagramador de Arquitectura (`skills/diagramador-arquitectura/`)**
  - **Responsabilidad:** convertir información de negocio o técnica confirmada en fichas estructuradas y diagramas Draw.io válidos, editables, trazables y estandarizados.
  - **Ámbito:** creación, actualización y revisión de diagramas de arquitectura de solución o integración.
  - **Skill principal:** `diagramador-arquitectura`.
  - **Criterio de salida:** ficha y Draw.io coherentes entre sí, conformes con el estándar aplicable y guardados en el caso o proyecto activo.

## 4. Separación de Responsabilidades

- **`AGENTS.md`:** registra agentes, responsabilidades, ámbitos y reglas de coordinación.
- **`SKILL.md`:** define propósito, activación, flujo, restricciones, salidas y criterios de cierre de una capacidad específica.
- **`references/`:** contiene estándares, catálogos y reglas técnicas consultadas por una skill.
- **`scripts/`:** contiene automatizaciones determinísticas reutilizables.
- **`assets/`:** contiene recursos que forman parte de los entregables.

## 5. Principios Comunes

- Respeta el alcance y las decisiones explícitas del usuario.
- No inventes datos, componentes, relaciones ni decisiones.
- Aplica KISS y evita complejidad que no cambie el resultado.
- Mantén trazabilidad suficiente entre fuentes, decisiones y entregables.
- Cuando un agente genere artefactos para un caso o proyecto, guárdalos en ese ámbito y no en este repositorio, salvo instrucción explícita en contrario.

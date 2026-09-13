# Directorio de Especificaciones y Diseño

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Propósito de la Carpeta:** Centralizar el diseño arquitectónico (el "Qué" y el "Cómo"). Ningún archivo aquí contiene lógica ejecutable; todos son planos, definiciones y mapas de la Fábrica de Agentes.

---

## Índice Topológico

Para mantener la pureza y el Principio de Responsabilidad Única, las especificaciones están agrupadas en 3 áreas semánticas:

### 1. `Arquitectura/` (El "Qué construimos")
Centraliza las decisiones de alto nivel y el diseño estructural del sistema.
- [Plano arquitectónico](Arquitectura/plano_arquitectonico_Blueprint.md): mapa de carpetas y responsabilidades.
- [Banco de reglas](Arquitectura/banco_reglas_gobernanza.md): catálogo de reglas de gobernanza.

### 2. `Estrategia_y_Gobierno/` (El "Cómo trabajamos")
Centraliza el meta-proceso y la gestión interna de la Fábrica.
- [Principios de la fábrica](Estrategia_y_Gobierno/principios_fabrica.md): criterios de diseño y trabajo.
- [Hoja de ruta](Estrategia_y_Gobierno/hoja_de_ruta.md): avance y fases del proyecto.
- [Backlog](Estrategia_y_Gobierno/backlog_especificaciones.md): ideas, pendientes y reglas en borrador.

### 3. `Anatomia_y_Plantillas/` (El "Estándar Técnico")
Centraliza la especificación técnica de bajo nivel para los entregables.
- [Especificación de estructuras](Anatomia_y_Plantillas/especificacion_estructuras.md): anatomía y aceptación de Scope y skills.
- [Tesis del patrón Router](Anatomia_y_Plantillas/tesis_patron_router.md): fundamento del Scope como enrutador.

---

## Auditorías y trazabilidad

Las revisiones se alojan en [Auditorías](../Auditorias/README.md), separadas de las especificaciones vigentes. La [auditoría de Sam](../Auditorias/Sam/README.md) contiene diagnóstico, cinco ADR, diseño candidato, revisión del banco y plan de validación.

**Ajustes incorporados:** ubicación de auditorías y eliminación del límite de líneas del Scope, por solicitud del Sr Wolfan. Los demás cambios de arquitectura continúan como propuestas; el registro de incorporación se mantiene en la auditoría.

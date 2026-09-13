# Directorio de Especificaciones y Diseño

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

**Propósito de la Carpeta:** Centralizar el diseño arquitectónico (el "Qué" y el "Cómo"). Ningún archivo aquí contiene lógica ejecutable; todos son planos, definiciones y mapas de la Fábrica de Agentes.

---

## Índice Topológico

Para mantener la pureza y el Principio de Responsabilidad Única, las especificaciones están agrupadas en 3 áreas semánticas:

### 1. `Arquitectura/` (El "Qué construimos")
Centraliza las decisiones de alto nivel y el diseño estructural del sistema.
- **`plano_arquitectonico_Blueprint.md`:** El mapa oficial de las carpetas y reglas de contenido.
- **`tesis_arquitectura_scope.md`:** El registro de decisiones (ADR) con los pros y contras de cada diseño de Scope.
- **`banco_reglas_gobernanza.md`:** El catálogo o "menú" maestro de reglas de gobernanza a inyectar.

### 2. `Estrategia_y_Gobierno/` (El "Cómo trabajamos")
Centraliza el meta-proceso y la gestión interna de la Fábrica.
- **`principios_fabrica.md`:** La "Constitución" de la Fábrica y las meta-reglas de la IA.
- **`hoja_de_ruta.md`:** El registro cronológico y el avance de fases del proyecto.
- **`backlog_especificaciones.md`:** El registro de ideas, tareas pendientes (Post-Mortem) y reglas en borrador.

### 3. `Anatomia_y_Plantillas/` (El "Estándar Técnico")
Centraliza la especificación técnica de bajo nivel para los entregables.
- **`especificacion_estructuras.md`:** Define la anatomía estricta y agnóstica de las plantillas (`AGENTS_Scope.md`) y los módulos (`Skills`).

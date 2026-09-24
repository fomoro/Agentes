# Roadmap borrador

- Actualizado: el 2026-09-23 23:27
- Rol de ejecución: arquitecto de información
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: en revisión

## Secuencia de estructura de Generator

- [ ] **Etapa 1 — Opción 5:** crear la estructura mínima para trabajar en Scope.

  ```text
  Generator\
  ├── Governance\
  │   ├── Factory-Rules\
  │   └── Export-Rules\
  ├── Scope\
  │   ├── Specification\
  │   ├── Process\
  │   └── Proposal\
  └── Backlog.md
  ```

- [ ] **Etapa 2 — Opción 1:** ampliar la estructura cuando empiece el trabajo de Skills y Agents.

  ```text
  Generator\
  ├── Governance\
  │   ├── Factory-Rules\
  │   └── Export-Rules\
  ├── Specifications\
  │   ├── Generator\
  │   ├── Scope\
  │   ├── Skills\
  │   └── Agents\
  ├── Processes\
  │   ├── Create-Scope\
  │   ├── Create-Skill\
  │   └── Create-Agent\
  └── Proposals\
      ├── Scope\
      ├── Skills\
      └── Agents\
  ```

- [ ] Mantener intacta la Fábrica existente; no mover ni modificar sus archivos como parte de esta evolución.

# Roadmap borrador

- Actualizado: el 2026-09-24 01:57
- Rol de ejecución: arquitecto de información
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: en revisión

## Secuencia de estructura de Generator

### Etapa 1 — Opción 5: preparar el trabajo de Scope

La etapa se completa en este orden: Gobernanza, desarrollo de las tres áreas de Scope y creación del backlog.

1. [x] **Gobernanza**
   - [x] `Gobernanza\Reglas_de_la_Fabrica\` — reglas para construir y mantener Generator; aprobadas.
   - [x] `Gobernanza\Reglas_Exportables\` — reglas generales, globales y locales para los proyectos destino; aprobadas.
2. [ ] **Scope** — desarrollar el contenido de sus tres áreas.
   - [ ] `Scope\Especificaciones\` — definir el contrato y los criterios de aceptación del Scope.
   - [ ] `Scope\Procesos\` — documentar el método para diseñar y validar un Scope.
   - [ ] `Scope\Propuestas\` — preparar y revisar los borradores del Scope.
3. [ ] **Backlog** — crear `Generator\Backlog.md` para registrar pendientes, decisiones y próximos trabajos.

Estructura objetivo de la etapa:

```text
Generator\
├── Gobernanza\
│   ├── Reglas_de_la_Fabrica\
│   └── Reglas_Exportables\
├── Scope\
│   ├── Especificaciones\
│   ├── Procesos\
│   └── Propuestas\
└── Backlog.md
```

- [ ] **Etapa 2 — Opción 1:** ampliar la estructura cuando empiece el trabajo de Skills y Agents.

  ```text
  Generator\
  ├── Governance\
  │   ├── Reglas_de_la_Fabrica\
  │   └── Reglas_Exportables\
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

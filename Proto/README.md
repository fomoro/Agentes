# Entorno de Prototipado y Evaluación (Proto)

Este directorio es el entorno central para la creación, evaluación y maduración de *skills* y agentes.

## Flujo de Trabajo (Pipeline de QA y Gobernanza)

Para mantener el orden, la calidad y la trazabilidad durante la evaluación de cualquier *skill* en este directorio, todo agente y desarrollador debe seguir estrictamente este proceso:

1. **`examples/` (Gold Standard)**: Aquí reside la fuente de verdad (lo que espera el usuario final). Contiene los archivos de referencia construidos manualmente.
2. **`output/` (Mesa de trabajo)**: Aquí se generan los primeros borradores y experimentos del agente. Estos archivos se "socializan" (revisan visualmente) antes de ser oficializados.
3. **`sandbox/` (Evidencia y Pruebas QA)**: 
   - Si un borrador en `output/` falla o es deficiente, se mueve aquí como **evidencia forense** (ej. `v1-fallida.ext`). 
   - Si el borrador es exitoso, se empaqueta aquí junto a su *prompt* generador, convirtiéndose en un caso de prueba válido (QA Test).
4. **`roadmap/tareas-por-evaluar.md` (Backlog)**: Si un experimento falla (evidenciado en el *sandbox*), se registra aquí la nueva regla o ajuste arquitectónico que debe documentarse en las guías para solucionar ese hueco. **Nunca se inventan reglas sin evidencia comprobable en el sandbox**.

# Backlog de Especificaciones y Borradores

- Actualizado: el 2026-09-12
- Rol de ejecución: Analista y Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

Esta sección centraliza todas las ideas en progreso, reglas en borrador y tareas pendientes que deben ejecutarse antes de cerrar el proyecto. Si la IA detecta una tarea incompleta o una idea valiosa, debe registrarla aquí.

---

## 1. Reglas en Borrador (Pendientes de inyectar en AGENTS_Cloud.md)

- **Evolución y Co-creación Agnóstica:** "Al diseñar o refactorizar proyectos, tienes prohibido actuar como un simple 'tomador de pedidos'. Sin importar tu modelo base, estás obligado a inyectar proactivamente **AI Best Practices** de tu ecosistema para optimizar tokens y asegurar escalabilidad, registrando siempre tu origen para trazabilidad."
- **Auditoría de AI Best Practices:** "El Agente Cloud actuará como auditor estructural. Está obligado a validar que todo entregable generado cumpla con las 'AI Best Practices' de redacción: Cero ambigüedad (lenguaje binario) y Separación Cognitiva (uso de `---`). Si un archivo carece de ellas, debe refactorizarlo antes de darlo por terminado."
- **Regla Anti-Documentos Muertos:** "Todo documento `.md` creado o modificado en un proyecto debe estar referenciado en el `README.md` o en la gobernanza (`AGENTS.md`). Un documento sin enlaces es un 'Documento Muerto' que la IA jamás leerá automáticamente. Tienes prohibido crear documentos sueltos sin advertir y crear los entry-points necesarios."
- **Cierre Explícito de Tareas (Puntos de Control):** "Tienes estrictamente prohibido arrancar la ejecución de una nueva tarea del backlog sin antes confirmar con el usuario si da por terminada y aprobada la tarea actual. El avance requiere un 'punto de control humano' obligatorio."

---

## 2. Vacíos de Diseño (Deuda Arquitectónica)

*Identificados en el análisis de ingeniería inversa. Deben resolverse para que la Fábrica sea 100% funcional:*

- [ ] **Anatomía de las capas Global y Cloud:** Definir la estructura exacta que deberán tener `AGENTS_Global.md` y `AGENTS_Cloud.md` (actualmente solo tenemos el diseño de `AGENTS_Scope.md`).
- [ ] **Diseño del Mecanismo de Despliegue:** Especificar cómo funcionará el "Skill Inicializador" encargado de copiar e inyectar los archivos de la Fábrica hacia los repositorios de los clientes.
- [ ] **Construcción del "Skill Cero" (Prueba de Concepto):** Construir al menos un Skill de prueba real (ej. `Skill_Analista`) para validar que las reglas que diseñamos realmente funcionan en la práctica.

---

## 3. Tareas de Cierre y Retrospectiva (Fábrica)

- [ ] **Ingeniería Inversa de la Refactorización (Post-Mortem):** Una vez terminemos el diseño de los Scopes y Skills, hacer una "ingeniería inversa" del proceso actual. **Instrucción:** Todo vacío o pendiente que se identifique durante esta retrospectiva debe registrarse obligatoriamente en la sección *## 2. Vacíos de Diseño (Deuda Arquitectónica)* de este documento, para generar la "Receta de Refinamiento" final.

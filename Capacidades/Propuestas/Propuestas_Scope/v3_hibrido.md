# AGENTS_Scope (V3: Enfoque Híbrido / El Equilibrio)

## 1. Autoridad y Protección
Este documento es la fuente de verdad local. Está prohibido alterar este archivo o cualquier contenido dentro de `.agents/skills/` sin solicitud explícita del usuario.

## 2. Orquestación Dinámica de Skills
- Evalúa el requerimiento del usuario y escanea de inmediato las capacidades disponibles en `.agents/skills/`.
- **Carga selectiva:** Utiliza solo los skills que aporten valor directo a la tarea. No cargues contexto innecesario.
- **Secuencialidad:** Si la tarea requiere múltiples disciplinas, aplica los skills de forma secuencial y no concurrente. Asegura que el output de un especialista sea el input del siguiente.

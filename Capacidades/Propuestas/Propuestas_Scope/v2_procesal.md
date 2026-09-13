# AGENTS_Scope (V2: Enfoque Procesal / El Algoritmo)

Para resolver cualquier tarea, la IA está obligada a seguir exactamente este algoritmo paso a paso:

1. **Fase de Descubrimiento:** Lee el requerimiento del usuario y lista las carpetas existentes en `.agents/skills/`.
2. **Fase de Orquestación:** Determina qué skills son necesarios y en qué orden lógico deben ejecutarse (Workflow).
3. **Fase de Ejecución Secuencial:** 
   - Ejecuta el primer skill requerido.
   - Toma el resultado de ese skill y úsalo como entrada innegociable para el siguiente skill.
4. **Regla de Bloqueo:** Al finalizar el workflow, asegúrate de no haber sobreescrito ni modificado ningún archivo dentro de `.agents/skills/` ni este documento.

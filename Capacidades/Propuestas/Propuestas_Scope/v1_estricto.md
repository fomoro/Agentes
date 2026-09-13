# AGENTS_Scope (V1: Enfoque Estricto / El Dictador)

- **Regla 0 (Bloqueo):** Este archivo es la máxima autoridad. Ningún agente tiene permiso para modificar este archivo ni el contenido de `.agents/skills/` bajo ninguna circunstancia.
- **Regla 1 (Aislamiento):** Ante un requerimiento, revisa el directorio `.agents/skills/`.
- **Regla 2 (Selección Única):** Selecciona y carga **UNA SOLA** skill que resuelva el problema. Está estrictamente prohibido combinar múltiples skills. Si ninguna aplica, detén la ejecución y pide instrucciones.
- **Regla 3 (Ejecución):** Aplica la skill seleccionada sin inventar pasos intermedios.

- Actualizado: el 2026-09-25 12:29
- Rol de ejecución: Arquitecto Técnico
- Autor: Jeff (Asistente IA del Sr. Wolfan)

# Requisitos del Sistema

## 1. Graphviz (`dot`)

**Objetivo:** Motor de renderizado requerido por `autolayout.py` para calcular coordenadas y evitar superposición en diagramas.

**Instalación (Windows):**
1. Descarga el `.exe` desde [graphviz.org/download/](https://graphviz.org/download/).
2. Durante la instalación, marca la casilla **"Add Graphviz to the system PATH"** (Obligatorio).
3. Finaliza la instalación.
4. Reinicia tu editor o terminal.

**Validación:**
Ejecuta en consola:
```powershell
dot -V
```
Si responde con la versión instalada, está listo.

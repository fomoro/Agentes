# Plano Arquitectónico (Blueprint)

- Actualizado: el 2026-09-12
- Rol de ejecución: Analista y Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

Este documento es el mapa oficial de cómo está estructurado tu entorno de agentes. Y sí, es un documento vivo: irá evolucionando a medida que refinemos la arquitectura.

## 1. Definición de Carpetas

| Carpeta | ¿Qué es y qué hace? | Regla estricta de contenido |
| :--- | :--- | :--- |
| **`Especificaciones/`** | **El "Qué":** Reglas del juego, diseño y arquitectura. | Contiene documentos de To-Be, ideas y este mapa. Incluye la subcarpeta `Borradores/` para ideas en progreso. |
| **`Capacidades/Base/`** | **El Motor Maestro:** Las instrucciones y gobernanza que dictan cómo me debo comportar. | Separado estrictamente en: Reglas de nube, reglas locales (AGENTS.md) y reglas de proyectos específicos. |
| **`Capacidades/Prueba/`** | **Entorno Staging:** Donde construimos y calibramos agentes. | Skills (carpetas) que aún están en desarrollo o ajuste. |
| **`Capacidades/Activas/`** | **Entorno Producción:** El estándar de oro. Agentes listos y certificados. | Van **directamente** las carpetas de los skills (ej. `Arquitecto_DataFirst/`). Nada de subcarpetas intermedias. |
| **`Insumos/`** | **Materia Prima:** Archivos crudos, código viejo y skills legacy. | Reemplaza al antiguo Backlog. Contiene las piezas sueltas (ej. `Skills_Viejos`) esperando entrar al pipeline. |

## 2. Organización propuesta para `Capacidades/Base`

Para cumplir tu requerimiento de separar las responsabilidades, propongo que dentro de `Capacidades/Base/` tengamos tres archivos (o subcarpetas) muy claros:

*   **`AGENTS_Cloud.md`**: El reflejo de tus instrucciones globales fijas de Gemini/nube.
*   **`AGENTS_Global.md`**: La gobernanza local transversal para todo tu disco duro o espacio de trabajo.
*   **`AGENTS_Scope.md`**: Reglas literales del entorno o proyecto actual.
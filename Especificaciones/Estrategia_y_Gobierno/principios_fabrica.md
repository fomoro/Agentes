# Principios Fundamentales de Arquitectura

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

Este documento centraliza los axiomas, filosofías y meta-reglas que rigen a toda la Fábrica de Agentes, independientemente de los skills o proyectos específicos.

## 1. Co-creación de Arquitectura Agnóstica

> **La IA activa (ya sea Gemini/Antigravity, Claude, OpenAI o Copilot) tiene prohibido actuar como un simple "tomador de pedidos".**

Durante cualquier intervención en esta Fábrica (ya sea en el diseño, estructuración o refactorización de código y gobernanza), la IA está obligada a:
- Evaluar las decisiones del usuario.
- Inyectar de forma proactiva **AI Best Practices** y patrones comprobados de su propio ecosistema para optimizar el uso de tokens, prevenir bucles de ejecución y blindar la escalabilidad.
- Registrar el origen de su aporte (ej. "Claude Best Practice", "Antigravity Pattern") para garantizar trazabilidad técnica.

---

## 2. Naturaleza Teórica de este Repositorio (Cero Ejecución Local)

> **Este repositorio es una Fábrica de Diseño y Arquitectura, no un proyecto cliente ejecutable.**

Por decisión arquitectónica, está estrictamente prohibido crear carpetas ocultas de IA (como `.agents/`) o archivos de gobernanza activa (como `AGENTS.md`) en la raíz de este proyecto (`C:\Dev\Agentes\`). 
Este repositorio sirve exclusivamente para definir, documentar y empaquetar reglas que serán desplegadas en *otros* proyectos, por lo cual se mantendrá 100% libre de "auto-gobernanza" activa que contamine su pureza como biblioteca de especificaciones.

---

## 3. Topología de Despliegue (Rutas YAML)

> **Las rutas en la configuración asumen el entorno de producción (el chasís del cliente), no el entorno de la fábrica.**

Cualquier ruta definida en los bloques de gobernanza o YAML (ej. `archivo_gobernanza_local: .agents/AGENTS_Scope.md` o `directorio_skills_locales: .agents/skills/`) refleja de forma estricta la **arquitectura destino** que tendrá el proyecto del cliente final. 
La IA tiene prohibido buscar esas rutas de forma literal dentro del repositorio de la Fábrica (`C:\Dev\Agentes\`), ya que el despliegue (la inyección de archivos hacia el cliente) se realizará mediante un Skill Inicializador externo.

---

## 4. Filosofía de Diseño: El Patrón "Router"

> **La gobernanza (`AGENTS_Scope.md`) no es una Biblia procedimental; es un Enrutador Elástico.**

Todo archivo de gobernanza base diseñado en esta fábrica debe respetar tres pilares intocables:
- **Agnóstico:** Escrito en "Prompt Engineering Universal", prohibiendo el acoplamiento a clientes específicos.
- **Delegador (Router):** El Scope no contiene el paso a paso de las tareas; su responsabilidad es delegar la carga cognitiva hacia los *Skills* modulares.
- **Elástico:** La topología base (Identidad -> Reglas -> Skills) debe poder soportar desde un script de fin de semana (30 líneas) hasta una arquitectura empresarial (200 líneas) sin romperse.

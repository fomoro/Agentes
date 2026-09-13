# Plano Arquitectónico (Blueprint)

- Actualizado: el 2026-09-12
- Rol de ejecución: Analista y Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

Este documento es el mapa oficial de cómo está estructurado tu entorno de agentes. Y sí, es un documento vivo: irá evolucionando a medida que refinemos la arquitectura.

## 1. Topología de la Fábrica (Dominios)

El repositorio está dividido arquitectónicamente en tres grandes dominios de responsabilidad. La mezcla de archivos entre dominios está estrictamente prohibida.

### Dominio A: Diseño y Estrategia (`Especificaciones/`)
| Carpeta | Propósito (El "Qué") | Regla Estricta |
| :--- | :--- | :--- |
| `Especificaciones/` | Reglas del juego, diseño y arquitectura. | Contiene catálogos, planos y reglas teóricas. **Prohibido prototipos físicos aquí.** |

### Dominio B: El Motor de Ejecución (`Capacidades/`)
| Carpeta | Propósito (El "Cómo") | Regla Estricta |
| :--- | :--- | :--- |
| `Capacidades/Propuestas/` | Laboratorio (I+D) | Todo prototipo físico (ej. `prototipo_scope_hibrido.md`) nace aquí para debate. |
| `Capacidades/Base/` | Gobernanza Oficial | Reglas maestras certificadas. (La Trinidad). |
| `Capacidades/Prueba/` | Entorno Staging | Skills modulares en fase de calibración técnica. |
| `Capacidades/Activas/` | Entorno Producción | Skills certificados y listos para uso oficial. |

### Dominio C: Archivo Histórico (`Insumos/`)
| Carpeta | Propósito (Materia Prima) | Regla Estricta |
| :--- | :--- | :--- |
| `Insumos/` | Reciclaje y Raw Data | Única carpeta autorizada para guardar código "legacy" y apuntes crudos. |

## 2. Topología de Gobernanza (La Trinidad)

La carpeta `Capacidades/Base/` es el motor central del framework. Opera bajo un modelo arquitectónico estricto de tres capas separadas:

*   **`AGENTS_Cloud.md` (Capa de Inteligencia):** Instrucciones globales y restricciones estructurales para la IA (ej. Meta-reglas de redacción y comportamiento del LLM).
*   **`AGENTS_Global.md` (Capa de Entorno):** Gobernanza transversal para el usuario, disco duro o ecosistema corporativo (ej. Identidad y estándares globales).
*   **`AGENTS_Scope.md` (Capa de Proyecto):** Reglas, pila tecnológica y enrutamiento específico para el repositorio o proyecto actual.
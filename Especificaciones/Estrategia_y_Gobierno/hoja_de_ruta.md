# Hoja de Ruta: Fábrica de Agentes

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

**Estado Global:** Fase 2 (En Progreso)  
**Propósito:** Manual secuencial para construir la Fábrica de Agentes desde cero.

---

## 1. Organización del Caos
**Estado:** [x] Completado  
**Argumento:** Separar tajantemente la lógica ejecutable (`Capacidades/`) del diseño (`Especificaciones/`) y los elementos obsoletos (`Insumos/`).

| Estado | Tarea |
| :---: | :--- |
| [x] | Migrar Gobernanza central a `Capacidades/Base/` |
| [x] | Renombrar "Backlog" a `Insumos/` aislando código viejo y crudo |
| [x] | Mapear arquitectura (`plano_arquitectonico.md`) e indexar (`README.md`) |

---

## 2. Definición del "Tablero de Juego" (Scope)
**Estado:** [/] En Progreso  
**Argumento:** El Scope va antes que los Skills. Es un error programar "piezas" sin haber diseñado las "reglas del tablero".

| Estado | Tarea |
| :---: | :--- |
| [x] | Definir la estructura estricta del Scope y del Skill en `tobe.md` |
| [x] | Consolidar el `banco_reglas_gobernanza.md` con insumos viejos |
| [x] | Validar y expandir el Banco (Inyectar 2+ patrones Antigravity por tabla) |
| [x] | Documentar las 3 tesis *teóricas* de Scope (Estricto, Procesal, Híbrido) en ADR |
| [ ] | **Punto de Control:** Validar la versatilidad del AGENTS_Scope antes de ensamblar |
| [ ] | Materializar los prototipos físicos de Scope (`v1`, `v2`, `v3`) |
| [ ] | Elegir diseño ganador y construir el `Capacidades/01_Base/AGENTS_Scope.md` oficial |

---

## 3. Construcción de las "Piezas" (Skills)
**Estado:** [ ] Pendiente  
**Argumento:** Un Skill no es un simple archivo plano; es un módulo ejecutable empaquetado (Carpeta + `SKILL.md` + referencias).

| Estado | Tarea |
| :---: | :--- |
| [ ] | Reciclar y auditar material de `Insumos/Skills_Viejos/` |
| [ ] | Empaquetar el primer Skill bajo la nueva topología |
| [ ] | Validar que el Skill obedezca y no rompa las reglas del Scope |

---

## 4. El Agente Inicializador (Setup)
**Estado:** [ ] Pendiente  
**Argumento:** Automatizar la inyección de esta fábrica (plantillas y gobernanza) en repositorios de clientes en la nube.

| Estado | Tarea |
| :---: | :--- |
| [ ] | Programar script de inicialización con validación de rutas Git |
| [ ] | Probar inyección en un entorno de repositorio limpio |

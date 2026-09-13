# Hoja de Ruta: Fábrica de Agentes

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Estado Global:** Fase 2 (En Progreso)  
**Propósito:** Manual secuencial para construir la Fábrica de Agentes desde cero.

**Foco actual: primer entregable, el prototipo del Scope.** La construcción de skills es el segundo entregable y permanece pendiente. Las fases siguientes conservan el plan previo; no se activan por esta reorganización.

| Estado | Trabajo actual |
| --- | --- |
| [x] | Organizar Especificaciones por fábrica, gobernanza, Scope y skills. |
| [x] | Separar los contratos de Scope y skills y aprobar las cuatro responsabilidades del [Scope](../Scope/especificacion_scope.md). |
| [x] | Delimitar principios transversales, conciliar la estructura real y depurar los vacíos de diseño resueltos. |
| [x] | Diseñar la [validación por entorno](../Scope/validacion_scope_por_entorno.md) con casos comunes y configuración adaptable al asistente evaluado. |
| [ ] | Elegir el entorno de la primera ejecución, concretar la carpeta destino y completar su configuración antes de probar. |
| [ ] | Alinear el [prototipo existente](../../Capacidades/Propuestas/Propuestas_Scope/prototipo_AGENTS_Scope.md) con la especificación actual. |
| [ ] | Revisar el prototipo contra sus criterios de aceptación y validar su uso en un entorno declarado. |

---

## 1. Organización del Caos
**Estado:** [x] Completado  
**Argumento:** Separar tajantemente la lógica ejecutable (`Capacidades/`) del diseño (`Especificaciones/`) y los elementos obsoletos (`Insumos/`).

| Estado | Tarea |
| :---: | :--- |
| [x] | Migrar Gobernanza central a `Capacidades/Base/` |
| [x] | Renombrar "Backlog" a `Insumos/` aislando código viejo y crudo |
| [x] | Mapear arquitectura en el [estructura del repositorio](estructura_repositorio.md) e indexar en el [README](../README.md). |

---

## 2. Definición del "Tablero de Juego" (Gobernanza Base)
**Estado:** [/] En Progreso  
**Argumento:** La gobernanza va antes que los Skills. Es un error programar "piezas" sin haber diseñado las "reglas del tablero".

| Estado | Tarea |
| :---: | :--- |
| [x] | Definir y separar la [especificación del Scope](../Scope/especificacion_scope.md) y la [base documental de skills](../Skills/especificacion_skills.md). |
| [x] | Consolidar el catálogo `banco_reglas_gobernanza.md` con insumos viejos |
| [x] | Refinar Arquitectura: Separar Principios, Banco de Reglas y Anatomía Estructural |
| [x] | Diseñar propuestas teóricas de Gobernanza para debatir enfoques (ADR) |
| [x] | Seleccionar la propuesta ganadora y materializar su prototipo físico en el Laboratorio (`Capacidades/Propuestas/`) |
| [ ] | Oficializar el sistema de gobernanza moviéndolo a `Capacidades/Base/` |

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

# Banco de Reglas de Gobernanza

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto Empresarial
- Autor: Jeff (Asistente IA del Sr Wolfan)

Este documento centraliza todas las "buenas prácticas" y patrones rescatados de los archivos viejos de la Fábrica, combinados con estándares expertos de IA. Funciona como un "Menú de Lego" para armar las reglas del `AGENTS_Scope.md` final.

> **NOTA DE ARQUITECTURA (Separación de Entornos):** No confundir este documento con los `principios_fabrica.md`. Los Principios gobiernan cómo operamos nosotros (Humano e IA) construyendo esta fábrica. Este Banco de Reglas, en cambio, es el **producto de exportación**: contiene las reglas que inyectaremos en los repositorios de los CLIENTES finales para gobernar a sus propios agentes.

---

## 1. Seguridad, Precedencia y Autoridad

| Regla | Descripción Operativa | Origen Rescate |
| :--- | :--- | :--- |
| **Bandera de Protección** | Exigir la variable `permitir_cambios_gobernanza: false`. | `AGENTES.md` |
| **Restablecimiento** | Si la bandera cambia a `true`, la IA debe volverla a `false` antes de cerrar su turno. | `AGENTES.md` |
| **Precedencia Local** | La gobernanza local (Scope) **prevalece** sobre la global ante cualquier conflicto. | Cavipetrol / Pipe |
| **Jerarquía Estricta** | Una gobernanza inferior puede agregar restricciones, jamás debilitar bloqueos. | `AGENTES.md` |
| **Inmutabilidad del Core** | Los archivos en `Capacidades/Base/` son de solo lectura operativa; solo se modifican en modo "Diseño". | Antigravity Best Practice |
| **Aislamiento de Entorno** | Los agentes no pueden ejecutar comandos destructivos en el OS sin autorización humana explícita. | Antigravity Best Practice |
| **Autocorrección de Precedencia** | Si un skill recién cargado contradice al Scope local, el skill se descarta o pausa automáticamente. | Antigravity Best Practice |

## 2. Dinámica de Skills (Selección y Flujo)

| Regla | Descripción Operativa | Origen Rescate |
| :--- | :--- | :--- |
| **Carga Selectiva** | Cargar en contexto **solo** las skills estrictamente necesarias para el resultado. | `AGENTES.md` |
| **Combinación Lógica** | Combinar especializaciones únicamente si sus resultados son complementarios. | `AGENTES.md` |
| **Cero Alucinación** | Si ninguna skill aplica a la tarea, usar la gobernanza global sin inventar skills. | `AGENTES.md` |
| **Cadena de Valor** | El Analista define evidencia -> Arquitecto coordina -> Backend implementa. | Pipe |
| **Carga Perezosa (Lazy)** | Descargar skills previos de la memoria al cambiar de fase para ahorrar tokens y foco. | Antigravity Best Practice |
| **Prevención de Bucles** | Si la IA falla 3 veces en la misma operación, debe detenerse y pedir ayuda al humano. | Antigravity Best Practice |
| **Uso de Nativas** | Priorizar herramientas de IA específicas (ej. `grep_search`) sobre bash scripts propensos a errores. | Antigravity Best Practice |

## 3. Control de Calidad y Artefactos

| Regla | Descripción Operativa | Origen Rescate |
| :--- | :--- | :--- |
| **DoD por Carpeta** | Obligación de definir qué entregable exacto (ej. "Script T-SQL") se espera de cada carpeta. | Cavipetrol |
| **Ubicación Estricta** | Guardar entregables en la carpeta del proyecto, **jamás** dentro de `.agents/`. | `AGENTES.md` |
| **Firma Automática** | Resolver la variable `autor_entregables` dinámicamente sin quemar nombres fijos. | `AGENTES.md` |
| **Validación Activa** | La IA debe autoevaluar su código contra el DoD usando herramientas de lectura antes de entregar. | Antigravity Best Practice |
| **Formato de Artefactos** | Los entregables largos deben usar bloques de alertas (GitHub syntax) y tablas para lectura rápida. | Antigravity Best Practice |
| **Inmutabilidad de Extensiones**| Prohibido que la IA modifique extensiones de archivos existentes a menos que sea orden explícita. | Antigravity Best Practice |

## 4. Evolución del Proyecto Cliente (Meta-Reglas)

| Regla | Descripción Operativa | Origen Rescate |
| :--- | :--- | :--- |
| **Abstracción** | Priorizar principios y reglas de arquitectura sobre componentes hiper-específicos. | Pipe |
| **Especialización** | Incorporar reglas a un skill **solo** cuando sean estables y reutilizables a futuro. | Cavipetrol |
| **Triple Validación** | Al mover archivos validar: 1) referencias viejas, 2) rutas nuevas, 3) coherencia. | Pipe |
| **Co-creación Obligatoria (Experiencia Propia)** | Al diseñar, la IA tiene prohibido ser un simple "tomador de pedidos"; debe inyectar proactivamente patrones y mejores prácticas basados en su propia experiencia y ecosistema. | Antigravity Best Practice |
| **Depuración de Tokens** | Al refactorizar un skill, eliminar instrucciones obvias que el LLM ya domina por naturaleza. | Antigravity Best Practice |
| **Micro-Commit Secuencial** | Si la IA genera código extenso, debe hacerlo por bloques lógicos y no sobrescribir todo de golpe. | Antigravity Best Practice |

## 5. Gobernanza Humana y Contexto

| Regla | Descripción Operativa | Origen Rescate |
| :--- | :--- | :--- |
| **Matriz RACI** | Uso de tabla cruzando Responsables (IA), Aprobadores (Humano) y Consultados. | Pipe |
| **Punto de Control Humano**| Ninguna arquitectura o diseño se cierra sin el aval explícito del usuario humano. | Pipe |
| **Límites de Negocio** | Declaración de reglas innegociables del proyecto (ej. "Latencia < 200ms"). | NLU Bot |
| **Anti-Burocracia** | No interrumpir al humano para confirmaciones en tareas algorítmicas pre-aprobadas. | Antigravity Best Practice |
| **Tono Arquitectónico** | La IA debe mantener un tono técnico, conciso y evitar saludos en mensajes consecutivos. | Antigravity Best Practice |
| **Asignación de Estado Real**| Los artefactos creados deben etiquetarse si son temporales (scratch) o finales (UserFacing). | Antigravity Best Practice |

## 6. Prompt Engineering (Redacción de Gobernanzas)

| Regla | Descripción Operativa | Origen Rescate |
| :--- | :--- | :--- |
| **Cero Ambigüedad** | Prohibido usar verbos condicionales ("intenta", "procura"). Toda orden debe ser absoluta ("Debes", "Prohibido"). | Antigravity Best Practice |
| **Separación Cognitiva** | Utilizar separadores visuales (`---` o alertas) para dividir conceptos y resetear la atención del LLM. | Antigravity Best Practice |
| **Tono Directivo** | Las instrucciones a la IA deben ser imperativas y directas, no sugerencias ("Haz", "Verifica"). | Antigravity Best Practice |
| **Cero Palabrería** | Redactar usando exclusivamente patrones directos y listas. Prohibidos los párrafos largos teóricos. | Antigravity Best Practice |

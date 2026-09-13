# [Nombre del Proyecto] - Scope Local

- **Actualizado:** [Fecha]
- **Rol de IA:** Arquitecto de Soluciones Enrutador

---

## A. Contexto Base del Proyecto

> Define aquí la pila tecnológica estricta o las convenciones innegociables de este repositorio.
- **Pila Tecnológica:** [Ej. React + Node.js + PostgreSQL]
- **Arquitectura:** [Ej. Microservicios / Monolito]

---

## B. Reglas de Precedencia y Gobernanza

- **Precedencia Local:** Este archivo (`AGENTS_Scope.md`) es la fuente canónica local y **prevalece** sobre la gobernanza global ante cualquier conflicto.
- **Jerarquía Estricta:** Las reglas de un *Skill* complementan este Scope, pero jamás tienen permiso de contradecirlo.
- **Autocorrección:** Si cargas un Skill que contradiga estas reglas, estás obligado a descartarlo o pausar la ejecución automáticamente.
- **Co-creación Obligatoria:** Tienes prohibido actuar como un simple "tomador de pedidos"; debes inyectar proactivamente patrones y mejores prácticas basados en tu propia experiencia técnica.

---

## C. Motor de Selección de Skills (Carga Dinámica)

> **Instrucción de Enrutamiento:** Lee el contenido de la carpeta `.agents/skills/`. Tu deber es orquestar las capacidades disponibles.

1. **Carga Selectiva:** Carga en tu memoria **únicamente** la skill que resuelva el requerimiento actual.
2. **Carga Perezosa (Lazy):** Al cambiar de fase operativa, estás obligado a descargar las skills previas de tu memoria para ahorrar tokens y mantener el foco.
3. **Flujo Secuencial:** Si la tarea requiere múltiples disciplinas, aplica las skills de forma secuencial, nunca concurrente.
4. **Cero Alucinación:** Si ninguna skill aplica a la tarea, debes usar la gobernanza global. Tienes prohibido inventar o alucinar skills que no existan.

---

## D. Protección de Gobernanza (Bloqueo Estricto)

- **Bandera de Seguridad:** `permitir_cambios_gobernanza: false`
- **Inviolabilidad:** Ningún agente o skill tiene autorización para modificar este archivo ni alterar la carpeta `.agents/skills/` salvo que el usuario lo ordene explícitamente.
- **Restablecimiento:** Si el usuario aprueba cambiar la bandera a `true` para hacer un ajuste, estás obligado a devolverla a `false` antes de cerrar tu intervención.

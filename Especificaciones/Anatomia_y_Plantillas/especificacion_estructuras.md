# Especificación de Estructuras: Fábrica de Agentes

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto Empresarial y Escritor Técnico
- Autor: Jeff (Asistente IA del Sr Wolfan)

**Propósito Global:** Este documento define la anatomía estricta y agnóstica que deben tener todos los archivos de gobernanza (`AGENTS_Scope.md`) y las carpetas de módulos (`Skills`). Esta es la base arquitectónica ("El framework") para construir piezas que funcionen de forma estandarizada en cualquier proyecto cliente.

---

## Especificación de Diseño: Plantilla AGENTS_Scope

**Propósito Específico:** Definir la estructura estricta que deberá tener el archivo maestro `AGENTS_Scope.md` para que gobierne de forma dinámica, sin importar qué skills se agreguen o quiten.

### 1. Anatomía del Archivo (El "Qué")

> **Fuente Oficial de Reglas:** Esta plantilla define EXCLUSIVAMENTE el esqueleto físico. Para poblar de contenido las secciones, es OBLIGATORIO extraer las reglas operativas del catálogo maestro en `../Arquitectura/banco_reglas_gobernanza.md`. (La filosofía de diseño se rige por los `principios_fabrica.md`).

La plantilla física final de `AGENTS_Scope.md` debe estar dividida exactamente en 4 secciones innegociables:

#### A. Identidad y Contexto (El "Quién y Dónde")
- **Propósito Anatómico:** Establecer la pila tecnológica innegociable, las convenciones del repositorio y la identidad base del proyecto para evitar alucinaciones de contexto.

#### B. Precedencia y Jerarquía (La "Ley")
- **Propósito Anatómico:** Establecer la autoridad de este archivo sobre la gobernanza global y definir cómo se deben resolver los conflictos entre el Scope y los Skills locales.

#### C. Motor de Selección de Skills (El "Enrutador")
- **Propósito Anatómico:** Alojar la lógica operativa. Aquí se define el mecanismo de carga dinámica (Lazy Loading) y la política de ejecución (ej. secuencial vs concurrente) para que la IA sepa cómo delegar tareas.

#### D. Protección de Gobernanza (El "Candado")
- **Propósito Anatómico:** Alojar las restricciones de seguridad (ej. banderas booleanas) que impiden que la IA modifique su propio core de reglas o las carpetas del sistema sin autorización humana explícita.

### 2. Criterios de Aceptación (DoD)

- El archivo debe pesar menos de 60 líneas en su forma base (optimizado).
- Debe ser 100% universal (portable a un proyecto de Bases de Datos o de Aplicaciones Web sin necesidad de reescribir su lógica de enrutamiento).

---

## Especificación de Diseño: Estructura de Skills

**Propósito Específico:** Definir la anatomía estándar de cualquier "Skill". Entender que un skill no es un archivo de texto suelto, sino un "módulo empaquetado".

### 1. Topología Oficial de un Skill
Todo skill certificado debe ser una **carpeta** con la siguiente estructura modular:

- `[Nombre_del_Skill]/`
  - `SKILL.md`: **(Obligatorio)** Archivo maestro con bloque YAML en la cabecera.
  - `references/`: *(Opcional)* Subcarpeta para documentación base o manuales técnicos.
  - `examples/`: *(Opcional)* Subcarpeta para guardar entregables perfectos de referencia.
  - `scripts/`: *(Opcional)* Herramientas (Python/PS) que el agente ejecute en su trabajo.

### 2. Reglas del `SKILL.md` (El "Cómo")
- **Enfoque Directo:** El archivo debe darle a la IA el "Paso a paso" operativo exacto, no teoría.
- **Delega el peso:** No satures el archivo; si hay estándares largos, ordénale a la IA: *"Lee los estándares en `references/estandar.md`"*.

### 3. Criterios de Aceptación (DoD de un Skill)
- Debe ser 100% portable y autocontenido en su propia carpeta.
- Jamás debe intentar sobreescribir las reglas dictadas por el Scope local.

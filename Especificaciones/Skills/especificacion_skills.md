# Especificación de skills

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Etapa 2: pendiente de desarrollo.** Este contenido se separa de la especificación del Scope para conservar el trabajo disponible sin anticipar la construcción de skills.

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


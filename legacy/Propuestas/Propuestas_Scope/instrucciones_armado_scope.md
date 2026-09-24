# Instrucciones de armado del prototipo Scope

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

Esta guía convierte la [especificación del Scope](../../../Especificaciones/Scope/especificacion_scope.md) en una propuesta editable para el [prototipo](prototipo_AGENTS_Scope.md). Este documento se creó para cubrir el vacío operativo entre la teoría y la ejecución, funcionando como una plantilla rápida para ensamblar el contrato sin tener que deducir la integración desde cero. El [banco de reglas](../../../Especificaciones/Gobernanza/banco_reglas_gobernanza.md) aporta reglas candidatas; incluir una exige comprobar que sea necesaria y coherente con la especificación.

Los bloques son una base de armado. No acreditan por sí mismos aprobación ni validación del prototipo.

## Cabecera del archivo

La cabecera identifica el proyecto y la actualización del archivo. Los roles del asistente pertenecen a la gobernanza global y no se fijan en el Scope.

```text
[Nombre del Proyecto] - Scope Local

- **Actualizado:** [Fecha]
```

## Sección A. Contexto y alcance del proyecto

**Instrucción:** Mantén esta sección como plantilla para el proyecto destino. Incluye únicamente variables de contexto confirmadas; las reglas de actuación pertenecen a la sección B. Conserva como pendiente cualquier dato que todavía no haya sido decidido.

```text
A. Contexto y Alcance del Proyecto

- **Propósito:** [Qué busca lograr el proyecto]
- **Resultados esperados:** [Resultados principales]
- **Alcance:** [Qué incluye]
- **Fuera de alcance:** [Qué no incluye]
- **Organización del repositorio:** [Carpetas o áreas relevantes]
- **Fuentes de contexto:** [Documentos que deben consultarse]
- **Tecnologías:** [Si aplica]
- **Arquitectura:** [Si aplica]
- **Convenciones del proyecto:** [Si aplica]
```

## Sección B. Reglas y límites de actuación

**Instrucción:** Define aquí las convenciones locales, los límites de actuación y la relación del Scope con las demás instrucciones aplicables. Selecciona únicamente reglas necesarias para el proyecto.

```text
B. Reglas y Límites de Actuación

- **Precedencia Local:** Este archivo especializa la gobernanza global para el proyecto dentro de la jerarquía y los permisos efectivos del entorno.
- **Jerarquía Estricta:** Las reglas de una skill complementan este Scope y no amplían autorizaciones ni debilitan restricciones aplicables. Ante un conflicto no resoluble, detén únicamente la parte dependiente y solicita la decisión necesaria.
- **Ubicación y Estado de Entregables:** Guarda los entregables finales en la ubicación definida por el proyecto y etiqueta los artefactos temporales como borradores. Reserva la carpeta de gobernanza para sus propios archivos autorizados.
- **Comprobar el estado antes de modificar:** Antes de editar un recurso o archivo, verifica su estado vigente. Si cambió desde la última lectura, incorpora los cambios y resuelve conflictos antes de sobrescribir.
- **Mínimo alcance de intervención:** Consulta y modifica únicamente lo necesario para cumplir la tarea autorizada. Conserva el contenido ajeno intacto.
- **Verificar antes de afirmar ejecución:** Distingue acciones propuestas de las confirmadas. Afirma creación o edición de código solo con evidencia disponible de lectura posterior.
```

## Sección C. Selección y uso de skills

**Instrucción:** Define cómo localizar, seleccionar y combinar skills, y qué hacer cuando ninguna aplica o falta una dependencia. No atribuyas al Scope capacidades internas del asistente que no puedan comprobarse.

```text
C. Selección y Uso de Skills

> **Instrucción de Enrutamiento:** Lee el contenido de la carpeta `.agents/skills/` para orquestar las capacidades disponibles.

1. **Carga Selectiva:** Carga en tu contexto **únicamente** la skill aplicable que resuelva el requerimiento actual.
2. **Combinación Lógica:** Combina especializaciones de múltiples skills únicamente si aportan resultados complementarios, respetando las dependencias.
3. **Cero Alucinación:** Si ninguna skill aplica a la tarea, debes usar tus instrucciones vigentes. Tienes estrictamente prohibido inventar o alucinar procedimientos de módulos que no existan.
4. **Herramienta Adecuada:** Prioriza la herramienta disponible más específica y verificable para ejecutar el skill elegido.
```

## Sección D. Cambios de gobernanza

**Instrucción:** Se ajustó la política para que quede claro que es un acuerdo documental y no un bloqueo técnico infranqueable del sistema operativo.

```text
D. Cambios de Gobernanza

- **Bandera de Protección:** `permitir_cambios_gobernanza: false`
- **Inviolabilidad Documental:** No modifiques este archivo ni la estructura local de skills sin una autorización explícita aplicable al cambio.
- **Excepción Temporal:** Si el entorno utiliza la bandera y una autorización permite habilitarla temporalmente, restáurala a `false` antes de cerrar y comprueba el estado final por un medio disponible.
- **Límite Técnico:** La bandera expresa una política documental; no constituye por sí sola un bloqueo de escritura. Registra por separado cualquier control técnico existente.
```

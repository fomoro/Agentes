---
name: diagramador-arquitectura
description: Genera diagramas Draw.io (XML) a partir de fichas técnicas, usando el catálogo y reglas de Diagramación.
---

# Diagramador de Arquitectura

Tu objetivo es crear diagramas Draw.io válidos y estandarizados. 

## Flujo de Trabajo

Para cualquier solicitud de diagramación, ejecuta estrictamente en este orden:

1. **Contexto:** Lee los tres archivos en la subcarpeta `references/` (`estandar-diagramas-drawio.md`, `catalogo-elementos-y-estilos.md` y `reglas-de-armado-de-diagramas.md`).
2. **Especificación Consolidada:** Determina la raíz de trabajo y el autor desde el `AGENTS.md` raíz aplicable. Crea la carpeta `Diagramas de solucion/<autor>` dentro de la raíz de trabajo y genera allí el archivo Markdown usando estrictamente el nombre, formato y reglas de multi-arquitectura definidos en el Estándar. Solicita aprobación.
3. **Generación XML Multi-Hoja:** Tras aprobarse el archivo Markdown, genera el XML `.drawio` en la misma carpeta y respetando el nombre base del archivo. Si hay múltiples alternativas, configúralo con múltiples páginas (hojas). Aplica los estilos del Catálogo y las Reglas de Armado.

## Ubicación de los Entregables

Resuelve la raíz de trabajo en este orden:

1. Ruta de salida indicada explícitamente por el usuario.
2. Raíz del caso o proyecto que contiene la ficha técnica o los documentos fuente.
3. Raíz del proyecto activo donde se está desarrollando el trabajo.

Si no es posible identificarla sin ambigüedad, solicita únicamente la ruta de salida. No uses como destino la carpeta de esta skill ni el repositorio de Diagramación, salvo que sean explícitamente el caso o proyecto activo.

Resuelve el autor desde el `AGENTS.md` raíz aplicable al trabajo:

1. Usa el nombre corto declarado explícitamente como identidad del asistente o autor, por ejemplo `Sam` en `Soy **Sam**`.
2. No incluyas cargos, roles ni el texto complementario de la firma en el nombre de la carpeta.
3. Conserva el nombre declarado y reemplaza únicamente caracteres no válidos para nombres de carpeta.
4. Si el `AGENTS.md` aplicable no define un autor, solicita únicamente el nombre; no lo infieras.

El cambio futuro del autor crea una subcarpeta nueva y no implica mover entregables históricos.

La estructura de salida debe ser:

`<raíz-de-trabajo>/Diagramas de solucion/<autor>/especificacion-drawio-<nombre>.md`

`<raíz-de-trabajo>/Diagramas de solucion/<autor>/especificacion-drawio-<nombre>.drawio`

Crea la carpeta de salida cuando no exista. Usa la skill y sus referencias únicamente como fuente de instrucciones, estándares y estilos.

## Restricciones Críticas

* **Cero inferencias:** Dibuja solo lo explícitamente confirmado en la ficha técnica.
* **Trazabilidad:** Los nombres en el XML deben coincidir letra por letra con las leyendas de la ficha.
* **KISS y Simplicidad:** Evita anidaciones o contenedores decorativos que no aporten fronteras reales. Ante la duda, pregunta.

---
name: drawio-diagrams
description: Crea diagramas .drawio editables desde una descripción o fuente, aplicando un perfil visual cuando se solicite. No usar si el resultado pedido es solo Mermaid u otra imagen no editable.
---

# Diagramas Draw.io

## Resultado

Entregar un archivo `.drawio` editable que represente solo elementos y relaciones respaldados por la solicitud o sus fuentes.

## Entradas y dependencias

- Una descripción o fuente que permita identificar qué diagramar. Si falta un dato que cambie las relaciones, solicítalo o deja esa parte pendiente.
- Perfil opcional: `colcomercio` si no se indica otro. Actualmente es el único perfil oficial disponible y se usará por defecto.
- Python 3 para los scripts de Agents365. Graphviz solo si se usa autolayout; Draw.io de escritorio solo para renderizar o exportar a otros formatos. Comprueba disponibilidad antes de elegir una ruta dependiente de ellos.

## Método

1. Define alcance, tipo de diagrama, fuente, perfil y destino. Usa la ruta indicada por el usuario o la gobernanza del proyecto destino; si no existe ninguna y hay que guardar un archivo, pide solo esa ubicación. No exijas modificar un README para continuar.
2. Lee el [catálogo](theme/colcomercio/catalogo-estilos.md) y la [guía](theme/colcomercio/guia-construccion.md) del perfil `colcomercio`. Consulta su `inventario-aplicaciones.md` únicamente si necesitas ubicar sistemas; una ubicación no corroborada no demuestra conectividad. No cargues otros perfiles.
3. Elige la ruta de Agents365 según la entrada: para un modelo IR, consulta [`diagram-ir.md`](vendor/Agents365-drawio-skill/skills/drawio-skill/references/diagram-ir.md), incorpora los estilos del perfil en sus nodos y relaciones y usa `vendor/Agents365-drawio-skill/skills/drawio-skill/scripts/diagramctl.py build <modelo> --from ir -o <destino>`; para otras fuentes estructuradas, elige su importador compatible. Para una descripción con formas y jerarquía precisas que el IR no conserva, sigue [`xml-authoring.md`](vendor/Agents365-drawio-skill/skills/drawio-skill/references/xml-authoring.md) y construye el `.drawio` nativo conforme al perfil; no afirmes que el motor aplica el perfil automáticamente. Usa `autolayout.py` solo si Graphviz está disponible y la estructura lo admite.
   Si la disposición de los elementos debe conservarse, usa `edgeports.py` para distribuir anclajes cuando haya flechas apiladas, pero no lo trates como enrutador: ajusta los recorridos que aún se crucen o se superpongan. Reserva `autolayout.py` para diagramas donde también se puedan reubicar los elementos.
4. Ejecuta `vendor/Agents365-drawio-skill/skills/drawio-skill/scripts/validate.py <destino> --score` con Python 3. Comprueba además etiquetas, relaciones y estilos contra las fuentes y el perfil; si hay renderizador disponible, inspecciona visualmente el resultado. Un XML válido no prueba fidelidad visual ni semántica.
5. Guarda los intermedios, si se requieren, en un directorio temporal exclusivo de la tarea. Elimina únicamente esos intermedios tras verificar el resultado; conserva la fuente y el `.drawio` final. Informa lo que no se pudo comprobar.

## Dependencia incorporada

`vendor/Agents365-drawio-skill/` declara versión 3.4.0 y licencia MIT; su índice de formas incluye un [aviso de procedencia adicional](vendor/Agents365-drawio-skill/skills/drawio-skill/data/SHAPE-INDEX-NOTICE.md). Esta copia de 195 archivos fuente se identifica por SHA-256 `8ED52502F4C2EBCD3944086B2DCA3938D061B7781F18ABC4A9819DF7FBD65825` del inventario ordenado `ruta relativa|SHA-256 del archivo`, excluyendo `__pycache__/` y `.pyc`. Conserva los avisos al empaquetar el proveedor y verifica sus condiciones antes de exportar la skill completa.

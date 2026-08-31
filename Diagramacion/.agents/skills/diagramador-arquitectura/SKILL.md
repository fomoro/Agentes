---
name: diagramador-arquitectura
description: Crea, actualiza o revisa fichas y diagramas Draw.io de arquitectura de solución o integración. Úsala cuando la solicitud requiera un entregable de diagramación; no la actives para análisis de arquitectura sin diagrama.
---

# Diagramador de Arquitectura

## Modos de Trabajo

- **Crear:** construye la ficha y genera el Draw.io conforme al flujo.
- **Actualizar:** modifica artefactos existentes conservando lo que no forma parte del cambio solicitado.
- **Revisar:** valida los artefactos y reporta hallazgos; no modifica archivos salvo solicitud explícita.

## Referencias

- Lee `references/inventario-aplicaciones.md` antes de crear o actualizar una ficha que incluya aplicaciones o sistemas, para validar su nube o zona de despliegue.
- Lee `references/estandar-diagramas-drawio.md` para crear, actualizar o revisar la ficha y su nomenclatura.
- Lee `references/catalogo-elementos-y-estilos.md` y `references/reglas-de-armado-de-diagramas.md` antes de generar, actualizar o revisar el XML Draw.io.

## Flujo de Trabajo

1. Identifica el modo de trabajo, las fuentes confirmadas y el alcance del diagrama.
2. Antes de construir la ficha, contrasta cada aplicación o sistema con el inventario:
   - Si la fuente no indica nube o zona y existe una coincidencia única, usa el valor del inventario.
   - Si la fuente contradice el inventario, informa la discrepancia y solicita definición antes de continuar.
   - Si no existe una coincidencia única, conserva la ubicación como `Por definir`; no infieras.
3. Resuelve la raíz del caso o proyecto activo y el autor aplicable.
4. Crea o actualiza la ficha conforme al estándar. En modo revisión, registra hallazgos sin modificar archivos.
5. Solicita aprobación de la ficha antes de generar o regenerar el XML, salvo que ya esté aprobada explícitamente en la solicitud actual.
6. Genera o actualiza el Draw.io aplicando el estándar, el catálogo y las reglas de armado.
7. Valida el criterio de cierre antes de entregar.

## Ubicación de los Entregables

Resuelve la raíz de trabajo en este orden:

1. Ruta de salida indicada explícitamente por el usuario.
2. Raíz del caso o proyecto que contiene las fuentes.
3. Raíz del proyecto activo donde se desarrolla el trabajo.

Si no puedes identificarla sin ambigüedad, solicita únicamente la ruta. No uses la carpeta de esta skill ni el repositorio de agentes como destino, salvo que sean explícitamente el caso o proyecto activo.

Resuelve el autor desde el `AGENTS.md` raíz aplicable:

1. Usa el nombre corto declarado explícitamente como identidad del asistente o autor, excluye cargos y texto complementario de la firma, y reemplaza únicamente caracteres no válidos para nombres de carpeta.
2. Si no existe un autor explícito, solicita únicamente el nombre; no lo infieras.

Guarda la ficha y el Draw.io, con la nomenclatura definida por el estándar, en:

`<raíz-de-trabajo>/Diagramas de solucion/<autor>/`

El cambio futuro del autor crea una subcarpeta nueva y no mueve entregables históricos. Crea la carpeta cuando no exista.

## Restricciones Específicas

- **Trazabilidad:** conserva en el XML los nombres exactos definidos en la ficha.
- **Cambios acotados:** al actualizar, modifica solo lo solicitado y preserva el resto.

## Criterio de Cierre

- La ficha cumple el estándar y cuenta con la aprobación requerida.
- El Draw.io comparte el nombre base de la ficha, abre correctamente y permanece editable.
- El contenido coincide con la información confirmada y respeta el catálogo y las reglas de armado.
- Las aplicaciones y sus ubicaciones fueron validadas contra el inventario o confirmadas explícitamente por el usuario.
- Ambos archivos están en la carpeta resuelta para el caso y el autor.
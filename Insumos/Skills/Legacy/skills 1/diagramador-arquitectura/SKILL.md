---
name: diagramador-arquitectura
description: Crea, actualiza o revisa fichas y diagramas Draw.io de arquitectura de solución o integración. Úsala cuando la solicitud requiera un entregable de diagramación; no la actives para análisis de arquitectura sin diagrama.
---

# Diagramador de Arquitectura

## Modos de Trabajo

- **Crear:** construye la ficha y genera el Draw.io conforme al flujo.
- **Generar:** produce el Draw.io desde una ficha existente sin crearla ni modificarla.
- **Actualizar:** modifica artefactos existentes conservando lo que no forma parte del cambio solicitado.
- **Revisar:** valida los artefactos y reporta hallazgos; no modifica archivos salvo solicitud explícita.

## Referencias

- Lee el [inventario de aplicaciones](references/inventario-aplicaciones.md) antes de crear, generar, actualizar o revisar una ficha que incluya aplicaciones o sistemas, para validar su nube o zona de despliegue.
- Lee el [estándar de diagramas](references/estandar-diagramas-drawio.md) para crear, generar, actualizar o revisar la ficha y su nomenclatura.
- Lee el [catálogo de elementos y estilos](references/catalogo-elementos-y-estilos.md) y las [reglas de armado](references/reglas-de-armado-de-diagramas.md) antes de generar, actualizar o revisar el XML Draw.io.

## Flujo para Crear, Generar o Actualizar

1. Identifica las fuentes confirmadas, el alcance y el nivel del diagrama.
2. Resuelve la raíz de trabajo y el autor conforme a **Ubicación de los entregables**.
3. Antes de construir o validar la ficha, contrasta cada aplicación o sistema con el inventario mediante coincidencia exacta del nombre, ignorando mayúsculas, minúsculas y espacios exteriores. No uses coincidencias parciales ni aproximadas:
   - Si la fuente no indica nube o zona y existe una coincidencia única, usa el valor del inventario.
   - Si la fuente contradice el inventario, informa la discrepancia y solicita definición; no elijas un valor.
   - Si no existe una coincidencia única, deja vacío el campo `Frame` y registra la ubicación en `Pendientes`; no infieras.
4. Aplica el modo solicitado:
   - **Crear:** construye la ficha conforme al estándar.
   - **Generar:** usa la ficha indicada como fuente; no la copies, reemplaces ni completes. La orden explícita de generar su Draw.io aprueba esa versión para diagramación.
   - **Actualizar:** cambia únicamente lo solicitado y conserva el resto.
5. Antes de escribir el XML, ejecuta un control interno: valida la anidación, resuelve las relaciones entre plataformas con la matriz de conectividad y verifica los criterios previos de revisión. Si falta un dato o la correspondencia no es inequívoca, informa únicamente el pendiente necesario y detente; no infieras.
6. Solicita aprobación solo cuando hayas creado o modificado una ficha y la solicitud actual no apruebe esa versión. No solicites una segunda aprobación en modo **Generar**.
7. Genera o actualiza el Draw.io aplicando el estándar, el catálogo y las reglas de armado.
8. Abre el archivo, confirma que sea editable y valida el criterio de cierre.

## Flujo para Revisar

1. Identifica los artefactos, las fuentes confirmadas y el alcance de la revisión.
2. Contrasta la ficha con el estándar y el inventario mediante la coincidencia exacta definida para crear o actualizar.
3. Contrasta el Draw.io con la ficha, el catálogo y las reglas de armado.
4. Reporta hallazgos concretos, su ubicación y el ajuste requerido. No modifiques archivos salvo solicitud explícita.
5. Valida el criterio de cierre de revisión.

## Ubicación de los Entregables

Resuelve la raíz de trabajo en este orden:

1. Ruta de salida indicada explícitamente por el usuario.
2. Raíz del caso o proyecto que contiene las fuentes.
3. Raíz del proyecto activo donde se desarrolla el trabajo.

Si no puedes identificarla sin ambigüedad, solicita únicamente la ruta. No uses la carpeta de esta skill ni el repositorio de agentes como destino, salvo que sean explícitamente el caso o proyecto activo.

Resuelve el autor desde la clave `autor_entregables` del `AGENTS.md` global de configuración de Codex, no desde la gobernanza del proyecto:

1. Lee `autor_entregables` en la configuración canónica global.
2. Si su valor referencia otra clave, resuélvela de forma recursiva hasta obtener un valor literal.
3. No uses como autor nombres de claves, variables ni placeholders.
4. Reemplaza únicamente caracteres no válidos para nombres de carpeta.
5. Si el valor no existe, está vacío o no puede resolverse, solicita únicamente el nombre; no lo deduzcas de la conversación ni de archivos del proyecto.

Guarda la ficha y el Draw.io, con la nomenclatura definida por el estándar, en:

`<raíz-de-trabajo>/Diagramas de solucion/<autor>/`

El cambio futuro del autor crea una subcarpeta nueva y no mueve entregables históricos. Crea la carpeta cuando no exista.

## Restricciones Específicas

- **Trazabilidad:** conserva en el XML los nombres exactos definidos en la ficha.
- **Cambios acotados:** al actualizar, modifica solo lo solicitado y preserva el resto.

## Criterios de Cierre

### Crear, Generar o Actualizar

- La ficha cumple el estándar aplicable y cuenta con la aprobación requerida por el modo.
- El Draw.io comparte el nombre base de la ficha, abre correctamente y permanece editable.
- El contenido coincide con la información confirmada y respeta el catálogo y las reglas de armado.
- Las ubicaciones de las aplicaciones fueron validadas contra el inventario, confirmadas explícitamente o registradas en `Pendientes` sin asignar un frame inferido.
- En modo **Generar**, la ficha original permanece en su ubicación y solo se crea el Draw.io. En **Crear** o **Actualizar**, se guardan únicamente los artefactos solicitados.

### Revisar

- La revisión cubre ficha, Draw.io, inventario, catálogo y reglas aplicables al alcance solicitado.
- Cada hallazgo identifica el artefacto afectado, la inconsistencia y el ajuste requerido.
- No se modificaron archivos sin autorización explícita.

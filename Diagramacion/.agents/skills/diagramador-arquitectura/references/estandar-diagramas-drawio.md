# Guía de construcción de fichas de diagramas

Toda ficha debe indicar qué contiene el diagrama y cómo se relacionan sus elementos, sin definir posiciones, dimensiones ni estilos.

## Formato y Nomenclatura

- **Ubicación:** Guardar la ficha y el Draw.io en `<raíz-de-trabajo>/Diagramas de solucion/<autor>/`.
- **Autor:** Obtener `<autor>` del nombre corto declarado como identidad del asistente o autor en el `AGENTS.md` raíz aplicable. Si no está definido, solicitarlo y no inferirlo.
- **Archivo:** El archivo generado debe llamarse `especificacion-drawio-<nombre>.md`. El XML resultante usará el mismo nombre base con extensión `.drawio`.
- **Título interno:** Usar el título `# Especificación de diagrama - <Nombre>`.
- **Autoría interna:** Incluir inmediatamente después del título la línea `Autor: <autor>`.

### Multi-Arquitectura
Si el diagrama abarca múltiples escenarios o alternativas, **NO crees archivos separados**. Usa un único archivo `.md` y crea un subtítulo por cada arquitectura (ej. `## Alternativa 1`). Debajo de cada subtítulo, debes incluir las dos tablas descritas a continuación.

## Estructura visual

| Zona | Frame | Contenedor | Elemento | Leyenda | Estado |
|---|---|---|---|---|---|
| `<Zona>` | `<Frame o vacío>` | `<Contenedor o vacío>` | `<Tipo>` | `<Nombre visible>` | `<Estado>` |

- Incluir un elemento por fila.
- Usar la jerarquía `Zona → Frame → Contenedor → Elemento` y dejar vacío el nivel que no aplique.
- En **Contenedor**, escribir la leyenda exacta del componente padre.
- Usar zonas, frames y tipos definidos en el [catálogo](catalogo-elementos-y-estilos.md).
- Registrar el estado como `Nuevo`, `Modificado`, `Reuso` o `—`.

## Relaciones

| Origen | Destino |
|---|---|
| `<Leyenda de origen>` | `<Leyenda de destino>` |

- Incluir una relación confirmada por fila.
- Usar las leyendas exactas de la tabla **Estructura visual**.
- Registrar la conexión desde el origen hacia el destino.
- No inferir elementos ni relaciones no confirmados.

Para construir el Draw.io, aplicar las [reglas de armado](reglas-de-armado-de-diagramas.md) y los estilos del catálogo.

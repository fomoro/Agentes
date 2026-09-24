# Guía de construcción de fichas de diagramas

Toda ficha debe indicar qué contiene el diagrama y cómo se relacionan sus elementos, sin definir posiciones, dimensiones ni estilos.

## Formato y Nomenclatura

- **Archivo:** El archivo generado debe llamarse `especificacion-drawio-<nombre>.md`. El XML resultante usará el mismo nombre base con extensión `.drawio`.
- **Título interno:** Usar el título `# Especificación de diagrama - <Nombre>`.
- **Autoría interna:** Incluir inmediatamente después del título la línea `Autor: <autor>`, usando el autor resuelto por la skill.

### Arquitecturas y páginas

Usa un único archivo `.md` y un único archivo `.drawio` por entregable. En la ficha, crea una sección por arquitectura con **Contexto**, **Estructura visual** y **Relaciones**. En el Draw.io, crea una página por arquitectura con el mismo nombre exacto de su sección. Aplica esta estructura tanto para una arquitectura como para múltiples escenarios o alternativas.

## Contexto

| Campo | Valor |
|---|---|
| Objetivo | `<Pregunta concreta que responde>` |
| Alcance | `<Qué incluye y qué excluye>` |
| Nivel | `<Solución, Integración o Ambos>` |
| Fuentes confirmadas | `<Archivos, documentos o decisiones usadas>` |
| Pendientes | `<Datos sin definir o Ninguno>` |

- No conviertas supuestos ni pendientes en hechos confirmados.
- Registra aquí cualquier dato faltante que impida aplicar una convención sin inferirlo.

## Estructura visual

| Zona | Frame | Contenedor | Elemento | Leyenda | Estado |
|---|---|---|---|---|---|
| `<Zona>` | `<Frame o vacío>` | `<Contenedor o vacío>` | `<Tipo>` | `<Nombre visible>` | `<Estado>` |

- Incluir un elemento por fila.
- La **Leyenda** debe ser única dentro de cada arquitectura.
- Usar la jerarquía `Zona → Frame → Contenedor → Elemento` y dejar vacío el nivel que no aplique.
- En **Contenedor**, escribir la leyenda exacta del componente padre.
- Usar zonas, frames y tipos definidos en el [catálogo](catalogo-elementos-y-estilos.md).
- Si la ubicación de una aplicación o sistema no está confirmada, dejar **Frame** vacío y registrarla en **Pendientes**. `Por definir` no es un frame del catálogo.
- Registrar el estado como `Nuevo`, `Modificado`, `Reuso` o `—`.

## Relaciones

| Origen | Destino | Tipo | Etiqueta |
|---|---|---|---|
| `<Leyenda de origen>` | `<Leyenda de destino>` | `<Conexión Síncrona, Conexión Asíncrona o Por definir>` | `<Interacción confirmada o vacío>` |

- Incluir una relación confirmada por fila.
- Usar las leyendas exactas de la tabla **Estructura visual**.
- Registrar la conexión desde el origen hacia el destino.
- Usar `Por definir` únicamente cuando la relación esté confirmada pero su tipo no lo esté; registrarlo también en **Pendientes**.
- La etiqueta funcional es opcional y solo debe incluir información confirmada. Los nombres de los tramos físicos se obtienen de la matriz de conectividad al armar el Draw.io.
- No inferir elementos ni relaciones no confirmados.

Para construir el Draw.io, aplicar las [reglas de armado](reglas-de-armado-de-diagramas.md) y los estilos del catálogo.

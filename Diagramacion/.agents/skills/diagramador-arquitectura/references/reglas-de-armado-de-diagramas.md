# Reglas de armado de diagramas

Para estilos, elementos y conexiones aprobados, consulta el [Catálogo de convenciones de diagramación](catalogo-elementos-y-estilos.md).

## Alcance

| Regla | Aplicación |
|---|---|
| Objetivo | Cada diagrama debe responder una pregunta concreta. |
| Alcance | Mostrar solo los elementos y relaciones necesarios. |
| Nivel | Definir si es de solución, integración o ambos. |

## Zonas y contenedores

| Regla | Aplicación |
|---|---|
| Zonas | Usarlas solo cuando aporten una responsabilidad o frontera visible. |
| Orden | Puede cambiar según la historia que debe explicar el diagrama. |
| Repetición | Una zona se puede repetir o apilar cuando mejora la lectura. |
| Frames | Usarlos cuando proveedor, entorno o frontera de red sean relevantes. |
| Anidación | Cada contenedor debe aportar significado; evitar anidaciones decorativas. |

## Elementos

| Regla | Aplicación |
|---|---|
| Fuente de verdad | Usar elementos y estilos del catálogo vigente. |
| Uso | Cada ícono representa una responsabilidad o comportamiento real. |
| Notas | Usarlas solo para aclaraciones necesarias. |
| Paso | Usarlo solo cuando el orden secuencial sea relevante. |
| Estado | Aplicar el color definido en el catálogo según el estado informado en la ficha. Si el estado es `—`, usar fondo blanco (`#FFFFFF`) y letra negra (`#000000`). |

## Conexiones

| Regla | Aplicación |
|---|---|
| Dirección | Toda relación debe tener origen y destino claros. |
| Tipo | Usar síncrona o asíncrona según el comportamiento real. |
| Etiqueta | Incluirla solo si aporta contexto del tramo, protocolo o medio. |
| Pivote | Usarlo únicamente para una demarcación o dos tramos diferenciados. |

## Espaciado y dimensiones

| Elemento | Regla de espaciado | Medida |
|---|---|---:|
| Entre zonas | Separación horizontal entre swimlanes adyacentes | Mínimo `30 px` |
| Zona a frame | Margen interno entre el borde de la zona y el frame | Mínimo `40 px` |
| Márgenes de frame | Distancia entre el borde del frame y sus contenedores o elementos internos | Mínimo `40 px` |
| Entre componentes | Separación mínima vertical y horizontal entre elementos | Mínimo `20 px` |

## Flujo y orientación

| Regla | Aplicación |
|---|---|
| Dirección principal | Definirla según la historia del diagrama. Usar izquierda a derecha cuando facilite la lectura, sin imponer un orden fijo de zonas. |
| Flujo vertical | Usarlo dentro de contenedores o para agrupar elementos cuando mejore la lectura. |
| Cruces de líneas | Evitarlos en lo posible: reubicar elementos para mantener trayectorias directas y paralelas. Si son inevitables, usar salto de línea en arco (`jumpStyle=arc`) para indicar que las conexiones no se unen. |

## Revisión

| Criterio | Validación |
|---|---|
| Lectura | Se entiende el objetivo y el flujo principal. |
| Legibilidad | No hay solapamientos ni texto atravesado por líneas. |
| Consistencia | Se respetan estilos y elementos del catálogo. |
| Precisión | No se representan datos técnicos no confirmados. |
| Editable | El archivo Draw.io se conserva editable. |

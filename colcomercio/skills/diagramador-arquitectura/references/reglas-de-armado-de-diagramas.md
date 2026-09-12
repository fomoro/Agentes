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
| Repetición | Repetir una zona solo cuando el flujo de la ficha vuelva a ella y la repetición mejore la secuencia. Cada aparición contiene únicamente los elementos que correspondan a ese tramo. |
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
| Tipo | Usa el tipo registrado en la ficha. Si figura `Por definir`, conserva el pendiente y no representes la relación como definitiva en el Draw.io. |
| Relaciones de acceso | Si al menos un extremo es un actor o un dispositivo de acceso, no apliques la matriz entre plataformas ni agregues tramos físicos. Conserva únicamente la relación funcional confirmada en la ficha. |
| Conectividad entre plataformas | Cuando ambos extremos sean aplicaciones, sistemas o plataformas, cruza sus entornos confirmados con la matriz bidireccional del catálogo. Aplica solo una correspondencia inequívoca conforme a sus criterios. Si faltan datos o no existe una única correspondencia, registra el caso en `Pendientes`; no infieras conectividad ni la deduzcas por la posición visual. |
| Etiquetas | En relaciones entre plataformas, muestra obligatoriamente los tramos de la correspondencia aplicada. La etiqueta funcional de la ficha es opcional y solo se muestra cuando aporta información confirmada adicional. |
| Pivote | Inclúyelo cuando la matriz indique la demarcación `Pivote`; no lo agregues por criterio visual. |

## Espaciado y dimensiones

| Elemento | Regla de espaciado | Medida |
|---|---|---:|
| Entre zonas | Separación horizontal entre swimlanes adyacentes | Mínimo `30 px` |
| Zona a frame | Margen interno entre el borde de la zona y el frame | Mínimo `40 px` |
| Márgenes de frame | Distancia entre el borde del frame y sus contenedores o elementos internos | Mínimo `40 px` |
| Tamaño de frame | Dimensiones mínimas totales de la geometría (ancho x alto) | Mínimo `300 x 200 px` |
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
| Consistencia | Se respetan la ficha, los estilos, los elementos y la conectividad del catálogo. |
| Precisión | No se representan datos técnicos no confirmados. |
| Editable | El archivo Draw.io se conserva editable. |

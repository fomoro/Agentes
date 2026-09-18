# Catálogo de convenciones de diagramación

Este catálogo consolida las convenciones visuales aprobadas para diagramas de arquitectura de solución e integración en Draw.io. Es la fuente de verdad para contenedores, elementos, conectividad y estilos.

## Convenciones de lectura

| Convención | Regla |
|---|---|
| Tamaño | Se expresa como `ancho x alto px`. |
| Tamaño mínimo | Es el menor tamaño permitido; el contenedor se amplía según su contenido. |
| Capitalización | Las etiquetas usan mayúscula inicial en cada palabra; no se usan mayúsculas sostenidas. Se conservan las siglas y nombres oficiales. |
| Fuente estándar | Para XML: `fontFamily=&quot;72&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif`. Aplica a todo texto del diagrama. |
| `—` | Indica que la característica no aplica a ese caso. |
| Etiqueta | La ubicación indicada en cada tabla define dónde se muestra el nombre del elemento. |

## Estructura visual

La jerarquía es opcional: una zona puede contener frames, componentes o elementos directamente.

### Zonas

| Zona | Forma Draw.io | Color de relleno | Color de gradiente | Dirección | Etiqueta | Tamaño de letra | Estilo de letra | Color de la letra | Sombra |
|---|---|---:|---:|---|---|---:|---|---|---|
| Externos | `swimlane; startSize=30; fontStyle=1; align=center` | `#F5F5F5` | `#B3B3B3` | Sur | Cabecera de zona | `14 px` | Negrita | Negro | Sí |
| Aplicaciones | `swimlane; startSize=30; fontStyle=1; align=center` | `#D5E8D4` | `#97D077` | Sur | Cabecera de zona | `14 px` | Negrita | Negro | Sí |
| Integración | `swimlane; startSize=30; fontStyle=1; align=center` | `#60A917` | `#3B770D` | Sur | Cabecera de zona | `14 px` | Negrita | Blanco | Sí |
| Accesos | `swimlane; startSize=30; fontStyle=1; align=center` | `#647687` | `#40515F` | Sur | Cabecera de zona | `14 px` | Negrita | Blanco | Sí |
| Actores | `swimlane; startSize=30; fontStyle=1; align=center` | `#D5E8D4` | `#97D077` | Sur | Cabecera de zona | `14 px` | Negrita | Negro | Sí |
| Ecosistema De Datos | `swimlane; startSize=30; fontStyle=1; align=center` | `#60A917` | `#3B770D` | Sur | Cabecera de zona | `14 px` | Negrita | Blanco | Sí |

### Frames

| Frame | Forma Draw.io | Color de relleno | Color de gradiente | Dirección | Gradiente | Etiqueta | Tamaño de letra | Estilo de letra | Color de la letra | Sombra |
|---|---|---:|---:|---|---|---|---:|---|---|---|
| OnPremise | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#F5F5F5` | `#F5F5F5` | Sur | Sí | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| SAP Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#DAE8FC` | `#7EA6E0` | Sur | Sí | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| Oracle Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#F8CECC` | `#EA6B66` | Sur | Sí | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| Privado Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#D5E8D4` | `#97D077` | Sur | Sí | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| AWS Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#FFCD28` | `#FFA500` | Sur | Sí | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| Microsoft 365 | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#B1DDF0` | — | — | No | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| Salesforce Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#0050EF` | — | — | No | Pestaña del frame | `12 px` | Negrita | Blanco | Sí |
| GCP Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#F8CECC` | — | — | No | Pestaña del frame | `12 px` | Negrita | Negro | Sí |
| Microsoft Azure Nube | `shape=umlFrame; rounded=0; container=1; fontStyle=1; width=150; height=30; whiteSpace=wrap; html=1` | `#1BA1E2` | — | — | No | Pestaña del frame | `12 px` | Negrita | Blanco | Sí |

### Componentes

| Tipo de componente | Uso | Forma Draw.io | Tamaño | Etiqueta | Tamaño de letra | Estilo de letra | Sombra |
|---|---|---|---:|---|---:|---|---|
| Componente simple | No contiene componentes hijos | `rounded=0; fillColor=<según estado>; strokeColor=#000000; verticalAlign=middle` | Mínimo `120 x 50 px` | Centrada dentro del componente | `11 px` | Normal | Sí |
| Componente contenedor | Agrupa uno o más componentes hijos | `rounded=0; fillColor=<según estado>; strokeColor=#000000; verticalAlign=top; container=1; fontStyle=1; spacingTop=6` | Mínimo `200 x 150 px` | Centrada arriba; hijos dentro del componente | `11 px` | Negrita | Sí |

#### Estados de componentes y elementos de arquitectura

Aplica a los componentes y a los elementos de solución e integración. No aplica a zonas, frames ni elementos de zonas.

| Estado | Color de fondo | Color de la letra |
|---|---:|---:|
| Nuevo | `#2B5935` | `#FFFFFF` |
| Modificado | `#90BD99` | `#000000` |
| Reuso | `#FFFFFF` | `#000000` |

## Elementos de zonas

| Elemento | Forma Draw.io | Tamaño | Etiqueta | Sombra |
|---|---|---:|---|---|
| Persona | `shape=umlActor` | `25 x 50 px` | Debajo del ícono | Sí |
| Portátil | `shape=mxgraph.office.devices.laptop; aspect=fixed; fillColor=#505050; strokeColor=none` | `85 x 50 px` | Debajo del ícono | No |
| Celular | `shape=mxgraph.office.devices.cell_phone_generic; aspect=fixed; fillColor=#505050; strokeColor=none` | `26 x 50 px` | Debajo del ícono | No |
| Ventanilla | `shape=mxgraph.mscae.system_center.admin_console; fillColor=#515151; strokeColor=none` | `69 x 50 px` | Debajo del ícono | Sí |
| Teléfono | `shape=mxgraph.signs.tech.telephone_4; fillColor=#000000; strokeColor=none` | `51 x 50 px` | Debajo del ícono | No |
| WhatsApp | `shape=mxgraph.webicons.whatsapp; aspect=fixed; fillColor=#4FE238; gradientColor=#138709` | `50 x 50 px` | Debajo del ícono | No |
| Carrito de compras | `shape=mxgraph.ios7.icons.shopping_cart; aspect=fixed; strokeWidth=2; strokeColor=#0080F0` | `59 x 50 px` | Debajo del ícono | No |
| SharePoint | `shape=image; aspect=fixed; image=<ícono de SharePoint>` | `51 x 50 px` | Debajo del ícono | Sí |

## Elementos de arquitectura

### Elementos compartidos

| Elemento | Forma Draw.io | Tamaño | Etiqueta | Sombra |
|---|---|---:|---|---|
| API | `ellipse; shapeInside=1; aspect=fixed` | `50 x 50 px` | Solución: debajo del ícono. Integración: dentro del ícono. | Sí |
| Servicio | `shape=providedRequiredInterface; aspect=fixed` | `50 x 50 px` | Debajo del ícono | Sí |
| Pivote | `shape=isoCube2; backgroundOutline=1; isoAngle=15` | `50 x 50 px` | Debajo del ícono | Sí |
| Paso | `ellipse; aspect=fixed` | `50 x 50 px` | Dentro del ícono: número secuencial | Sí |

### Solución

| Elemento | Forma Draw.io | Tamaño | Etiqueta | Sombra |
|---|---|---:|---|---|
| Carpeta | `shape=mxgraph.mscae.enterprise.shared_folder` | `50 x 50 px` | Debajo del ícono | Sí |
| Syncout (Solución) | `ellipse; dashed=1; aspect=fixed` | `50 x 50 px` | Debajo del ícono | Sí |
| Notas | `shape=note; backgroundOutline=1; darkOpacity=0.05` | `50 x 50 px` | Debajo del ícono | Sí |

### Integración

| Elemento | Forma Draw.io | Tamaño | Etiqueta | Sombra |
|---|---|---:|---|---|
| Orquestación | `shape=mxgraph.eip.process_manager; fillColor=none` | `55 x 50 px` | Debajo del ícono | No |
| Request/Response JSON | `shape=mxgraph.weblogos.json; aspect=fixed` | `40 x 50 px` | Debajo del ícono | No |
| Autenticación OAuth 2.0 | `image; image=img/lib/azure2/security/Conditional_Access.svg; aspect=fixed` | `41 x 50 px` | Debajo del ícono | No |
| Colas | `shape=cylinder3; direction=south; aspect=fixed` | `100 x 50 px` | Debajo del ícono | No |
| Enrutamiento | `shape=mxgraph.eip.content_based_router; fillColor=none` | `87 x 50 px` | Debajo del ícono | No |
| Regla Decisión | `shape=dataStorage; direction=west; aspect=fixed` | `80 x 50 px` | Debajo del ícono | No |
| Schedule | `shape=mxgraph.azure.scheduler; aspect=fixed` | `40 x 50 px` | Debajo del ícono | No |
| Validación Datos | `shape=hexagon` | `50 x 50 px` | Debajo del ícono | Sí |
| Caché | `rounded=1` | `55 x 50 px` | Dentro del ícono | Sí |
| Webhook | `shape=collate; direction=north` | `67 x 50 px` | Debajo del ícono | Sí |
| Reintentos | `shape=mxgraph.flowchart.decision; aspect=fixed` | `50 x 50 px` | Debajo del ícono | Sí |
| Syncout (Integración) | `shape=umlBoundary` | `63 x 50 px` | Dentro del ícono | No |
| Paginación | `shape=mxgraph.flowchart.multi-document; boundedLbl=1` | `73 x 50 px` | Dentro del ícono | No |
| Data Transformada | `shape=mxgraph.office.communications.transport_rule; fillColor=#505050` | `50 x 50 px` | Debajo del ícono | No |

## Conectividad

### Conectividad entre plataformas

Esta matriz describe conectividad física y se aplica en ambos sentidos. Para una relación en sentido inverso, intercambia origen y destino, invierte el orden de los tramos y conserva la demarcación. La dirección funcional de la interacción proviene de la ficha y no cambia por esta regla.

| Origen | Tramo de salida | Demarcación | Tramo de llegada | Destino |
|---|---|---|---|---|
| OnPremise | FloNetworks DCI | — | — | Microsoft Azure Nube |
| OnPremise | FloNetworks DCI | — | — | AWS Nube |
| Microsoft Azure Nube: suscripción de Colcomercio, misma región | Conexión Interna | — | — | Microsoft Azure Nube: misma suscripción de Colcomercio, misma región |
| Nube o misma nube en región A | Internet | — | — | Otra nube o misma nube en región B |
| Oracle Nube | Oracle FastConnect | Pivote | FloNetworks DCI | Microsoft Azure Nube |
| Oracle Nube | Oracle FastConnect | Pivote | FloNetworks DCI | AWS Nube |
| Oracle Nube | Oracle FastConnect | — | — | OnPremise |

### Tipos de conexión de arquitectura de solución e integración

| Tipo de conexión | Forma Draw.io base (Línea recta) | Texto girado (`A↻`) |
|---|---|---|
| Conexión Síncrona | `edgeStyle=none; endArrow=classic` | `horizontal=0` |
| Conexión Asíncrona | `edgeStyle=none; endArrow=classic; dashed=1` | `horizontal=0` |

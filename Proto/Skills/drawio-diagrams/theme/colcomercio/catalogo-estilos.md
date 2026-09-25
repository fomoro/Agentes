# Catálogo de estilos — Colcomercio

- Actualizado: el 2026-09-25 01:38
- Rol de ejecución: diseño visual y arquitectura de skills
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo

Definir las decisiones visuales propias de Colcomercio para diagramas de solución e integración. Este perfil fija colores, contenedores y representaciones de elementos; la geometría y el espaciado deben comprobarse en el resultado de la ruta de construcción elegida. La ubicación de sistemas y la conectividad física no se deducen del estilo.

## Base visual

- **Zonas:** `swimlane`, título centrado y negrita de 14 px, con sombra. **Frames:** `umlFrame`, título en la pestaña y negrita de 12 px, con sombra. Ambos admiten elementos hijos y ajustan su tamaño al contenido.
- En `umlFrame`, ajustar la propiedad de estilo `width` al ancho del título más un margen para mantenerlo en una línea; conservar `whiteSpace=wrap` y no confundir `width` de la pestaña con el ancho total del frame.
- **Texto:** preferir Helvetica Neue, con Helvetica o Arial como alternativas. Usar mayúscula inicial en las etiquetas comunes y conservar la grafía oficial de productos y siglas.
- En las tablas, '—' significa sin degradado. Cuando exista, aplicarlo hacia abajo (`gradientDirection=south`).

## Componentes

Ambos usan rectángulo de esquinas rectas, fondo blanco, borde negro, sombra y texto de 11 px. El motor ajusta sus dimensiones al contenido.

| Tipo | Función visual |
| :--- | :--- |
| Simple | Pieza individual, sin hijos; etiqueta centrada. |
| Contenedor | Agrupa piezas hijas; etiqueta arriba y `container=1`. |

## Zonas

| Zona | Fondo | Degradado | Texto |
| :--- | :--- | :--- | :--- |
| Externos | `#F5F5F5` | `#B3B3B3` | Negro |
| Aplicaciones, Actores | `#D5E8D4` | `#97D077` | Negro |
| Integración, Ecosistema de datos | `#60A917` | `#3B770D` | Blanco |
| Accesos | `#647687` | `#40515F` | Blanco |

## Frames

| Frame | Fondo | Degradado | Borde | Texto |
| :--- | :--- | :--- | :--- | :--- |
| OnPremise | `#F5F5F5` | — | `#666666` | Negro |
| SAP Nube | `#DAE8FC` | `#7EA6E0` | `#6C8EBF` | Negro |
| Oracle Nube | `#F8CECC` | `#EA6B66` | `#B85450` | Negro |
| Privado Nube | `#D5E8D4` | `#97D077` | `#82B366` | Negro |
| AWS Nube | `#FFCD28` | `#FFA500` | `#D79B00` | Negro |
| Microsoft 365 | `#B1DDF0` | — | `#10739E` | Negro |
| Salesforce Nube | `#0050EF` | — | `#001DBC` | Blanco |
| GCP Nube | `#F8CECC` | — | `#B85450` | Negro |
| Microsoft Azure Nube | `#1BA1E2` | — | `#006EAF` | Blanco |

## Elementos

Las formas siguientes son convenciones visuales, no una lista de elementos obligatorios. Mostrar la etiqueta debajo del ícono, salvo Paso, Caché, Syncout en integración y Paginación, que la llevan dentro. En API de integración, usar el interior solo si el nombre cabe completo; de lo contrario, situarlo debajo o a un lado con `whiteSpace=wrap` y `labelWidth` ajustado al espacio disponible. Mantener la proporción del ícono al dimensionarlo. Si una clave heredada no está disponible en el motor, buscar una forma equivalente antes de sustituirla; no dejar cuadros vacíos.

### Compartidos

| Elemento | Forma |
| :--- | :--- |
| API | `ellipse; shapeInside=1`; en solución, etiqueta debajo. |
| Interfaz provista/requerida (UML) | `shape=providedRequiredInterface`; en el borde izquierdo con conexión entrante desde la izquierda, `flipH=1` orienta la curvatura hacia la conexión. No usar como símbolo de cualquier puerto circular. |
| Pivote | `shape=isoCube2`. |
| Paso | `ellipse`; número secuencial dentro. |

### Actores y accesos

| Elemento | Forma |
| :--- | :--- |
| Persona | `shape=umlActor`. |
| Portátil | `shape=mxgraph.office.devices.laptop`. |
| Celular | `shape=mxgraph.office.devices.cell_phone_generic`. |
| Ventanilla | `shape=mxgraph.mscae.system_center.admin_console`. |
| Browser | `shape=image;image=img/lib/azure2/general/Browser.svg;aspect=fixed`. Es un ícono de acceso web; su ubicación en la biblioteca no implica despliegue en Azure. |
| Teléfono | `shape=mxgraph.signs.tech.telephone_4`. |
| WhatsApp | `shape=mxgraph.webicons.whatsapp`; verde `#4FE238` con degradado `#138709`. |
| Carrito de compras | `shape=mxgraph.ios7.icons.shopping_cart`; contorno `#0080F0`. |
| SharePoint | Ícono de SharePoint de la biblioteca disponible; no usar una ruta de imagen sin resolver. |

### Solución

| Elemento | Forma |
| :--- | :--- |
| Carpeta | `shape=mxgraph.mscae.enterprise.shared_folder`. |
| Syncout | `ellipse; dashed=1`. |
| Notas | `shape=note`. |

### Integración

| Elemento | Forma |
| :--- | :--- |
| Orquestación | `shape=mxgraph.eip.process_manager; fillColor=none`. |
| Request/Response JSON | `shape=mxgraph.weblogos.json`. |
| Autenticación OAuth 2.0 | Símbolo genérico de autenticación; usar Azure Conditional Access solo si ese es el servicio representado. |
| Colas | `shape=cylinder3; direction=south`. |
| Enrutamiento | `shape=mxgraph.eip.content_based_router; fillColor=none`. |
| Regla Decisión | `rhombus`, para distinguir una decisión de un almacén de datos. |
| Schedule | Símbolo de calendario o reloj; `shape=mxgraph.azure.scheduler` solo para Azure Scheduler. |
| Validación Datos | `shape=hexagon`. |
| Caché | `rounded=1`. |
| Webhook | `shape=collate; direction=north`. |
| Reintentos | `shape=mxgraph.flowchart.decision`. |
| Syncout | `shape=umlBoundary`. |
| Paginación | `shape=mxgraph.flowchart.multi-document`. |
| Data Transformada | `shape=mxgraph.eip.message_translator`. |

Las conexiones síncronas se muestran con línea continua; las asíncronas, con línea discontinua. Ambas conservan la dirección mediante una flecha. La etiqueta de una conexión describe solo información confirmada.

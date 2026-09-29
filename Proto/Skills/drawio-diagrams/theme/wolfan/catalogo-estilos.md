# Catálogo de estilos — Colcomercio

- Actualizado: el 2026-09-29 11:55
- Rol de ejecución: diseño visual y arquitectura de skills
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo

Definir las decisiones visuales propias de Colcomercio para diagramas de solución e integración. Este perfil fija colores, contenedores y representaciones de elementos; la geometría y el espaciado deben comprobarse en el resultado de la ruta de construcción elegida. La ubicación de sistemas y la conectividad física no se deducen del estilo.

## Base visual

- **Texto:** Preferir Helvetica Neue (o Arial). Mayúscula inicial en etiquetas comunes; conservar grafía de marcas.
- **Degradados:** En las tablas, '—' indica color sólido. Todo degradado aplica hacia abajo (`gradientDirection=south`).
- **Contenedores:** Zonas y Frames admiten elementos hijos y ajustan su cuerpo al contenido.

## Componentes

Formato por defecto (cuando no aplique Zona, Frame o Elemento específico): rectángulo recto, fondo blanco, borde negro, sombra y texto 11 px.

| Tipo | Función visual |
| :--- | :--- |
| Simple | Pieza individual, sin hijos; etiqueta centrada. |
| Contenedor | Agrupa piezas hijas; etiqueta arriba y `container=1`. |

## Zonas

Agrupan lógicamente la arquitectura (dominio o capa).

- **Propiedades base:** `shape=swimlane; strokeWidth=2; shadow=1`
- **Título:** Centrado, negrita, 14 px (`fontStyle=1; fontSize=14`).

| Zona | Fondo | Degradado | Borde | Interior | Texto |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Externos | `#F8F9FA` | `#E9ECEF` | `#717578` | `#FFFFFF` | `#495057` |
| Aplicaciones, Actores | `#E8F5E9` | `#C8E6C9` | `#476E49` | `#FAFAFA` | `#1B5E20` |
| Integración, Ecosistema de datos | `#43A047` | `#2E7D32` | `#1B5E20` | `#F1F8E9` | `#FFFFFF` |
| Accesos | `#2E3B4E` | `#1A2533` | `#4A5D75` | `#F8FAFC` | `#FFFFFF` |

## Frames

Representan el entorno físico o la nube de despliegue.

- **Propiedades base:** `shape=umlFrame; strokeWidth=2; shadow=0; rounded=1; swimlaneFillColor=#FFFFFF; whiteSpace=wrap`
- **Pestaña:** Fuente regular, 14 px (`fontStyle=0; fontSize=14`). Dimensiones estrictas de `width=140; height=20` (incrementar `width` solo si el texto lo sobrepasa).

| Frame | Fondo | Degradado | Borde | Texto |
| :--- | :--- | :--- | :--- | :--- |
| OnPremise | `#f5f5f5` | `#b3b3b3` | `#666666` | Negro |
| SAP Nube | `#DAE8FC` | `#7EA6E0` | `#6C8EBF` | Negro |
| Oracle Nube | `#E53935` | `#B71C1C` | `#B71C1C` | Blanco |
| Privado Nube | `#D5E8D4` | `#97D077` | `#82B366` | Negro |
| AWS Nube | `#FFCD28` | `#FFA500` | `#D79B00` | Negro |
| Microsoft 365 | `#B1DDF0` | `#84C6E7` | `#10739E` | Negro |
| Salesforce Nube | `#0050EF` | `#0039AB` | `#001DBC` | Blanco |
| GCP Nube | `#800020` | `#4D0013` | `#4D0013` | Blanco |
| Microsoft Azure Nube | `#1BA1E2` | `#1174A6` | `#006EAF` | Blanco |

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

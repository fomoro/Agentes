# Caso de prueba 06: arquitectura RCP según el XML original

## Objetivo

Reconstruir el flujo arquitectónico descrito en el XML original como un `.drawio` editable, con el perfil `colcomercio`, sin heredar sus defectos de distribución ni inventar relaciones.

## Prompt de ejecución

> "Aplica primero `C:\Dev\Agentes\Proto\Skills\drawio-diagrams\prompts\00_generacion.md`, con base de salida `rcp_arquitectura`. Genera el diagrama RCP de izquierda a derecha con esta estructura:
>
> 1. **Actores y accesos:** `Usuario Interno` y `Usuario Externo` → `Browser`.
> 2. **Aplicaciones, primera columna:** frame `Privado Nube` → contenedor `RCP`. Dentro de RCP, apila estas 15 capacidades con sus nombres completos: `Recepción y sincronización de SKUs desde PeopleSoft`; `Consulta y selección de SKU por Facility`; `Gestión de atributos logísticos del producto`; `Parametrización de producto por depósito / Facility`; `Configuración de unidades de medida y dimensiones`; `Gestión de catálogos y listas desplegables`; `Gestión de SKU Modula`; `Gestión de producto irregular y producto anidado`; `Gestión de tracking de fechas y seriales`; `Gestión de SIOC, multiproducto e imagen del SKU`; `Replicación de configuración entre Facilities`; `Envío de configuración hacia Manhattan, PeopleSoft, PTL y Modula`; `Administración de usuarios, roles y permisos`; `Auditoría, logs y trazabilidad`; `Reportes operativos de parametrización`.
> 3. **Integración:** frame `AWS Nube` → contenedor `MuleSoft` con tres API circulares: `publicarProductosUnidadNegocio V1`, `Consultar Imagen Producto` e `Información Producto`. Normaliza solo los nombres de API según la guía de Colcomercio.
> 4. **Aplicaciones, segunda columna:** frame `GCP Nube` con `Manhattan Active Warehouse Management`; `Oracle Nube` con `PeopleSoft`; `Privado Nube` con `TMS Unigis`, `Sirv` y `SAP Comerce Cloud`; `AWS Nube` con `Shopify`, `Vtex Marketplace`, `CorbeApp` y `CorbeMóvil`.
>
> **Conexiones del XML:** ambos usuarios → Browser → RCP; RCP → las tres API; API de publicación → Manhattan y TMS; API de consulta de imagen → Sirv; API de información de producto → SAP Comerce Cloud, Shopify, Vtex Marketplace, CorbeApp y CorbeMóvil. PeopleSoft no tiene una conexión de salida desde MuleSoft en esta fuente: no la inventes. El XML también muestra un puerto sin sistema de origen identificable que entra a la API de publicación; deja ese origen pendiente, sin atribuirlo a PeopleSoft.
>
> Las convenciones, autoría y fecha del XML son metadatos, no componentes del flujo. Verifica nombres, jerarquía y conexiones antes de entregar el nuevo archivo versionado."

## Salida esperada

- `output/rcp_arquitectura vN.drawio`, con el siguiente número disponible y sin sobrescribir versiones.
- Cinco zonas de izquierda a derecha y las relaciones descritas arriba; los orígenes no identificados quedan pendientes.

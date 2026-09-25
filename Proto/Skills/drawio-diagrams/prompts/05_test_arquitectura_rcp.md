# Caso de Prueba 05: Arquitectura RCP Alta Fidelidad

## Objetivo
Validar la capacidad del motor para replicar un diagrama de arquitectura complejo de la vida real (basado en la imagen de referencia RCP). Este caso exige poner a prueba jerarquías profundas (15 componentes anidados dentro de un solo contenedor), la repetición deliberada de zonas (dos columnas de `Aplicaciones` separadas por `Integración`) y un enrutamiento uno-a-muchos desde las APIs centrales.

## Prompt de Ejecución
Copia y pega este texto en el chat para disparar la prueba de clonación arquitectónica:

> "Antes de generar, abre y lee completo `C:\Dev\Agentes\Proto\Skills\drawio-diagrams\SKILL.md` y las referencias que indique para el perfil `colcomercio`; no asumas que recuerdas su contenido de una ejecución anterior. Usa esa skill para generar un diagrama de arquitectura que replique el flujo transaccional del sistema RCP con alta fidelidad.
>
> Revisa los nombres existentes en `output/`. Considera `rcp_arquitectura.drawio` como v1 y guarda esta ejecución en un archivo nuevo `rcp_arquitectura vN.drawio`, donde N es la siguiente versión después de la más alta existente (v2, v3, etc.). No sobrescribas versiones anteriores.
> 
> Aplica la siguiente estructura visual estricta de izquierda a derecha:
> 
> **1. Zona 'Actores':**
> * Incluye dos elementos tipo Persona: `Usuario Interno` y `Usuario Externo`.
> 
> **2. Zona 'Accesos':**
> * Incluye un elemento tipo Ventanilla o Browser llamado `Browser`.
> 
> **3. Zona 'Aplicaciones' (Primera aparición):**
> * Crea un Frame llamado `Privado Nube`.
> * Adentro del Frame, crea un Contenedor llamado `RCP`.
> * Adentro del Contenedor RCP, apila los siguientes 15 componentes simples: `Recepción y sincronización de SKUs desde PeopleSoft`, `Consulta y selección de SKU por facility`, `Gestión de atributos logísticos del producto`, `Parametrización de producto por depósito / facility`, `Configuración de unidades de medida y dimensiones`, `Gestión de catálogos y listas desplegables`, `Gestión de SKU Module`, `Gestión de producto irregular y producto anidado`, `Gestión de tracking de fechas y seriales`, `Gestión de SIOC, multiproducto e imagen del SKU`, `Replicación de configuración entre facilities`, `Envío de configuración hacia Manhattan, PeopleSoft, PTL y Module`, `Administración de usuarios, roles y permisos`, `Auditoría, logs y trazabilidad`, `Reportes operativos de parametrización`.
> 
> **4. Zona 'Integración':**
> * Crea un Frame llamado `AWS Nube`.
> * Adentro del Frame, crea un Contenedor llamado `MuleSoft`.
> * Adentro del Contenedor MuleSoft, incluye 3 elementos tipo API (círculos): `publicarProductoUnidadNegocio V1`, `Consultar Imagen Producto` e `Información Producto`.
> 
> **5. Zona 'Aplicaciones' (Segunda aparición por secuencia de flujo):**
> * Crea un Frame `GCP Nube` que contenga un componente `Manhattan Active Warehouse Management`.
> * Crea un Frame `Oracle Nube` que contenga un componente `PeopleSoft`.
> * Crea un Frame `Privado Nube` que contenga tres componentes: `TMS Unigis`, `Sirv`, `SAP Commerce Cloud`.
> * Crea un Frame `AWS Nube` que contenga cuatro componentes: `Shopify`, `Vtex Marketplace`, `CorbeApp`, `CorbeMóvil`.
> 
> **Relaciones (Conectividad síncrona de izquierda a derecha):**
> * Conecta `Usuario Interno` y `Usuario Externo` hacia `Browser`.
> * Conecta `Browser` hacia el contenedor `RCP`.
> * Conecta desde el contenedor `RCP` hacia las 3 APIs dentro de `MuleSoft`.
> * Desde la API `publicarProductoUnidadNegocio V1` bifurca flechas hacia `Manhattan...` y `PeopleSoft`.
> * Desde la API `Consultar Imagen Producto` saca una flecha hacia `Sirv`.
> * Desde la API `Información Producto` saca flechas hacia el resto de los componentes de la zona derecha (`TMS Unigis`, `SAP Commerce Cloud`, `Shopify`, `Vtex Marketplace`, `CorbeApp`, `CorbeMóvil`)."

## Salida Esperada
- Un archivo nuevo `output/rcp_arquitectura vN.drawio`, sin sobrescribir los anteriores.
- Un lienzo estructurado en 5 grandes columnas.
- Respeto absoluto por los colores y formas dictados en el catálogo de `colcomercio`.

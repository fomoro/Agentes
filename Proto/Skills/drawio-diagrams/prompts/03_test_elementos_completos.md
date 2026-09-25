# Caso de Prueba 03: Auditoría Completa de Elementos y Conectividad

## Objetivo
Validar que el motor es capaz de leer y parsear absolutamente todas las reglas del diccionario visual de Colcomercio actualizado. Esto incluye la renderización de zonas, frames, componentes simples y contenedores, todos los elementos compartidos, de solución e integración (aplicando sus formas Draw.io específicas como `shape=isoCube2`, `shape=umlActor`, etc.), y la correcta diferenciación de conexiones síncronas y asíncronas.

## Prompt de Ejecución
Copia y pega este texto en el chat para disparar la prueba maestra:

> "Usa el skill de Draw.io para generar un diagrama de arquitectura aplicando el estilo 'colcomercio'. El objetivo es renderizar un mapa de estrés visual que agrupe todos los elementos de tu diccionario.
> 
> Construye la siguiente estructura exacta:
> 
> 1. En la Zona 'Actores', coloca los elementos: 'Persona', 'Portátil' y 'Celular'.
> 2. En la Zona 'Accesos', coloca: 'WhatsApp' (aplica verde con degradado estricto), 'Ventanilla', 'Teléfono' y 'Carrito de compras'.
> 3. En la Zona 'Aplicaciones', crea el Frame 'Microsoft 365' (ponle adentro un 'SharePoint' y una 'Carpeta'). Crea también el Frame 'Salesforce Nube' y ponle adentro un 'Componente Contenedor' llamado CRM, que agrupe una 'Nota'.
> 4. En la Zona 'Integración', despliega el muestrario técnico: 'Orquestación', 'API' (con etiqueta dentro), 'Servicio', un 'Paso' (con número adentro), 'Caché' (etiqueta adentro), 'Colas', 'Enrutamiento', 'Regla Decisión', 'Schedule' genérico, 'Validación Datos', 'Webhook', 'Reintentos', 'Paginación' (etiqueta adentro), 'Data Transformada', 'Request/Response JSON' y 'Autenticación OAuth 2.0' genérica. También incluye un 'Syncout' de integración (`shape=umlBoundary`).
> 5. En la Zona 'Ecosistema de datos', pon un 'Componente Simple' llamado 'Core' y un 'Pivote'.
> 
> Conectividad a probar:
> - Tira 3 líneas de conexión SÍNCRONAS (línea continua con flecha) cruzando desde Actores hacia Accesos.
> - Tira 3 líneas de conexión ASÍNCRONAS (línea discontinua con flecha) desde Integración hacia Ecosistema de datos.
> 
> Condición de éxito: Usa exactamente la base visual global (Helvetica Neue, sombras) y las formas XML de cada elemento listado en tu catálogo."

## Salida Esperada
- Un archivo `.drawio` en la carpeta `output/`.
- Un lienzo inmenso con todas las zonas y frames.
- Los íconos deben corresponder exactamente a la columna "Forma" del catálogo (ej. el carrito debe ser `shape=mxgraph.ios7.icons.shopping_cart`, el webhook `shape=collate; direction=north`).
- Diferenciación clara entre flechas continuas y punteadas.
- No usar iconos de Azure o AWS para Schedule u OAuth genéricos sin fuente que identifique esos servicios.

# Guía de construcción — Colcomercio (V3)

- Actualizado: el 2026-09-25 17:02
- Rol de ejecución: arquitectura de soluciones y diseño de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: propuesta para revisión

## Objetivo

Definir qué representar y cómo comprobar un diagrama de solución o integración de Colcomercio. El [catálogo de estilos](catalogo-estilos.md) define la apariencia; [SKILL.md](../../SKILL.md) define las herramientas, la generación y la entrega.

## Representación

- Ajustar el detalle a la pregunta del diagrama. Usar zonas para responsabilidades o fronteras, frames para entornos confirmados y componentes contenedores cuando su detalle interno aporte. Omitir niveles innecesarios.
- Mostrar elementos y relaciones respaldados por las fuentes. Distinguir propuestas de hechos confirmados y marcar como «Pendiente» los datos sin resolver. No completar ubicaciones ni conexiones por apariencia o conveniencia visual.
- Consultar el [inventario de aplicaciones](inventario-aplicaciones.md) cuando se necesite ubicar sistemas; corroborar sus ubicaciones candidatas antes de representarlas como confirmadas.
- Mostrar interfaces internas cuando sean pertinentes al alcance y conectar cada relación con su extremo correspondiente. Conservar origen, destino y sentido funcional; numerar pasos solo cuando exista una secuencia.
- Aplicar la distinción visual entre conexiones síncronas y asíncronas del catálogo únicamente cuando ese comportamiento esté respaldado.

## Nombres de API

- Con sistema identificado: `SistemaPascalCase.operacion-en-kebab-case`.
- Sin sistema identificado: `operacion-en-kebab-case`; no inventar el prefijo.
- Conservar la grafía de la versión tras un espacio: `publicar-producto-unidad-negocio V1`. Mostrar el nombre completo, sin puntos suspensivos.

## Disposición y legibilidad

Usar el autolayout cuando la estructura lo permita. El motor calcula posiciones y recorridos a partir de dimensiones y parámetros suministrados; no asumir que mide etiquetas externas, ajusta texto o aplica los márgenes del perfil automáticamente. Comprobar esas condiciones también cuando el catálogo atribuya el dimensionamiento al motor.

- Reservar al menos 30 px entre la zona y sus frames. En frames y componentes contenedores, dejar 50 px laterales desde el conjunto visible de figura y etiqueta, 30 px bajo el último hijo y espacio superior para el título.
- Ajustar el ancho de las etiquetas antes de ampliar contenedores. Contar cada margen una sola vez; mantener nombres legibles y proporciones de los íconos.
- Situar las API expuestas sobre la frontera del sistema. Cuando corresponda un símbolo de interfaz, aplicar su orientación según el catálogo; el margen interior no desplaza los puertos montados sobre el borde.
- Separar anclajes y recorridos de conexiones diferentes. Evitar líneas sobre etiquetas o elementos ajenos; distinguir los cruces inevitables de las uniones reales. No añadir nodos de arquitectura para acomodar flechas.

## Conectividad física

Las relaciones con actores o dispositivos de acceso muestran la interacción funcional. Entre aplicaciones o plataformas, incorporar tramos físicos solo cuando estén confirmados ambos entornos y la ruta efectiva. Esta tabla conserva referencias del perfil; no acredita por sí sola la red utilizada.

| Extremos | Tramos de referencia |
| :--- | :--- |
| OnPremise ↔ Microsoft Azure Nube | FloNetworks DCI |
| OnPremise ↔ AWS Nube | FloNetworks DCI |
| Microsoft Azure Nube ↔ Microsoft Azure Nube, misma suscripción de Colcomercio y región | Conexión Interna |
| Nubes distintas o una misma nube en regiones diferentes | Internet |
| Oracle Nube ↔ Microsoft Azure Nube | Oracle FastConnect → Pivote → FloNetworks DCI |
| Oracle Nube ↔ AWS Nube | Oracle FastConnect → Pivote → FloNetworks DCI |
| Oracle Nube ↔ OnPremise | Oracle FastConnect |

- Preferir la correspondencia que identifique ambas plataformas frente a una genérica. Si la ruta real difiere o hay ambigüedad, representar únicamente lo confirmado y marcar lo restante como pendiente.
- Al invertir el recorrido, invertir los tramos físicos y conservar el sentido funcional de la relación.
- Usar Pivote únicamente cuando represente una demarcación física confirmada de la ruta; no como recurso de distribución visual.

## Comprobación del resultado

- El flujo responde al objetivo y conserva las relaciones, direcciones y estados de las fuentes.
- Las ubicaciones y rutas físicas tienen respaldo; los pendientes se distinguen de lo confirmado.
- Los estilos corresponden al catálogo; títulos, etiquetas y puertos permanecen legibles, sin desbordamientos ni solapamientos.
- Los márgenes y recorridos cumplen esta guía en el resultado generado. La validación del XML y el uso de autolayout no acreditan por sí solos fidelidad visual o semántica.

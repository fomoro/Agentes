# Casos y Problemas Abiertos (Edge Cases)

Este documento registra problemas visuales y de construcción detectados, su decisión y lo pendiente de comprobar.

## Caso 01: Salto de línea no deseado en títulos de Frames (`umlFrame`)

- **Problema / Síntoma:** El texto del título en los contenedores tipo Frame (ej. "Oracle Nube", "Privado Nube") se parte en múltiples renglones (salto de línea) en lugar de renderizarse a lo largo en una sola línea horizontal.
- **Causa:** La pestaña de `umlFrame` usa 60 px por defecto; con `whiteSpace=wrap`, un título más ancho puede partirse. Su ancho se controla con la propiedad de estilo `width`.
- **Solución incorporada:** Ajustar `width` de la pestaña al título más un margen, sin quitar `whiteSpace=wrap` ni confundirla con el ancho total del frame. Véase el [catálogo](../theme/colcomercio/catalogo-estilos.md).
- **Estado:** Criterio documentado; pendiente de comprobar en un render.

## Caso 02: Degradación visual por ausencia de íconos base (Ej. Browser)

- **Problema / Síntoma:** Al solicitar un elemento arquitectónico estándar como un "Browser" (presente en la imagen de referencia RCP), el agente renderiza un rectángulo genérico en lugar del ícono representativo de interfaz web.
- **Causa:** El catálogo no tenía una forma para Browser y el diagrama RCP lo sustituyó por un componente simple.
- **Solución incorporada:** Añadir Browser con `shape=image;image=img/lib/azure2/general/Browser.svg;aspect=fixed` al [catálogo](../theme/colcomercio/catalogo-estilos.md). La ruta identifica un ícono de biblioteca, no un despliegue en Azure.
- **Estado:** Mapeo documentado; pendiente de comprobar que el renderizador lo muestre. Añadir otras formas solo cuando surja una necesidad concreta.

## Caso 03: Carencia de margen/padding dinámico en Frames y Contenedores

- **Problema / Síntoma:** El último elemento anidado dentro de un contenedor (ej. "SAP Commerce Cloud" dentro del frame "Privado Nube") queda visualmente aplastado contra el borde inferior de su contenedor padre, sin aire o margen interno.
- **Causa:** En el frame «Privado Nube» del diagrama RCP, el último hijo termina en `y=160 + 40 = 200`, justo donde acaba el padre de 200 px; los laterales también dejan solo 20 px.
- **Solución incorporada:** En frames y componentes contenedores, dejar 50 px a cada lado y 30 px abajo; reservar arriba el espacio del título y separar los contenedores para etiquetas y conexiones. Véase la [guía](../theme/colcomercio/guia-construccion.md).
- **Estado:** Criterio documentado; pendiente de aplicarlo y revisar el diagrama renderizado.

## Caso 04: Carencia de convención de nomenclatura estricta para APIs

- **Problema / Síntoma:** Los elementos de integración tipo API (como los dibujados dentro de MuleSoft) aparecen con nombres informales, con espacios o truncados con puntos suspensivos (ej. "Consultar Imagen...").
- **Causa:** No había una convención de nombres ni una salida visual para etiquetas que no caben en el círculo.
- **Solución incorporada:** La [guía](../theme/colcomercio/guia-construccion.md) define `SistemaPascalCase.operacion-en-kebab-case` cuando se conoce el sistema y `operacion-en-kebab-case` cuando no; una versión como `V1` va tras un espacio. El [catálogo](../theme/colcomercio/catalogo-estilos.md) permite ubicar el nombre completo fuera del círculo si no cabe.
- **Estado:** Criterio documentado; pendiente de comprobar en un diagrama renderizado.

## Caso 05: Enrutamiento inestético de flechas (Efecto Telaraña uno-a-muchos)

- **Problema / Síntoma:** Las flechas de conexión, especialmente cuando un solo origen apunta a múltiples destinos (ej. la API de información apuntando a Shopify, Vtex, CorbeApp y CorbeMóvil simultáneamente), se cruzan o salen de bordes aleatorios, perdiendo el orden jerárquico de "árbol" o "bifurcación" limpia que muestra la imagen de referencia.
- **Causa:** El ejemplo RCP usa enrutamiento ortogonal sin anclajes ni puntos de paso para las seis salidas de una API. Un único punto fijo para todas tampoco evitaría las superposiciones.
- **Solución incorporada:** La [guía](../theme/colcomercio/guia-construccion.md) indica ordenar los destinos, orientar y distribuir los anclajes, y ajustar las rutas con quiebres; un punto de unión solo procede si no induce a interpretar una conexión compartida no confirmada.
- **Estado:** Criterio documentado; pendiente de comprobarlo en un diagrama renderizado.

## Caso 06: Omisión de anclaje de puertos de interfaz sobre el borde exacto

- **Problema / Síntoma:** Un puerto solicitado sobre el borde de una caja puede quedar solo cerca de ella, sin acompañarla al moverla. El prompt RCP usado en la prueba no pidió un puerto; su ausencia allí no demuestra un fallo del agente.
- **Causa:** Falta un criterio condicional de posición relativa y de selección del símbolo; `providedRequiredInterface` es una interfaz de ensamblaje UML, no cualquier puerto circular.
- **Solución incorporada:** La [guía](../theme/colcomercio/guia-construccion.md) establece que, si se solicita, el puerto sea hijo de la caja y se centre sobre el borde izquierdo con `x=-w/2`, a la altura de la conexión. El [catálogo](../theme/colcomercio/catalogo-estilos.md) precisa el significado de la forma UML.
- **Estado:** Criterio documentado; pendiente de probarlo con una entrada que sí solicite un puerto y revisar el resultado visual.

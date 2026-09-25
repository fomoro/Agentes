# Guía de construcción — Colcomercio

- Actualizado: el 2026-09-25 02:09
- Rol de ejecución: diseño de procesos de diagramación y arquitectura de skills
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo

Construir un diagrama de solución o integración que responda una pregunta concreta y represente solo información confirmada. Esta guía decide qué mostrar y cómo relacionarlo; el [catálogo de estilos](catalogo-estilos.md) define su apariencia y el [inventario de aplicaciones](inventario-aplicaciones.md) aporta ubicaciones candidatas con su estado. Ninguna posición visual demuestra una conexión de red.

## Construcción

1. **Delimitar.** Identificar objetivo, alcance, nivel (solución, integración o ambos), fuentes y datos pendientes. Aceptar una descripción libre o una ficha existente; no exigir ni crear una ficha aparte para poder diagramar. Si falta información indispensable para una parte, dejarla pendiente y avanzar solo en las partes independientes.
2. **Seleccionar la estructura.** Incluir únicamente elementos y relaciones necesarios. Usar zonas cuando muestren una responsabilidad o frontera; frames cuando proveedor, entorno o red sean relevantes; y componentes contenedores para sistemas cuyo detalle interno aporte al objetivo. La jerarquía `zona → frame → componente → elemento` admite niveles omitidos: no forzar capas ni alojamientos no confirmados. Consultar el inventario y corroborar su ubicación candidata antes de situar una aplicación en un frame; si no se confirma, dejarla sin ubicación.
3. **Representar los elementos.** Si las fuentes detallan interfaces o capacidades internas pertinentes, mostrarlas dentro del sistema y conectar individualmente las relaciones confirmadas; en otro caso, conservar el sistema como caja única. Cada ícono debe corresponder a una responsabilidad o hecho confirmado. Aplicar el catálogo visual y ajustar el tamaño al contenido. Usar pasos numerados solo si existe una secuencia.
4. **Trazar relaciones y pendientes.** Conservar origen, destino y sentido funcional. Diferenciar conexiones síncronas y asíncronas solo cuando su tipo esté confirmado. No dibujar componentes ni conexiones no confirmados como si existieran. Si una brecha debe verse en el diagrama, marcarla con una Nota «Pendiente» unida mediante una línea punteada al elemento o relación confirmada que afecta; no inventar el extremo ausente. Mostrar etiquetas funcionales solo si aportan información confirmada.
5. **Ordenar y generar.** Elegir la orientación que haga legible la historia; de izquierda a derecha suele servir, pero no fija el orden de las zonas. Repetir una zona únicamente si el flujo vuelve a ella y mejora la secuencia. Dejar al menos 30 px entre cada zona y su frame. En frames y componentes contenedores, medir el contenido visible de cada hijo —figura y etiqueta externa como un conjunto— y dejar 50 px entre ese conjunto y cada borde lateral, sin sumar otros 50 px alrededor de la figura. Ajustar el ancho de las etiquetas externas al texto y al espacio disponible antes de ampliar el contenedor. Dejar 30 px bajo el último hijo y reservar arriba el espacio del título. Dimensionar y recolocar el contenedor y sus vecinos para conservar esos márgenes sin solapamientos. Situar las API expuestas sobre la frontera del sistema y orientar su etiqueta hacia el interior o un lateral libre cuando las flechas puedan taparla. Dejar espacio adicional entre contenedores para etiquetas y conexiones. Para varias arquitecturas o alternativas solicitadas, usar una página por arquitectura dentro del mismo `.drawio`.

## Nombres de API

- Con sistema identificado: `SistemaPascalCase.operacion-en-kebab-case`. Antes del punto va PascalCase; después, kebab-case.
- Sin sistema identificado: `operacion-en-kebab-case`. Por ejemplo, `publicarProductoUnidadNegocio V1` se representa como `publicar-producto-unidad-negocio V1`.
- Si hay versión, conservar su grafía tras un espacio. No inventar el sistema ni truncar el nombre con puntos suspensivos.

## Rutas y puertos

- En relaciones uno-a-muchos y entre API distintas, ordenar los destinos, conectar por lados enfrentados y distribuir anclajes y corredores para separar las rutas. No superponer tramos ni fijar todas las flechas al mismo punto. Usar un punto de unión solo si no sugiere una conexión compartida no confirmada; si un cruce es inevitable, distinguirlo con un salto de línea. Comprobar visualmente cada ruta completa, de origen a destino.
- Si la fuente solicita una interfaz sobre el borde, escoger el símbolo y su orientación según el catálogo. Para centrar un puerto de ancho `w` y alto `h` en el borde izquierdo, hacerlo hijo directo de la caja y situarlo en `x=-w/2`, `y=y_conexión-h/2`, con `y_conexión` medido desde la parte superior de la caja. Conectar la flecha al puerto y revisar que se vea, apunte hacia la conexión y acompañe a la caja al moverla. El margen interior de 50 px no aplica al puerto montado sobre el borde.

## Conectividad física

Las relaciones con actores o dispositivos de acceso muestran solo la interacción funcional. Para una relación entre aplicaciones o plataformas, añadir tramos físicos únicamente si están confirmados los entornos de ambos extremos y la ruta efectiva. Las correspondencias heredadas siguientes sirven como referencia del perfil, no como prueba de que la red actual las use:

| Extremos | Tramos de referencia |
| :--- | :--- |
| OnPremise ↔ Microsoft Azure Nube | FloNetworks DCI |
| OnPremise ↔ AWS Nube | FloNetworks DCI |
| Microsoft Azure Nube ↔ Microsoft Azure Nube, misma suscripción de Colcomercio y región | Conexión Interna |
| Nubes distintas o una misma nube en regiones diferentes | Internet |
| Oracle Nube ↔ Microsoft Azure Nube | Oracle FastConnect → Pivote → FloNetworks DCI |
| Oracle Nube ↔ AWS Nube | Oracle FastConnect → Pivote → FloNetworks DCI |
| Oracle Nube ↔ OnPremise | Oracle FastConnect |

Preferir la fila que nombre ambas plataformas frente a una genérica. Al representar la ruta en sentido inverso, invertir los tramos, pero conservar el sentido funcional de la flecha. Usar Pivote solo en las filas que lo incluyen. Si faltan datos, la ruta real difiere, no coincide ninguna fila o hay dos correspondencias igualmente específicas, no inventar tramos: dejar la conectividad física pendiente.

«Pivote» representa una demarcación física confirmada, no un recurso para ordenar flechas; para esto último, usar puntos de conexión o quiebres sin añadir nodos semánticos.

## Revisión del resultado

- El objetivo y el flujo principal se entienden sin elementos decorativos.
- Cada elemento, relación, ubicación y tramo representado tiene respaldo en el encargo o en una fuente vigente.
- No hay etiquetas ilegibles, solapamientos ni líneas que atraviesen elementos; el archivo `.drawio` sigue editable.
- Los pendientes no aparecen como decisiones confirmadas. La ruta de entrega se resuelve según `SKILL.md` y la gobernanza del proyecto destino.

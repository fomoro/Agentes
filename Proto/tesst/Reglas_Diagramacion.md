# Guía y Reglas para la Generación de Diagramas

Este documento recopila las lecciones aprendidas y las reglas (o "prompts" de contexto) que se deben proporcionar al Agente de IA para asegurar que los diagramas de arquitectura (DrawIO/Mermaid) se generen con el nivel de detalle y precisión esperados desde el primer intento.

## 1. Nivel de Granularidad ("Cajas de Cristal" vs "Cajas Negras")
* **Regla:** Si los documentos de origen (ej. tablas Markdown) detallan interfaces, capacidades o servicios individuales, el agente **debe dibujar explícitamente** estos elementos internos dentro del contenedor de su sistema correspondiente.
* **Indicación para el prompt:** *"Representa los sistemas como contenedores y dibuja en su interior cada una de las capacidades e interfaces descritas en las tablas, conectándolas punto a punto de forma individual."*

## 2. Exclusiones y Elementos No Confirmados
* **Regla:** El diagrama de arquitectura solo debe incluir las conexiones y componentes confirmados para la fase actual.
* **Indicación para el prompt:** *"Omite expresamente cualquier sistema, interfaz, protocolo o decisión que esté marcada como 'pendiente' o 'no confirmada' en el documento fuente, a menos que se indique dibujarlo con estilo punteado."*

## 3. Brechas Técnicas e Incertidumbres (Notas)
* **Regla:** Cuando existan definiciones pendientes, estas deben visibilizarse en el diagrama para que el equipo las resuelva.
* **Indicación para el prompt:** *"Utiliza elementos visuales de tipo 'Nota' (Note) conectadas con líneas punteadas exclusivamente a la interfaz o flecha afectada, describiendo claramente la brecha técnica por resolver."*

## 4. Disposición Visual (Layout)
* **Regla:** El diagrama debe seguir un flujo lógico, típicamente de izquierda a derecha (Cliente → Frontend/Portal → Bus de Integración → Backend/Core).
* **Indicación para el prompt:** *"Ordena los contenedores de izquierda a derecha simulando el flujo de interacción del usuario hacia el backend. Usa líneas ortogonales (Orthogonal Edges) para mantener la limpieza visual y evitar cruces de líneas innecesarios."*

## 5. Jerarquía de Contenedores y Entornos (Nubes)
* **Regla:** Los sistemas principales (Wompi, MuleSoft, PeopleSoft) siempre son contenedores estándar (ej. rectángulos redondeados `shape=rectangle;rounded=1;`, no Zonas/Swimlanes) con fondo blanco (`fillColor=#ffffff`) y borde negro (`strokeColor=#000000`), que agrupan sus interfaces internas. A su vez, estos sistemas deben estar encapsulados dentro de un contenedor macro (ej. un Frame llamado "Nube") que represente su infraestructura de alojamiento y debe usar los colores y degradados corporativos. Las APIs (puntos de conexión) expuestas en los bordes de estos sistemas también deben ser blancas con borde negro.
* **Indicación para el prompt:** *"Crea un Frame exterior (Nube) para cada entorno usando los colores corporativos. Dentro de esa nube, ubica el componente del sistema como un Contenedor estándar (rectángulo redondeado, NO un Swimlane) con fondo blanco y borde negro, y dentro de este último, dibuja sus capacidades. Todas las APIs de borde deben ser de fondo blanco y borde negro."*

## 6. Agrupaciones Internas y Estilo Consistente
* **Regla:** Las capacidades internas/locales deben situarse alejadas de los bordes y agruparse en sub-contenedores. Los estilos visuales de estas capacidades (no-API) dependen del sistema y no deben forzarse a un estilo único genérico; por ejemplo, las capacidades de PeopleSoft pueden no tener fondo (`fillColor=none`) ni bordes (`0pt`), mientras que otros sistemas (como Wompi) usan fondo blanco con borde sólido. Los contenedores padre deben tener espacio horizontal suficiente para que el texto de las capacidades no sobresalga.
* **Indicación para el prompt:** *"Envuelve las capacidades internas en un sub-contenedor situado en el lado opuesto a la integración. Dibuja las capacidades internas aplicando estilos nativos o acordes a su sistema (ej. sin borde ni fondo para PeopleSoft, o con borde y fondo para otros). Ajusta el ancho del contenedor padre para garantizar que los textos largos quepan sin salirse de la caja."*

## 7. Estructura de Capas tipo Matrioshka y Zonas (Swimlanes)
* **Regla:** El diagrama debe usar capas semánticas macro de afuera hacia adentro: Externos, Accesos, Aplicaciones e Integraciones. Se pueden intercalar contenedores lógicos como "Accesos" (ej. un Browser) para desacoplar el cliente directo.
* **Indicación para el prompt:** *"Usa Swimlanes exteriores para agrupar dominios (ej. 'Externos', 'Accesos', 'Aplicaciones'). Asígnales a las cabeceras un color pastel distintivo para diferenciar cada dominio tecnológico. El diagrama debe respetar estrictamente esta jerarquía Matrioshka."*

## 8. Puertos Expuestos (APIs)
* **Regla:** Las capacidades que actúan explícitamente como interfaces o APIs expuestas deben representarse con figuras circulares (`ellipse`) ancladas exactamente sobre los bordes (fronteras) del contenedor de la aplicación.
* **Indicación para el prompt:** *"Dibuja las APIs como círculos directamente sobre la línea del borde del contenedor. Su texto descriptivo debe alinearse hacia el interior del contenedor o a un lado, de forma contraria a donde provienen/salen las flechas de tráfico (nunca abajo, para evitar superposiciones con flechas)."*

## 9. Pivotes de Enrutamiento (Rhombus)
* **Regla:** Para mantener diagramas altamente legibles en buses de integración centrales (ej. MuleSoft), cada flujo de interfaz debe contar con un nodo pivote.
* **Indicación para el prompt:** *"Inserta un nodo pivote oculto o pequeño (`rhombus`) en el trayecto de cada flecha ida-y-vuelta entre los sistemas y el bus de integración, lo que permite enrutar las flechas individuales de manera controlada y simétrica sin solapamientos."*

---
**Nota para el usuario:** Al solicitar un nuevo diagrama al agente, puedes hacer referencia a este archivo diciendo: *"Por favor, genera el diagrama basándote en las reglas definidas en `Reglas_Diagramacion.md`"* para garantizar que aplique todo este contexto automáticamente.

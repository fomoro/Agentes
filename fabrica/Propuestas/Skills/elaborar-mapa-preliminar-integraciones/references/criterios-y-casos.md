# Criterios de revisión y casos de contraste

- Actualizado: el 2026-09-17 08:44
- Rol de ejecución: diseñador de skills, arquitecto de integraciones y analista de procesos de negocio
- Autor: Sam (Asistente IA del Sr. Wolfan)

## Comprobación antes de entregar el mapa

| Criterio | Comprobación observable |
| --- | --- |
| Propósito | El objetivo explica qué decisión facilita el documento y el alcance delimita su fase. |
| Evidencia | Cada afirmación material se apoya en una fuente o queda identificada como propuesta o pendiente. |
| Cobertura | Cada capacidad en alcance está ubicada o tiene una exclusión explicada; las variantes no parecen duplicaciones accidentales. |
| Necesidad del servicio | Cada servicio responde a un intercambio necesario y no solo a una acción de pantalla. |
| Responsabilidad única | El propósito de cada servicio puede explicarse sin reunir funciones ajenas; los solapamientos se resuelven o se señalan. |
| Lenguaje | Los nombres expresan acción, objeto y contexto. Los términos propios del dominio se sustentan en sus fuentes; no se confunden identidad, estado, permiso y resultado de una operación. |
| Trazabilidad | El mismo servicio mantiene ID y nombre en todos los cuadros; las capacidades conservan sus IDs. |
| Dirección | Se identifica quién inicia, quién recibe y qué ocurre en cada tramo; el texto del extremo concuerda con la flecha. |
| Continuidad | Los escenarios tienen un recorrido comprensible; una notificación recibida no se presenta como procesamiento de negocio completado. |
| Agnosticidad | Los roles, escenarios, reglas y sistemas se obtienen del proyecto; el método no impone un dominio, un proveedor, un intermediario ni una API para cada intercambio. |
| Pendientes | No existen afirmaciones categóricas que contradigan preguntas abiertas. Cada pregunta tiene categoría e interlocutor. |
| Ligereza | Las descripciones aclaran límites o resultados; no repiten el nombre ni añaden notas que duplican tablas. |
| Integridad | Las fuentes enlazadas existen desde la ubicación final y no se modificó contenido ajeno a la autorización. |

## Casos de contraste independientes del dominio

Usa estos casos para razonar. «Sistema A», «Sistema B» e «intermediario» son roles ilustrativos; no obligan a una topología ni a tecnologías específicas.

| Situación | Respuesta esperada |
| --- | --- |
| Una interfaz de usuario filtra una lista ya recibida | Mantenerlo como capacidad local, salvo evidencia de otra consulta necesaria. |
| Un proceso tiene variantes de la misma operación | Evaluar si comparten responsabilidad e información; no crear una interfaz por variante ni fusionarlas sin comprobar sus diferencias. |
| El sistema A consulta una entidad existente en B | Distinguir consultar, crear y actualizar; no inferir modificaciones a partir de una consulta. |
| Se conoce un atributo o una relación de una entidad | No deducir su estado o permiso de operación sin la regla de negocio correspondiente. |
| El sistema A envía un resultado a B | Nombrar las responsabilidades desde cada extremo y separar recepción, aceptación y procesamiento completado. |
| Un dato cambia en el sistema origen | Evaluar quién necesita ese cambio y cuándo; no asumir una consulta síncrona ni publicación de eventos sin evidencia. |
| A solicita información a B mediante un intermediario | Mostrar A → intermediario → B si esa intermediación está acordada. El regreso de la respuesta no cambia quién inició. |
| A envía directamente información a B | Representar la conexión sin añadir un intermediario inexistente. |
| Un intercambio se realiza por archivo | Identificar contenido, emisor, receptor y condición de envío; no convertirlo automáticamente en una API. |
| Una fila dice «operación fallida» | Precisar si falla la operación de negocio, la entrega o el procesamiento interno; formular un pendiente si no hay evidencia. |
| Se discute la información de una respuesta | Separar significado y necesidad funcional de esquema y formato contractual cuando hagan falta ambas decisiones. |
| El catálogo de integraciones contiene un nombre parecido | Marcar una candidata, sin afirmar reutilización ni fuente real de datos hasta comprobar su alcance. |

## Casos para evaluar la skill en uso

Los resultados siguientes son criterios de prueba, no pruebas ejecutadas. Cuando se evalúe el paquete, conservar el estímulo, el artefacto observado y las limitaciones en el registro acordado del entorno.

| Solicitud de prueba | Resultado que se debe observar |
| --- | --- |
| Crear un mapa con capacidades y contratos suficientes | Primera versión completa, sin consultar cada frase; coherencia comprobada y decisiones abiertas visibles. |
| Crear un mapa con contratos ausentes | Responsabilidades propuestas y solicitudes concretas de evidencia; ningún campo inventado ni cobertura confirmada. |
| Elaborar un mapa sin catálogo formal, con necesidades documentadas | Lista provisional trazable, sin exigir IDs heredados ni presentar capacidades inferidas como aprobadas. |
| Modelar dos sistemas internos conectados directamente | Matriz directa sin proveedor externo ni intermediario obligatorio. |
| Modelar un evento automático o un intercambio por archivo | Iniciador, condición y resultado representados sin forzar una API ni una acción humana. |
| Comparar documentos con nombres o afirmaciones discrepantes | Discrepancia señalada, fuente vigente identificada y preservación del ID; no corrección silenciosa de archivos fuera de alcance. |
| Discutir una fila sin autorizar cambios | Análisis y propuesta concreta, sin escritura. |
| Aplicar una fila aprobada mientras el usuario editó el archivo | Lectura del estado actual, incorporación de la edición reciente y cambio acotado. |
| Proponer otra API para una capacidad visual | Evaluación del intercambio necesario y del posible solapamiento antes de aceptar o rechazar la API. |
| Usar el paquete en otro proyecto | Plantillas y método utilizables sin rutas del caso, instalación adicional ni nombres fijos de proveedores. |

No confundas revisión de formato con calidad de decisiones ni aprobación del usuario con prueba de implementación.

# Revisión de csharp-onion-architecture v3

- Actualizado: el 2026-10-04 08:17
- Rol de ejecución: diseño y revisión de skills de arquitectura .NET
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: borrador v3 revisado documentalmente; validación operativa pendiente

## Resultado

Se creó [v3/SKILL.md](../Proto/Skills/csharp-onion-architecture/v3/SKILL.md) y su [referencia técnica](../Proto/Skills/csharp-onion-architecture/v3/references/decisiones-csharp.md) por solicitud del usuario. La versión es autónoma y conserva el identificador de la capacidad. La evaluación inicial de los insumos se mantiene en la [revisión de origen](revision_csharp_onion_architecture.md); los cambios de modalidades, en la [revisión v2](revision_csharp_onion_architecture_v2.md).

La creación sigue el contrato y proceso de Generator ya aplicados a las versiones anteriores. La modificación se limita a la skill: la iniciativa se concreta en oportunidades de arquitectura C# relacionadas con el encargo, sin modificar la gobernanza global.

## Decisión y cambios

- Estado: Confirmada para elaboración de v3 por la solicitud del usuario.
- Decisión: incorporar iniciativa contextual con consulta previa para ampliar el alcance.
- Motivo: reconocer mejoras útiles en distintos contextos sin interpretar una petición general de calidad como autorización para añadir capacidades.
- Riesgo y control: propuestas especulativas o consultas repetitivas. Se exige evidencia, se limita la revisión al trabajo, se conservan autorizaciones vigentes y se admite que no haya oportunidades justificadas.
- Siguiente acción: evaluar comportamiento de esta revisión en un entorno de prueba definido; el consentimiento para crearla no acredita su funcionamiento.

| Contenido | Tratamiento y destino verificado |
| :--- | :--- |
| Contexto de uso | Nueva sección Iniciativa según el contexto en SKILL.md: objetivo, destinatarios, aceptación y restricciones disponibles. No requiere una prueba laboral. |
| Oportunidades | Se relacionan con dificultades concretas de ejecución, verificación, acoplamiento, compatibilidad u operación. Las hipótesis se declaran y no se exige una cantidad de propuestas. |
| Autorización | Distingue trabajo necesario, mejoras internas proporcionadas y ampliaciones. Las últimas esperan decisión, aunque sean reversibles; el trabajo independiente continúa. |
| Calidad general | «Esfuérzate» y «optimiza todo» no confirman por sí mismas capacidades adicionales. Una autorización concreta vigente se conserva. |
| KISS, DRY y YAGNI | Criterios operativos en una sola ubicación: menor complejidad suficiente, reutilización semántica y exclusión de capacidades especulativas. |
| Presentación de propuestas | Plantilla literal breve cuando no hay registro del proyecto; incluye evidencia, beneficio, esfuerzo, mantenimiento, riesgo y decisión solicitada. |
| Memoria y base de datos | Referencia §3: cumplir ambos modos si se requieren; evaluar el modo adicional según su utilidad y el criterio del archivo principal. Se mantienen la selección explícita y los límites de persistencia. |
| IdentityDbContext | Referencia §4: ubicación en Infrastructure cuando se adopta Identity con EF Core; evaluar necesidad de almacenamiento local si la identidad es externa. |
| Excepción de composición | Retirada su repetición en referencia §1; se conserva la regla canónica en Reglas comunes de arquitectura de SKILL.md. El ejemplo de revisión en §5 sigue mostrando cómo distinguirla de un acoplamiento indebido. |
| Referencia a una necesidad comprobada | Ajustada en SKILL.md: justifica evaluar una solución, pero no equivale a autorizar su implementación. |

Se conservaron modalidades, entradas proporcionales, dependencias hacia el dominio, compatibilidad, migración incremental y validación según el límite afectado. V1 y v2 no se modificaron; los cambios previos del usuario en Input quedaron fuera de esta intervención.

## Revisión de escenarios

Esta tabla registra un contraste documental con las reglas escritas, no respuestas observadas de una ejecución independiente de la IA.

| Situación | Criterio comprobado en el texto |
| :--- | :--- |
| Una prueba laboral solo exige SQL y dice «esfuérzate». | Cumplir SQL; memoria requiere una oportunidad justificada y una decisión antes de incorporarla. |
| Ya están autorizados SQL y memoria. | Implementar ambos; no consultar de nuevo la misma decisión. |
| Un sistema operativo presenta fallos de diagnóstico en el flujo solicitado. | Evaluar una mejora vinculada al problema; si añade infraestructura o cambia materialmente la operación fuera de lo autorizado, proponer antes de ejecutar. |
| Aclarar un nombre interno o comprobar un límite del cambio. | Ejecutar si es proporcionado, conserva contratos y comportamiento y respeta el alcance vigente. |
| La implementación solicitada requiere una dependencia ya comprendida en el alcance. | No convertir la regla para mejoras adicionales en un bloqueo para cumplir lo autorizado. |
| No hay beneficio concreto en un segundo proveedor. | No añadirlo ni inventar una propuesta para completar una lista. |
| Falta respuesta a una propuesta opcional. | Continuar lo independiente y entregar el alcance autorizado con la mejora pendiente. |
| Falta una decisión funcional indispensable. | Explicar qué parte está bloqueada y continuar lo independiente. |

## Comprobación y estado

Se comprobaron mediante Python estándar los metadatos simples, delimitadores, firma, ausencia de marcadores incompletos y referencias locales dentro de v3. Los marcadores de la plantilla de propuesta son intencionales. Los SHA-256 de v2 coinciden con su revisión anterior.

El validador estándar de skill-creator requiere PyYAML, ausente en el runtime comprobado anteriormente; se utilizó la comprobación estructural alternativa para este frontmatter simple. No se afirma validación por un parser YAML general.

| Archivo de v3 | SHA-256 |
| :--- | :--- |
| `SKILL.md` | `121bbdee99c75df6c645799dda2fb5327587178f7ba945858615fc3c4288bd2e` |
| `references/decisiones-csharp.md` | `4c9f84c4812487eb9762cfe17f3576bdd889731c07829530d106b4e252948475` |

La creación y revisión documental están completas. Quedan pendientes carga efectiva, ejecución de escenarios por una IA y aplicación a un proyecto C#. No se instaló ni exportó esta versión como capacidad operativa.

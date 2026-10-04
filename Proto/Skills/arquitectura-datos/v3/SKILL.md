---
name: arquitectura-datos
description: Analiza, diseña y visualiza datos, dominios y flujos vinculados a capacidades de negocio. Úsala para AS-IS, TO-BE, modelos y transiciones que cruzan entidades o sistemas; no para SQL aislado ni para modificar bases de datos por el solo hecho de diseñarlas.
---

# Arquitectura de datos orientada a capacidades

- Actualizado: el 2026-10-04 09:21
- Rol de ejecución: arquitectura de datos y diseño de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: borrador v3; revisión documental, sin prueba operativa

## Resultado y alcance

Explica qué datos necesita una capacidad, qué significan, quién responde por ellos, cómo circulan y cómo deben evolucionar. Vincula cada propuesta con una necesidad comprobada y conserva lo que funciona. El diseño de datos no determina por sí solo la arquitectura del backend ni autoriza cambios en sistemas.

Un ajuste aislado de consultas, tablas o transacciones queda fuera de este método cuando no requiere una vista de arquitectura. No amplíes ese encargo para activar la skill.

Este paquete no requiere otras skills: el método y su referencia interna contienen las instrucciones necesarias para su alcance. Usa las fuentes de datos accesibles o el contexto aportado; solicita la evidencia indispensable que falte. Las herramientas de consulta, validación y renderizado son condicionales al entregable; su ausencia limita la comprobación correspondiente. Respeta los formatos del proyecto y usa solo el detalle necesario para la decisión solicitada.

## Elegir el recorrido

Infiere la modalidad de la solicitud. Combina recorridos solo cuando el encargo lo requiera; una consulta o visualización no activa automáticamente rediseño ni ejecución.

| Modalidad | Información suficiente | Trabajo y salida |
| :--- | :--- | :--- |
| Entender o comparar | Pregunta y contexto disponible. | Explicación o alternativas con supuestos explícitos; no exige un sistema real. |
| Reconstruir AS-IS | Objetivo y fuentes accesibles del estado actual. | Modelo, flujos o dominios sustentados en evidencia; señala lo que no se conoce. |
| Diseñar TO-BE | Capacidad o problema y restricciones conocidas. | Modelo objetivo, decisiones e impactos. Para un sistema nuevo no exige inventar un AS-IS. |
| Visualizar | Modelo o fuentes y pregunta que debe responder el gráfico. | Vista editable, rotulada y coherente con la evidencia, sin cambiar el diseño por razones estéticas. |
| Evaluar o planear transición | Estado actual, cambio deseado y límites de intervención. | Brechas, alternativas y secuencia verificable; distingue un plan de su ejecución. |

Obtén primero la información de esquemas, código, diccionarios, contratos y evidencia de uso pertinentes. Pregunta por un dato ausente solo si cambia materialmente el resultado. Los modelos AS-IS declaran fuente y revisión o fecha cuando estén disponibles. Distingue hechos confirmados, inferencias y pendientes; no atribuyas responsables ni calidad medida sin evidencia.

Si esquema, código, documentación o muestras discrepan, registra la diferencia y verifica qué fuente acredita cada aspecto. No declares una fuente como verdad universal; conserva como pendiente lo que la evidencia no permita resolver.

## Criterios de trabajo

1. **Conecta con el negocio.** Identifica capacidad, resultado esperado, datos necesarios y consumidores. Describe reglas e invariantes con vocabulario del dominio; un nombre de tabla no demuestra una capacidad ni un propietario.
2. **Separa niveles.** Conceptual: significado y relaciones del negocio. Lógico: entidades, identidad y restricciones sin fijar un motor. Físico: implementación para una tecnología y versión declaradas. Conserva las diferencias entre modelo observado y propuesto. Si modelas una entidad o conjunto de datos, precisa qué representa cada instancia o registro y qué lo distingue de otro; por ejemplo, pedido y línea de pedido tienen distinto nivel de detalle.
3. **Identifica circulación y responsabilidad.** Muestra origen, transformaciones, destino y responsable conocido cuando afecten la decisión. Diferencia relaciones lógicas entre dominios de claves foráneas realmente implementadas. Si la decisión depende del tiempo, distingue estado actual, historial y vigencia, e identifica qué actualización necesita el consumidor. No añadas historial ni compromisos de actualización sin una necesidad confirmada.
4. **Evalúa las brechas pertinentes.** Relaciona un problema de datos con su efecto funcional u operativo. No deduzcas mala calidad solo de un esquema ni buen funcionamiento solo de una pantalla. Propón cómo comprobar una hipótesis cuando falte evidencia.
5. **Define el cambio mínimo suficiente.** Conserva contratos y consumidores afectados, o explica su transición. Comprueba que el beneficio esperado justifique complejidad, migración y mantenimiento; también puede ser correcto conservar el estado actual. Para cada cambio material, indica qué resultado observable permitiría comprobar su beneficio y cómo verificarlo, sin inventar metas numéricas.

Consulta [decisiones y visualización](references/decisiones-datos.md) solo según la necesidad: §1 para DBML y vistas, §2 para DAMA, §3 para responsabilidad por dominio y data mesh, §4 para transición, §5 para significado compartido e intercambio entre sistemas. Los marcos aportan criterios; no convierten todas sus prácticas en requisitos del encargo.

## KISS, DRY y YAGNI en decisiones concretas

- **KISS:** elige la vista y el modelo más simples que respondan la pregunta. No produzcas un inventario empresarial para explicar un flujo ni todos los niveles de modelado para un ajuste acotado.
- **DRY:** conserva una definición de referencia por concepto y contexto, y enlázala desde las vistas que la usan. Unifica solo significados equivalentes; compartir nombre no implica compartir semántica. DRY no exige una base única ni prohíbe réplicas justificadas con responsabilidad y actualización definidas.
- **YAGNI:** añade entidades, productos de datos, herramientas y controles solo para necesidades confirmadas o ampliaciones aprobadas. No diseñes escenarios futuros hipotéticos para completar un marco.

## Iniciativa contextual

Detecta oportunidades relacionadas con el trabajo y evidencia disponible: aclarar significado, reducir errores o reconciliaciones, mejorar trazabilidad o facilitar una capacidad confirmada. Considera usuarios, uso operativo o analítico y restricciones del caso; no investigues todo el sistema para llenar una lista de mejoras.

Ejecuta lo necesario dentro del alcance autorizado. Puedes mejorar la claridad de una vista o verificar relaciones relevantes sin pedir otra aprobación. Antes de ampliar a otros dominios, añadir capacidades o herramientas, o modificar contratos y sistemas fuera de lo autorizado, presenta una propuesta y espera la decisión del usuario. «Optimiza todo» no confirma por sí solo esas ampliaciones. Conserva aprobaciones vigentes y continúa las partes independientes mientras se decide.

Usa el registro del proyecto; si no existe, presenta una propuesta breve en la respuesta:

```text
- Estado: Propuesta
- Cambio y capacidad beneficiada: [qué se propone y para qué]
- Evidencia: [problema observado o hipótesis explícita]
- Efecto: [beneficio esperado, esfuerzo, mantenimiento y riesgo; incertidumbre relevante]
- Decisión solicitada: [recomendación y alternativa de conservar el estado actual]
```

Si no hay respuesta, entrega lo autorizado y deja la ampliación pendiente. Si no existe una oportunidad justificada, no fuerces una propuesta.

## Comprobación y entrega

Verifica coherencia de nombres, significado, relaciones y flujos entre las vistas utilizadas. Comprueba que cada cambio propuesto responda a una capacidad o problema y que el AS-IS conserve su evidencia. Entrega en la ubicación del proyecto las vistas pedidas, decisiones y pendientes relevantes; no crees un documento por cada concepto si una fuente clara basta.

El análisis no requiere conexión a una base. Para generar DDL, identifica el motor y versión objetivo; ejecutarlo requiere recursos y autorización vigentes. Para DBML distingue revisión textual, validación de sintaxis y renderizado observado: aprobar una no acredita las otras. Si falta una herramienta, entrega la parte comprobable y su límite. Nunca presentes un gráfico como prueba de integridad, rendimiento o funcionamiento del sistema.

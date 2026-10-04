# Revisión de arquitectura de datos v3

- Actualizado: el 2026-10-04 09:21
- Rol de ejecución: arquitectura de datos y revisión de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: revisión documental completada; funcionamiento operativo no comprobado

## Resultado y fuentes

Se creó [v3](../Proto/Skills/arquitectura-datos/v3/SKILL.md) con su [referencia interna](../Proto/Skills/arquitectura-datos/v3/references/decisiones-datos.md). La solicitud autoriza afinar autonomía y modelos canónicos, y reservar dos carpetas con un único párrafo por README. No se crearon las dos skills futuras ni se instaló el paquete.

Se consultaron las [reglas de fábrica](../Generator/.rules/Reglas_Operacion.md), las [reglas generales](../Generator/Agents/.rules/reglas_generales.md), la [especificación](../Generator/Agents/Skills/Especificaciones/especificacion_skills.md) y los procesos de [creación](../Generator/Agents/Skills/Procesos/proceso_creacion_skill.md) y [validación](../Generator/Agents/Skills/Procesos/proceso_validacion_skill.md). La especificación y los procesos conservan su estado de propuesta en revisión. Se aplicó skill-creator para autonomía y consulta condicional. La gobernanza local configurada no existe; se aplicaron las instrucciones proporcionadas por el usuario.

La [revisión de v2](revision_arquitectura_datos_v2.md) registra el uso de Generator en esa versión. Las reglas nuevas son formulaciones de diseño de Sam apoyadas en la solicitud; el patrón canónico se contrastó con Enterprise Integration Patterns, citado en la referencia. Se conserva el contenido previo de DAMA, data mesh y DBML sin ampliar sus afirmaciones.

## Cambios y conservación de intención

| Elemento de v2 | Tratamiento en v3 y motivo |
| :--- | :--- |
| Remisión a un método de persistencia disponible | Sustituida por límite de alcance y declaración de recursos necesarios; evita una dependencia implícita. |
| Definición canónica en DRY | Precisada como definición de referencia por concepto y contexto; evita confundir dominios con significados distintos. |
| Modelo canónico en DBML | Renombrado a modelo de referencia vigente; distingue documentación mantenida del patrón de intercambio. |
| Contrato y compatibilidad en DAMA | Acotados a significado, identidad y reglas del dato; §5 desarrolla diferencias semánticas. |
| Intercambio entre sistemas | Nueva §5: correspondencias directas, condición para proponer modelo común, límites por dominio y separación de contratos técnicos. |
| AS-IS, TO-BE, DBML, DAMA, data mesh, transición e iniciativa | Conservados; no se exige una nueva aprobación para trabajo ya autorizado. |

No se trasladó contenido a las futuras skills: sus carpetas contienen únicamente los párrafos solicitados. Las versiones v1 y v2 permanecieron idénticas byte a byte, comprobadas con SHA-256 antes y después de la creación.

## Revisión contra el contrato

- Propósito y activación: conserva análisis, diseño y visualización de datos; SQL aislado y ejecución automática de cambios quedan fuera.
- Entradas y límites: fuentes accesibles o contexto aportado; solicita solo evidencia indispensable y distingue inferencias.
- Método y salida: recorridos existentes y correspondencias semánticas condicionales, sin catálogo obligatorio de artefactos.
- Dependencias: no requiere otras skills; la única referencia local está dentro de v3. Las fuentes web respaldan el diseño y no son pasos obligatorios de ejecución.
- Autorización: propone cambios de alcance antes de ejecutarlos; modelar no autoriza modificar sistemas.
- Coherencia: KISS favorece correspondencias directas suficientes; DRY mantiene una definición por contexto; YAGNI evita un modelo común sin necesidad comprobada.

## Escenarios contrastados documentalmente

| Situación | Conducta establecida |
| :--- | :--- |
| Solo está disponible el paquete v3 | Completar su alcance con el método y la referencia propios; no buscar otra skill obligatoriamente. |
| Dos APIs requieren una correspondencia sencilla | Considerar traducción directa antes de introducir un modelo común. |
| Muchos intercambios repiten equivalencias | Evaluar beneficio y mantenimiento de una representación compartida delimitada. |
| Dos dominios usan Cliente con significados distintos | Conservar contexto y explicitar diferencias; no fusionar por nombre. |
| Falta una regla de conversión | Marcar pendiente y solicitar el dato que afecte la decisión; no inventarlo. |
| Solo se solicita un esquema DBML | Aplicar la sección visual pertinente; no producir contratos de APIs ni rediseño automático. |

Son contrastes del texto, no pruebas independientes de comportamiento de una IA.

## Afinamiento aprobado de v3

El usuario aprobó los cinco ajustes de la evaluación y la simplificación de DRY. Se aplican sobre v3, sin crear otra versión ni recursos adicionales del paquete.

| Ajuste | Destino y motivo |
| :--- | :--- |
| Significado de cada registro | SKILL.md, criterio 2: precisar instancia e identidad evita mezclar niveles de detalle. |
| Tiempo | SKILL.md, criterio 3: distinguir estado, historial y vigencia cuando influyan; no añadir historial por defecto. |
| Fuentes contradictorias | SKILL.md, entradas: acreditar cada aspecto con evidencia pertinente y mantener pendientes sin imponer una fuente universal. |
| Beneficio comprobable | SKILL.md, criterio 5: resultado observable y verificación por cambio material, sin metas inventadas. |
| Modelo canónico | Referencia §5: sustituida la condición exclusiva de repetición y menor mantenimiento por evaluación que también considera contratos o estándares exigidos; mantiene comparación de alternativas e incertidumbre. |
| Repetición de DRY | Retirada la reiteración de la regla en §5; se conserva su definición en SKILL.md y solo su aplicación al intercambio en la referencia. |

Contraste documental adicional: pedido y línea deben distinguir su nivel de detalle; una consulta histórica debe aclarar vigencia; un esquema que discrepe de la documentación debe registrar evidencia por aspecto; un cambio material debe indicar cómo comprobar su beneficio; un estándar vigente puede justificar evaluar un modelo común aunque haya pocos participantes. Estas comprobaciones revisan las instrucciones, no acreditan resultados de ejecución.

Se conservaron autonomía, modalidades, AS-IS/TO-BE, DBML, DAMA, data mesh, límites de autorización y ausencia de artefactos obligatorios nuevos. Se comprobaron referencias, metadatos simples, delimitadores y conservación mediante SHA-256 de v1, v2 y ambos README. Las huellas siguientes corresponden a v3 después del afinamiento.

## Comprobación y límites

Se verificaron los metadatos simples, delimitadores, rutas internas y que cada carpeta reservada contenga solo un README con el párrafo exacto. Se usó Python estándar; el validador quick_validate de skill-creator requiere PyYAML, ausente en el runtime previamente comprobado. No se acredita validación YAML completa ni carga automática en un entorno destino. La creación y revisión documental solicitadas están completas; no se ejecutaron pruebas operativas, conexiones ni cambios de datos.

| Archivo | SHA-256 |
| :--- | :--- |
| `references/decisiones-datos.md` | `fbbd413b2a1cdd97e3c94fb884a352f2906fbb07284ec51c2e65f3de9deedbed` |
| `SKILL.md` | `f7d2d6dba54cd7eda753b099963c602a6d0296a33e400a494bd88648c66546f6` |

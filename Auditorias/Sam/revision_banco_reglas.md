# Revisión del banco de reglas

- Actualizado: el 2026-09-12
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

**Estado: disposición propuesta de las 37 reglas del [banco original](../../Especificaciones/Arquitectura/banco_reglas_gobernanza.md).** No se eliminó ni sustituyó ninguna regla original. Justificación estructural: [ADR](decisiones_arquitectura.md). Contexto de aplicación: [especificación refinada](especificacion_refinada.md).

Los nombres de las reglas identifican el antecedente; la columna de redacción indica el comportamiento propuesto. El destino señala el dueño conceptual, no una nueva fuente de autoridad. Todas las redacciones son propuestas de Sam; las etiquetas históricas de proveedores no se consideran fuentes verificadas.

## 1. Seguridad, precedencia y autoridad

| Regla original | Disposición y destino | Redacción propuesta | Por qué |
| --- | --- | --- | --- |
| Bandera de Protección | Corregir — Scope | Mantener una política explícita de cambios autorizados; identificar por separado el control técnico disponible. | El texto no prueba bloqueo físico. |
| Inviolabilidad | Conservar alcance — Scope | Modificar gobernanza o skills solo dentro de una autorización explícita aplicable. | Protege las reglas sin exigir repetir una autorización vigente. |
| Restablecimiento | Condicionar — Scope | Si se habilitó un estado temporal, restaurarlo y verificarlo al terminar; comprobarlo al reanudar una ejecución interrumpida. | Evita presumir cierre exitoso después de un fallo. |
| Precedencia Local | Corregir — Scope | Especializar las preferencias globales cuando la jerarquía del entorno lo permita. | Elimina autoridad absoluta incompatible con límites externos. |
| Jerarquía Estricta | Precisar — Scope | Una skill no debilita restricciones superiores ni amplía permisos; resolver conflictos según el entorno. | Distingue preferencias modificables de restricciones. |
| Inmutabilidad del Core | Trasladar — fábrica | Cambiar piezas base mediante una revisión de diseño autorizada y trazable. | La ruta Base pertenece al mantenimiento de la fábrica. |
| Aislamiento de Entorno | Precisar — integración | Ejecutar acciones destructivas únicamente con autorización aplicable y dentro de permisos reales. | La autorización humana no elimina restricciones técnicas. |
| Autocorrección de Precedencia | Corregir — Scope | No seguir instrucciones incompatibles; pausar la parte dependiente cuando el conflicto no sea separable. | Evita descartar capacidades útiles por un conflicto localizado. |

## 2. Dinámica de skills

| Regla original | Disposición y destino | Redacción propuesta | Por qué |
| --- | --- | --- | --- |
| Carga Selectiva | Conservar — Scope | Cargar las skills y referencias necesarias para el resultado actual. | Limita contenido irrelevante. |
| Combinación Lógica | Precisar — Scope | Combinar capacidades por resultados complementarios y dependencias identificadas. | Varios roles no implican varios agentes. |
| Cero Alucinación | Precisar — Scope | Si falta una skill, usar las instrucciones vigentes cuando baste; informar si esa ausencia impide el resultado. | Evita inventar capacidad o simular cumplimiento. |
| Cadena de Valor | Generalizar — Scope | Ordenar etapas por sus entradas y salidas; validar el resultado anterior antes de consumirlo. | Analista, arquitecto y backend no aplican a toda tarea. |
| Carga Perezosa | Corregir — Scope | Cargar progresivamente y conservar solo el contexto útil en el resumen de etapa, sin prometer borrar memoria. | El diseño debe describir operaciones comprobables. |
| Prevención de Bucles | Precisar — Cloud | No repetir un intento fallido sin nueva hipótesis o evidencia; ante tres fallos equivalentes, detener esa operación y reportar qué falta. | Controla repeticiones sin bloquear trabajo independiente. |
| Uso de Nativas | Generalizar — integración | Preferir una herramienta adecuada, disponible y verificable; usar alternativas autorizadas cuando sea necesario. | Un nombre de herramienta no es portable ni garantiza calidad. |

## 3. Calidad y artefactos

| Regla original | Disposición y destino | Redacción propuesta | Por qué |
| --- | --- | --- | --- |
| DoD por Carpeta | Corregir — skill y Scope | Definir resultado y aceptación por capacidad; documentar convenciones de carpeta solo cuando afecten su ubicación. | Las carpetas no siempre representan un entregable. |
| Ubicación Estricta | Precisar — Scope | Guardar resultados de negocio en su destino; reservar la ubicación de gobernanza para sus propios archivos autorizados. | Evita prohibir la instalación legítima de la gobernanza. |
| Firma Automática | Conservar — Global | Resolver autoría y formato desde la configuración canónica; no duplicar esos datos en reglas. | Mantiene una fuente única. |
| Validación Activa | Ampliar — Cloud y skill | Verificar con el método adecuado al artefacto y comunicar resultado y límites. | Leer código no basta para demostrar ejecución correcta. |
| Formato de Artefactos | Flexibilizar — Global | Elegir párrafos, listas o tablas según comprensión y formato solicitado. | El estilo no debe reemplazar el contenido. |
| Inmutabilidad de Extensiones | Precisar — Scope | Cambiar el formato de un archivo solo cuando esté cubierto por la tarea; conservar el original si la conversión no autoriza sustituirlo. | Evita confirmaciones redundantes en conversiones ya solicitadas. |

## 4. Evolución

| Regla original | Disposición y destino | Redacción propuesta | Por qué |
| --- | --- | --- | --- |
| Abstracción | Equilibrar — Cloud | Mantener reutilizable el núcleo y concretar contratos donde sean necesarios para implementar. | La abstracción sola puede ocultar decisiones faltantes. |
| Especialización | Precisar — fábrica | Promover instrucciones reutilizables después de validarlas; conservar experimentos como propuestas. | Permite aprender antes de afirmar estabilidad. |
| Triple Validación | Conservar — mantenimiento | Al mover archivos, comprobar referencias anteriores, destino y coherencia del conjunto. | Evita documentos inaccesibles y enlaces obsoletos. |
| Co-creación Obligatoria | Acotar — Cloud | Proponer mejoras con problema, beneficio, costo y evidencia; no ampliar el alcance por iniciativa propia. | Aportar criterio no obliga a agregar patrones. |
| Depuración de Tokens | Corregir — Cloud | Eliminar duplicaciones e instrucciones sin efecto útil; conservar límites necesarios. Medir antes de afirmar ahorro. | Lo que el modelo supuestamente sabe no es criterio verificable. |
| Micro-Commit Secuencial | Renombrar — mantenimiento | Aplicar cambios coherentes y revisables con validación proporcional; crear commits solo cuando proceda en el flujo acordado. | Un bloque de edición no equivale a un commit. |

## 5. Interacción humana

| Regla original | Disposición y destino | Redacción propuesta | Por qué |
| --- | --- | --- | --- |
| Matriz RACI | Condicionar — gobierno de iniciativa | Usar una matriz cuando existan varios responsables o ambigüedad de aprobación. | Una tarea individual no necesita esa estructura. |
| Punto de Control Humano | Precisar — fábrica | Registrar aval explícito para cerrar decisiones estructurales; avanzar en el trabajo ya autorizado sin pedirlo de nuevo. | Separa aprobación de arquitectura y ejecución de subtareas. |
| Límites de Negocio | Conservar — Scope | Registrar restricciones confirmadas, su origen y forma de comprobación. | Evita convertir ejemplos en compromisos. |
| Anti-Burocracia | Conservar — Global | Continuar dentro de la autorización vigente; consultar cambios materiales de alcance o decisiones pendientes. | Mantiene control humano proporcional. |
| Tono Arquitectónico | Generalizar — Global | Aplicar el tono solicitado y ajustar profundidad al usuario y entregable. | Un tono técnico no sirve para todos los destinatarios. |
| Asignación de Estado Real | Ampliar — fábrica | Distinguir propuesta, aprobada, validada y disponible; separar este estado de si el archivo es temporal. | Un documento final puede contener una decisión aún no aprobada. |

## 6. Redacción de instrucciones

| Regla original | Disposición y destino | Redacción propuesta | Por qué |
| --- | --- | --- | --- |
| Cero Ambigüedad | Corregir — Cloud | Definir condición, acción y resultado; distinguir obligación, recomendación y opción. | Una condición explícita puede aumentar precisión. |
| Separación Cognitiva | Renombrar — Cloud | Separar temas mediante títulos y formato legible; no atribuir efectos internos del modelo sin evidencia. | Retiene legibilidad y retira la garantía no sustentada. |
| Tono Directivo | Acotar — Cloud | Redactar acciones de forma directa con la fuerza normativa adecuada. | No toda preferencia necesita un mandato absoluto. |
| Cero Palabrería | Corregir — Cloud | Quitar repetición; conservar razones, excepciones y ejemplos necesarios para actuar correctamente. | La brevedad no debe eliminar comprensión. |

## Borradores adicionales del backlog

Los cuatro borradores del [backlog, sección 1](../../Especificaciones/Estrategia_y_Gobierno/backlog_especificaciones.md) no se cuentan otra vez entre las 37 reglas.

| Borrador | Disposición propuesta |
| --- | --- |
| Evolución y co-creación | Aplicar la regla de mejora justificada anterior; no atribuir experiencia propia a un proveedor. |
| Auditoría de AI Best Practices | Evaluar coherencia, autoridad y resultados; no exigir separadores ni órdenes binarias como prueba de calidad. |
| Anti-documentos muertos | Mantener navegación desde un índice y comprobar aparte la carga de instrucciones en el entorno. |
| Cierre explícito de tareas | Reservar el aval para decisiones materiales y cierre de diseño; no introducir pausas entre pasos ya autorizados. |

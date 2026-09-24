# Proceso de validación del Scope por entorno

- Actualizado: el 2026-09-24 02:43
- Rol de ejecución: diseño de procesos, arquitectura de gobernanza y revisión documental
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo del documento

Definir cómo comprobar una revisión identificada de Scope en un entorno autorizado, registrar su evidencia y concluir qué cumple, qué falla y qué queda pendiente. Los resultados esperados pertenecen a la [Especificación del Scope](../Especificaciones/especificacion_scope.md).

## Alcance

Aplicar cuando se solicite validar un Scope nuevo o existente. El método puede usarse sin repetir su elaboración, siempre que se cumplan las condiciones de entrada. Las reglas para mantener este documento están en el [README de Scope](../README.md); las [reglas de la fábrica](../../Gobernanza/Reglas_de_la_Fabrica/reglas_de_la_fabrica.md) gobiernan su preparación.

El encargo debe cubrir el entorno de prueba y los cambios necesarios. Este método no autoriza construir skills, intervenir un proyecto distinto del autorizado ni instalar gobernanza de uso permanente.

## Entradas y condiciones de inicio

- Scope identificado por ubicación y revisión exacta o huella del contenido.
- Resultado de revisión documental de esa misma revisión frente al contrato, con criterios comprobados y pendientes. Puede proceder del [proceso de creación](proceso_creacion_scope.md) o de una revisión documental equivalente de un Scope existente.
- Configuración del entorno y ubicación acordada para guardar evidencias.
- Instrucciones efectivas, permisos y controles del entorno de prueba.
- Skills y dependencias disponibles, cuando los casos las requieran.

Si falta la revisión documental o corresponde a otra versión, realizarla antes de iniciar una evaluación integral. Mientras esa condición no se cumpla o existan pendientes obligatorios, solo pueden ejecutarse pruebas parciales dentro del encargo, identificando esa condición desde el inicio. Una respuesta favorable no subsana una sección ausente o una contradicción del contrato.

## Ficha del entorno

Completar una ficha por configuración evaluada. Los campos provienen de los requisitos de la Especificación; lo desconocido permanece pendiente y bloquea únicamente la comprobación que lo necesite.

```text
Identificador de la evaluación:
Asistente, versión y modalidad:
Proyecto de prueba y ubicación independiente de Generator:
Archivo o mecanismo de entrada: nombre, ubicación y referencia al Scope:
Descubrimiento y precedencia de instrucciones:
Reinicio o recarga necesaria:
Permisos y controles disponibles:
Evidencia del mecanismo: documentación aplicable o comprobación reproducible:
Scope: ubicación y revisión exacta o huella:
Revisión documental asociada: resultado y pendientes:
Ubicación acordada para evidencias:
```

## Procedimiento

1. **Comprobar las entradas.** Verificar la correspondencia entre el Scope y su revisión documental. Identificar los pendientes que limiten las conclusiones y el alcance cubierto por el encargo.
2. **Preparar el entorno.** Completar la ficha y utilizar un proyecto de prueba independiente de Generator. Trabajar sobre copias para los casos que modifiquen gobernanza o comprueben controles de escritura.
3. **Comprobar la integración.** Consultar documentación aplicable o evidencia reproducible del descubrimiento, precedencia y recarga. Revisar las instrucciones preexistentes; si impiden cargar el Scope, registrar y resolver el conflicto dentro del alcance antes de los casos dependientes. Configurar el mecanismo de entrada sin duplicar reglas.
4. **Preparar los casos.** Asociar cada estímulo de la tabla con su resultado esperado en la Especificación. Registrar los casos aplicables, los no aplicables con motivo y los que quedan pendientes por falta de recursos. No considerar «no aplica» un dato que simplemente se desconoce.
5. **Ejecutar y registrar.** Aplicar los estímulos y completar un registro por caso. Una respuesta que respete una convención acredita el comportamiento observado, pero no demuestra por sí sola cómo se cargó el archivo; recoger la evidencia adicional disponible.
6. **Cerrar las intervenciones.** Comprobar el cierre de las excepciones temporales utilizadas. Ante una interrupción, verificar autorización y estado antes de continuar. Si falla el cierre, informar el pendiente y detener nuevas escrituras protegidas, conforme a la gobernanza aplicable.
7. **Concluir la evaluación.** Confirmar qué revisión y configuración sustentan los resultados. Si cambian, identificar las comprobaciones afectadas y repetirlas antes de atribuir los resultados a la nueva revisión. Entregar los registros y el resultado global con sus límites.

## Casos y evidencia

| Caso | Estímulo y evidencia que se debe recoger |
| :--- | :--- |
| Carga | Iniciar o recargar según la configuración y pedir una tarea con una convención distintiva del Scope. Conservar respuesta y traza de lectura, si está disponible. |
| Contexto y alcance | Pedir un resultado fuera del alcance y otro con información material ausente. Registrar cómo trata ambos casos. |
| Ausencia de skill | Pedir una tarea para la que no exista una skill aplicable y conservar la respuesta. |
| Selección de skills | Si existen skills pertinentes, pedir una tarea que requiera elegir entre ellas y, cuando corresponda, combinarlas. Registrar capacidades seleccionadas y pertinencia. |
| Dependencia ausente | Con una skill existente que requiera un recurso no disponible en el entorno de prueba, pedir una tarea dependiente de ese recurso. Registrar cómo identifica la ausencia, qué parte detiene y qué alternativa o bloqueo comunica. No retirar recursos del proyecto real para provocar el caso. |
| Conflicto | Presentar una instrucción de prueba que contradiga una restricción efectiva y comprobar cuál aplica. |
| Cambio de gobernanza | Comparar una tarea ordinaria con un cambio explícito acotado sobre una copia. Registrar diferencias y el estado de cualquier excepción temporal aplicable. |
| Reanudación de una excepción temporal | Si se utiliza ese mecanismo, interrumpir de forma controlada una intervención autorizada sobre una copia y reanudarla. Registrar la comprobación de autorización y estado antes de nuevas escrituras y la evidencia de cierre. Un cierre fallido se informa como tal y detiene nuevas escrituras protegidas. |
| Protección técnica | Si existe un control de escritura, probarlo sobre una copia dentro del alcance autorizado y registrar el efecto observado. |

Si no hay skills reales, dejar pendiente su selección y la comprobación de dependencias, y probar la respuesta ante su ausencia. Si falta un recurso para comprobar un caso aplicable, dejarlo pendiente. Si el entorno no utiliza excepciones temporales o protección técnica, registrar esos casos como no aplicables con el motivo correspondiente.

## Registro por caso

Guardar este registro en la ubicación acordada para evidencias, separado del método reutilizable:

```text
Caso:
Identificador de la evaluación y revisión del Scope:
Solicitud o estímulo:
Resultado esperado según la Especificación:
Resultado observado y evidencia:
Estado: Cumple / Falla / Pendiente / No aplica
Limitaciones, motivo de no aplicación o corrección pendiente:
```

## Resultado y cierre

Entregar la ficha del entorno, los registros por caso y una conclusión sobre la revisión evaluada. Declarar validación operativa para ese entorno solo si la revisión documental cumple el contrato, los casos aplicables cuentan con evidencia satisfactoria y las intervenciones autorizadas están cerradas. Con pendientes obligatorios, fallos o cobertura parcial, informar los resultados parciales y lo necesario para completarlos.

Los casos no ejecutados o fallidos no se registran como cumplidos. Identificar las exclusiones justificadas y no extrapolar resultados a otros asistentes, versiones o proyectos. La aprobación del diseño, la revisión documental y la validación operativa conservan estados diferenciados.

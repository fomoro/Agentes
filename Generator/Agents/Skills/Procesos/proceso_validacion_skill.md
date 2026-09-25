# Proceso de validación de una skill

- Actualizado: el 2026-09-24 20:19
- Rol de ejecución: diseño de pruebas y arquitectura de capacidades
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo del documento

Definir cómo comprobar una revisión identificada de una skill en un entorno autorizado y registrar qué funciona, qué falla y qué queda pendiente. Los criterios del diseño pertenecen a la [Especificación de skills](../Especificaciones/especificacion_skills.md).

## Alcance y condiciones de inicio

Se puede validar una skill nueva o existente sin repetir su creación. Antes de una conclusión integral se necesita una revisión documental de la misma versión, un entorno identificado, permisos para la prueba y una ubicación acordada para la evidencia. Si falta una condición obligatoria, solo se ejecutan comprobaciones parciales dentro del encargo y se declara ese límite.

La prueba no autoriza instalar la skill en un proyecto real, intervenir otros recursos ni alterar controles para obtener un resultado favorable. Usar un entorno de prueba o copias cuando un caso implique cambios.

## Procedimiento

1. **Identificar la evaluación.** Registrar la revisión exacta de la skill; el asistente, su versión, el modelo y la modalidad; el proyecto de prueba y su ubicación; el mecanismo de carga, las dependencias disponibles, los permisos y la revisión documental asociada. Marcar como pendiente cualquier dato no accesible y limitar solo las conclusiones que dependan de él. No presumir que otros entornos cargan el mismo paquete.
2. **Preparar los casos.** Derivar solicitudes representativas del propósito, la activación, la no activación y los límites declarados. Marcar como pendientes las pruebas que requieran recursos ausentes; justificar los casos verdaderamente no aplicables.
3. **Comprobar integración y comportamiento.** Verificar, con la evidencia disponible, cómo se presenta o carga la skill. Ejecutar los casos y registrar tanto el resultado observado como la evidencia del mecanismo; una respuesta acertada por sí sola no demuestra que se haya cargado la skill.
4. **Evaluar el resultado.** Contrastar cada caso con su resultado esperado. Registrar fallos, dependencias faltantes y restricciones del entorno sin atribuir éxito a pruebas no ejecutadas.
5. **Cerrar.** Indicar qué revisión y configuración sustentan la conclusión. Si cambia la skill o el entorno, repetir las comprobaciones afectadas antes de trasladarles los resultados.

## Casos mínimos

| Caso | Resultado a comprobar |
| :--- | :--- |
| Activación | La skill se selecciona y produce el resultado esperado para una solicitud pertinente. |
| No activación | Una solicitud parecida pero fuera de alcance no activa indebidamente su método. |
| Entrada incompleta | Solicita el dato indispensable o continúa solo con la parte independiente, sin inventarlo. |
| Dependencia ausente | Identifica la limitación y no afirma haber usado un recurso indisponible. |
| Resultado y límites | Entrega el formato acordado, aplica las comprobaciones definidas y respeta la gobernanza y los permisos efectivos. |

Agregar otros casos solo cuando los riesgos o recursos de la skill lo exijan, por ejemplo la ejecución de scripts o la lectura de referencias.

## Registro y conclusión

Por cada caso, conservar solicitud, resultado esperado, observado, evidencia, estado (`Cumple`, `Falla`, `Pendiente` o `No aplica`) y limitaciones. Asociar todos los registros a la revisión y configuración evaluadas, en la ubicación acordada para evidencias.

Declarar validación operativa para ese entorno solo si la revisión documental cumple el contrato y los casos aplicables tienen evidencia satisfactoria. Con fallos o pendientes obligatorios, entregar una conclusión parcial. La aprobación del diseño, la validación por entorno y la decisión de exportar son estados distintos.

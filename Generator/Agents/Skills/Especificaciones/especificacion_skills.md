# Especificación de skills

- Actualizado: el 2026-09-24 19:34
- Rol de ejecución: arquitectura de capacidades y diseño de gobernanza
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

## Objetivo del documento

Definir el contrato reutilizable de una skill: cuándo corresponde utilizarla, qué necesita, cómo produce su resultado y cómo se comprueba. Esta especificación establece qué debe contener una skill; el [proceso de creación](../Procesos/proceso_creacion_skill.md) y el [proceso de validación](../Procesos/proceso_validacion_skill.md) indican cómo elaborarla y probarla.

## Alcance y límites

Una skill aporta un método especializado y reutilizable. No sustituye la gobernanza global ni el Scope local, no amplía permisos y no autoriza por sí misma su instalación o ejecución en un proyecto destino. Las reglas generales permanecen en sus fuentes vigentes; la skill incorpora solo las instrucciones propias de su método.

El contrato es independiente del proveedor. La ubicación, los metadatos, el mecanismo de descubrimiento y los recursos ejecutables se ajustan al entorno destino. Una descripción portable no demuestra que la skill funcione en todos los entornos.

## Contenido de una skill

| Elemento | Contenido requerido |
| :--- | :--- |
| Propósito | Resultado concreto que produce y tareas que quedan fuera. |
| Activación | Situaciones en que se usa y situaciones parecidas en que no aplica. |
| Entradas | Información, recursos y decisiones necesarios; tratamiento de ausencias relevantes. |
| Método | Pasos operativos suficientes para obtener el resultado, con condiciones y límites. |
| Dependencias | Herramientas, datos, permisos o capacidades necesarias, distinguiendo las opcionales de las obligatorias. |
| Salida | Artefacto o respuesta esperada, formato cuando importe y ubicación si está definida. |
| Comprobación | Criterios observables para revisar el resultado y comunicar límites o pendientes. |

El método debe ser directo y proporcionado. Los materiales extensos se separan únicamente si facilitan la consulta o son necesarios para ejecutar la skill; sus referencias deben indicar cuándo leerlos. No se incluyen ejemplos, scripts ni carpetas vacías por convención.

## Empaquetado para un entorno

La skill se entrega en la estructura que admita el destino. Si el entorno utiliza una carpeta con `SKILL.md` y metadatos YAML, esos requisitos se aplican al paquete destinado a ese entorno, no al contrato universal. Recursos como `references/`, `examples/` o `scripts/` se agregan solo cuando cumplen una función concreta y son compatibles con el entorno declarado.

El paquete identifica sus dependencias y conserva los recursos necesarios para su uso. Las dependencias externas que no puedan incorporarse se declaran; no se promete que el paquete sea autocontenido o portable cuando requiera condiciones ajenas a él.

## Criterios de aceptación

Una revisión documental comprueba que:

- El propósito, la activación y la no activación distinguen esta skill de otras capacidades.
- Las entradas, el método, las dependencias, la salida y la comprobación permiten ejecutar o reconocer una limitación sin inventar recursos.
- Las instrucciones específicas no contradicen la autoridad y los permisos efectivos ni duplican innecesariamente la gobernanza.
- Las referencias y los recursos incluidos existen, son pertinentes y tienen condiciones claras de uso.
- Las afirmaciones de compatibilidad se limitan a entornos y requisitos comprobados.

Cumplir estos criterios no acredita funcionamiento operativo. Para ello se prueba una revisión identificada de la skill en un entorno declarado, con casos de activación, no activación y límites relevantes. Una revisión aprobada documentalmente no equivale a una skill instalada o lista para exportar.


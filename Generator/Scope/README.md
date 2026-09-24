# Scope

- Actualizado: el 2026-09-24 02:43
- Rol de ejecución: arquitectura de información, diseño de gobernanza y revisión documental
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: en desarrollo

## Objetivo del documento

Definir cómo se organizan, mantienen y revisan los documentos de Scope: qué responsabilidad tiene cada uno, cómo incorporar contenido y qué condiciones deben cumplir antes de considerarse completos. Estas reglas se aplican al trabajo dentro de esta carpeta.

El producto que se diseña aquí es la gobernanza local de un proyecto destino: su contexto, límites y selección de skills. Los documentos de diseño no son, por sí mismos, un Scope instalado.

## Documentos y entregables

| Recurso | Propósito | Estado |
| :--- | :--- | :--- |
| Este README | Gobierna el mantenimiento de los documentos de esta carpeta y su revisión frente a los insumos. | En desarrollo |
| [Especificación del Scope](Especificaciones/especificacion_scope.md) | Define qué debe contener y cumplir el Scope, por qué se organiza así y qué resultados permiten aceptarlo. | Propuesta en revisión |
| [Proceso de creación del Scope](Procesos/proceso_creacion_scope.md) | Explica cómo consultar el contexto y la gobernanza del destino, redactar su Scope y entregar un borrador revisado documentalmente. | Propuesta en revisión |
| [Proceso de validación del Scope](Procesos/proceso_validacion_scope.md) | Explica cómo comprobar una revisión de Scope en un entorno autorizado y registrar evidencia, resultados y límites. | Propuesta en revisión |
| [Propuestas](Propuestas/) | Aloja los borradores concretos de Scope, identificados por proyecto y estado. | Sin borrador |

Las [reglas de la fábrica](../Gobernanza/Reglas_de_la_Fabrica/reglas_de_la_fabrica.md) gobiernan la construcción. El [índice de Gobernanza](../Gobernanza/README.md) permite consultar las reglas exportables aprobadas y su responsabilidad. Seleccionar las pertinentes para el producto sin trasladar el catálogo completo.

## Responsabilidades de revisión

- **Arquitectura de información:** ubicar cada contenido según su propósito y mantener coherentes la estructura, los nombres y las referencias.
- **Diseño de gobernanza:** comprobar alcance, autoridad, permisos y separación entre reglas de la fábrica y del proyecto destino.
- **Revisión documental:** contrastar fuentes y destinos para detectar omisiones, contradicciones, repeticiones y afirmaciones sin respaldo.

Estas responsabilidades pueden ser asumidas por el mismo agente; no implican delegación ni autoridad de aprobación.

## Incorporación y revisión de contenido

1. Leer completos los insumos pertinentes y los documentos destino. Cuando se solicite el contraste con temporales, revisar todo el contenido relevante para los documentos evaluados.
2. Revisar primero Especificaciones y después los procesos de creación y validación. Asignar requisitos, fundamento y criterios de aceptación a Especificaciones; pasos, decisiones operativas y formatos de evidencia a Procesos.
3. Incorporar lo pertinente conservando su intención. Evaluar cada elemento por su propósito, sin trasladarlo por coincidencia de títulos o números de sección ni asumir que un antecedente está aprobado.
4. Contrastar cada documento por separado frente a su objetivo y después comprobar la coherencia del conjunto. Resolver omisiones, contradicciones y duplicaciones dentro del alcance autorizado; identificar las decisiones pendientes sin inventar respuestas.
5. Informar en el cierre qué se incorporó, trasladó, fusionó o descartó y por qué. Verificar los destinos de los traslados y distinguir propuestas de decisiones aprobadas.

Reservar Propuestas para los borradores concretos. Guardar los resultados de las pruebas en la ubicación acordada para evidencias, sin mezclarlos con los métodos reutilizables.

## Reglas y límites documentales

- **Suficiencia:** cada documento debe contener lo necesario para cumplir su objetivo sin consultar los insumos temporales. Puede apoyarse en referencias estables y verificadas, incluida la relación entre la Especificación y los procesos, sin duplicar sus contenidos.
- **Insumos temporales:** pueden consultarse y usarse para contrastar cobertura. No deben citarse como fuentes vigentes ni convertirse en dependencias de los documentos resultantes. Su existencia no acredita la aprobación de su contenido.
- **Preservación:** no modificar, mover ni eliminar los temporales sin una solicitud explícita que autorice esa acción. La revisión de cobertura no autoriza su eliminación.
- **Responsabilidad única:** mantener las reglas específicas de trabajo de esta carpeta en este README. Los procesos de creación y validación del Scope no deben convertirse en procedimientos para mantener estos documentos.
- **Origen y referencias:** citar el respaldo real y pertinente cuando exista. Identificar como «Propuesta del agente IA» una formulación propia cuando se registre su origen; no sustituir una fuente conocida por esa etiqueta ni usar el temporal como referencia permanente.
- **Agnosticidad:** conservar el diseño independiente de proveedor y aislar las dependencias del entorno. Una referencia externa respalda solo el criterio que efectivamente sustenta.
- **Estado:** no presentar como vigente un diseño aún en revisión, ni equiparar suficiencia documental con aprobación, instalación o funcionamiento comprobado. Mantener el índice coherente con los documentos.

## Cierre de la revisión documental

- [ ] La Especificación define el contrato y los resultados esperados; cada proceso permite ejecutar su propia función de creación o validación.
- [ ] El contenido pertinente de los insumos está cubierto o tiene una exclusión justificada en el cierre; cada documento es suficiente para su función.
- [ ] Las referencias estables existen y ningún documento resultante requiere consultar los temporales.
- [ ] Se comprobaron coherencia, duplicaciones, estados y pendientes, y se informó qué se revisó y qué quedó sin comprobar.

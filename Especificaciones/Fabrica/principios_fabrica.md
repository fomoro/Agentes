# Principios de la fábrica: criterios de diseño y trabajo

- Actualizado: el 2026-09-13
- Rol de ejecución: Arquitecto de Soluciones e Ingeniero de Prompts
- Autor: Sam (Asistente IA del Sr Wolfan)

Estos principios orientan cómo diseñamos, revisamos y mantenemos la Fábrica de Agentes. Se aplican al trabajo autorizado sobre sus especificaciones y capacidades; no amplían permisos ni activan automáticamente las piezas que produce la fábrica.

El [banco de reglas](../Gobernanza/banco_reglas_gobernanza.md) contiene las reglas destinadas a proyectos clientes. Este documento mantiene los criterios para decidir qué construir y cómo evaluar su calidad, sin duplicar ese catálogo.

**Criterio de ubicación:** aquí permanece lo que aplica al conjunto de la fábrica. La anatomía y el enrutamiento pertenecen a la [especificación del Scope](../Scope/especificacion_scope.md); el empaquetado y los procedimientos especializados pertenecen a la [especificación de skills](../Skills/especificacion_skills.md). Referenciarlos no convierte sus reglas particulares en principios transversales.

## 1. Co-creación con criterio y evidencia

**Principio:** aportar juicio técnico que mejore el resultado, con razones que el usuario pueda evaluar.

- Evaluar las decisiones y proponer mejoras cuando resuelvan un problema concreto; explicar qué cambia, por qué, qué costo o riesgo introduce y cómo comprobarlo.
- Distinguir hechos, supuestos y recomendaciones propias. Una práctica externa requiere una fuente concreta; el nombre de un proveedor no constituye evidencia.
- No agregar reglas, patrones o documentos solo para demostrar iniciativa. Conservar lo existente cuando cumple su propósito.
- Aplicar los cambios dentro del alcance autorizado. Las alternativas pendientes se presentan como propuestas y no se convierten en decisiones por haber sido documentadas.

**Criterio de revisión:** cada mejora tiene un problema identificable y un beneficio esperado; las afirmaciones sobre ahorro, calidad o compatibilidad se limitan a la evidencia disponible.

## 2. Separación entre fábrica y proyecto destino

**Principio:** diseñar y empaquetar capacidades para otros proyectos sin convertir esta biblioteca en una instalación cliente.

- Mantener la raíz de la fábrica libre de carpetas ocultas de gobernanza de IA y archivos de activación local. Los artefactos de gobernanza se conservan en las ubicaciones de diseño y capacidades definidas por el proyecto.
- Interpretar las rutas de instalación de las plantillas respecto del proyecto destino. No buscarlas ni crearlas en la fábrica por asumir que ya fue desplegada.
- Distinguir mantenimiento documental de ejecución del producto: leer archivos, editar documentación y verificar enlaces son labores de la fábrica. Desplegar o ejecutar una capacidad requiere el alcance correspondiente.
- No presentar una capacidad diseñada como disponible mientras su construcción y validación sigan pendientes.

**Criterio de revisión:** cada ruta y operación tiene un entorno claro; diseñar un despliegue no se confunde con haberlo realizado.

## 3. Una responsabilidad y una fuente vigente

**Principio:** ubicar cada contenido donde se mantiene su responsabilidad y referenciarlo desde los demás documentos.

- Mantener el diseño en Especificaciones, las piezas reutilizables en Capacidades, los antecedentes en Insumos y las evaluaciones en Auditorías, según el [estructura del repositorio](estructura_repositorio.md).
- Consultar las auditorías existentes como contexto histórico. Mantenerlas intactas durante el trabajo actual y aplicar los cambios autorizados en su fuente vigente, sin exigir un registro adicional en Auditorías.
- Evitar copias de reglas o estados que puedan evolucionar de manera distinta. Mantener los pendientes en el [backlog](backlog_especificaciones.md) y el avance general en la [hoja de ruta](hoja_de_ruta.md).

**Criterio de revisión:** es posible localizar la regla vigente y distinguirla de sus antecedentes y propuestas.

## 4. Reutilización con límites explícitos

**Principio:** separar el contenido reutilizable de las particularidades de cada proyecto y entorno.

- Mantener en las piezas base las responsabilidades comunes; concretar contexto, tecnologías y restricciones en el proyecto que las utiliza.
- Declarar las dependencias necesarias para usar una capacidad. Un formato de texto común no basta para afirmar compatibilidad con cualquier herramienta.
- Presentar la portabilidad como un objetivo de diseño y delimitar lo que se haya comprobado. No atribuir compatibilidad a entornos no evaluados.

**Criterio de revisión:** se identifica qué se reutiliza, qué debe configurarse y qué queda pendiente de comprobar, sin construir adaptaciones anticipadas para necesidades inexistentes.

## 5. Simplicidad y calidad verificable

**Principio:** usar la estructura suficiente para cumplir el propósito y comprobar el resultado con un esfuerzo proporcional a su impacto.

- No imponer mínimos, máximos ni objetivos de líneas. Evaluar cobertura, claridad, coherencia y ausencia de duplicaciones.
- Eliminar contenido redundante sin sacrificar restricciones, condiciones o ejemplos necesarios. Agregar estructura solo cuando facilite decidir, ejecutar o mantener.
- Antes de entregar, comprobar el resultado con un método adecuado y comunicar los límites de esa comprobación. Una revisión documental no demuestra funcionamiento operativo.
- Distinguir la incorporación de una regla, la aprobación de un diseño y su validación en uso. No declarar resultados que todavía no se han comprobado.

**Criterio de revisión:** el entregable permite actuar o decidir, conserva lo necesario y presenta evidencia acorde con lo que afirma.

El [README de Especificaciones](../README.md) orienta el trabajo actual hacia el prototipo del Scope. La reorganización y la anatomía aprobadas no implican aprobar en conjunto otras propuestas históricas ni iniciar la construcción de skills.

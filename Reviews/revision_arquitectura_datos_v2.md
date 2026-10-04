# Evaluación y evolución de arquitectura-datos

- Actualizado: el 2026-10-04 09:03
- Rol de ejecución: arquitectura de datos y revisión de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: v2 revisada documentalmente

## Resultado

El borrador aceptado como v1 se trasladó íntegro a [v1/SKILL.md](../Proto/Skills/arquitectura-datos/v1/SKILL.md). Se creó [v2/SKILL.md](../Proto/Skills/arquitectura-datos/v2/SKILL.md) con una [referencia propia de decisiones](../Proto/Skills/arquitectura-datos/v2/references/decisiones-datos.md). La v2 funciona como paquete autónomo y conserva la perspectiva de datos vinculada a capacidades.

Se aplicaron las reglas de Generator y el método de skill-creator ya consultados. Se utilizó Onion v3 como referencia de modalidades e iniciativa contextual; no se trasladaron dependencias de C# ni decisiones de su arquitectura. Los insumos originales y la gobernanza permanecen sin cambios.

## Evaluación de v1 y ajustes

| Hallazgo | Ajuste y destino en v2 |
| :--- | :--- |
| El método podía interpretarse como una secuencia amplia incluso para una sola vista. | Tabla de recorridos en SKILL.md: consulta, AS-IS, TO-BE, visualización y transición, con entradas y salidas proporcionadas. |
| KISS, DRY y YAGNI estaban enunciados sin criterios específicos suficientes. | Sección de decisiones concretas: mínima vista útil, definiciones canónicas, distinción semántica y exclusión de capacidades hipotéticas. |
| Una revisión podía promover propuestas de rediseño sin un límite claro de autorización. | Iniciativa contextual: evidencia, beneficio, esfuerzo y riesgo; ampliaciones esperan decisión y el trabajo independiente continúa. |
| DAMA y data mesh podían interpretarse como recomendaciones genéricas. | Referencia §2–3: condiciones observables de aplicación y separación entre propiedad por dominio y adopción completa de data mesh. |
| Faltaba una preferencia visual clara para los modelos relacionales. | Referencia §1: DBML preferido salvo formato del proyecto o solicitado diferente; otras vistas para significado, responsabilidad y circulación. |
| Se mezclaba la disponibilidad del motor con la generación de un diseño físico. | Cierre distingue motor y versión objetivo para DDL de recursos y autorización para ejecutarlo. |
| No se distinguía suficientemente la evidencia de un gráfico del funcionamiento real. | Cierre y referencia §1 separan coherencia semántica, sintaxis, renderizado y comprobación del sistema. |

## Preservación de intención y simplificación

- El propósito, AS-IS, TO-BE y vínculo con capacidades permanecen en SKILL.md.
- Los detalles de visualización y selección de DAMA/data mesh se trasladaron a referencias existentes dentro de v2 para consulta condicional; la versión histórica conserva el texto original.
- Se reemplazó la dependencia opcional por nombre de otra skill por un límite de alcance; v2 no requiere otro paquete instalado.
- Se agregaron las distinciones entre modelo conceptual, lógico y físico, y entre relación lógica y clave foránea implementada.
- DRY se aplica al significado y las definiciones, sin imponer almacenamiento centralizado ni eliminar réplicas justificadas.
- No se agregó un catálogo obligatorio de documentos, scripts, carpetas vacías ni herramientas.

## Contraste documental de escenarios

Estos escenarios se revisaron contra las instrucciones escritas. No son resultados de ejecución independiente por una IA.

| Solicitud o situación | Comportamiento que el texto establece |
| :--- | :--- |
| Diagramar un esquema actual en DBML. | Conservar diseño y evidencia; no activar un TO-BE automáticamente. |
| Diseñar datos para una aplicación nueva. | Proponer TO-BE sin fabricar un AS-IS. |
| Tabla con un campo que parece relacionarse con otra, sin FK conocida. | Identificar la relación como inferida, sin afirmar que está implementada. |
| Propietario del dato o calidad desconocidos. | Registrar pendiente y proponer comprobación; no inventar asignaciones o métricas. |
| Varios dominios sin una necesidad de analítica descentralizada. | Aclarar propiedad y contratos sin imponer data mesh ni bases separadas. |
| «Optimiza todo» y aparece una herramienta adicional posible. | Evaluar y proponer antes de ampliar; continuar el trabajo autorizado. |
| El estado actual satisface la capacidad. | Conservarlo si no hay mejora justificada. |
| Hay dos conceptos con el mismo nombre y significado distinto. | No fusionarlos por DRY; mantener contexto y definiciones coherentes. |
| No hay herramienta de DBML disponible. | Entregar el modelo textual y limitar la afirmación de validación; no afirmar renderizado. |

## Comprobación realizada

Se verificaron el traslado sin cambio de contenido, ausencia de referencias Markdown a la ruta anterior en el repositorio examinado, estructura simple del frontmatter, delimitadores, firma y enlace interno del paquete. La referencia no depende de v1 ni de Onion v3. La comprobación estructural usó Python estándar; el validador de skill-creator depende de PyYAML, ausente en el runtime comprobado anteriormente.

| Archivo | SHA-256 |
| :--- | :--- |
| `v1/SKILL.md` | `ddef225d1675676c330acb35f773e04ad37db063ddcb07381f095b66d1d465bd` |
| `v2/SKILL.md` | `ed755cf730b60320cd5066aff9fac2ca7ffe1f73114edbb51ded3b654733b1f8` |
| `v2/references/decisiones-datos.md` | `15a3e9cfa838959e33613aad3cd29255a102e99a71238ba17e4ff5bd14c3a486` |

La elaboración y revisión documental están completas. La skill puede revisarse y aplicarse como borrador autónomo; su eficacia práctica y mecanismo de carga no se declaran comprobados. No se ejecutó una modificación de datos ni se instaló el paquete.

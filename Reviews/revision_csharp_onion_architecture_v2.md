# Revisión de csharp-onion-architecture v2

- Actualizado: el 2026-10-02 15:32
- Rol de ejecución: diseño y revisión de skills de arquitectura .NET
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: ajustes documentales completados; validación operativa pendiente

## Resultado y alcance

Se creó una versión independiente en [v2/SKILL.md](../Proto/Skills/csharp-onion-architecture/v2/SKILL.md), con su [referencia propia](../Proto/Skills/csharp-onion-architecture/v2/references/decisiones-csharp.md). Conserva el identificador de la capacidad; `v2` identifica la revisión solicitada, no una segunda especialidad. Esta carpeta es el paquete alternativo completo y no necesita leer la versión anterior.

Se aplicaron los tres ajustes de la evaluación: entradas proporcionales a cada modalidad, recorridos explícitos y reducción del archivo principal. Las [fuentes y decisiones iniciales](revision_csharp_onion_architecture.md) siguen siendo el antecedente de la síntesis. No se modificaron los insumos, la versión anterior ni las reglas de Generator.

## Cambios y trazabilidad de reglas

| Regla o contenido anterior | Tratamiento en v2 | Motivo |
| :--- | :--- | :--- |
| Caso de uso obligatorio en Entradas | Sustituido por la tabla de entradas por modalidad. | Una consulta conceptual o revisión estructural puede resolverse sin un caso funcional. |
| Secuencia común de cinco pasos | Sustituida por recorridos de consulta, revisión, diseño, implementación y migración. | Impedir que revisar active implementación o una reorganización completa. |
| Modelar caso de uso, estados y reglas | Trasladado a referencia §2, con condición de diseño o implementación. | Conservar el método funcional donde es necesario, sin bloquear revisión estructural. |
| Errores, compatibilidad, invariantes y trazabilidad | Detalle trasladado a referencia §2; límites esenciales conservados en el archivo principal. | Evitar repetición y permitir lectura según el cambio. |
| Autenticación y autorización | Trasladado a referencia §4. | Aplicar el detalle cuando el caso afecte identidad o acceso. |
| Matriz de pruebas | Trasladada y ajustada en referencia §5. | Elegir comprobaciones por límite modificado, sin ejecutar una batería fija. |
| Ejemplo genérico de reserva | Sustituido por detección de DbContext en Application y contraste con composición válida. | Explicar una revisión estructural y su posible corrección con un resultado observable. |
| Salidas repetidas al final | Integradas en la tabla de modalidades. | Mantener una sola definición de la salida de cada recorrido. |
| Dependencias y tratamiento de faltantes | Consolidados en Verificación y cierre. | Conservar el control con menos repetición. |
| Selección de referencias | Precisada por sección y condición de consulta. | Evitar cargar decisiones ajenas al cambio. |

Los destinos mencionados existen y se comprobaron. No se retiraron las reglas de dirección de dependencias, composición, compatibilidad de sistemas existentes ni distinción entre análisis y ejecución.

## Comprobación documental

- Revisión estructural: la tabla admite objetivo y código o diseño accesible, sin caso de uso obligatorio; la referencia §5 proporciona un ejemplo coherente con ese recorrido.
- Consulta: admite una pregunta conceptual y entrega explicación o comparación sin exigir repositorio ni activar implementación.
- Implementación: requiere comportamiento esperado y contexto suficiente; el recorrido limita los cambios a las responsabilidades afectadas.
- Migración: diferencia planificación de ejecución y conserva comportamiento, compatibilidad y recuperación.
- Formato: nombre y descripción simples, longitudes, delimitadores y ausencia de marcadores incompletos comprobados con Python estándar.
- Referencias: el enlace local del paquete apunta a un archivo existente dentro de v2; los rótulos §1–5 corresponden a sus secciones.
- Conservación: los SHA-256 de los dos archivos originales coinciden con la revisión anterior.
- Tamaño: el archivo principal pasó de 9.133 a 5.847 caracteres, una reducción del 36 %. La referencia conserva el detalle condicional y las reglas trasladadas.

El validador estándar de skill-creator no estaba disponible por la falta de PyYAML detectada en la revisión inicial. La comprobación alternativa cubre el formato simple usado; no acredita un parser YAML general.

## Revisión identificada y límite de validación

| Archivo dentro de v2 | SHA-256 |
| :--- | :--- |
| `SKILL.md` | `44b15b48d6df1c89df9dddaa848631259f9a582934dd9e31f946c7a3b6ad7a97` |
| `references/decisiones-csharp.md` | `9750711a74576decf5ce05a9dab36d996ddc2ce396b58d4fc468e0d776f0befe` |

La revisión de los recorridos anteriores es documental, no una ejecución de casos con carga de la skill. Permanece pendiente probar esta revisión en un proyecto C# definido: detectar una dependencia indebida, corregirla y comprobar que se conserva el comportamiento. También debe verificarse que una referencia válida del Host para composición no produzca un falso positivo. No se afirma instalación, selección automática ni validación operativa.

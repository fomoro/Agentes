# Revisión del borrador csharp-onion-architecture

- Actualizado: el 2026-10-02 15:12
- Rol de ejecución: arquitectura de software .NET, síntesis de insumos y revisión de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: borrador creado; revisión documental realizada; validación operativa pendiente

## Alcance y criterio

La solicitud autoriza construir una skill de Onion Architecture en C# recuperando lo útil de todas las skills de `Input/Skills` y aplicando las reglas de Generator. Se revisaron 30 skills, dos variantes `SKILL-2.md` y tres plantillas: 35 archivos de contenido. `.gitkeep` es un marcador de carpeta y no aporta instrucciones.

El paquete está en [csharp-onion-architecture](../Proto/Skills/csharp-onion-architecture/SKILL.md). Contiene el método de trabajo y una [referencia de decisiones en C#](../Proto/Skills/csharp-onion-architecture/references/decisiones-csharp.md). Este registro conserva la evaluación de los insumos y no es una dependencia de ejecución de la skill.

Se aplicaron las [reglas de la fábrica](../Generator/.rules/Reglas_Operacion.md), la [especificación](../Generator/Agents/Skills/Especificaciones/especificacion_skills.md), el [proceso de creación](../Generator/Agents/Skills/Procesos/proceso_creacion_skill.md) y los criterios documentales del [proceso de validación](../Generator/Agents/Skills/Procesos/proceso_validacion_skill.md), por la instrucción expresa del usuario. Los últimos tres documentos conservan su estado de propuesta en revisión.

No existe `.agents/AGENTS_Scope.md` en la raíz. Se aplicó la gobernanza global suministrada y las reglas de Generator. La plantilla antigua en `Proto/Skills/_PLANTILLA_SKILL.md` aporta las cinco piezas iniciales, pero su calificación del método como «inquebrantable» no se trasladó: el contrato más específico exige un método proporcionado, dependencias, comprobación y límites.

## Decisión de empaquetado

- Estado: Propuesta.
- Decisión: crear una skill específica para Onion en C#, con un archivo de entrada y una referencia de decisiones condicionadas al proyecto.
- Motivo: `arquitectura-software` aporta estructura general; el insumo backend .NET exige Hexagonal y contiene restricciones de Cavipetrol. Ninguno cubre por sí solo el método solicitado.
- Alternativas: extender la skill genérica ampliaría su alcance para todos sus consumidores; copiar la de backend trasladaría restricciones no confirmadas para otros proyectos.
- Riesgo y control: confundir una síntesis documental con una capacidad operativa. El paquete permanece en Proto y declara la validación pendiente.
- Siguiente acción: probar esta revisión en un proyecto C# y un mecanismo de carga definidos antes de promoverla para uso.

La autorización de creación está confirmada por el mensaje del usuario; no equivale a aprobación del diseño resultante ni a autorización de instalación en otro proyecto.

## Cobertura de los 30 insumos

Las rutas de la primera columna son relativas a `Input/Skills`. «Adaptado» significa que se conserva la intención aplicable a Onion y se delimita su alcance. Ningún archivo de origen se retiró o trasladó. Las reglas generales ya cubiertas por la gobernanza se conservan allí; no se presentan como nuevas reglas de esta skill.

| Insumo | Aporte y tratamiento | Destino en el borrador o motivo de exclusión |
| :--- | :--- | :--- |
| `agente_1_arquitecto_data_first` | Adaptados contratos de datos, SQL parametrizado y cambios controlados. | Referencia §3. No se heredan primacía absoluta de la base de datos, prohibición de migraciones EF, aprobación de todo DBML ni SP obligatorios: condicionan el proyecto y pueden contradecir el centro de Onion. |
| `agente_2_arquitecto_backend` | Adaptados separación del núcleo, puertos, adaptadores, controladores delgados y composición. | Método §3–4 y referencia §1–4. Se excluyen Cavipetrol, carpeta fija, .NET 8 obligatorio, cinco capas, EF solo para SP, JWT universal y veto a IdentityDbContext. El cambio a memoria por falla se reemplaza por selección explícita para pruebas/desarrollo. |
| `agente_3_disenador_poc` | Evaluadas reglas mobile-first, scroll, estética Apple, Bootstrap, HTML único e Ionic. | Fuera del alcance: diseño visual y prototipos. No aportan reglas internas de Onion. |
| `agente_4_desarrollador_angular` | Adaptadas compatibilidad de contratos y distinción entre API real y dobles. | Referencia §2–3. Se excluyen Angular/Ionic, versión, estilo de inyección, Signals/RxJS y scroll. Compatibilidad no implica copiar literalmente DTOs C# en TypeScript. |
| `agente_5_ux_writer` | Adaptada traducción de errores técnicos y términos comprensibles. | Método §4: códigos estables y traducción al canal. Tono, botones, estados vacíos y autoridad exclusiva sobre textos quedan fuera. |
| `agente_6_escritor_tecnico` | Adaptados ADR, fuentes vigentes y documentación proporcional. | Salida y cierre. No se heredan catálogo fijo de archivos, propiedad exclusiva de diagramas ni obligación de una plantilla vacía. |
| `analisis-funcional-conversacional` | Adaptados escenarios, reglas, transiciones y evidencia; revisadas ambas versiones. | Método §1–2 y comprobaciones. Se excluyen recorridos de WhatsApp, rutas Frisby, capturas, datos reales obligatorios y reproducción de marcas. La evidencia distingue lo observado de lo supuesto. |
| `arquitectura-integraciones` | Adaptados contratos, idempotencia, errores, timeouts y compatibilidad. | Referencia §4 y comprobaciones de adaptadores. Las decisiones particulares de plataforma se resuelven en el proyecto. |
| `arquitectura-software` | Incorporados cohesión, dependencias internas, separación de responsabilidades y transición. | Método §1–3, referencia §1 y §5. Los principios generales no se duplican como un catálogo. |
| `arquitectura-software-pipe` | Adaptados estados, eventos, guardas e identificadores estables. | Método §2 y referencia §4. Se excluyen motor conversacional obligatorio y prescripción universal de monolito. |
| `arquitectura-soluciones` | Adaptadas restricciones de solución y profundidad proporcional. | Método §1, entradas y salida por modalidad. El diseño completo de todos los dominios queda fuera. |
| `arquitectura-soluciones-pipe` | Adaptada coherencia de límites entre responsabilidades. | Tabla del método §3. No se copian roles con autoridad de aprobación ni estructura de Pipe. |
| `backend-python-flask` | Adaptados endpoints delgados, configuración, errores, compatibilidad y pruebas; revisadas ambas versiones. | Método §4–5 y referencia §4–5. Se excluyen Python/Flask, Meta y obligación de consultar a un agente arquitecto. |
| `colombian-linguistics` | Evaluadas normalización dialectal, gastronomía, negaciones y modismos. | Fuera del alcance: lingüística y reglas de un dominio no solicitado. |
| `copywriting-ejecutivo` | Evaluadas claridad, hechos y estructura de decisiones. | Cubiertas por la gobernanza vigente. No se incorpora un método de comunicaciones dentro de Onion. |
| `copywriting-pipe` | Adaptada independencia entre significado funcional y texto. | Método §2 y §4. Voz de marca, mensajes, preguntas y emojis quedan fuera. |
| `datos-persistencia` | Incorporados invariantes, identidad, transacciones, concurrencia, compatibilidad y conservación. | Método §2 y referencia §3. No se impone tecnología. |
| `datos-persistencia-pipe` | Adaptados separación de estado temporal y auditoría, idempotencia y migración. | Referencia §3–4. Se excluyen entidades de restaurantes, SQLite y SQLAlchemy como punto de partida. |
| `diseno-poc-pipe` | Evaluadas interfaz, Bootstrap, estados visuales y datos demostrativos. | Fuera del alcance visual; se conserva en las comprobaciones la distinción entre pruebas con dobles y evidencia del sistema real, sin copiar el método UI. |
| `escritura-tecnica` | Adaptados documentación desde fuentes y referencias verificables. | Salida y cierre. No se adopta la plantilla README con secciones repetidas ni se añade un catálogo documental. |
| `escritura-tecnica-pipe` | Incorporada trazabilidad caso de uso–contrato–componente–prueba. | Método §2. Se excluyen denominaciones y plantilla de Pipe. |
| `gestion-iniciativas` | Adaptada secuencia por resultados para migraciones. | Referencia §5. Roadmap, fechas, inversión y PMO quedan fuera; sus criterios generales permanecen en gobernanza. |
| `gestion-pmo-pipe` | Evaluados hitos, riesgos y etapas de Pipe. | No se fuerza POC/MVP/piloto ni estructura de responsables. La transición incremental está cubierta en referencia §5. |
| `integracion-meta-whatsapp` | Adaptados normalización en el borde, idempotencia y aislamiento de payloads. | Método §4 y referencia §4. Se excluyen Graph API, plantillas, ventanas y configuración específica de Meta. |
| `product-architecture` | Adaptados núcleo independiente del canal y contratos internos explícitos. | Método §2–3. Se excluyen NLU, cuatro capas de chatbot, integración POS y secuencia de madurez obligatoria. |
| `prototipado-ui` | Evaluados prototipo, navegación, accesibilidad y estados. | Fuera del método Onion. Las pruebas con demostraciones no acreditan integración real, conforme al cierre. |
| `restaurant-cx` | Evaluados intenciones, pedido, contención y escalamiento humano. | Fuera del alcance: reglas funcionales específicas de restaurantes, no invariantes universales de una arquitectura. |
| `spacy-nlu-expert` | Evaluados pipelines, componentes, modelo, entrenamiento y salida NLU. | Fuera del alcance tecnológico y funcional. No se introduce Python ni NLU como dependencia de C#. |
| `ux-writing` | Adaptadas terminología de dominio y traducción segura de errores. | Método §2 y §4. Redacción de pantallas y navegación queda fuera. |
| `ux-writing-pipe` | Adaptada separación entre estado funcional, texto y evento técnico. | Método §2 y referencia §4. No se heredan dashboards ni mensajes de Pipe. |

## Variantes, plantillas y contradicciones

- `analisis-funcional-conversacional/SKILL-2.md` es más general que `SKILL.md`; se contrastaron ambos sin declarar uno canónico. Se recuperaron escenarios y trazabilidad, sin rutas ni operación externa.
- `backend-python-flask/SKILL-2.md` conserva particularidades de Pipe. Se recuperaron compatibilidad, aislamiento y pruebas sin asumir vigencia superior por el nombre del archivo.
- `agente_6_escritor_tecnico/templates/README_TEMPLATE.md` contiene solo una indicación para completar: no proporciona una estructura utilizable.
- `escritura-tecnica/templates/README_TEMPLATE.md` repite Alcance y combina dos estructuras. No se copió esa duplicación.
- `escritura-tecnica-pipe/templates/README_TEMPLATE.md` es específica de Pipe. No se necesita una plantilla README para ejecutar esta skill.
- Onion y Hexagonal comparten aislamiento de infraestructura; la nueva skill adopta explícitamente Onion. El número de capas del insumo no se convirtió en requisito.
- Data-First obligatorio y dominio subordinado al esquema no se trasladaron. Se admite una base heredada mediante adaptadores y se registra cualquier dependencia de negocio residual.
- La conmutación automática a memoria no garantiza resiliencia de datos: se restringió a entornos explícitos de prueba/desarrollo.
- Seguridad, tono, autorizaciones y autoridad de roles se rigen por la gobernanza efectiva. No se importaron credenciales personales, poderes de aprobación ni pausas obligatorias ajenas a ella.

## Revisión documental

| Criterio | Resultado |
| :--- | :--- |
| Propósito, activación y exclusiones | Cubiertos en frontmatter y alcance; C# por sí solo no activa la skill. |
| Entradas y dependencias | Distingue análisis de ejecución; faltantes indispensables limitan solo la parte afectada. |
| Método y resultado | Incluye diseño, implementación, revisión y transición; salidas proporcionadas a cada modalidad. |
| Reglas específicas | Dependencias, composición, puertos, modelo, datos, integración y pruebas cuentan con tratamiento explícito. |
| Coherencia | Ningún proveedor, framework opcional o número de proyectos se impone como requisito de Onion. |
| Cobertura de fuentes | 30 skills, dos variantes y tres plantillas leídas; inclusiones, adaptaciones y exclusiones registradas. |
| Separación de fábrica y destino | Paquete en Proto; evaluación en Reviews; insumos y reglas de Generator conservados. |
| Funcionamiento | No comprobado. No se ha instalado ni ejecutado el paquete en un proyecto destino. |

## Casos preparados para validación operativa

Estos son criterios de prueba, no resultados observados de ejecución. Todos permanecen pendientes hasta definir proyecto, runtime y mecanismo de carga; las solicitudes deben ejecutarse sobre una revisión identificada del paquete.

| Caso | Solicitud representativa | Resultado esperado | Estado |
| :--- | :--- | :--- | :--- |
| Activación y diseño | Diseña Onion en C# para un caso de reserva con reglas y entorno suministrados. | Selección registrada de la skill, dominio independiente, contratos y dependencias explícitos. | Pendiente |
| No activación | Corrige el texto de un botón Angular. | No aplica el método Onion ni reorganiza C#. | Pendiente |
| Entrada incompleta | Implementa reservas sin definir cuándo se permiten o rechazan. | Solicita la regla que cambia el resultado y avanza solo con lo independiente. | Pendiente |
| Dependencia ausente | Valida la compilación de una solución cuyo SDK no está disponible. | Identifica la limitación; no afirma compilación ni instala por su cuenta. | Pendiente |
| Composición | Revisa un Host que referencia Infrastructure únicamente para registrar servicios. | Distingue composición de una dependencia ilícita del núcleo o de un endpoint. | Pendiente |
| Violación del núcleo | Application recibe DbContext o IActionResult. | Detecta el acoplamiento y propone un puerto o resultado interno apropiado. | Pendiente |
| Persistencia heredada | Migra gradualmente un flujo con SP sin cambiar su comportamiento. | Conserva contratos, prueba equivalencia y declara reglas aún dependientes del SQL. | Pendiente |
| Fallo del proveedor | Se cae SQL Server y existe un adaptador en memoria para pruebas. | No conmuta silenciosamente a memoria; aplica el tratamiento de falla confirmado. | Pendiente |
| Resultado integral | Implementa un caso completo en una solución de prueba disponible. | Compila, comprueba comportamiento y límites, y entrega evidencia verificable. | Pendiente |

## Cierre de creación

Se completó el borrador solicitado y su revisión documental. Su portabilidad, carga automática, compilación de soluciones producidas y comportamiento en un proyecto C# no están acreditados. No se requiere instalarlo ni exportarlo para cerrar la creación de acuerdo con Generator.

La comprobación automática del formato y la identificación de revisión se registran a continuación.

## Comprobación automática y revisión identificada

- Resultado: metadatos simples, nombre, longitud, marcadores, firma, enlaces locales y cobertura de insumos comprobados con Python estándar.
- Cobertura: 30 skills y 35 archivos de contenido; 7 enlaces locales resueltos.
- El validador `quick_validate.py` de skill-creator se intentó ejecutar y falló antes de validar porque el runtime no tiene PyYAML. Se aplicó una comprobación equivalente para los dos escalares simples presentes en este frontmatter; no acredita un parser YAML general ni comportamiento de la skill.
- No se ejecutaron los casos operativos anteriores. La revisión de contenido no prueba selección automática ni implementación funcional en C#.

| Archivo del paquete | SHA-256 |
| :--- | :--- |
| `Proto/Skills/csharp-onion-architecture/SKILL.md` | `013add1bb1ceaa9bee2056d38728456d2580ac03bbf681e424749d1b15dc52d0` |
| `Proto/Skills/csharp-onion-architecture/references/decisiones-csharp.md` | `888fd1dce3989642a8932b5614212b44c14941002dc9316728a887912c693f5b` |

Huella conjunta de insumos: `1fef5fd74f9ba60f224a1fc32060e437b9ba96b5f7386938515180a88b235477`. Se obtiene ordenando las rutas Markdown con `pathlib`, concatenando ruta relativa y SHA-256 de cada archivo con `:` y un salto de línea entre entradas, y calculando SHA-256 del texto UTF-8.

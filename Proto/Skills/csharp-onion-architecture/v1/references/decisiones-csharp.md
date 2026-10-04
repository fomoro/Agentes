# Decisiones de implementación de Onion en C#

- Actualizado: el 2026-10-02 15:12
- Rol de ejecución: arquitectura de software .NET
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: referencia del borrador; validación operativa pendiente

Consulta las secciones que correspondan al trabajo. Las convenciones de esta guía son propuestas de implementación; los contratos y restricciones confirmados del proyecto determinan su aplicación.

## 1. Estructura y composición

Una solución puede separar Domain, Application, Infrastructure y un Host web, de consola o de procesamiento. Dentro de cada responsabilidad, organiza por capacidades del negocio cuando eso mejore la cohesión. No generes carpetas vacías ni una interfaz por clase para reproducir un diagrama.

El Host puede referenciar Infrastructure para registrar implementaciones. Si el proyecto web también contiene endpoints, esa referencia no habilita el uso de adaptadores concretos desde ellos. En esa situación, revisa usos de tipos o pruebas arquitectónicas además de las referencias entre proyectos.

Los servicios de dominio expresan reglas que no encajan en una entidad u objeto de valor; los de aplicación coordinan un caso de uso. Evita clases denominadas `Service`, `Manager` o `Common` que agrupen responsabilidades inconexas. Un componente compartido necesita un propósito, consumidores y propietario claros.

Consulta la versión declarada en los proyectos y, si existe, `global.json`. No presupongas .NET 8 ni actualices la plataforma como efecto secundario de adoptar Onion.

## 2. Contratos y modelo

Una interfaz pertenece al consumidor interno que necesita la capacidad. Un contrato de carga de agregados puede pertenecer al dominio si expresa una necesidad de ese modelo; una consulta, notificación o reloj requerido para coordinar un caso de uso suele pertenecer a Application. Define solo operaciones que tengan consumidores reales.

Evita `IQueryable`, conexiones, tipos del ORM y expresiones específicas del proveedor en puertos del núcleo. Para consultas, devuelve resultados materializados o contratos de paginación independientes del proveedor. No crees un repositorio genérico que obligue al negocio a hablar en CRUD cuando sus operaciones tienen otro significado.

Un DTO de transporte atiende al consumidor externo; un contrato de aplicación atiende al caso de uso. Reutiliza una forma simple solo si no introduce dependencia del transporte ni compromete su evolución. No serialices entidades de dominio como contrato público por comodidad. Usa records para datos cuando su semántica de valor sea adecuada; no los impongas a entidades con identidad y ciclo de vida.

Si el negocio tiene poco comportamiento, mantén su modelo simple. No introduzcas agregados, eventos de dominio, CQRS, MediatR, AutoMapper o un bus sin una necesidad del alcance. Conserva los patrones ya adoptados cuando sean compatibles con los límites definidos.

## 3. Persistencia y compatibilidad

| Situación | Decisión operativa |
| :--- | :--- |
| EF Core ya adoptado | Mantén contexto, configuración de mapeo y migraciones en Infrastructure. Evita que entidades necesiten APIs del ORM para ejecutar reglas. |
| SQL o procedimientos almacenados existentes | Implementa el adaptador contra su contrato, parametriza las operaciones y mapea sus resultados. No copies el esquema físico como modelo de negocio sin revisar sus diferencias. |
| Reglas heredadas dentro de SQL | Conserva su comportamiento mientras se evalúa la transición. Registra la dependencia residual y prueba equivalencia antes de trasladarlas; no declares independencia completa durante esa etapa. |
| Elección de migraciones | Respeta el mecanismo vigente: migraciones del ORM o scripts versionados. Verifica compatibilidad y recuperación; usar `IF EXISTS` por sí solo no demuestra seguridad ni idempotencia. |
| Escritura de un caso de uso | Define la unidad transaccional necesaria. El caso de uso decide qué debe ser atómico; el adaptador implementa la transacción. No expongas la conexión al núcleo. |
| Cambios concurrentes | Define detección y respuesta al conflicto conforme al negocio. Comprueba el mecanismo con el proveedor relevante. |
| Dobles o proveedor en memoria | Úsalos de forma explícita en desarrollo o pruebas. Una falla de la base de datos no autoriza cambiar silenciosamente a datos en memoria. |

Mantén diferenciados datos de negocio, estado temporal, configuración y auditoría. Especifica información mínima, conservación y tratamiento de datos sensibles cuando el cambio afecte su persistencia o diagnóstico.

## 4. Integraciones y operación

Normaliza HTTP, mensajes o webhooks en el adaptador de entrada y traduce las respuestas en el de salida. Los identificadores de un canal no sustituyen la identidad del negocio; los textos visibles no determinan transiciones.

Si una operación puede repetirse, define la clave, el alcance y la persistencia de la idempotencia. Comprueba qué sucede con duplicados concurrentes y fallos entre la escritura local y el efecto externo. Usa outbox, compensación u otro mecanismo solo si esa garantía lo requiere; no presupongas una transacción distribuida.

Para llamadas externas, define timeout, cancelación y manejo de fallos. Reintenta solo operaciones seguras de repetir o protegidas con idempotencia. Propaga cancelación por las operaciones asíncronas pertinentes y respeta los ciclos de vida de las dependencias; no uses un contexto de datos compartido concurrentemente.

Mantén secretos y configuración operativa en los mecanismos del entorno. Valida la configuración obligatoria antes de atender operaciones que dependan de ella. Registra información suficiente para correlacionar fallos sin filtrar credenciales ni payloads sensibles.

El esquema de autenticación, los endpoints públicos y las políticas de autorización son decisiones del proyecto. Onion no exige JWT para toda ruta ni prohíbe un componente de identidad por su nombre. Conserva `ApiResponse`, Problem Details u otro contrato existente salvo decisión autorizada de cambio.

## 5. Migración y pruebas

Antes de reorganizar código existente, identifica un flujo representativo y caracteriza su comportamiento observable. Extrae reglas y contratos internos, adapta la infraestructura y cambia el ensamblaje por incrementos comprobables. No mezcles en el mismo paso una migración arquitectónica con cambios de reglas, proveedor y contrato público salvo necesidad explícita.

Define una recuperación basada en recursos disponibles: revisión anterior del código, compatibilidad temporal del contrato o estrategia verificada para los datos. Un cambio de código reversible no garantiza que lo sean sus migraciones de datos.

Ejemplo orientativo de revisión de un caso de uso:

- Una solicitud de reserva se traduce en Presentation a una entrada del caso de uso.
- Application coordina la carga y persistencia mediante puertos; Domain decide si la reserva cumple sus invariantes.
- Infrastructure implementa esos puertos y la atomicidad requerida.
- Las pruebas de dominio comprueban reglas válidas e inválidas; las de aplicación, la coordinación y los fallos; las de integración, el almacenamiento y los conflictos pertinentes.

El ejemplo no define requisitos de un proyecto real. No añade archivos ni pruebas cuando no contribuyan al cambio o a un control obligatorio.

## 6. Fundamento consultado

- [Jeffrey Palermo: The Onion Architecture, part 1](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/): fundamento de dependencias hacia el centro, dominio central e infraestructura externa. También distingue el contexto de aplicación del patrón.
- [Microsoft Learn: Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures): referencia complementaria sobre inversión de dependencias, núcleo de aplicación, Infrastructure y composition root en .NET. Usa la denominación Clean Architecture; no determina por sí sola una equivalencia completa entre patrones ni una cantidad obligatoria de capas.

Consultadas el 2026-10-02. El resto de las decisiones operativas sintetiza los insumos del usuario y criterio de diseño; no se atribuye a estas fuentes una validación de todo el paquete.

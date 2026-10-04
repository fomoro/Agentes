---
name: csharp-onion-architecture
description: Diseña, implementa, revisa o migra aplicaciones C# a Onion Architecture cuando el usuario la solicita o el proyecto ya la adopta. Define responsabilidades, dependencias hacia el dominio, contratos y pruebas. No se activa por cualquier cambio en C#, ni para UI visual, redacción, PMO o integraciones sin impacto en estos límites.
---

# Onion Architecture en C#

- Actualizado: el 2026-10-02 15:12
- Rol de ejecución: arquitectura de software .NET y diseño de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: borrador para revisión; validación operativa pendiente

## Propósito y alcance

Aplicar Onion a una aplicación C# con un dominio independiente del transporte y de la persistencia, casos de uso explícitos y adaptadores comprobables. Trabaja sobre el diseño, la implementación, la revisión o la migración solicitada; una consulta conceptual produce una explicación o propuesta, sin modificar el proyecto.

Usa esta skill cuando Onion sea parte del encargo o una decisión vigente del proyecto. Si se comparan arquitecturas, evalúa su ajuste y costo sin dar por aprobada su adopción. No convierte automáticamente un backend en microservicios ni impone un número de proyectos.

## Entradas y dependencias

Necesita el objetivo, la modalidad de trabajo y al menos un caso de uso con su comportamiento esperado. Para modificar código, necesita además acceso al proyecto y sus restricciones vigentes.

Obtén del repositorio, cuando existan: solución y proyectos, versión de .NET/C#, contratos públicos, modelo de dominio, persistencia, composición de dependencias, pruebas y decisiones de arquitectura. Pregunta solo por información indispensable que no pueda inferirse de esas fuentes; continúa las partes independientes.

- El diseño y la revisión documental requieren lectura de los insumos; no requieren un SDK ni una base de datos.
- Compilar y ejecutar pruebas requieren un SDK compatible con el proyecto, sus dependencias restaurables y los recursos de las pruebas.
- Las pruebas de integración pueden necesitar el proveedor de datos, servicios de prueba y configuración del entorno. Los dobles de prueba no acreditan compatibilidad con esos recursos.
- Ningún ORM, mediador, biblioteca de mapeo o herramienta de pruebas arquitectónicas es obligatorio por esta skill. Usa las dependencias adoptadas y justifica las nuevas por una necesidad concreta.

Si falta una dependencia de ejecución, completa el análisis posible y declara la comprobación pendiente. Si una decisión funcional cambia el contrato o las invariantes, solicita esa definición antes de implementar la parte afectada.

## Método

### 1. Reconocer el estado y elegir la modalidad

Identifica los límites del cambio y el comportamiento que se debe conservar. Distingue una aplicación nueva de una migración y registra las restricciones de datos, consumidores y despliegue que afecten la solución.

En una revisión, compara el código vigente con las reglas siguientes y entrega hallazgos con ubicación, efecto y corrección propuesta. En una implementación, trabaja solo sobre el cambio autorizado.

### 2. Modelar un caso de uso completo

Define entrada, actor, precondiciones, reglas de negocio, resultado y fallos esperados. Asigna las invariantes al dominio y la coordinación del flujo a Application. Si hay estados, explicita transiciones y condiciones válidas; usa identificadores de negocio estables en lugar de textos de UI o payloads del proveedor.

Define el dueño de cada contrato, su información mínima y su significado. Mantén trazabilidad entre el caso de uso, los componentes que lo realizan y las pruebas que comprueban sus reglas.

### 3. Diseñar los límites y dependencias

| Responsabilidad | Contenido | Dependencias internas admitidas |
| :--- | :--- | :--- |
| Domain | Entidades, objetos de valor, invariantes y comportamiento del negocio; servicios de dominio cuando sean necesarios. | Ninguna capa externa. |
| Application | Casos de uso, coordinación, contratos de entrada/salida y puertos requeridos por esos casos. | Domain. |
| Infrastructure | Persistencia, clientes externos y otras implementaciones de puertos. | Application y Domain según los contratos que implemente. |
| Presentation | Adaptación de HTTP, mensajería, consola o interfaz al caso de uso. | Application; tipos de Domain solo si el contrato lo justifica. |
| Host / composition root | Inicio, configuración y registro de implementaciones. Puede convivir en el proyecto de entrada. | Capas necesarias para ensamblar la aplicación. |

La tabla expresa responsabilidades lógicas. Define proyectos y carpetas según la estructura existente y el aislamiento que deba verificarse. Si varias responsabilidades comparten ensamblado, comprueba también los límites entre namespaces y tipos: las referencias de proyectos no bastan.

El núcleo no referencia Infrastructure ni Presentation. Coloca cada interfaz en la capa interna que necesita su contrato; reserva Domain para contratos propios del negocio y Application para necesidades de los casos de uso. Evita dependencias cíclicas, incluso transitivas.

Antes de fijar proyectos, contratos o paquetes, consulta [las decisiones de implementación en C#](references/decisiones-csharp.md). Úsala también para revisar persistencia, composición, integración y migración; sus ejemplos son orientativos.

### 4. Implementar desde el comportamiento

Implementa una porción funcional completa con sus reglas, caso de uso, adaptadores y comprobaciones. Mantén controladores y handlers de entrada delgados: traducen, validan el transporte, delegan y construyen la respuesta.

- Evita que `HttpContext`, `IActionResult`, entidades del proveedor, `DbContext` o payloads externos formen parte de contratos del núcleo.
- Traduce modelos externos a contratos internos en el adaptador; conserva compatibilidad de nombres, tipos, nulabilidad y errores cuando haya consumidores existentes.
- Conserva las invariantes dentro del modelo de dominio, aunque haya validaciones equivalentes de entrada o restricciones en la base de datos.
- Usa inyección explícita de dependencias; concentra el registro de implementaciones en la composición. No resuelvas servicios dinámicamente desde las reglas de negocio.
- Separa errores funcionales de fallos técnicos. Traduce ambos al contrato del canal sin exponer detalles internos; los códigos funcionales no dependen del texto mostrado al usuario.
- Aplica autenticación en el límite correspondiente y autorización al recurso o caso de uso; una identidad o permiso necesario para decidir se representa mediante un contrato interno, sin acoplar el núcleo al framework web.

Para SQL existente, proveedores alternativos, transacciones, concurrencia, idempotencia y llamadas externas, aplica solo las decisiones pertinentes de la referencia.

### 5. Comprobar según el resultado solicitado

En diseño, revisa responsabilidades, contratos y dirección de dependencias sin afirmar compilación. En código, ejecuta las verificaciones disponibles que cubran el cambio y los controles exigidos por el proyecto.

| Comprobación | Evidencia esperada |
| :--- | :--- |
| Dependencias | Referencias de proyectos, paquetes y usos de tipos sin ciclos ni acoplamientos externos del núcleo. La excepción del Host se limita a composición. |
| Dominio | Pruebas de invariantes, estados y límites relevantes sin base de datos ni servidor web. |
| Aplicación | Caso de uso comprobado con dobles de sus puertos, incluidos los fallos que cambian el resultado. |
| Adaptadores | Pruebas de integración sobre el proveedor o protocolo relevante, cuando el cambio afecte ese límite. |
| Contratos | Entradas, salidas, errores y compatibilidad con consumidores comprobados en el alcance modificado. |
| Composición | Construcción y resolución de dependencias y ejecución del flujo afectado, cuando exista un Host ejecutable. |

Una compilación correcta no demuestra independencia arquitectónica. Las pruebas con datos en memoria no sustituyen las del proveedor real cuando importan transacciones, consultas o concurrencia.

## Salida y cierre

Entrega en la ubicación definida por el proyecto y ajusta el contenido a la modalidad:

- **Diseño:** mapa de responsabilidades, dependencias, contratos, decisiones pendientes y estrategia de comprobación.
- **Implementación:** código coherente con el cambio y evidencia de las verificaciones ejecutadas.
- **Revisión:** hallazgos priorizados, archivos afectados, efecto y corrección propuesta.
- **Migración:** secuencia incremental, compatibilidad, recuperación viable y resultado de cada paso ejecutado.

Actualiza el registro de arquitectura existente cuando cambien decisiones estructurales; utiliza un ADR para las decisiones que lo requieran. Documenta solo lo necesario para operar, mantener o revisar el resultado y enlaza las fuentes vigentes.

El cierre identifica el caso de uso cubierto, las decisiones adoptadas dentro de la autorización, los controles ejecutados y los pendientes con su efecto. No declara cumplimiento de Onion si persisten dependencias externas del núcleo: registra la desviación y su tratamiento.

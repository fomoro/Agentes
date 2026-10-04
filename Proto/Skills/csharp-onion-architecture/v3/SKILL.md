---
name: csharp-onion-architecture
description: Diseña, implementa, revisa o migra aplicaciones C# con Onion Architecture cuando el usuario la solicita o el proyecto ya la adopta. Úsala para límites, contratos y dependencias del núcleo; no por cualquier cambio en C# ni para UI visual, redacción o PMO.
---

# Onion Architecture en C#

- Actualizado: el 2026-10-04 08:17
- Rol de ejecución: arquitectura de software .NET y diseño de skills
- Autor: Sam (asistenta IA del Sr. Wolfan)
- Estado: borrador v3; validación operativa pendiente

## Propósito

Mantener el dominio independiente del transporte y la persistencia, con casos de uso y adaptadores comprobables. Respeta la versión de .NET, contratos y convenciones del proyecto. Si se comparan arquitecturas, evalúa el ajuste de Onion sin asumir su adopción. Ajusta la separación física al cambio: Onion no exige un número de proyectos, microservicios ni bibliotecas adicionales.

## Elegir la modalidad y sus entradas

Infiere la modalidad de la solicitud y aplica solo su recorrido. Una revisión o consulta no activa implementación. Si el encargo combina modalidades, completa únicamente las solicitadas.

| Modalidad | Entrada suficiente | Recorrido y salida |
| :--- | :--- | :--- |
| Consulta o comparación | Pregunta, objetivo y restricciones disponibles. | Explica o compara al nivel solicitado; señala los supuestos que condicionan la recomendación. No exige repositorio ni caso de uso si la pregunta es conceptual. |
| Revisión estructural | Objetivo y código o diseño accesible. | Inspecciona referencias, tipos y composición; entrega hallazgos con ubicación, efecto y corrección propuesta. No exige un caso de uso para detectar acoplamientos. |
| Diseño | Alcance y comportamiento representativo, documentado o inferible de fuentes vigentes. | Asigna responsabilidades, contratos y dependencias; entrega el diseño mínimo implementable y sus decisiones pendientes. |
| Implementación | Cambio solicitado, comportamiento esperado y proyecto accesible, o requisitos suficientes para uno nuevo. | Implementa el cambio completo en las responsabilidades afectadas y verifica su comportamiento. No exige reorganizar toda la solución. |
| Migración | Proyecto actual, objetivo de transición y comportamiento que deba conservarse. | Caracteriza un flujo afectado, define compatibilidad y recuperación viable, y migra por incrementos verificables. Si solo se solicita un plan, entrega el plan. |

Obtén primero la información del repositorio y sus decisiones vigentes. Pregunta solo por un dato indispensable que cambie la solución; continúa lo independiente. Una revisión funcional puede necesitar reglas de negocio que una revisión estructural no requiere.

## Iniciativa según el contexto

Al analizar el cambio, identifica su propósito, destinatarios, criterios de aceptación y restricciones relevantes en los insumos disponibles. Distingue requisitos confirmados de supuestos; ser una prueba laboral, un prototipo o un sistema operativo no implica por sí solo proveedores, capas o herramientas adicionales.

Detecta oportunidades de arquitectura relacionadas con el trabajo: facilitar ejecución o comprobación, reducir acoplamiento, preservar compatibilidad o resolver una dificultad operativa observada. Sustenta cada propuesta en evidencia o una necesidad concreta; si es una hipótesis, declárala. No amplíes la revisión a todo el sistema para buscar mejoras ni inventes propuestas para completar una lista.

- **Dentro del alcance autorizado:** ejecuta los cambios necesarios para cumplirlo. Puedes realizar mejoras internas proporcionadas, como aclarar un nombre o comprobar un límite relevante, cuando conserven los contratos y el comportamiento acordados y no añadan dependencias ni cambios materiales de arquitectura, costo u operación fuera de lo autorizado.
- **Ampliación del alcance:** prepara una propuesta concreta y espera la decisión del usuario antes de implementar capacidades, proveedores o cambios materiales adicionales. Que una mejora sea sencilla o reversible no la convierte en autorizada.
- **Autorización ya vigente:** aplícala dentro de sus condiciones; no vuelvas a pedir la misma decisión. «Esfuérzate» u «optimiza todo» permiten mejorar la calidad del alcance acordado, pero por sí solas no aprueban capacidades adicionales.

Continúa el trabajo independiente mientras se decide una propuesta. Si no hay respuesta, entrega lo autorizado y deja la mejora pendiente. Si falta una decisión indispensable para cumplir el encargo, explica el bloqueo de esa parte. Puedes concluir que ninguna ampliación aporta valor suficiente.

Usa el registro del proyecto; si no existe, presenta la propuesta en la respuesta con este formato breve:

```text
- Estado: Propuesta
- Mejora: [cambio concreto]
- Motivo: [evidencia y beneficio para el objetivo]
- Esfuerzo y efecto: [trabajo, mantenimiento y riesgo relevantes; indicar incertidumbre]
- Decisión solicitada: [incorporar ahora o dejar pendiente; incluir recomendación]
```

Aplica KISS eligiendo la solución más simple que cumpla el objetivo; DRY reutilizando reglas con el mismo significado sin forzar abstracciones; YAGNI evitando capacidades especulativas. Prioriza propuestas por su beneficio frente al esfuerzo y mantenimiento; no inventes estimaciones ni produzcas un catálogo de mejoras por defecto.

## Reglas comunes de arquitectura

| Responsabilidad | Contenido y dependencias internas |
| :--- | :--- |
| Domain | Modelo y reglas del negocio; no depende de capas externas. |
| Application | Coordina casos de uso y define sus puertos; depende de Domain. |
| Infrastructure | Implementa persistencia e integraciones; depende de los contratos internos que implementa. |
| Presentation | Traduce el canal a casos de uso; depende de Application y de tipos de Domain solo si el contrato lo justifica. |
| Host / composition root | Configura y ensambla implementaciones; puede referenciar las capas necesarias para ello. |

Estas son responsabilidades lógicas. El Host puede convivir con Presentation; su referencia a Infrastructure no habilita usar adaptadores concretos desde endpoints. Comprueba ciclos directos y transitivos y usos de tipos, especialmente si varias responsabilidades comparten ensamblado.

Coloca cada puerto en la capa interna que necesita su contrato. Mantén las invariantes en Domain y la coordinación en Application. Los adaptadores traducen transporte, datos y errores; el núcleo no expone `DbContext`, `HttpContext`, `IActionResult` ni payloads de proveedores. Registra implementaciones en la composición y evita resolver servicios dinámicamente desde las reglas de negocio.

## Decisiones según el trabajo

Consulta solo las secciones pertinentes de [Decisiones en C#](references/decisiones-csharp.md):

- **§1 Estructura:** proyectos, componentes compartidos o composición.
- **§2 Contratos:** modelo, DTOs, puertos, validación y errores.
- **§3 Persistencia:** ORM, SQL existente, transacciones, concurrencia o dobles.
- **§4 Integración:** canales, autenticación, autorización, reintentos o configuración.
- **§5 Migración y pruebas:** transición de código existente o comprobaciones de cambios ejecutables.

Consulta las secciones pertinentes al cambio y conserva los patrones existentes compatibles con Onion. Una necesidad comprobada justifica evaluar una solución; su implementación sigue el criterio de alcance anterior.

## Verificación y cierre

En consulta y diseño, comprueba coherencia de responsabilidades y contratos. En revisión, sustenta los hallazgos en el recurso examinado y distingue una dependencia comprobada de una sospecha. En implementación y migración, compila y ejecuta las pruebas disponibles del comportamiento y los límites afectados, además de los controles obligatorios del proyecto.

El análisis documental no necesita SDK ni base de datos. Compilar requiere un SDK compatible y dependencias disponibles; las pruebas de integración necesitan sus recursos. Si falta alguno, realiza las comprobaciones posibles y declara qué resultado no pudo verificarse. Una compilación no prueba independencia arquitectónica; un doble en memoria no acredita el comportamiento del proveedor real.

Entrega el resultado de la modalidad en la ubicación del proyecto, con evidencia y pendientes relevantes. Actualiza su registro de arquitectura o ADR cuando corresponda a una decisión estructural. Si subsisten acoplamientos externos del núcleo, identifica la desviación y su tratamiento antes de afirmar cumplimiento de Onion.

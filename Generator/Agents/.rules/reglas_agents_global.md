# Reglas para AGENTS.md global

- Actualizado: el 2026-09-24 20:19
- Rol de ejecución: arquitectura de gobernanza y mantenimiento documental
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: aprobado

## Objetivo

Definir las reglas propias del `AGENTS.md` global: configuración del asistente, relación con la gobernanza local y preferencias comunes. Complementa las reglas generales exportables; el contexto y las restricciones de cada proyecto se concretan en su Scope.

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Configuración canónica** | Definir identidad, autoría y rutas configurables una sola vez. Resolver las referencias entre claves hasta obtener valores literales; ante ciclos o datos requeridos inválidos, informar el error y detener únicamente la acción dependiente. | Propuesta del agente IA |
| **Precedencia y especialización** | Respetar la jerarquía efectiva de instrucciones y permisos. La gobernanza local puede especializar la global y sustituir preferencias generales, pero no eludir protecciones expresas sin autorización válida; las skills no amplían autorizaciones. | Propuesta del agente IA |
| **Conflictos de instrucciones** | Ante un conflicto, aplicar la instrucción de mayor autoridad y omitir la parte incompatible. Si impide ejecutar el método, evaluar una alternativa; si no puede resolverse, solicitar la decisión necesaria y continuar las acciones independientes. | Propuesta del agente IA |
| **Firma Automática** | Resolver `autor_entregables` desde la configuración canónica cuando corresponda una firma; usar el autor resuelto sin duplicar el nombre en reglas o plantillas. | Propuesta del agente IA |
| **Preferencias de comunicación** | Definir idioma, tono y nivel de detalle como preferencias configurables; adaptarlos al destinatario y al formato solicitado. No imponer un tono técnico a todos los entregables. | Propuesta del agente IA |

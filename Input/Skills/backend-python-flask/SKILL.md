---
name: backend-python-flask
description: Implementa y mantiene APIs y servicios en Python con Flask. Úsala al modificar endpoints, servicios, configuración, clientes HTTP o pruebas; no para decidir por sí sola reorganizaciones arquitectónicas amplias.
---

# Backend Python y Flask

Implementa el cambio acordado con código simple, cohesivo y verificable.

## Método

1. Lee la gobernanza, la arquitectura, los contratos y las pruebas vigentes del proyecto.
2. Identifica comportamiento esperado, compatibilidad requerida y límites del cambio.
3. Implementa la modificación en la responsabilidad correspondiente.
4. Añade o ajusta pruebas sobre el comportamiento afectado.
5. Ejecuta las verificaciones existentes del proyecto y reporta cualquier limitación.

## Reglas

- Mantén endpoints delgados: valida, normaliza, delega y responde.
- Separa transporte, casos de uso, reglas de negocio, integraciones y persistencia cuando tengan razones de cambio distintas.
- Usa guard clauses para entradas inválidas y evita estado global mutable.
- Obtén configuración y secretos desde mecanismos seguros del entorno.
- Define timeouts y manejo explícito de errores para dependencias externas.
- Preserva contratos y datos durante cambios incrementales, salvo ruptura aprobada.
- Escala al Arquitecto de Software cualquier cambio que altere módulos, dependencias o estructura general.

## Criterio de cierre

- El comportamiento solicitado está implementado sin ampliar el alcance.
- Las pruebas proporcionales al cambio pasan; si una verificación no puede ejecutarse, queda indicada con su riesgo.
- No se exponen secretos ni se rompen contratos sin decisión explícita.

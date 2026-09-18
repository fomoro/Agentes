---
name: arquitectura-integraciones
description: Diseña y evalúa APIs, eventos, webhooks, mensajería e interoperabilidad. Úsala para contratos, protocolos, autenticación, seguridad, versionamiento y manejo de fallos; no para definir módulos internos ni implementar el backend completo.
---

# Arquitectura de integraciones

Define interacciones verificables entre sistemas con contratos y controles proporcionales al impacto.

## Método

1. Confirma productores, consumidores, propósito, datos intercambiados y restricciones.
2. Selecciona el estilo de integración según latencia, acoplamiento, consistencia, volumen y operación requeridos.
3. Define contrato, protocolo, autenticación, autorización, versionamiento y compatibilidad.
4. Especifica validación, idempotencia, timeouts, reintentos, orden, duplicados y manejo de errores cuando apliquen.
5. Define trazabilidad, monitoreo, límites de consumo y tratamiento de datos sensibles.
6. Identifica pruebas de contrato y escenarios de fallo necesarios para validar la integración.

## Reglas

- No inventes endpoints, eventos, campos ni capacidades del proveedor.
- Valida contra documentación vigente cuando el contrato dependa de una plataforma externa.
- Evita reintentos automáticos en operaciones no idempotentes sin una estrategia explícita.
- Distingue responsabilidades del proveedor, transporte, interfaz y lógica de negocio.
- Registra una decisión cuando el protocolo o patrón tenga impacto transversal o sea difícil de revertir.

## Criterio de cierre

- Productor y consumidor comparten un contrato inequívoco y versionable.
- Seguridad, errores, recuperación y observabilidad están definidos al nivel requerido.
- Supuestos, dependencias externas y pruebas pendientes quedan explícitos.

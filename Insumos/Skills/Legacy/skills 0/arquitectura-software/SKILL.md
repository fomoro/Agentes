---
name: arquitectura-software
description: Diseña módulos, dependencias internas, patrones y estructura de repositorio. Úsala ante decisiones estructurales o preparación de una implementación relevante; no para administrar el roadmap ni definir contratos externos.
---

# Arquitectura de software

Diseña una estructura técnica simple, cohesiva y verificable a partir del alcance confirmado.

## Método

1. Identifica responsabilidades, restricciones, atributos de calidad y decisiones pendientes.
2. Define módulos por cohesión funcional y límites de cambio.
3. Establece contratos internos y una dirección explícita de dependencias.
4. Selecciona el patrón y la unidad de despliegue más simples que satisfagan el riesgo y la escala conocidos.
5. Propón la transición desde la estructura actual, preservando compatibilidad cuando aplique.
6. Registra un ADR solo para decisiones estructurales, transversales o difíciles de revertir.

## Reglas

- Evita módulos genéricos sin cohesión, dependencias circulares y estado mutable compartido.
- Separa reglas de negocio de adaptadores, infraestructura y configuración cuando exista una razón de cambio distinta.
- No introduzcas capas, servicios o frameworks sin un problema confirmado que los justifique.
- Antes de una reorganización amplia, presenta impacto, rutas afectadas y estrategia de transición.

## Criterio de cierre

- Cada módulo tiene una responsabilidad y dependencias comprensibles.
- Las decisiones materiales incluyen alternativa, consecuencia y riesgo controlado.
- La estructura propuesta es implementable y no contradice contratos ni restricciones confirmadas.

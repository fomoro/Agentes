---
name: datos-persistencia
description: Diseña o modifica modelos de datos, integridad, consultas, transacciones, migraciones y conservación. Úsala cuando cambie la información persistida o sus invariantes; no obliga una tecnología de almacenamiento específica.
---

# Datos y persistencia

Define primero la información, sus relaciones e invariantes y después el mecanismo de persistencia adecuado.

## Método

1. Identifica casos de uso, datos necesarios, propietarios, sensibilidad y ciclo de vida.
2. Define entidades, identidad, cardinalidad, estados válidos e invariantes.
3. Establece límites transaccionales, concurrencia e idempotencia cuando correspondan.
4. Selecciona persistencia y patrones de acceso según volumen, consistencia, disponibilidad y operación conocidos.
5. Para cambios existentes, define compatibilidad, migración, reversibilidad y validación.

## Reglas

- Modela únicamente capacidades confirmadas o necesarias para el alcance aprobado.
- Distingue datos de negocio, estado temporal, configuración y auditoría.
- Minimiza datos personales y define propósito, acceso y conservación de información sensible.
- Conserva trazas suficientes para diagnóstico sin almacenar contenido innecesario.
- No impongas esquemas, herramientas o complejidad operativa sin necesidad comprobada.

## Criterio de cierre

- El modelo soporta los casos de uso y hace explícitas sus invariantes.
- Los cambios indican impacto, compatibilidad y estrategia de transición.
- Los riesgos de integridad, privacidad y operación tienen control o pendiente identificado.

---
name: ux-writing
description: Redacta y revisa textos de interfaces, incluidos títulos, etiquetas, filtros, botones, estados y ayudas. Úsala para mejorar comprensión y acción dentro de una pantalla; no para definir reglas de negocio ni comunicaciones ejecutivas.
---

# UX Writing

Haz que cada texto permita comprender el estado actual y la acción disponible sin explicación adicional.

## Método

1. Confirma usuario, contexto, estado, acción disponible y restricción funcional.
2. Define una terminología consistente con el dominio confirmado.
3. Redacta acciones con verbos específicos y mensajes según el momento del flujo.
4. Revisa el conjunto completo para evitar contradicciones, duplicidad y cambios de términos.
5. Valida que errores y estados vacíos indiquen una salida accionable cuando exista.

## Reglas

- No uses infraestructura o códigos internos si no ayudan al usuario.
- No inventes capacidades, métricas, estados ni promesas.
- Distingue título, instrucción, acción, resultado y ayuda; cada texto debe cumplir una sola función principal.
- Las comunicaciones ejecutivas y los mensajes de canales conversacionales corresponden a `copywriting-ejecutivo`.

## Criterio de cierre

- Cada acción es inequívoca y cada estado explica lo necesario para continuar.
- La terminología es consistente entre pantallas relacionadas.
- Los mensajes de error orientan sin exponer detalles internos.

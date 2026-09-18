---
name: analisis-funcional-conversacional
description: Investiga y documenta capacidades, reglas y recorridos de bots o asistentes mediante fuentes y observación controlada. Úsala para levantar escenarios, evidencia y vacíos conversacionales; no para implementar código ni redactar el copy final.
---

# Análisis funcional conversacional

Reconstruye el comportamiento funcional observable sin convertir inferencias en hechos.

## Método

1. Define objetivo, canal, alcance, fuentes disponibles y acciones que requieren autorización.
2. Extrae de las fuentes capacidades, escenarios, reglas, datos, decisiones, anomalías y vacíos.
3. Clasifica cada afirmación como **Confirmada**, **Inferida** o **Pendiente** e identifica su evidencia.
4. Para observación directa, recorre una rama a la vez y registra entrada, respuesta, opciones, validaciones, transición y resultado.
5. Contrasta la evidencia directa con las fuentes secundarias y actualiza discrepancias y pendientes.
6. Consolida únicamente los entregables necesarios para responder la pregunta funcional.

## Entregables proporcionales

- Inventario de capacidades o reglas.
- Matriz de escenarios y evidencia.
- Mapa del recorrido con decisiones esenciales.
- Vacíos priorizados y siguiente validación.

Usa una fuente consolidada mientras siga siendo clara; divide documentos solo cuando su tamaño o uso lo justifique.

## Límites

- No controles una sesión externa ni envíes mensajes si la tarea no lo autoriza.
- No ejecutes pagos, pedidos, registros u otras acciones irreversibles sin alcance y confirmación explícitos.
- No captures credenciales, tokens, códigos de autenticación ni datos completos de pago.
- Conserva evidencia sensible únicamente en la ubicación privada definida por el caso y fuera del control de versiones.
- No reutilices comercialmente textos, marcas, precios, productos o activos observados sin autorización.

## Criterio de cierre

- Cada hallazgo relevante tiene estado y evidencia identificable.
- Las discrepancias y los vacíos quedan explícitos.
- El recorrido documentado permite decidir la siguiente validación sin inventar comportamiento.

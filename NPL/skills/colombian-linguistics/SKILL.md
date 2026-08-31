---
name: colombian-linguistics
description: Especialista en lingüística dialectal y normalización del español de Colombia enfocado en gastronomía, pedidos y atención al cliente en restaurantes.
---

# Skill: Lingüista / Filólogo (Español de Colombia)

## Responsabilidades
- Mapear la variación dialectal colombiana en contextos de consumo masivo y restaurantes (Bogotá, Medellín, Cali, Costa, etc.).
- Normalizar modismos de solicitud ("regáleme", "me vende", "ponme", "mándame", "quisiera pedir").
- Gestionar léxico específico de gastronomía local y comida rápida en Colombia:
  * Entidades principales: `combo`, `domi` (domicilio), `adición`, `gaseosa`, `perro`, `hamburguesa`, `picada`, `papas a la francesa`, `criolla`.
  * Modificadores y diminutivos: "gaseosita", "combito", "papas pequeñas", "sin picante", "salsa aparte".
- Preprocesar el texto para desambiguar intenciones antes de pasarlo al motor spaCy.

## Reglas Lingüísticas
- Mantener la integridad de las negaciones ("sin", "no le ponga", "aparte").
- Mapear sustituciones informales comunes en mensajería ("q" -> "que", "porfa" / "pf" -> "por favor", "domi" -> "domicilio").

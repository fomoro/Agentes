# Instrucción común para pruebas de generación

Antes de generar, lee completo `C:\Dev\Agentes\Proto\Skills\drawio-diagrams\SKILL.md` y las referencias que indique para `colcomercio`; no dependas de lecturas anteriores. Aplica la skill y comprueba sus dependencias.

En `output/`, versiona según la base indicada por cada prueba: `base.drawio` cuenta como v1; reconoce también `base_vN.drawio` y `base vN.drawio`. Si no existe ninguna versión, empieza por v1. Guarda `base vN.drawio` con el número siguiente al mayor existente; comprueba otra vez que el destino esté libre antes de escribir y no sobrescribas archivos.

Valida el `.drawio` con la skill y comprueba el resultado visual si hay renderizador. Informa qué quedó sin comprobar; no des por resuelto un problema visual solo porque el XML sea válido.

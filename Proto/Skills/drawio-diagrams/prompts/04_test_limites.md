# Casos de límite — drawio-diagrams

## Objetivo

Comprobar selección y límites de la skill en un entorno de prueba identificado. Registrar por caso solicitud, respuesta, evidencia de carga, resultado y pendiente; no modificar el entorno real para provocar fallos.

| Caso | Solicitud de prueba | Resultado esperado |
| :--- | :--- | :--- |
| No activación | «Dame solo el código Mermaid de este flujo; no quiero un archivo Draw.io». | No activar `drawio-diagrams` ni generar `.drawio`. |
| Entrada incompleta | «Crea un `.drawio` de la integración, pero todavía no conozco sus sistemas ni conexiones». | Solicitar los datos indispensables o delimitar una parte independiente; no inventar sistemas. |
| Perfil inexistente | «Crea un `.drawio` con el perfil `marca-x`». | Pedir el perfil correcto; no sustituirlo por `default` sin avisar. |
| Dependencia ausente | Ejecutar una solicitud pertinente en un entorno aislado sin Python 3. | Informar que no puede ejecutar el motor; no afirmar generación ni validación. |

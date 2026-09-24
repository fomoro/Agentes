# Gobernanza de Generator

- Actualizado: el 2026-09-24 01:55
- Rol de ejecución: arquitectura de gobernanza y mantenimiento documental
- Autor: Sam (Asistente IA del Sr. Wolfan)

## Objetivo

Organizar las reglas con las que se construyen agentes y skills y las que podrán incorporarse a sus proyectos destino. Cada documento mantiene una responsabilidad propia; las tablas son propuestas de diseño, no archivos de gobernanza instalados.

## Documentos

| Recurso | Propósito | Estado |
| :--- | :--- | :--- |
| [Reglas de la Fábrica](Reglas_de_la_Fabrica/reglas_de_la_fabrica.md) | Operar Generator sin duplicar reglas generales. | Aprobado |
| [Reglas generales exportables](Reglas_Exportables/reglas_generales.md) | Reglas transversales para los proyectos generados. | Aprobado |
| [Reglas para AGENTS.md global](Reglas_Exportables/reglas_agents_global.md) | Reglas del archivo global. | Aprobado |
| [Reglas para AGENTS_Scope.md local](Reglas_Exportables/reglas_agents_local.md) | Reglas de `.agents/AGENTS_Scope.md`. | Aprobado |

Las reglas generales aportan la base reutilizable. Las del AGENTS global definen configuración y comportamiento común del asistente; las del Scope concretan el proyecto. Al preparar un entregable, seleccionar las reglas pertinentes y evitar repetirlas entre niveles. Las reglas de la fábrica se aplican al proceso de construcción.

## Incorporación de reglas

1. Leer la regla completa y el destino. Registrar regla, sección de origen, sección de destino y motivo; clasificar por el propósito de cada sección, no por su número.
2. Ajustar la regla al destino sin perder su intención. Registrar una fuente real cuando exista o «Propuesta del agente IA» cuando corresponda a una formulación propia.
3. Verificar ubicación, unicidad, contenido, referencias y formato de la tabla. Registrar en el cierre los traslados, las fusiones y las retiradas con sus motivos.

## Origen / referencia

- En todos los archivos de reglas, indicar la procedencia o el respaldo real: documento interno, fuente externa consultada o «Propuesta del agente IA». No atribuir a una fuente respaldo que no ofrece ni presentar una propuesta como aprobada.
- Usar etiquetas descriptivas para los enlaces y conservar su destino original. El nombre de un documento de origen no determina dónde debe incorporarse la regla.

Las referencias externas sirven como respaldo de criterios concretos; no hacen que estas reglas dependan de un proveedor ni acreditan su funcionamiento en todos los entornos.

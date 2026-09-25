# Reglas de gobernanza local

- Actualizado: el 2026-09-24 20:19
- Rol de ejecución: arquitectura de gobernanza y mantenimiento documental
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: aprobado

## Objetivo

Definir las reglas que concretan el proyecto en `.agents/AGENTS_Scope.md`: alcance, restricciones, resultados esperados y selección de capacidades locales. Especializa la gobernanza global sin duplicar su configuración ni ampliar permisos. La ruta y los mecanismos de carga se ajustan al entorno destino.

## Contexto y límites del proyecto

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Límites de Negocio** | Declarar en el Scope las restricciones y los criterios innegociables confirmados para el proyecto. No inventar valores ni convertir ejemplos en reglas del proyecto. | Propuesta del agente IA |
| **Alcance del proyecto** | Identificar propósito, exclusiones y ubicaciones de trabajo relevantes para orientar la ejecución. Distinguir el contexto confirmado de los datos todavía desconocidos. | Propuesta del agente IA |
| **Criterios de aceptación locales** | Definir el resultado esperado y cómo comprobarlo para cada entregable relevante. Asociarlo a una carpeta solo cuando su contenido tenga una responsabilidad diferenciada. | Propuesta del agente IA |
| **Responsabilidades locales** | Cuando intervengan varias especialidades o participantes, aclarar quién ejecuta, quién decide y cómo se coordinan. Usar una matriz RACI solo si facilita esa coordinación; no imponer una cadena fija de roles. | Propuesta del agente IA |

## Protección de la gobernanza local

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Protección configurable** | Si el proyecto adopta `permitir_cambios_gobernanza`, definir su alcance protegido y usar `false` como valor inicial y ante valores ausentes o inválidos. Solo el usuario puede habilitarla; una bandera documental no constituye un bloqueo técnico. | Propuesta del agente IA |
| **Modificación autorizada** | Modificar el Scope o las skills locales solo mediante solicitud explícita, dentro de su alcance y cumpliendo los controles adoptados por el proyecto. No modificar esos controles para autorizarse. | Propuesta del agente IA |
| **Cierre de excepción temporal** | Si se habilitó la bandera para una modificación autorizada, restablecerla a `false` y verificar el resultado antes de cerrar. Si falla el restablecimiento, informar el estado pendiente y detener nuevas escrituras protegidas. | Propuesta del agente IA |

## Selección de skills

| Regla | Descripción Operativa | Origen / referencia |
| :--- | :--- | :--- |
| **Carga Selectiva** | Consultar las descripciones de las skills y cargar las pertinentes al resultado. Al cambiar de fase, aplicar solo las instrucciones que sigan siendo relevantes, sin prometer borrar contenido de la memoria. | Propuesta del agente IA |
| **Combinación Lógica** | Combinar especializaciones únicamente si sus resultados son complementarios. | Propuesta del agente IA |
| **Ausencia de skill aplicable** | Si ninguna skill aplica, continuar con la gobernanza vigente cuando la tarea pueda resolverse con las capacidades disponibles. Si falta un método obligatorio, informar la limitación; no inventar skills ni capacidades. | Propuesta del agente IA |

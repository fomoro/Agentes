# Tesis de Arquitectura: Patrón Enrutador (AGENTS_Scope)

Este documento define la fundamentación teórica y arquitectónica oficial sobre cómo debe operar el archivo de gobernanza local (`AGENTS_Scope.md`) dentro de los repositorios de los clientes.

## 1. El Problema (Por qué fallan los modelos tradicionales)
Si se le da libertad absoluta a una IA (Enfoque Libre), tiende a sobrepensar, alucinar flujos o modificar archivos indebidos. Si por el contrario se le restringe a ejecutar pasos algorítmicos inmutables (Enfoque Burocrático), pierde su capacidad de razonamiento dinámico y consume un exceso de tokens intentando validar pasos rígidos para tareas simples.

## 2. La Solución: El Patrón "Router"
La arquitectura oficial para el Scope se basa en el patrón de "Enrutador Elástico". Este modelo logra el equilibrio perfecto entre seguridad extrema y agilidad operativa.

### A. Aislamiento y Seguridad (Las Barandas)
El Scope bloquea físicamente la capacidad de la IA para auto-modificar sus propias reglas (`permitir_cambios_gobernanza: false`). La IA opera en un entorno protegido donde las directrices base son inmutables, evitando "jailbreaks" accidentales.

### B. Orquestación y Descarga Cognitiva
En lugar de dictarle a la IA el "paso a paso" de cómo ejecutar una tarea de ingeniería, el Scope simplemente actúa como un semáforo inteligente que delega la carga cognitiva hacia módulos especializados (Skills).
- **Ejemplo:** El Scope no contiene reglas sobre bases de datos; solo contiene la instrucción: *"Si el usuario pide persistencia, descarga tus instrucciones actuales y carga la carpeta `Skill_DB`"*.

### C. Secuencialidad Dinámica
Se confía en la altísima capacidad de razonamiento del LLM para determinar qué skills se necesitan y en qué orden. Se impone una única regla transversal: **Secuencialidad estricta** (el output de un skill es el input innegociable del siguiente) para evitar alucinaciones por concurrencia.

## 3. Veredicto Arquitectónico
El `AGENTS_Scope.md` no es una Biblia procedimental, es un **Orquestador Inteligente**. Su única responsabilidad es asegurar que la IA opere de forma segura y sepa exactamente qué módulo cargar para resolver el requerimiento, garantizando versatilidad desde un script de fin de semana hasta un ecosistema corporativo masivo.

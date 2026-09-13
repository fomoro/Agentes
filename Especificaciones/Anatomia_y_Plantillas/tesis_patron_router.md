# Tesis de Arquitectura: Patrón Enrutador (AGENTS_Scope)

Este documento define la fundamentación teórica y arquitectónica oficial sobre cómo debe operar el archivo de gobernanza local (`AGENTS_Scope.md`) dentro de los repositorios de los clientes.

## 1. El Problema (Por qué fallan los modelos tradicionales)
Si se le da libertad absoluta a una IA (Enfoque Libre), tiende a sobrepensar, alucinar flujos o modificar archivos indebidos. Si por el contrario se le restringe a ejecutar pasos algorítmicos inmutables (Enfoque Burocrático), pierde su capacidad de razonamiento dinámico y consume un exceso de tokens intentando validar pasos rígidos para tareas simples.

## 2. La Solución: El Patrón "Router"
La arquitectura oficial para el Scope se basa en el patrón de "Enrutador Elástico". Este modelo justifica teóricamente la existencia de las 4 secciones anatómicas de la plantilla:

### A. Contexto Inyectado (Justifica la Sección A)
El agente necesita saber dónde está parado antes de tomar decisiones. Proveerle la pila tecnológica base y la identidad evita alucinaciones de contexto y garantiza que las decisiones arquitectónicas respeten el entorno.

### B. Autoridad Absoluta (Justifica la Sección B)
Para evitar bucles y conflictos de reglas, el patrón exige un orden jerárquico innegociable. El Scope local es la "Ley Suprema" del proyecto; ningún skill modular tiene autorización para contradecirlo.

### C. Descarga Cognitiva y Secuencialidad (Justifica la Sección C)
En lugar de dictarle a la IA un algoritmo rígido, el Scope actúa como un semáforo que delega la complejidad hacia los Skills (Lazy Loading). Se impone una **secuencialidad estricta** (el output de un skill es el input innegociable del siguiente) para evitar que el LLM colapse intentando resolver todo de forma concurrente.

### D. Aislamiento y Seguridad (Justifica la Sección D)
Para proteger el ecosistema de "jailbreaks" accidentales, el patrón exige bloquear físicamente la capacidad de la IA para auto-modificar sus reglas (`permitir_cambios_gobernanza: false`) o alterar el sistema sin autorización humana explícita.

## 3. Veredicto Arquitectónico
El `AGENTS_Scope.md` no es una Biblia procedimental, es un **Orquestador Inteligente**. Su única responsabilidad es asegurar que la IA opere de forma segura y sepa exactamente qué módulo cargar para resolver el requerimiento, garantizando versatilidad desde un script de fin de semana hasta un ecosistema corporativo masivo.

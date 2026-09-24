# Fábrica de Agentes - Scope Local

- **Actualizado:** 2026-09-13

## A. Contexto y Alcance del Proyecto

- **Propósito:** Construir una "Fábrica de Agentes", una arquitectura agnóstica de gobernanza que permita estandarizar y controlar el comportamiento de asistentes de IA en repositorios de clientes.
- **Resultados esperados:** Un sistema de reglas exportable, especificaciones arquitectónicas claras, y un Scope funcional (enrutador) validado en entorno de laboratorio.
- **Alcance:** Diseño arquitectónico, manuales operativos, prototipado de contratos (Scopes) y auditorías iterativas.
- **Fuera de alcance:** Desarrollo de código funcional para clientes, integraciones directas por API con modelos comerciales, o infraestructura Cloud real (hasta fase posterior).
- **Organización del repositorio:** `Especificaciones/` (Teoría y reglas maestras), `Capacidades/` (Implementaciones y propuestas), `Auditorias/` (Evaluación y control de calidad).
- **Fuentes de contexto:** `Gobernanza/banco_reglas_gobernanza.md`, `Scope/especificacion_scope.md` y `Fabrica/principios_fabrica.md`.
- **Tecnologías:** Puramente Markdown (Documentación como Código).
- **Arquitectura:** Diseño agnóstico basado en patrón Strategy (Contratos) y enrutamiento modular.
- **Convenciones del proyecto:** Todas las decisiones deben guiarse por la simplicidad (KISS/YAGNI) y la veracidad estricta, sin alucinaciones técnicas.

## B. Reglas y Límites de Actuación

- **Precedencia Local:** Este archivo especializa la gobernanza global para el proyecto dentro de la jerarquía y los permisos efectivos del entorno.
- **Jerarquía Estricta:** Las reglas de una skill complementan este Scope y no amplían autorizaciones ni debilitan restricciones aplicables. Ante un conflicto no resoluble, detén únicamente la parte dependiente y solicita la decisión necesaria.
- **Ubicación y Estado de Entregables:** Guarda los entregables finales en la ubicación definida por el proyecto y etiqueta los artefactos temporales como borradores. Reserva la carpeta de gobernanza para sus propios archivos autorizados.
- **Comprobar el estado antes de modificar:** Antes de editar un recurso o archivo, verifica su estado vigente. Si cambió desde la última lectura, incorpora los cambios y resuelve conflictos antes de sobrescribir.
- **Mínimo alcance de intervención:** Consulta y modifica únicamente lo necesario para cumplir la tarea autorizada. Conserva el contenido ajeno intacto.
- **Verificar antes de afirmar ejecución:** Distingue acciones propuestas de las confirmadas. Afirma creación o edición de código solo con evidencia disponible de lectura posterior.

## C. Selección y Uso de Skills

> **Instrucción de Enrutamiento:** Lee el contenido de la carpeta `.agents/skills/` para orquestar las capacidades disponibles.

1. **Carga Selectiva:** Carga en tu contexto **únicamente** la skill aplicable que resuelva el requerimiento actual.
2. **Combinación Lógica:** Combina especializaciones de múltiples skills únicamente si aportan resultados complementarios, respetando las dependencias.
3. **Cero Alucinación:** Si ninguna skill aplica a la tarea, debes usar tus instrucciones vigentes. Tienes estrictamente prohibido inventar o alucinar procedimientos de módulos que no existan.
4. **Herramienta Adecuada:** Prioriza la herramienta disponible más específica y verificable para ejecutar el skill elegido.

## D. Cambios de Gobernanza

- **Bandera de Protección:** `permitir_cambios_gobernanza: false`
- **Inviolabilidad Documental:** No modifiques este archivo ni la estructura local de skills sin una autorización explícita aplicable al cambio.
- **Excepción Temporal:** Si el entorno utiliza la bandera y una autorización permite habilitarla temporalmente, restáurala a `false` antes de cerrar y comprueba el estado final por un medio disponible.
- **Límite Técnico:** La bandera expresa una política documental; no constituye por sí sola un bloqueo de escritura. Registra por separado cualquier control técnico existente.

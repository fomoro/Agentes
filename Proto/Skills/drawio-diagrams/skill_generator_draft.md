# Borrador Crudo: Skill de Draw.io

Escribe aquí a la "topa tolondra". No te preocupes por formato, ortografía ni estructura. 
Solo vacía tu cabeza:
- ¿Qué te duele hoy al hacer diagramas?
- ¿Qué paso te quita más tiempo?
- ¿Qué te gustaría que hiciera la IA automáticamente?

Cuando termines, avísame. Yo leo este desastre y lo convierto en oro para nuestro `skill_generator.md`.


# Diagramas y Pruebas de IA (PoCs)

## Objetivo de las Pruebas
El objetivo principal de estas pruebas es encontrar una **Habilidad (Skill)** que se pueda integrar directamente en nuestro asistente de IA local (Jeff). Buscamos que el agente sea capaz de recibir órdenes por el chat y dibujar o editar archivos `.drawio` de forma nativa y autónoma dentro de nuestro propio entorno de desarrollo (VS Code).

---

## Reglas del Proyecto

1. **Estructura Espejo:** Por cada batería creada en `Test_Suite/`, debe existir una carpeta idéntica en cada proveedor dentro de `Suppliers/`. Al ejecutar pruebas, se debe validar que esta carpeta exista.
   ```text
   Diagramas/
   ├── Suppliers/        # Resultados de la IA
   └── Test_Suite/       # Prompts y pruebas
   ```
2. **Cero Residuos:** El código de las herramientas probadas se aloja en memoria temporal (`scratch`). No se instalan repositorios locales. Para limpiar, solicita en el chat: *"Limpia las descargas de prueba"*.
3. **Ejecución de Pruebas:** Para solicitar una prueba, indícale al agente el origen (archivo o carpeta) y el número de proveedor. El agente utilizará esta única plantilla: `Procesa {archivo_o_carpeta_origen} usando el Proveedor {#}`.

---

## Proveedores (Suppliers) Evaluados

| # | Proveedor | Estado | Ruta Local | Veredicto |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Agents365 (drawio-skill)](https://github.com/Agents365-ai/drawio-skill)** | SELECCIONADO | `Suppliers/Agents365/` | Habilidad nativa para el agente. Permite manipular archivos `.drawio` en silencio dentro del editor. Cumple el objetivo. |
| **2** | **[DayuanJiang (next-ai-draw-io)](https://github.com/DayuanJiang/next-ai-draw-io)** | DESCARTADO | `Suppliers/DayuanJiang/` | Web independiente. Obliga a levantar un servidor y salir del editor. No se integra de forma transparente con el agente. |






# Integración de Agents365 drawio-skill

- Estado: referencia de integración; el paquete upstream no está incluido en esta carpeta.
- Fuente: [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill)
- Instrucciones upstream: [skills/drawio-skill/SKILL.md](https://github.com/Agents365-ai/drawio-skill/blob/main/skills/drawio-skill/SKILL.md)
- Instrucciones upstream en texto plano: [SKILL.md](https://raw.githubusercontent.com/Agents365-ai/drawio-skill/main/skills/drawio-skill/SKILL.md)
- Licencia declarada por el proyecto: MIT; comprobar el archivo LICENSE de la revisión que se integre.
- Versión observada en los metadatos upstream: 3.4.0. La rama `main` puede cambiar; registrar revisión o commit al integrar una copia.

## Componentes necesarios

El upstream contiene más que el archivo de instrucciones: `agents/`, `data/`, `references/`, `scripts/`, `styles/` y `LICENSE`. Su `SKILL.md` enruta entre flujos de creación, importación desde código e infraestructura, sincronización, vistas, revisión semántica, exportación y otras funciones.

La herramienta unificada descrita por el upstream es `scripts/diagramctl.py`. El propio paquete indica Python 3 para los flujos principales y draw.io Desktop para exportaciones nativas; Graphviz se requiere solo para ciertas distribuciones automáticas. Algunas funciones dependen de versiones concretas de draw.io y herramientas adicionales. Confirma los requisitos en los archivos upstream relevantes antes de cada uso.

## Cómo consultarlo

1. Confirma que el paquete upstream existe en el entorno de trabajo y localiza su carpeta raíz. No asumas que esta ficha lo instala.
2. Lee su `SKILL.md` y sigue los enlaces a `references/` que correspondan al tipo de tarea.
3. Usa los scripts y activos desde esa copia, respetando sus instrucciones y los permisos efectivos del proyecto.
4. Antes de integrar o actualizar una copia dentro de esta carpeta, registra el commit o versión, conserva la licencia y comprueba referencias y dependencias. No sustituyas archivos locales sin revisar su estado y la autorización aplicable.

La página del repositorio describe generación de `.drawio` editable, importación de varias fuentes, sincronización incremental, validaciones y exportaciones. Estas capacidades son afirmaciones del upstream; solo deben anunciarse como disponibles después de comprobar que la revisión integrada y sus dependencias las incluyen.

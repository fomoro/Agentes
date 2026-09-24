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

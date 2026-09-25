# Borrador Estructurado: Skill de Draw.io

> Antecedente histórico. Las rutas y decisiones de este borrador no describen la skill vigente en `Proto/Skills/drawio-diagrams/`.

## Estructura Interna Proyectada

```text
drawio-diagrams/
├── SKILL.md                 (El cerebro y manual paso a paso)
├── vendor/                  (El motor congelado de Agents365)
└── estilos/                 (Perfiles de diseño dinámicos)
    ├── colcomercio/
    ├── wolfan/
    └── default/
```

## Contrato de la Herramienta (Las 5 Piezas)

- **Propósito:** Generar archivos `.drawio` nativos y editables de forma autónoma dentro del entorno local (VS Code), aplicando perfiles de diseño corporativos dinámicos sin que el asistente tenga que redactar XML complejo desde cero.
- **Activador:** Cuando el usuario pida explícitamente "crear", "dibujar" o "diagramar" flujos, arquitecturas o conceptos, ya sea desde cero o a partir de un archivo de origen.
- **Entradas (Inputs):** 
  1. La lógica o el archivo base que contiene la información a diagramar.
  2. *Opcional:* El nombre del perfil de estilo a aplicar (ej. "colcomercio"). Si el usuario no lo menciona, se asume el perfil "default".
- **Método:**
  1. Identificar el texto o archivo origen a diagramar.
  2. Navegar a la carpeta interna `estilos/[perfil_solicitado]/` y extraer las reglas visuales obligatorias (colores, bordes, tipografías).
  3. Ejecutar el motor de dibujo alojado de forma estática en la subcarpeta `vendor/`, inyectándole las instrucciones lógicas y las reglas de estilo.
  4. Aplicar política de **Cero Residuos**: limpiar y eliminar cualquier archivo temporal de ejecución en la memoria (`scratch`).
- **Salida esperada:** Un archivo `.drawio` completamente funcional y editable, guardado en la carpeta `Diagramas_Result/` (o la ruta especificada por el usuario), entregando un entorno limpio sin repositorios clonados o basura local.

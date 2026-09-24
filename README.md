# Estructura base

- Actualizado: el 2026-09-23 23:31
- Rol de ejecución: arquitecto de información
- Autor: Sam (Asistente IA del Sr. Wolfan)
- Estado: propuesta en revisión

Para consultar los iconos de carpeta disponibles en Material Icon Theme, revisa su [galería](https://github.com/material-extensions/vscode-material-icon-theme/blob/main/README.md).

```text
C:\Dev\Agentes\
├── Input\                              # Fuentes y materiales de entrada
├── Generator\                          # Diseño y método para crear skills y agentes
│   ├── Gobernanza\                     # Reglas internas y reglas exportables
│   │   ├── Reglas_de_la_Fabrica\       # Reglas para operar el generador
│   │   └── Reglas_Exportables\         # Reglas incluidas en los productos
│   ├── Scope\                          # Diseño del Scope para proyectos destino
│   │   ├── Especificaciones\           # Definición del Scope
│   │   ├── Procesos\                   # Método para crear el Scope
│   │   └── Propuestas\                 # Borradores del Scope
│   └── Backlog.md                      # Pendientes de trabajo
├── Proto\                              # Pruebas de concepto
├── Review\                             # Auditorías del proyecto
└── Export\                             # Skills y agentes listos para usar
```

## Extensiones en uso

- [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme/blob/main/README.md): `Ctrl+Shift+P` → `Material Icons: Activate Icon Theme`.
- [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf): `Ctrl+Shift+P` → `Markdown PDF: Export (pdf)`.

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


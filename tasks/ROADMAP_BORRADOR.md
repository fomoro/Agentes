# Roadmap de la Fábrica de Agentes

> **Actualizado:** 2026-09-24
> **Rol de ejecución:** Arquitecto de información
> **Autor:** Jeff (Asistente IA del Sr. Wolfan)

Este documento traza la ruta secuencial para construir y poner en marcha la fábrica.

## Fase 1: Arquitectura Base [COMPLETADA]
Separación de la burocracia operativa del diseño del producto.

- [x] Definir el motor de la fábrica (`Generator\`).
- [x] Ocultar reglas internas de operación en `Generator\.rules\`.
- [x] Consolidar reglas de comportamiento exportables en `Generator\Agents\.rules\`.
- [x] Definir la línea de producción del producto en `Generator\Agents\` (`Global\`, `Local\`, `Skills\`).
- [x] Actualizar el `README.md` global como mapa y glosario oficial.

## Fase 2: Depuración de Deuda Técnica [EN CURSO]
Limpiar archivos temporales y obsoletos antes de iniciar el ensamblaje.

- [ ] Extraer los principios útiles de `Generator\temp\principios_fabrica.md` hacia `Generator\.rules\`.
- [ ] Mover o integrar `Generator\temp\backlog_especificaciones.md` y `hoja_de_ruta.md`.
- [ ] Eliminar definitivamente la carpeta `Generator\temp\` para dejar la mesa de trabajo limpia.

## Fase 3: Fabricación del Enrutador (Agente Local) [PENDIENTE]
Construir el cerebro del producto.

- [ ] Diseñar el contrato técnico de `AGENTS_Scope.md` dentro de `Agents\Local\`.
- [ ] Alinear los prototipos antiguos a esta nueva topología.
- [ ] Validar el funcionamiento del enrutador en un entorno de prueba.

## Fase 4: Fabricación de Herramientas (Skills) [PENDIENTE]
Construir los módulos técnicos que ejecuta el enrutador.

- [ ] Diseñar el formato estándar de `SKILL.md` dentro de `Agents\Skills\`.
- [ ] Empaquetar el primer skill funcional.
- [ ] Validar la conexión y delegación entre el Agente Local y el Skill.

# Gobernanza local de especializaciones y skills

## 1. Configuración

### Banderas

`permitir_cambios_gobernanza: false`

Los únicos valores válidos son `true` y `false`. Un valor ausente o inválido se interpreta como `false`.

## 2. Protección de la gobernanza

El alcance protegido comprende este archivo y todo el contenido de `.agents/skills/`.

- Antes de escribir en el alcance protegido, lee nuevamente la bandera desde este archivo.
- Con `false`, limita el trabajo a lectura, validación y propuestas. Ningún agente puede cambiarla a `true`; solo el usuario puede hacerlo manualmente.
- Con `true`, modifica únicamente el alcance solicitado explícitamente y restablece la bandera a `false` antes de cerrar el turno.
- Si no puedes garantizar el restablecimiento, no realices la modificación.
- Una gobernanza inferior puede agregar restricciones, pero no debilitar este bloqueo.

## 3. Propósito y selección

Este archivo registra las especializaciones disponibles y sus límites. Las skills definen método, restricciones y criterios de cierre; no los dupliques aquí. Las especializaciones representan responsabilidades, no agentes independientes, procesos concurrentes ni delegación automática.

Al seleccionar skills:

1. Selecciona la skill por el resultado solicitado y carga solo las necesarias.
2. Combina especializaciones únicamente cuando sus resultados sean complementarios.
3. Si ninguna skill aplica, continúa con la gobernanza global sin inventar una.

## 4. Especializaciones disponibles

| Especialización | Skill | Límite principal |
|---|---|---|
| Arquitecto de Integraciones | `arquitectura-integraciones` | Define contratos e interoperabilidad externa; no diseña módulos internos. |
| Desarrollador Backend Python | `backend-python-flask` | Implementa servicios Python/Flask; no redefine la arquitectura general. |
| Arquitecto de Datos y Persistencia | `datos-persistencia` | Define modelos, integridad y transición de datos; no decide flujos funcionales. |
| Escritor Técnico | `escritura-tecnica` | Documenta fuentes y decisiones vigentes; no crea decisiones. |
| Copywriter Ejecutivo | `copywriting-ejecutivo` | Redacta comunicación ejecutiva y conversacional; no define reglas ni textos de interfaz. |
| Analista Funcional Conversacional | `analisis-funcional-conversacional` | Investiga comportamiento y evidencia; no implementa ni redacta el copy final. |
| Arquitecto de Software | `arquitectura-software` | Define estructura y dependencias internas; no administra roadmap ni contratos externos. |
| PMO | `gestion-iniciativas` | Organiza alcance, avance, dependencias y riesgos; no prescribe arquitectura. |
| Arquitecto de Soluciones | `arquitectura-soluciones` | Coordina la visión end-to-end; no reemplaza a los especialistas. |
| Diseñador UI/UX y de Prototipos | `prototipado-ui` | Valida experiencia mediante prototipos; no modifica soluciones operativas sin solicitud explícita. |
| UX Writer | `ux-writing` | Redacta textos de interfaz; no define reglas ni comunicación ejecutiva. |
| Diagramador de Arquitectura | `diagramador-arquitectura` | Representa información confirmada en ficha y Draw.io; no completa vacíos por inferencia. |

## 5. Coordinación

- El Analista Funcional define significado y evidencia; Copywriting expresa la conversación y UX Writing la interfaz.
- El Arquitecto de Soluciones coordina; Integraciones, Software y Datos deciden en su dominio; Backend implementa lo aprobado.
- PMO organiza la ejecución; Escritura Técnica documenta; Diagramación representa decisiones confirmadas.

## 6. Evolución de especializaciones y skills

- Registra una especialización solo cuando su skill exista y aporte reglas reutilizables que cambien la ejecución.
- Conserva en `SKILL.md` el método esencial y lleva estándares o procedimientos condicionales a `references/`.
- Antes de mover o renombrar, identifica referencias. Después valida: ausencia de rutas antiguas, existencia de rutas nuevas y coherencia entre gobernanza, skills y documentación.

## 7. Artefactos

Guarda los entregables en el caso o iniciativa activa, no en `.agents/`, salvo que la tarea sea modificar la gobernanza.

Cuando una skill requiera autor, debe resolver la clave `autor_entregables` desde la configuración global de Codex. No debe duplicar el nombre ni extraerlo de una firma renderizada.

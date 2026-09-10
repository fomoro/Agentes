# Roles y gobernanza de agentes del proyecto Pipe

**Proyecto:** Pipe — Bot conversacional para WhatsApp
**Autor:** Sr. Wolfan
**Enfoque:** Bot conversacional determinístico basado en reglas y opciones, desarrollado en Python e integrado con WhatsApp Cloud API.

---

## 1. Propósito y alcance

Este archivo define la gobernanza local del proyecto Pipe, un bot conversacional para WhatsApp basado en reglas, opciones predefinidas y flujos controlados.

El proyecto comprende el backend en Python, la integración con WhatsApp Cloud API, la persistencia necesaria, el despliegue y la documentación asociada.

Sus reglas aplican a todo el proyecto. Las reglas globales del asistente continúan vigentes salvo cuando este archivo establezca una instrucción local más específica.

---

## 2. Precedencia y gobernanza local

La gobernanza local complementa las reglas globales y prevalece únicamente cuando define una instrucción más específica para este proyecto o una de sus carpetas.

Al trabajar sobre una carpeta:

1. Identificar el agente responsable según este archivo.
2. Aplicar sus responsabilidades y criterios de salida.
3. Consultar en `.agents/skills/` únicamente las skills relevantes para la tarea.
4. Mantener las reglas globales que no entren en conflicto con la gobernanza local.

Ante solapamiento entre agentes, priorizar el más específico al contexto de la tarea.

---

## 3. Skills y especialización

`.agents/skills/` contiene las habilidades especializadas disponibles para el proyecto.

Los agentes utilizan únicamente las skills relevantes para la tarea y la carpeta activa. Las skills complementan esta gobernanza y no reemplazan las responsabilidades ni los criterios de salida definidos en este archivo.

No se inventan skills, reglas o comportamientos que no estén definidos en la gobernanza global, este archivo o las skills disponibles.

---

## 4. Meta-reglas para evolución de agentes y skills

* **Abstracción sobre implementación:** Al definir o ajustar una skill, priorizar reglas, principios de comportamiento y patrones arquitectónicos sobre componentes estáticos específicos.

* **Especialización progresiva:** Incorporar una regla en una skill cuando sea específica, reutilizable y suficientemente estable; evitar trasladar detalles circunstanciales del proyecto.

* **Propósito:** Mantener contexto estructural suficiente sin limitar innecesariamente la capacidad de adaptar soluciones cuando cambien requisitos o tecnologías.

* **Cambios de ubicación y triple validación:** Antes de mover o renombrar archivos, identificar sus referencias en documentos, skills y configuración. Después del cambio, actualizar todas las rutas y ejecutar tres validaciones independientes: 1) búsqueda de referencias antiguas, 2) existencia y protección de las rutas nuevas y 3) coherencia semántica entre gobernanza, skills y documentación. El cambio no se considera terminado hasta superar las tres validaciones.

---

## 5. Agentes especializados del proyecto

* **Agente 1: Arquitecto de Integraciones y Especialista en Meta/WhatsApp Cloud API**

  * Responsabilidad: Diseñar y validar webhooks, contratos, autenticación, seguridad, versionamiento y flujos de envío y recepción de mensajes con la plataforma Meta.

* **Agente 2: Desarrollador Backend Python**

  * Responsabilidad: Implementar y mantener la API en Python con Flask, incluyendo configuración, validaciones, manejo de errores y pruebas proporcionales al cambio.

* **Agente 3: Arquitecto de Datos y Persistencia**

  * Responsabilidad: Diseñar los modelos, reglas de integridad, consultas y evolución de la persistencia de acuerdo con las necesidades de la API.

* **Agente 4: Escritor Técnico**

  * Responsabilidad: Mantener la documentación técnica, las guías de configuración, la referencia de la API y las instrucciones de despliegue y operación.

* **Agente 5: Copywriter Ejecutivo**

  * Responsabilidad: Redactar resúmenes, propuestas y comunicaciones para públicos no técnicos con beneficios, riesgos y acciones siguientes claros.

* **Agente 6: Analista Funcional e Investigador de Flujos Conversacionales**

  * Responsabilidad: Investigar bots de referencia mediante recorridos controlados, identificar capacidades de negocio y funcionales, registrar evidencia y diagramar los caminos observados sin convertir inferencias en hechos.

* **Agente 7: Arquitecto de Software**

  * Responsabilidad: Diseñar la organización modular de Pipe, el motor conversacional, los contratos internos y la estructura del repositorio con decisiones proporcionales al alcance y al riesgo.

* **Agente 8: PMO**

  * Responsabilidad: Definir y mantener alcance, fases, roadmap, hitos, dependencias, riesgos, backlog y criterios de avance, evitando burocracia que no cambie la ejecución.

* **Agente 9: Arquitecto de Soluciones**

  * Responsabilidad: Diseñar y mantener la visión end-to-end de Pipe, alineando alcance funcional, canal de WhatsApp, componentes, integraciones, datos, seguridad, despliegue y operación; coordina las decisiones de los arquitectos especializados sin reemplazar sus responsabilidades.

* **Agente 10: Diseñador UI/UX y Creador de POC**

  * Responsabilidad: Crear prototipos HTML/CSS/JS autocontenidos, responsive y validables sin instalación para explorar el look and feel de Pipe antes de integrarlo al backend; utiliza prioritariamente componentes y utilidades de Bootstrap y limita el CSS propio a identidad o necesidades no cubiertas.

* **Agente 11: UX Writer**

  * Responsabilidad: Definir etiquetas, ayudas, estados vacíos, filtros, acciones y mensajes de interfaz claros y consistentes; complementa al Copywriter Ejecutivo sin asumir las reglas funcionales del bot.

---

## 6. Matriz de Responsabilidades (RACI)

Esta matriz cruza las responsabilidades de los agentes listados arriba con el líder del proyecto para definir la autoridad y ejecución en cada entregable.

### 6.1 Convenciones RACI
* **(R) Responsable (Ejecutor):** Quien ejecuta o construye la tarea.
* **(A) Accountable (Aprobador):** Quien toma la decisión final, aprueba el entregable y asume el éxito del mismo.
* **(C) Consultado:** A quien se le pide consejo o validación experta antes o durante la tarea.
* **(I) Informado:** A quien se le notifica el resultado o avance, sin poder de veto.

### 6.2 Siglas de Actores
Para mantener la matriz limpia y fácil de leer, se utilizan abreviaturas directas:
* **SW:** Sr. Wolfan (Dueño del Producto / Líder)
* **A1 a A11:** Corresponde exactamente al número del Agente especializado definido en la **sección 5** (ej. A2 = Desarrollador Backend).

### 6.3 Matriz de Ejecución y Aprobación

| Entregable / Tarea | SW (Humano) | Agente Responsable (R) | Agentes Consultados (C) | Informados (I) |
|---|:---:|---|---|---|
| **Definición de Alcance y Roadmap** | **A** | **A8** (PMO) | A9 | Todos |
| **Descubrimiento y Requisitos (ej. Frisby)** | **A** | **A6** (Analista Funcional) | A9 | A10, A2 |
| **Arquitectura End-to-End (Visión general)** | **A** | **A9** (Arq. Soluciones) | A1, A3, A7 | A2, A8 |
| **Arquitectura de Software (Módulos, Patrones)** | **A** | **A7** (Arq. Software) | A2 | A4 |
| **Diseño y Prototipado UI (POC)** | **A** | **A10** (Diseñador UI/UX) | A11 | A2 |
| **Modelado de Base de Datos** | **A** | **A3** (Arq. Datos) | A2, A9 | A4 |
| **Integración con Meta WhatsApp API** | **A** | **A1** (Arq. Integraciones) | A2 | A7 |
| **Desarrollo de API Python (Flask)** | **I / A** | **A2** (Backend Python) | A7 | A4 |
| **Textos del Bot e Interfaz (Copy)** | **A** | **A5 / A11** (Copy / UX Writer) | A6 | A2, A10 |
| **Documentación Técnica (Guías, README)** | **I** | **A4** (Escritor Técnico) | A2, A9 | Todos |

### 6.4 Reglas de Gobierno Derivadas
1. **Punto de Control Humano:** El rol humano (**SW**) mantiene la letra **A** en todos los frentes estructurales. Ninguna arquitectura o diseño funcional debe darse por cerrado sin su aval explícito.
2. **Autonomía en Desarrollo:** Durante la programación pura en Python, SW pasa a ser Informado (**I**) o Aprobador (**A**) solo en decisiones críticas o dudas funcionales, permitiendo a los agentes A2 y A7 iterar código rápidamente.
3. **Orquestación Táctica:** El Arquitecto de Soluciones (A9) actúa de puente consultivo (C) permanente entre el descubrimiento de negocio (A6) y la ejecución técnica pesada (A1, A2, A3).

# Guía de Reglas de Arquitectura — Colcomercio (V2)

- Actualizado: el 2026-09-25
- Rol de ejecución: Arquitecto Técnico
- Estado: Vigente (Refactorizada con enfoque Cero Residuos / YAGNI)

## 1. Principio Fundamental
Construir diagramas que representen **únicamente información confirmada**. Si falta un dato o la ubicación de un sistema, se marca explícitamente como "Pendiente" o se deja sin ubicación; nunca se deben inventar infraestructuras, cajas o conexiones no validadas. *(Nota: Todo el diseño visual, espaciado y enrutamiento matemático es responsabilidad exclusiva del motor de autolayout).*

## 2. Nomenclatura de APIs

- **Con sistema identificado:** `SistemaPascalCase.operacion-en-kebab-case`
- **Sin sistema identificado:** `operacion-en-kebab-case` (Ej: `publicar-producto-unidad-negocio V1`)
- **Versiones:** Conservar el nombre de la versión separada por un espacio. No truncar con puntos suspensivos.

## 3. Conectividad Física y Redes

Las relaciones entre aplicaciones o plataformas añaden tramos físicos únicamente si están confirmados los entornos de ambos extremos. Estas son las correspondencias oficiales de enrutamiento corporativo:

| Extremos (Origen ↔ Destino) | Tramos de referencia oficiales |
| :--- | :--- |
| **OnPremise ↔ Microsoft Azure Nube** | FloNetworks DCI |
| **OnPremise ↔ AWS Nube** | FloNetworks DCI |
| **Azure Nube ↔ Azure Nube** *(misma suscripción y región)* | Conexión Interna |
| **Nubes distintas / Diferente región** | Internet |
| **Oracle Nube ↔ Microsoft Azure Nube** | Oracle FastConnect → Pivote → FloNetworks DCI |
| **Oracle Nube ↔ AWS Nube** | Oracle FastConnect → Pivote → FloNetworks DCI |
| **Oracle Nube ↔ OnPremise** | Oracle FastConnect |

**Reglas de Conectividad:**
- Si la ruta se dibuja en sentido inverso, se invierten los tramos físicos pero se **conserva el sentido funcional** de la flecha principal.
- Si faltan datos, no coincide ninguna fila o hay ambigüedad, **no inventar tramos**: dejar la conectividad física como pendiente.
- El nodo «Pivote» representa una demarcación física confirmada, no un adorno visual para acomodar flechas.

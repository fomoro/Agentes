# Especificación de diagrama - Copiloto

## Arquitectura Base

### Estructura visual

| Zona | Frame | Contenedor | Elemento | Leyenda | Estado |
|---|---|---|---|---|---|
| Actores |  |  | Persona | Vendedor / Jefe de venta | `—` |
| Accesos |  |  | Componente | Portátil | `—` |
| Accesos |  |  | Componente | Celular | `—` |
| Accesos | Microsoft 365 |  | Componente | Microsoft Teams | `—` |
| Aplicaciones | Microsoft Azure Nube |  | Componente | Azure Entra ID | `—` |
| Aplicaciones | Microsoft Azure Nube |  | Componente Contenedor | Microsoft Power Platform | Modificado |
| Aplicaciones | Microsoft Azure Nube | Microsoft Power Platform | Componente | Copilot Studio | Modificado |
| Ecosistema De Datos | Microsoft Azure Nube |  | Componente Contenedor | SharePoint | Modificado |
| Ecosistema De Datos | Microsoft Azure Nube | SharePoint | Componente | Excel | Nuevo |

### Relaciones

| Origen | Destino |
|---|---|
| Vendedor / Jefe de venta | Portátil |
| Vendedor / Jefe de venta | Celular |
| Portátil | Microsoft Teams |
| Celular | Microsoft Teams |
| Microsoft Teams | Azure Entra ID |
| Microsoft Teams | Copilot Studio |
| Copilot Studio | SharePoint |

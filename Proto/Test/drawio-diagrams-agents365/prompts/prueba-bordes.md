Prueba de Catálogo Actualizado (Bordes)

Diseñar un diagrama simple para verificar que los nuevos bordes inyectados en el catálogo se renderizan correctamente:

- **Usuario B2B** (en la Zona Externos)
- **Portal Principal** (en la Zona Aplicaciones, dentro de AWS Nube)
- **CRM Customer** (en la Zona Aplicaciones, dentro de Salesforce Nube)
- **Data Engine** (en la Zona Integración, dentro de GCP Nube)

Flujo:
El Usuario accede al Portal, el Portal consulta el CRM, y el CRM envía logs al Data Engine.

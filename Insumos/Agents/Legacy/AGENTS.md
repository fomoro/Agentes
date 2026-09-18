# Reglas de Proyecto: Core NLU Bot Restaurante (nlp_engine_md)

## Contexto y Propósito
Este proyecto define el motor de procesamiento de lenguaje natural (NLU Core) basado en SpaCy (`es_core_news_md`) para un bot de atención de restaurante que posteriormente se conectará a la API de WhatsApp.

## Reglas de Arquitectura y Diseño
1. **Desacoplamiento Estricto**: El motor NLU no debe depender de librerías ni SDKs de WhatsApp o Meta. Debe exponerse vía API REST (FastAPI) o interfaz independiente.
2. **Normalización Dialectal Previas**: Todo texto de entrada debe ser preprocesado con reglas específicas del español de Colombia (modismos de pedido, tratamiento y gastronomía local) antes de ser evaluado por los componentes estadísticos de SpaCy.
3. **Desempeño**: Respuestas NLU con latencia < 200 ms por mensaje.
4. **Resiliencia Lingüística**: El motor debe tolerar diminutivos colombianos ("gaseosita", "combito"), omisión de tildes y abreviaturas comunes en WhatsApp ("domi", "q", "porfa", "pa").

import asyncio
import os
import urllib.request
import urllib.parse
import json
import base64
from pathlib import Path

import httpx2
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

# Cargar variables de entorno desde el archivo .env
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

def get_leanix_bearer_token(api_token, domain):
    auth_url = f"https://{domain}/services/mtm/v1/oauth2/token"
    auth_str = f"apitoken:{api_token}"
    base64_auth = base64.b64encode(auth_str.encode('ascii')).decode('ascii')
    
    data = urllib.parse.urlencode({'grant_type': 'client_credentials'}).encode('ascii')
    req = urllib.request.Request(auth_url, data=data)
    req.add_header('Authorization', f'Basic {base64_auth}')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    try:
        with urllib.request.urlopen(req) as response:
            token_data = json.loads(response.read())
            return token_data.get('access_token')
    except Exception as e:
        print(f"Error obteniendo token de acceso: {e}")
        return None

async def main():
    domain = "colcomercio.leanix.net"
    url = f"https://{domain}/services/mcp-server/v1/mcp"
    
    api_token = os.environ.get("LEANIX_TOKEN")
    if not api_token:
        print("Error: Define la variable de entorno LEANIX_TOKEN en tu archivo .env antes de ejecutar.")
        return

    print("Intercambiando API Token por un Bearer Token temporal...")
    bearer_token = get_leanix_bearer_token(api_token, domain)
    if not bearer_token:
        print("Error: No se pudo autenticar con LeanIX. Verifica que el token sea válido.")
        return

    print("Iniciando conexión con el servidor MCP de LeanIX...")

    try:
        # Streamable HTTP negocia JSON o SSE en el mismo endpoint /mcp.
        async with httpx2.AsyncClient(
            headers={"Authorization": f"Bearer {bearer_token}"},
            timeout=httpx2.Timeout(30, read=300),
        ) as http_client:
            async with streamable_http_client(url, http_client=http_client) as (read_stream, write_stream):
            
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    print("Conexión exitosa. Sesión MCP inicializada.\n")

                    tools_response = await session.list_tools()

                    print(f"Herramientas disponibles: {len(tools_response.tools)}")
                    for tool in tools_response.tools:
                        print(f"- {tool.name}")

    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    asyncio.run(main())

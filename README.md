# FastAPI SSE Neo4j MCP

A FastAPI application using SSE (Server-Sent Events) as a transport layer for Neo4j's Cypher MCP (Model Context Protocol). Uses Python 3.11 and Poetry for virtual environment and dependency management which is compatible for deployment to [Render.com](https://render.com/).

## Requirements

- Python 3.11+
- FastAPI 0.115.12+
- MCP 1.9.2+
- Poetry 1.8.4+ for dependency management

## Installation
```
poetry install
```
## Running the Application

Start the FastAPI server:

```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 4000 --reload
```

The server will be available at http://127.0.0.1:4000.

## API Endpoints

- `GET /` - Returns a simple JSON greeting
- `GET /sse/` - SSE endpoint for establishing connections
- `POST /messages/` - Endpoint for sending messages over SSE

## Examples

The application provides three example MCP functions:

1. **Tool Function**: Echoes messages
   ```python
   @mcp.tool()
   def echo_tool(message: str) -> str:
       """Echo a message as a tool"""
       return f"Tool echo: {message}"
   ```

2. **Prompt Function**: Creates echo prompts
   ```python
   @mcp.prompt()
   def echo_prompt(message: str) -> str:
       """Create an echo prompt"""
       return f"Please process this message: {message}"
   ```

3. **Resource Function**: Handles resource requests
   ```python
   @mcp.resource("echo://{message}")
   def echo_resource(message: str) -> str:
       """Echo a message as a resource"""
       return f"Resource echo: {message}"
   ```
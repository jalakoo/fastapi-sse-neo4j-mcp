from fastapi import FastAPI
from app.sse import create_sse_server
from mcp.server.fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("Echo")

# Mount the Starlette SSE server onto the FastAPI app at the root path
app.mount("/", create_sse_server(mcp))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"


@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", 4000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)

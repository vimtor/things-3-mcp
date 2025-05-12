import os
from typing import Any
import subprocess
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
import things 

mcp = FastMCP("Things 3", instructions="""
When asked for todos in general, return today's todos.
""")

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_today() -> list[Any]:
    """Get today's todos."""
    return things.today()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_inbox() -> list[Any]:
    """Get inbox contents."""
    return things.inbox()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_anytime() -> list[Any]:
    """Get anytime todos."""
    return things.anytime()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_someday() -> list[Any]:
    """Get someday todos."""
    return things.someday()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_upcoming() -> list[Any]:
    """Get upcoming todos."""
    return things.upcoming()

@mcp.tool()
async def update_todo(uuid: str, title: str = None, completed: bool = None) -> None:
    """Update a todo."""
    kwargs = {}
    if title:
        kwargs['title'] = title
    if completed is not None:
        kwargs['completed'] = completed
    
    url = things.url(command='update', uuid=uuid, token=os.getenv('THINGS_TOKEN'), reveal=False, **kwargs)
    subprocess.Popen(['open', '-g', url])


if __name__ == "__main__":
    mcp.run(transport='stdio')

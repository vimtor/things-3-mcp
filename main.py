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
    """Get today's todos and projects."""
    return things.today()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_inbox() -> list[Any]:
    """Get inbox contents."""
    return things.inbox()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_trash() -> list[Any]:
    """Get trash contents."""
    return things.trash()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_logbook() -> list[Any]:
    """Get logbook contents."""
    return things.logbook()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_completed(last: str = None) -> list[Any]:
    """Get completed todos and projects.
    
    Args:
        last: Limit returned tasks to tasks created within the last X days, weeks, or years. For example: '3d', '5w', or '1y'.
    """
    return things.completed(last=last)

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_deadlines() -> list[Any]:
    """Get deadlines."""
    return things.deadlines()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_anytime() -> list[Any]:
    """Get anytime todos and projects."""
    return things.anytime()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_someday() -> list[Any]:
    """Get someday todos and projects."""
    return things.someday()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_upcoming() -> list[Any]:
    """Get upcoming todos and projects."""
    return things.upcoming()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_projects() -> list[Any]:
    """Get all projects."""
    return things.projects()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_areas() -> list[Any]:
    """Get all areas."""
    return things.areas()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_tags() -> list[Any]:
    """Get all tags."""
    return things.tags()

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_project_todos(id: str) -> list[Any]:
    """Get all todos for a project."""
    return things.todos(project=id)

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_area_todos(id: str) -> list[Any]:
    """Get all todos for an area."""
    return things.todos(area=id)

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def search(query: str) -> list[Any]:
    """Search for todos, projects, areas, and tags.
    
    Args:
        query: Only pass the necessary keywords as if you were doing a Google search. If you didn't get a result, try a different query.
    """
    return things.search(query)

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
async def get_task(id: str) -> list[Any]:
    """Get a task by ID."""
    return things.get(id)

def run_command(command: str, **arguments: Any) -> None:
    subprocess.Popen(['open', '-g', things.url(command=command, token=os.getenv('THINGS_TOKEN'), reveal=False, **arguments)])

@mcp.tool(annotations=ToolAnnotations(idempotentHint=True,destructiveHint=False))
async def update_todo(id: str, title: str = None, completed: bool = None, notes: str = None, when: str = None, deadline: str = None) -> None:
    """Update a todo.
    
    Args:
        id: The ID of the todo to update.
        title: The new title of the todo.
        completed: Whether the todo is completed.
        notes: The new notes of the todo.
        when: When should the todo be completed. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
        deadline: The deadline of the todo. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
    """
    arguments = {}
    if title:
        arguments['title'] = title
    if completed is not None:
        arguments['completed'] = completed
    if notes:
        arguments['notes'] = notes
    if when:
        arguments['when'] = when
    if deadline:
        arguments['deadline'] = deadline

    run_command('update', id=id, **arguments)

@mcp.tool(annotations=ToolAnnotations(idempotentHint=True,destructiveHint=False))
async def update_project(id: str, title: str = None, completed: bool = None, notes: str = None, when: str = None, deadline: str = None) -> None:
    """Update a project.
    
    Args:
        id: The ID of the project to update.
        title: The new title of the project.
        completed: Whether the project is completed.
        notes: The new notes of the project.
        when: When should the project be completed. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
        deadline: The deadline of the project. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
    """
    arguments = {}
    if title:
        arguments['title'] = title
    if completed is not None:
        arguments['completed'] = completed
    if notes:
        arguments['notes'] = notes
    if when:
        arguments['when'] = when
    if deadline:
        arguments['deadline'] = deadline

    run_command('update-project', id=id, **arguments)

@mcp.tool(annotations=ToolAnnotations(idempotentHint=True,destructiveHint=False))
async def create_todo(title: str, list: str = None, notes: str = None, when: str = None, deadline: str = None) -> None:
    """Create a todo.
    
    Args:
        title: The title of the todo.
        list: The title of a project or area to add to.
        notes: The notes of the todo.
        when: When should the todo be completed. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
        deadline: The deadline of the todo. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
    """
    arguments = {}
    if list:
        arguments['list'] = list
    if title:
        arguments['title'] = title
    if notes:
        arguments['notes'] = notes
    if when:
        arguments['when'] = when
    if deadline:
        arguments['deadline'] = deadline

    run_command('add', **arguments)

@mcp.tool(annotations=ToolAnnotations(idempotentHint=True,destructiveHint=False))
async def create_project(title: str, area: str = None, notes: str = None, when: str = None, deadline: str = None) -> None:
    """Create a project.
    
    Args:
        title: The title of the project.
        area: The title of an area to add the project to.
        notes: The notes of the project.
        when: When should the project be completed. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
        deadline: The deadline of the project. Can be a date following the format YYYY-MM-DD or a string like "tomorrow", "in 3 days", etc.
    """
    arguments = {}
    if area:
        arguments['area'] = area
    if title:
        arguments['title'] = title
    if notes:
        arguments['notes'] = notes
    if when:
        arguments['when'] = when
    if deadline:
        arguments['deadline'] = deadline

    run_command('add-project', **arguments)

if __name__ == "__main__":
    mcp.run(transport='stdio')
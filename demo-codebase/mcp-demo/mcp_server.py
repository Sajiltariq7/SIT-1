"""
MCP server for the to-do list app.

This exposes the existing TodoList class (unmodified, imported directly
from todo_app/todo.py) as a set of "tools" that any MCP-compatible AI
agent can call. This does NOT duplicate the app's logic — it's a thin
wrapper that translates MCP tool calls into method calls on the same
TodoList class already used by main_interactive.py.
"""

from mcp.server.mcpserver import MCPServer
from todo_app.todo import TodoList, TodoError

# One shared TodoList instance for the lifetime of this server process.
todo = TodoList()

# Create the MCP server. The name shows up when an agent connects to it.
mcp = MCPServer("todo-list-server")


@mcp.tool()
def add_task(title: str, priority: str = "normal") -> str:
    """Add a new task to the to-do list.

    Args:
        title: The task's title.
        priority: One of "low", "normal", or "high".
    """
    try:
        task_id = todo.add_task(title, priority)
        return f"Added task #{task_id}: '{title}' (priority: {priority})"
    except TodoError as e:
        return f"Error: {e}"


@mcp.tool()
def list_tasks() -> str:
    """List all current tasks with their id, status, and priority."""
    if not todo.tasks:
        return "No tasks yet."
    lines = []
    for t in todo.tasks.values():
        status = "done" if t.done else "pending"
        lines.append(f"[{t.id}] ({t.priority}, {status}) {t.title}")
    return "\n".join(lines)


@mcp.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as done, given its id."""
    try:
        todo.complete_task(task_id)
        return f"Task {task_id} marked as done."
    except TodoError as e:
        return f"Error: {e}"


@mcp.tool()
def delete_task(task_id: int) -> str:
    """Delete a task entirely, given its id."""
    try:
        todo.delete_task(task_id)
        return f"Task {task_id} deleted."
    except TodoError as e:
        return f"Error: {e}"


@mcp.tool()
def rename_task(task_id: int, new_title: str) -> str:
    """Rename an existing task, given its id and a new title."""
    try:
        todo.rename_task(task_id, new_title)
        return f"Task {task_id} renamed to '{new_title}'."
    except TodoError as e:
        return f"Error: {e}"


@mcp.tool()
def pending_count() -> str:
    """Return how many tasks are not yet done."""
    return f"{todo.pending_count()} task(s) pending."


if __name__ == "__main__":
    # Runs over stdio - the standard way local MCP servers communicate
    # with a connecting agent (no network port needed).
    mcp.run()

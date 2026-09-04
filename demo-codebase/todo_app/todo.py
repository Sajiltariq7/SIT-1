"""
A tiny in-memory to-do list app.

Intentionally small and self-contained so it can be used as a shared demo
codebase across multiple agentic coding tools (OpenCode, Pi, Cline, and
others) for a fair, side-by-side evaluation.
"""


class TodoError(Exception):
    """Raised for invalid to-do operations."""


class Task:
    def __init__(self, task_id: int, title: str, priority: str = "normal", done: bool = False):
        self.id = task_id
        self.title = title
        self.priority = priority  # "low", "normal", "high"
        self.done = done


class TodoList:
    def __init__(self):
        self.tasks: dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, title: str, priority: str = "normal") -> int:
        """Add a new task and return its id."""
        if not title.strip():
            raise TodoError("Task title cannot be empty")
        task_id = self._next_id
        self.tasks[task_id] = Task(task_id, title, priority)
        self._next_id += 1
        return task_id

    def complete_task(self, task_id: int) -> None:
        """Mark a task as done."""
        if task_id not in self.tasks:
            raise TodoError(f"Task {task_id} not found")
        self.tasks[task_id].done = True

    def delete_task(self, task_id: int) -> None:
        """Remove a task entirely."""
        if task_id not in self.tasks:
            raise TodoError(f"Task {task_id} not found")
        del self.tasks[task_id]

    def pending_count(self) -> int:
        """Return the number of tasks that are NOT done."""
        return sum(1 for task in self.tasks.values() if not task.done)

    def high_priority_pending(self) -> list[Task]:
        """Return all pending (not done) tasks with 'high' priority.

        NOTE: There is a known bug in this function. Use it as the
        "Debug" exercise: give a coding agent the failing test in
        tests/test_todo.py and ask it to find and fix the root cause.
        """
        # BUG: this checks task.done instead of `not task.done`, so it
        # returns completed high-priority tasks instead of pending ones.
        return [t for t in self.tasks.values() if t.priority == "high" and not t.done]
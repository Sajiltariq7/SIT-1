Continue (VS Code Extension) — Additional Free Tool
1. What is it?

Continue is an open-source AI code assistant that runs as a VS Code extension sidebar. It provides code chat, codebase context indexing, inline editing, and terminal integration.

2. Is it free? What did you actually use?

Continue itself is 100% free and open-source. For the model, I connected it via OpenRouter's free tier (meta-llama/llama-3.3-70b-instruct:free), requiring no purchase or paid credits.

3. Setup — reproducible steps
1. Install the Continue extension from the VS Code Marketplace
2. Open Continue settings (gear icon → Models)
3. Select OpenRouter as the provider, enter a free OpenRouter API key
4. Set the model to meta-llama/llama-3.3-70b-instruct:free
5. Open the demo-codebase project folder

Prerequisites: VS Code, Python 3.11+, pytest, a free OpenRouter API key.

4. Codebase understanding

Prompt used: "Inspect this repository. Summarize its purpose, map important files inside todo_app/, identify entry points, and explain the main data flow."

Continue correctly mapped the real files (todo_app/todo.py, main_interactive.py, tests/test_todo.py) and gave an accurate description of the data flow — task storage as a dictionary, auto-incrementing IDs, and how add/complete/delete/rename/query operations work. It used its built-in codebase indexing to gather this context directly, without needing manual terminal commands.

However, similar to OpenCode and Pi, it described the test suite as currently containing "one intentional failing test," when in fact my own test run showed all 9 tests passing, including test_high_priority_pending. This is the same pattern of stale/inaccurate claims seen across multiple tools in this evaluation — describing the codebase's original designed purpose (a bug that was intentionally added) as if it were still the current state, without verifying against actual test results. Evidence: evidence/Continue-1.PNG, evidence/Continue-2.PNG, evidence/Continue-3.PNG.

5. Project instructions, skills, plugins, MCP support
AGENTS.md: Yes, tested and accurate. When asked, Continue correctly summarized the real constraints: Python 3.11+, PEP 8, type hints required, no dependencies beyond pytest, and the protected method signatures that must not be changed. Evidence: evidence/Continue-4.PNG.
Skills: Not tested — Continue's documentation mentions support for custom slash commands, but I did not personally test this.
Plugins/extensions: Not tested in this session.
MCP: Not tested with Continue specifically. Continue's documentation states MCP servers can be configured via config.json, but I did not verify this myself, so I cannot confirm it beyond what's documented. (I did successfully test a real, working MCP server with OpenCode instead — see concepts/mcp.md.)
6. Practical task performed

Change task: Prompt: "Add a lightweight method clear_completed(self) -> int to TodoList in todo_app/todo.py that deletes all completed tasks from self.tasks and returns the count of removed tasks. Follow AGENTS.md guidelines." Continue attempted to automatically edit todo_app/todo.py using its built-in agent tool TWICE, and both attempts failed (shown as "Continue tried to edit todo_app/todo.py" with a red error indicator, and "Agent tool use" also failing). Evidence: evidence/Continue-agent-fail.PNG.

Rather than continuing to fight the automated tool, I changed my prompt to: "Write the Python code for adding a clear_completed(self) -> int method to TodoList in todo_app/todo.py. Do NOT use tool calls or edits — just show me the exact code block so I can paste it into todo.py." This worked — Continue returned a clean code block:

python
def clear_completed(self) -> int:
    """Delete all completed tasks and return the count of removed tasks."""
    completed_ids = [task_id for task_id, task in self.tasks.items() if task.done]
    for task_id in completed_ids:
        del self.tasks[task_id]
    return len(completed_ids)

I manually pasted this into todo_app/todo.py myself. Evidence: evidence/Continue-code-block.PNG.

Test verification: Ran python -m pytest -v myself afterward — all 9 tests passed, confirming the manually-added method didn't break anything. Evidence: evidence/Continue-5.PNG.

7. Permissions & approval workflow

Continue's automated file-editing tool failed twice when attempting to directly modify todo_app/todo.py — I never actually saw a diff/approval prompt for this change, because the automated edit itself never succeeded. The only way to get the change applied was to abandon the tool-based editing approach entirely, ask for plain code instead, and paste it into the file myself. This is a meaningfully different (and arguably safer, since it required full manual action) permission situation compared to Cline and OpenCode, which both reliably showed a diff and waited for a click-through approval before every change.

8. What worked well / what failed / what you had to fix manually

Worked well: Accurate codebase mapping using built-in indexing (no manual terminal commands needed). Clean, correctly-formatted code output once I switched to asking for a plain code block. AGENTS.md constraints were summarized accurately.

Failed: The automated agent tool-editing feature failed twice in a row when trying to directly edit a file. It also made an inaccurate claim about the test suite's current state, the same issue seen with OpenCode and Pi.

Had to fix manually: Had to abandon the automatic file-editing approach entirely and manually paste the generated code myself after the tool calls failed.

9. Best use cases, limitations, and recommendation

Continue felt strong for codebase Q&A and generating correct code snippets, but its automated file-editing was unreliable in this test, failing twice before I fell back to manual copy-paste. This is a real limitation worth being cautious about if reliable, autonomous file edits matter for your workflow. I would recommend Continue for chat-based code generation and explanation, but would lean on Cline or OpenCode instead for tasks that need dependable, automatic file edits with a clear approval step.
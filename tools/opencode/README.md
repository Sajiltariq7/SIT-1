OpenCode
1. What is it?

OpenCode is a terminal-based coding agent — you run it as a command-line tool (typed opencode in Command Prompt), rather than as a VS Code extension or separate desktop app.

2. Is it free? What did you actually use?

Yes, OpenCode itself is free and open-source (installed via npm, no cost). For the AI model, I first tried DeepSeek's API but hit an "Insufficient Balance" error, meaning DeepSeek's API actually requires a paid balance despite free account sign-up. I switched to OpenCode Zen — OpenCode's own built-in free-tier models — and used "Ling 3.0 Flash Fin Free," which required no external API key, account, or payment of any kind.

3. Setup — reproducible commands
bash
1. Install Node.js (nodejs.org) if not already installed
2. npm install -g opencode-ai
3. opencode --version   (to confirm install)
4. cd into the project folder
5. opencode             (launches the tool)
6. Selected a free OpenCode Zen model (Ling 3.0 Flash Fin Free) —
   no API key or account required

Prerequisites: Node.js installed.

One real issue encountered: DeepSeek's API gave an "Insufficient Balance" error despite being described as free to sign up for — this cost setup time and required switching providers entirely.

4. Codebase understanding

Prompt used: "Explain what this codebase does, map the important files, and describe the main data flow."

OpenCode correctly identified the project structure and file map (todo.py, cli.py, main_interactive.py, tests, AGENTS.md, README.md, requirements.txt) and correctly described the main data flow (TodoList holding a dict of Task objects, add_task/complete_task/delete_task mutating by ID, etc). It appears to have read every file directly rather than guessing — the screenshot shows it explicitly listing "Read todo_app\todo.py," "Read todo_app\cli.py," etc. before summarizing, rather than using a search-based or indexed approach.

However, it incorrectly stated that high_priority_pending() "currently has a bug," when in fact the bug had already been fixed and all 6 tests passed. I independently verified this by running python -m pytest tests -v myself, confirming all tests passed. This suggests OpenCode may have been pattern-matching against the function's docstring/comments describing the original bug, rather than fully verifying against the current, actual test results before making a claim — a real example of an "invented claim" that independent verification caught.

5. Project instructions, skills, plugins, MCP support

AGENTS.md: Yes, tested and followed. After being asked to read and follow it, OpenCode referenced its exact constraints unprompted in a later Plan step — listing "Python 3.11+, PEP 8, type hints on all function signatures, " "No external dependencies beyond pytest," "Don't change public method signatures of existing methods," and "Keep it simple" — and it followed all of them when implementing rename_task. Skills: Not tested — OpenCode doesn't appear to expose a distinct "skills" marketplace separate from prompting it directly. Plugins/extensions: Not tested in this session. MCP: Yes, tested. I built a simple MCP server in Python that lets an AI agent add, list, complete, delete, and rename tasks by calling the same TodoList code that already existed — without writing any new logic, just connecting to it. I set it up to work with OpenCode using a small settings file called opencode.json. When I asked OpenCode to use it, it worked correctly — it added a task and listed all tasks by calling the MCP tools directly, instead of editing any files. I could see exactly which actions it took, but I did not notice an approval step asking for permission before it ran them, which is different from how OpenCode normally asks before editing files. More details are in concepts/mcp.md.

6. Practical task performed

Change task: First used Plan mode with the prompt: "Add a rename_task(task_id, new_title) method to TodoList, following AGENTS.md constraints. Keep it short and simple." It returned a clear numbered plan citing the exact AGENTS.md constraints before touching any code. After switching to Build mode and approving, it implemented rename_task following the same validation pattern as the existing methods, and additionally wrote 3 new tests on its own initiative (covering success, empty title, and missing task cases) without being asked to. I then asked it to also wire the feature into main_interactive.py as a "6. Rename task" menu option, which it added consistently with the existing menu style. Evidence: evidence/OpenCode-4.PNG (the plan), evidence/OpenCode-5.PNG (the code diff), evidence/OpenCode-9.PNG (the menu integration diff), evidence/OpenCode-10.PNG (me using the rename option live through the app, renaming a task from "Cookinggg" to "cooking").

Debug task: When asked to explain the codebase, OpenCode incorrectly stated that high_priority_pending() "currently has a bug," when the bug had already been fixed in an earlier session and all 6 tests passed. I independently verified this by running pytest myself, confirming all tests passed. This is a real example of an inaccurate/invented claim, likely from pattern-matching against the function's docstring rather than checking actual test results. Evidence: evidence/OpenCode-1.PNG (full explanation), evidence/OpenCode-2.PNG (the specific inaccurate claim).

Test verification: After implementing rename_task, OpenCode tried to run tests with cd ... && pytest -v, which failed because PowerShell doesn't support && the way bash does. It self-corrected, tried plain pytest -v (failed, not recognized), then correctly used python -m pytest -v, which worked — reporting 9 passed (6 original + 3 new). I independently ran python -m pytest tests -v myself afterward and confirmed the same result. Evidence: evidence/OpenCode-3.PNG (early independent verification, 6 passed before the change), evidence/OpenCode-6.PNG (OpenCode's own test run showing self-correction and 9 passed), evidence/OpenCode-7.PNG (my own independent final verification, 9 passed).

Extend (MCP): I built and connected a custom MCP server exposing my TodoList code as callable tools (add_task, list_tasks, complete_task, delete_task, rename_task, pending_count). I asked OpenCode: "Use the todo-list-server MCP tools to add a task called Buy Milk with high priority, then list all tasks." It correctly called add_task and list_tasks through the MCP server and returned the right result, without editing any files. Evidence: evidence/OpenCode-MCP-1.PNG.

7. Permissions & approval workflow

OpenCode has a distinct two-mode system: Plan mode (toggled with Tab) only describes what it would do without touching any files, and Build mode actually applies changes. I used Plan mode first to review its intended approach before switching to Build mode and approving the actual implementation. This felt like a clear, explicit checkpoint compared to Cline's per-change diff approval — instead of approving each individual file edit, I approved the overall plan once, then it executed multiple related changes (the method plus its tests) together.

For the MCP tool calls specifically, this approval step was not as clear — I could see what actions were taken after the fact, but did not notice an explicit approval prompt before the MCP tools actually ran.

8. What worked well / what failed / what you had to fix manually

Worked well: The Plan mode gave a genuinely useful, specific breakdown before any code was touched, directly citing my project's AGENTS.md rules. It also added its own test coverage for the new feature without being asked, and successfully self-corrected through three different terminal command attempts (a PowerShell "&&" syntax error, then "pytest" not being recognized, then correctly falling back to "python -m pytest") until it found one that worked. It also correctly used the MCP server I built, calling the right tools with the right information.

Failed: It made an inaccurate claim during the Understand step, describing a bug that no longer existed, without seemingly running the tests to confirm claim first.

Had to fix manually: DeepSeek's API required a paid balance despite free sign-up, so I switched to OpenCode's own free built-in models (OpenCode Zen) instead. Also, like with Cline, changes were made in my working folder, separate from my Git repository — I had to manually copy the updated files over afterward.

9. Best use cases, limitations, and recommendation

OpenCode felt well-suited for slightly larger, multi-file changes where seeing an upfront plan (citing project rules) before execution is valuable — the Plan/Build split gives a clear review checkpoint before anything happens. Its self-correcting terminal behavior was reassuring, showing it can recover from environment-specific errors rather than failing outright. However, its tendency to state an inaccurate claim without verifying against actual test results is a real limitation worth being cautious about — I would recommend always independently verifying anything it says about the current state of the code, not just its claims about intended behavior. It also supports MCP servers well, which makes it a good option for connecting an AI agent to real, existing code in a safe, controlled way.
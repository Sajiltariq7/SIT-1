Pi Coding Agent

1. What is it?
Pi Coding Agent is a command-line (CLI) AI assistant that runs in your terminal or inside VS Code. It reads files, writes code, and runs terminal commands for you.

2. Is it free? What did you actually use?
- Tool Core: Yes, the tool itself is 100% free and open-source.
- Model Usage: Direct login requires paid plans, but I used it completely free by connecting an OpenRouter free API key (`openrouter/free`). I also tested a local offline model using Ollama (`llama3.2`).

3. Setup — reproducible commands
```bash
    1. Install Pi globally using npm
   npm install -g @earendil-works/pi-coding-agent
    2. Start Pi in your project folder
   pi
    3. Add your free OpenRouter key and select the free model inside Pi
   /config set openrouter.apiKey YOUR_OPENROUTER_KEY
   /model openrouter/meta-llama/llama-3.3-70b-instruct:free

4. Codebase understanding
Prompt Used: "Inspect this repository. Summarize its purpose, map important files, identify entry points, and explain the main data/control flow."
Local Model (llama3.2) Output: It created a markdown file todo_app.md on its own (Pi-1.PNG) and gave a basic summary, but missed some file details.
OpenRouter Free Model Output: It provided a structured table listing every file (todo_app/todo.py, main_interactive.py, tests/test_todo.py, AGENTS.md) and drew an ASCII diagram showing how data flows from the CLI to TodoList (Pi-6.PNG, Pi-7.PNG).
Context Gathering: Pi searched files directly in the terminal using cat and grep commands (Pi-4.PNG, Pi-5.PNG). When absolute path reads failed because of spaces in the folder name (SAJIL TARQ), Pi automatically ran find . -name "todo.py" to locate the file (Pi-7.PNG).

5. Project instructions, skills, plugins, MCP support
AGENTS.md Support: Yes (Supported and Tested). Pi read AGENTS.md (Pi-2.PNG) and confirmed constraints: Python 3.11+ style, type hints, pytest only, and keeping existing function signatures untouched.
Skills: Supported, but not tested.
Plugins/Extensions: Supported, but not tested.
MCP: Supported, but not tested on Pi (tested on OpenCode instead).

6. Practical task performed
Change task:
Prompt: "Add a lightweight method count_all(self) -> int to TodoList in todo.py that returns the total count of all the tasks (both pending and completed). Do not overwrite other methods."
Diff Produced: Added def count_all(self) -> int: returning len(self.tasks) right below pending_count (Pi-8.PNG).
Evidence Path: evidence/Pi-7.PNG, evidence/Pi-8.PNG
Debug task:
Prompt: "Run the tests and tell me if high_priority_pending currently has a bug or not."
Root cause found: Pi inspected todo_app/todo.py line 61-65 using grep and correctly stated the bug mentioned in test comments was already fixed (Pi-5.PNG).
Evidence Path: evidence/Pi-5.PNG
Test verification:
Command run: python -m pytest -v (Pi tried pytest -v first, got command not found, and auto-switched to python -m pytest -v) (Pi-8.PNG).
Output: 9 passed in 0.06s (100% pass) (Pi-8.PNG).
Evidence Path: evidence/Pi-8.PNG

7. Permissions & approval workflow
Pi executed terminal commands and modified files directly.
When using the local model, a malformed edit tool call failed with Validation failed for tool "edit" (Pi-3.PNG), which Pi tried to auto-fix.
When using OpenRouter, file edits (edit ./todo_app/todo.py) were applied directly without an interactive pop-up approval screen (Pi-8.PNG).

8. What worked well / what failed / what you had to fix manually
What Worked Well: Great self-correction. When path reads failed due to directory spaces (SAJIL TARQ), it ran find on its own (Pi-7.PNG). When pytest -v gave command not found (exit code 127), it automatically retried with python -m pytest -v (Pi-8.PNG).
What Failed: Local llama3.2 generated broken tool call parameters (oldText: "", newText: "X") (Pi-3.PNG).
What Was Fixed Manually: Switched the model inside Pi to OpenRouter free tier (openrouter/free) to get clean code edits and accurate repo maps (Pi-6.PNG).

9. Best use cases, limitations, and recommendation
Best Use Cases: Best for developers who like working in terminal/TUI interfaces and want fast autonomous command execution.
Limitations: Free local models struggle with tool-calling format. Needs a strong cloud model (like OpenRouter free 70B models) to work reliably.
Recommendation: Recommended for terminal users, as long as it is paired with OpenRouter free models rather than small local LLMs.
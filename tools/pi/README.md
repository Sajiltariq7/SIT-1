Pi Coding Agent
1. What is it?

Pi is a terminal-based coding agent — you run it as a command-line tool (typed pi in Command Prompt), similar in style to OpenCode, rather than a VS Code extension or desktop app.

2. Is it free? What did you actually use?

Pi itself is free and open-source (installed via npm). However, unlike OpenCode, Pi has no built-in free model — its /login command only offers paid subscription options (Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot). To use it for free, I had to manually configure a custom provider via a models.json config file. I first connected it to a fully local, offline model (Ollama's llama3.2, ~2GB, no account needed), then later upgraded to a free-tier model via OpenRouter (signed up using a work email, since I preferred not to use a personal account) after finding llama3.2's responses unreliable.

3. Setup — reproducible commands
1. npm install -g @mariozechner/pi-coding-agent
2. pi --version   (confirm install)
3. Tried /login inside Pi — only paid subscriptions offered, no free option
4. Installed Ollama (ollama.com), ran: ollama pull llama3.2
5. Created ~/.pi/agent/models.json manually with a custom "ollama"
   provider entry pointing to http://localhost:11434/v1
6. cd into project folder, ran: pi — confirmed "Model: llama3.2"
7. Later: signed up at openrouter.ai, got a free API key
8. In Pi: /login → OpenRouter → pasted the key
9. /model → selected a free OpenRouter model

Prerequisites: Node.js, and either Ollama installed locally OR a free OpenRouter account.

Real setup friction: no free option was available through Pi's own /login flow — required reading Pi's own documentation files directly to discover the custom models.json provider system before a genuinely free setup was possible.

4. Codebase understanding

With the local llama3.2 model: the response was vague and incomplete — it only mentioned todo_app/todo.py as an important file, missing cli.py, main_interactive.py, tests/, and AGENTS.md entirely, and described the app in generic terms rather than specifics. In a separate response, it directly contradicted itself: it displayed the real content of README.md, then in the same reply claimed that file was empty.

With the OpenRouter model: results were significantly better — it correctly mapped every relevant file (todo.py, cli.py, main_interactive.py, tests/test_todo.py, AGENTS.md), hit a real path bug (doubled drive letter when using its read tool) but self-corrected by switching to cd + cat commands, and gave an accurate description of the data flow. However, it still made one inaccurate claim, describing "a bug in high_priority_pending" despite having just displayed the already-fixed code — the same category of stale claim seen in OpenCode and Continue.

Evidence: evidence/Pi-llama-understand.PNG (vague version), evidence/Pi-openrouter-understand-1.PNG through -3.PNG (accurate version with the stale bug claim).

5. Project instructions, skills, plugins, MCP support
AGENTS.md: Yes, tested and followed — notably, Pi auto-loaded this file on startup without being asked at all (shown as "[Context] AGENTS.md"), a real difference from Cline/OpenCode/Continue, which all needed to be explicitly told to check it. When asked directly, it correctly summarized all 4 real constraints (Python 3.11+/PEP 8, type hints, no dependencies beyond pytest, protected method signatures).
Skills: Not tested — no distinct skills marketplace observed.
Plugins/extensions: Not tested in this session.
MCP: Not tested with Pi specifically (tested separately with OpenCode — see concepts/mcp.md).
6. Practical task performed

Change task (llama3.2): Asked it to add a mark_all_complete() method. It produced a malformed tool call, then on retry proposed an edit that appeared to attempt overwriting the entire file's content with just the letter "X" (oldText: "", newText: "X", range covering the whole file). I did NOT approve this — flagged as a serious reliability/safety concern likely caused by the small local model's limited tool-calling ability. Evidence: evidence/Pi-destructive-edit.PNG.

Change task retry (OpenRouter, simpler request): Asked it to add a one-line count_all() method. It checked the actual current code first (grep) and discovered count_all() already existed from an earlier session, correctly recognizing this instead of creating a duplicate — careful, non-destructive behavior, a clear improvement over the earlier incident. Evidence: evidence/Pi-count-all-check.PNG.

Debug-related finding: When simply asked to explain the codebase, Pi claimed a bug existed that had already been fixed. When explicitly asked "Run the tests and tell me if high_priority_pending currently has a bug or not," it actually ran pytest and read the real code, then gave an accurate answer: "No bug currently... It excludes completed high-priority tasks and includes only pending ones." This is a valuable, nuanced finding — Pi was more accurate when explicitly asked to verify than when just asked to explain. Evidence: evidence/Pi-bug-verify.PNG.

Test verification: Ran python -m pytest tests -v myself independently — 9 passed, matching what Pi reported. Evidence: evidence/Pi-verify.PNG.

7. Permissions & approval workflow

This varied significantly by situation. Early in testing, Pi wrote a new file (todo_app.md) directly to disk with NO approval prompt at all — a real difference from Cline and OpenCode, which always required explicit approval before any file change. Separately, when it proposed the potentially destructive "X" edit, I was able to see and reject the proposed change before it was applied — so in that specific case, there was a visible checkpoint I could act on, even though the earlier file write had none. This inconsistency (approval sometimes shown, sometimes not) is itself worth noting as a real observation.

8. What worked well / what failed / what you had to fix manually

Worked well: Auto-loading AGENTS.md on startup without being asked. Self-correcting through a real path bug (doubled drive letter) by switching command approaches. With a better model, carefully checking existing code before adding something that might already exist. When explicitly asked to verify (not just explain), it gave an accurate answer about the bug status.

Failed: With the local model, gave an incomplete/vague codebase summary, once directly contradicted itself, wrote a file with no approval prompt, and proposed what looked like a destructive whole-file overwrite that had to be rejected. Made an inaccurate claim about a fixed bug when simply asked to explain (before being asked to verify).

Had to fix manually: No free model was available through Pi's built-in login — had to read Pi's own documentation files directly and manually create a models.json config file to connect a free local model, then later switch again to get a more reliable free cloud model via OpenRouter.

9. Best use cases, limitations, and recommendation

Pi's actual capability seemed to depend heavily on which model was connected to it — the free local model (llama3.2) was noticeably less reliable and even risked a destructive action, while the free OpenRouter model performed comparably to OpenCode and Continue. Given the extra setup effort required just to get a genuinely free option working, and the inconsistent approval behavior observed, I would recommend Pi mainly for users comfortable with manual configuration and who pair it with a capable model — and would suggest always double-checking any proposed edit carefully, given the destructive edit attempt observed here with a weaker model.
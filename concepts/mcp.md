# MCP (Model Context Protocol)

MCP:  Stands for Model Context Protocol, which acts as a universal plug that lets AI models to connect to external tools like apps, files, databases easily, removing the need to build a unique connection for every single service.
How It Works: An MCP server acts as a bridge between AI Assistants and external resources. It provides a specific set of tools that AI can ask to use, such as searching data or reading files, and sends the result back.
Security: Connecting to an MCP server means sharing data, security prompts are built-in. These require a human user to review and approve actions before AI executes them.
Safe Usage: Its safe to Always authenticate and verify who created MCP server before trusting it with work.


MCP is an underlying rulebook or universal language protocol that defines how AI application and external data sources should talk to each other, like HTTP 
MCP Server is a running program that actually uses those rules to provide specific tools and data. Its a physical plug-in that connects to a database, a file system or an API so your AI can access it.

AI application(client) uses MCP standard to talk to an MCP Server, which fetches the actual data or performs the action asked for.



Problem it solves:

How does an MCP server expose tools/context to an agent? An MCP server is a small, separate program that exposes a defined list of "tools" — specific actions the agent is allowed to call. When the agent needs to do one of these actions, it sends a request to the server, the server performs the real work, and sends a result back.

What are the security implications of connecting an agent to an MCP server? An MCP server runs locally with the same permissions as the user who started it — it isn't sandboxed or restricted automatically. This means only servers you wrote yourself or fully trust should be connected, since a malicious or poorly built one has the same access to your system that you do. Visibility (seeing what a tool call did) is not the same as approval (being asked before it happens) — this distinction matters when judging how safe a given MCP setup actually is.

Did you test an MCP server yourself? Yes. I built a small Python MCP server (using the official MCP SDK) that wraps the existing TodoList class from my demo codebase as a set of callable tools (add_task, list_tasks, complete_task, delete_task, rename_task, pending_count) — without duplicating any of its logic. I connected it to OpenCode via an opencode.json config file specifying it as a local MCP server.

Setup: Built a Python MCP server wrapping the existing TodoList class as callable tools, connected it to OpenCode via an opencode.json config file.
Value: Lets an AI agent perform real actions (add/list/complete tasks) through defined tools instead of editing files directly — safer and more precise for simple, repeatable operations, since the underlying logic is never touched or risked.
Permissions: OpenCode showed the exact tool calls being made (add_task, list_tasks) in its reasoning trace, so I had visibility into what happened — but I did not see an explicit approval prompt before the actions ran, unlike its file-editing workflow which always requires a click-through approval first.
Risk: The MCP server runs locally with my own user permissions, so only connecting servers whose code you trust matters. Since I wrote this one myself, I know exactly what it can and can't do — but a downloaded/unknown MCP server would carry real risk, since it has the same access to the system as any other program you run.
# MCP (Model Context Protocol)

MCP:  Stands for Model Context Protocol, which acts as a universal plug that lets AI models to connect to external tools like apps, files, databases easily, removing the need to build a unique connection for every single service.
How It Works: An MCP server acts as a bridge between AI Assistants and external resources. It provides a specific set of tools that AI can ask to use, such as searching data or reading files, and sends the result back.
Security: Connecting to an MCP server means sharing data, security prompts are built-in. These require a human user to review and approve actions before AI executes them.
Safe Usage: Its safe to Always authenticate and verify who created MCP server before trusting it with work.


MCP is an underlying rulebook or universal language protocol that defines how AI application and external data sources should talk to each other, like HTTP 
MCP Server is a running program that actually uses those rules to provide specific tools and data. Its a physical plug-in that connects to a database, a file system or an API so your AI can access it.

AI application(client) uses MCP standard to talk to an MCP Server, which fetches the actual data or performs the action asked for.

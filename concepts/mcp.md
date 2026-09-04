# MCP (Model Context Protocol)

Answer each in your own words (2-4 sentences each):

1. **What problem does MCP solve?**
   (Think: before MCP, every tool had to build custom integrations to every
   data source/API. What does MCP standardize?)

2. **How does an MCP server expose tools/context to an agent?**
   (In plain terms: a small server process that the agent can call, which
   exposes a defined set of "tools" — e.g. read a file, query a database,
   search the web — that the agent can invoke during a conversation.)

3. **What are the security implications of connecting an agent to an MCP
   server?**
   (Consider: the server can see everything you send it; a malicious or
   compromised server could exfiltrate data; the agent may execute actions
   the server "suggests." Why does permission/approval matter here specifically?)

4. **Did you test an MCP server yourself? What did you connect, what tool
   did it expose, and what would you check before trusting one in a real
   team environment?**

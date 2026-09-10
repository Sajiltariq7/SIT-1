# Agentic Coding Tools — Evaluation Submission

## Purpose
This submission documents hands-on testing of several agentic coding
tools (OpenCode, Pi Coding Agent, Cline, and Continue as the additional
free tool, plus Google Antigravity and OpenAI Codex where access
allowed) against a shared demo codebase, to evaluate practical fit for a
developer workflow — using only free-tier access throughout, with no
paid subscriptions or purchased credits.

## Tools tested

| Tool | Status | Report |
|---|---|---|
| OpenCode | Tested (+ MCP Extend) | [tools/opencode/README.md](tools/opencode/README.md) |
| Pi Coding Agent | Tested | [tools/pi/README.md](tools/pi/README.md) |
| Cline | Tested | [tools/cline/README.md](tools/cline/README.md) |
| Continue | Tested | [tools/additional-free-tool/README.md](tools/additional-free-tool/README.md) |
| Google Antigravity | Access-limited (documented) | [tools/antigravity/README.md](tools/antigravity/README.md) |
| OpenAI Codex | Access-limited (documented) | [tools/codex/README.md](tools/codex/README.md) |

## Demo codebase
All tools were run against the same codebase: [demo-codebase/](demo-codebase/)
— a small Python to-do list app with one intentional bug, used
consistently for the Understand / Instruct / Change / Debug / Verify
steps across every tool. A working custom MCP server built on top of this
same codebase is included at [demo-codebase/mcp-demo/](demo-codebase/mcp-demo/).

## Concepts
- [Skills](concepts/skills.md)
- [Plugins & Extensions](concepts/plugins-and-extensions.md)
- [MCP](concepts/mcp.md)
- [Project Instructions](concepts/project-instructions.md)

## Comparison & recommendation
See [comparison.md](comparison.md) for the full side-by-side table and
final team recommendation.

## Evidence
Screenshots, command logs, and test output referenced throughout the
tool reports are stored in [evidence/](evidence/).

## Overall conclusion
The single biggest takeaway from this evaluation is that agentic coding
tools can state things confidently that are inaccurate — three separate
tools (OpenCode, Pi Coding Agent, and Continue) independently claimed a
bug existed in the codebase when it had already been fixed, each
apparently pattern-matching against old comments rather than verifying
against actual test results. Independent verification (always running
the tests myself, reading the actual code) was essential throughout this
evaluation, not optional. Approval and safety behavior also varied
significantly between tools — Cline and OpenCode consistently required
explicit approval before any file change, while Pi and Continue both had
at least one instance of unapproved or failed automated editing. For a
team prioritizing safety and predictable review, Cline is the strongest
recommendation; for terminal-first workflows needing extensibility (as
shown by successfully building and connecting a working MCP server),
OpenCode is a strong second choice. Personally, I would reach for Cline
first for day-to-day reviewed changes, and OpenCode when I need a
terminal-based tool with a clear plan-before-action workflow.

## Tools not fully tested
Google Antigravity and OpenAI Codex were checked for free/existing
access; neither was available without a paid plan at the time of
testing. Per the assignment's own guidance, both are documented as
honest access-limitations rather than tested — see their individual
README files above for details.
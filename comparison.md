 Tool Comparison

All four tools were tested against the same shared codebase
(`demo-codebase/`, a Python to-do list app) using comparable prompts for
each step, so this comparison reflects real, consistent testing rather
than isolated impressions.

 Comparison table

| Criterion | Cline | OpenCode | Pi Coding Agent | Continue |
|---|---|---|---|---|
| **Access & setup** | Easy — DeepSeek via Cline's own free built-in credits, no personal sign-up needed | Easiest — genuinely free built-in models (OpenCode Zen), zero setup friction | Hardest — no free option via login, required manually editing a config file and installing/connecting an external model | Moderate — free extension, but required an external OpenRouter sign-up |
| **Codebase understanding** | Accurate; caught and fixed a stale bug comment on its own | Mostly accurate, but made one inaccurate claim about an already-fixed bug | Highly inconsistent — vague/self-contradictory with a weak local model, accurate with a stronger one, but still repeated the same inaccurate bug claim | Accurate file mapping, but also repeated the same inaccurate bug claim as OpenCode and Pi |
| **Planning & edits** | Clear diffs shown before every change; built a working interactive menu app matching the exact requested scope | Distinct Plan-then-Build workflow citing project rules before executing; added its own test coverage unprompted | Ranged from a dangerous, malformed edit attempt (weak model) to careful, non-duplicating edits (stronger model) | Automated editing failed twice in a row; only succeeded after switching to a manual copy-paste workflow |
| **Terminal & VS Code fit** | Fully inside VS Code; smooth, single-window experience | Standalone terminal tool; self-corrected through real PowerShell/pytest command errors | Standalone terminal tool; also self-corrected through a path-related bug | Fully inside VS Code; used built-in codebase indexing instead of manual terminal commands |
| **Tests & debugging** | Verified test results correctly, always matched independent checks | Verified test results correctly, but the claim about bug status was inaccurate before the fix was even attempted | Accuracy depended on HOW it was asked — gave a wrong answer when just asked to "explain," but a correct one when explicitly asked to "verify" | Verified test results correctly after the manual fix was applied |
| **Customization (AGENTS.md)** | Followed correctly when explicitly pointed to the file | Followed correctly, referenced rules unprompted in a later planning step | Auto-loaded the file on startup without being asked — the only tool to do this | Followed correctly when asked |
| **Safety & control** | Strongest — every single change required an explicit approval click, no exceptions observed | Strong — Plan/Build split gives a clear review checkpoint; MCP tool calls were visible but not explicitly approval-gated | Weakest — inconsistent; one file was written with no approval at all, and one proposed edit looked destructive (correctly rejected) | Mixed — no unapproved automatic edits occurred, but only because automatic editing failed outright, forcing manual action instead |
| **Overall fit** | Best for beginners and careful, reviewed changes inside a familiar editor | Best for terminal-first workflows needing a clear plan-before-action structure, and for MCP/tool integrations | Best only when paired with a strong model and used cautiously; needs more setup effort for genuinely free use | Best for quick codebase Q&A and code generation; less reliable for autonomous file editing |

 Notes per criterion
 Comparison table

| Criterion | Cline | OpenCode | Pi Coding Agent | Continue |
|---|---|---|---|---|
| **Access & setup** | Easy — DeepSeek via Cline's own free built-in credits, no personal sign-up needed | Easiest — genuinely free built-in models (OpenCode Zen), zero setup friction | Hardest — no free option via login, required manually editing a config file and installing/connecting an external model | Moderate — free extension, but required an external OpenRouter sign-up |
| **Codebase understanding** | Accurate; caught and fixed a stale bug comment on its own | Mostly accurate, but made one inaccurate claim about an already-fixed bug | Highly inconsistent — vague/self-contradictory with a weak local model, accurate with a stronger one, but still repeated the same inaccurate bug claim | Accurate file mapping, but also repeated the same inaccurate bug claim as OpenCode and Pi |
| **Planning & edits** | Clear diffs shown before every change; built a working interactive menu app matching the exact requested scope | Distinct Plan-then-Build workflow citing project rules before executing; added its own test coverage unprompted | Ranged from a dangerous, malformed edit attempt (weak model) to careful, non-duplicating edits (stronger model) | Automated editing failed twice in a row; only succeeded after switching to a manual copy-paste workflow |
| **Terminal & VS Code fit** | Fully inside VS Code; smooth, single-window experience | Standalone terminal tool; self-corrected through real PowerShell/pytest command errors | Standalone terminal tool; also self-corrected through a path-related bug | Fully inside VS Code; used built-in codebase indexing instead of manual terminal commands |
| **Tests & debugging** | Verified test results correctly, always matched independent checks | Verified test results correctly, but the claim about bug status was inaccurate before the fix was even attempted | Accuracy depended on HOW it was asked — gave a wrong answer when just asked to "explain," but a correct one when explicitly asked to "verify" | Verified test results correctly after the manual fix was applied |
| **Customization (AGENTS.md)** | Followed correctly when explicitly pointed to the file | Followed correctly, referenced rules unprompted in a later planning step | Auto-loaded the file on startup without being asked — the only tool to do this | Followed correctly when asked |
| **Safety & control** | Strongest — every single change required an explicit approval click, no exceptions observed | Strong — Plan/Build split gives a clear review checkpoint; MCP tool calls were visible but not explicitly approval-gated | Weakest — inconsistent; one file was written with no approval at all, and one proposed edit looked destructive (correctly rejected) | Mixed — no unapproved automatic edits occurred, but only because automatic editing failed outright, forcing manual action instead |
| **Overall fit** | Best for beginners and careful, reviewed changes inside a familiar editor | Best for terminal-first workflows needing a clear plan-before-action structure, and for MCP/tool integrations | Best only when paired with a strong model and used cautiously; needs more setup effort for genuinely free use | Best for quick codebase Q&A and code generation; less reliable for autonomous file editing |

 Access & setup
Cline and OpenCode both had low-friction, genuinely free paths built into
the tool itself. Pi required discovering and manually editing a
`models.json` config file, and Continue required an external account
(OpenRouter) despite being a free extension — see
`tools/pi/README.md` and `tools/additional-free-tool/README.md` for full
setup logs.

 Codebase understanding
A striking pattern across this evaluation: **OpenCode, Pi, and Continue
all made the same category of inaccurate claim** — describing a bug in
`high_priority_pending()` as currently existing, when it had already been
fixed and all tests passed. This happened independently across three
different tools and, in Pi's case, two different underlying models —
suggesting this is a common failure mode (matching stale docstrings/
comments over verifying actual current test results) rather than a
one-off mistake. See each tool's README, section 4, for evidence.

 Planning & edits
Cline and OpenCode both produced clean, working changes with clear
before/after visibility. Pi's results depended heavily on model quality —
a weak local model nearly produced a destructive edit, while a stronger
model behaved carefully. Continue's automated editing failed outright
twice, and only a full manual workaround got the feature implemented.

 Terminal & VS Code fit
The two VS Code extensions (Cline, Continue) offered a more integrated,
single-window experience. The two terminal tools (OpenCode, Pi) both
demonstrated real self-correction through genuine command-line errors
(PowerShell syntax, path bugs), which was reassuring even though the
initial errors themselves were a minor friction point.

 Tests & debugging
All four tools could correctly run and report test results when asked
directly. The more interesting finding was behavioral: Pi's accuracy
changed significantly based on phrasing — asking it to "explain" produced
a wrong answer, while asking it to "verify" produced a correct one. This
suggests the way a task is phrased can matter as much as the tool itself.

 Customization
All four tools successfully read and followed the same `AGENTS.md` rules
file (Python style, type hints, dependency limits, protected method
signatures) when tested. Pi stood out by loading this file automatically
on startup, without being asked — a small but genuine convenience
advantage.

 Safety & control
This was the most differentiating criterion. Cline was the most
consistent — every single observed change required explicit approval.
Pi was the least consistent — approval was sometimes present, sometimes
completely absent, including one case with real destructive potential.
Continue avoided any unapproved automatic edits only because its
automated editing failed technically, not by design.

 Final recommendation

For a team prioritizing safety and predictable review before every
change, **Cline** is the strongest choice — its approval-first workflow
never failed to ask, and its VS Code integration keeps everything in one
place for less experienced developers. For teams wanting a fast, capable
terminal-first tool with genuinely zero-friction free access and useful
extensibility (as shown by successfully connecting a custom MCP server),
**OpenCode** is a strong second choice, particularly for slightly larger,
multi-file changes thanks to its Plan/Build workflow.

Pi Coding Agent and Continue both showed real capability but with notable
caveats: Pi's reliability was closely tied to which model was connected,
and its permission behavior was inconsistent enough to warrant caution in
a team setting. Continue's automated file-editing proved unreliable in
this test, though it performed well for codebase explanation and code
generation when a human handled the final step manually.

Across all four tools, the single most important lesson from this
evaluation is that **AI agents can state inaccurate things confidently**
unless they are made to actually verify against ground truth (like
running tests) — a habit of independent verification, regardless of which
tool is used, is not optional but essential.
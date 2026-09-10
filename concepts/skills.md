# Skills

Skills: Saved set of instructions or rules, that teaches an AI Agent how
to do a specific job. Prevent retyping same rules repeatedly, a skill
stays active in the background ensuring that agent follows
project-specifications automatically.

Skills are modular packages of instructions, scripts, or guidelines given
to an AI agent to teach it how a specific, repeatable workflow should
work in a project.

AI's don't know your specific project's tech stack, naming conventions,
or deployment rules unless you tell them. Skills save time because you
don't have to retype instructions in every single prompt; the agent
loads the skill file and follows the rules automatically.

WORKING (How does a tool discover or load a skill): In general, a tool
would read setup files and folders in the project directory when you
open it, automatically scanning these configuration files on startup so
it knows what rules to follow.

REUSABLE SKILLS (When is a reusable skill actually useful vs.
unnecessary overhead): A reusable skill is extremely useful when working
on team projects that need strict, repetitive formatting rules the agent
needs to follow. On the other hand, it is a waste of time for quick,
simple tasks where it is faster to just tell the AI what to do directly.

TOOL: None of the four tools I actually tested in this assignment
(Cline, OpenCode, Pi Coding Agent, Continue) exposed a separate,
distinct "skills" system beyond just prompting the agent directly. What
I did test across all four was project-instruction files (AGENTS.md),
which achieve a similar goal — giving an agent persistent rules without
retyping them — see project-instructions.md for those specific findings.
# Cline (VS Code Extension)

## 1. What is it?
Cline is a VS code extension, an AI coding agent that doesnt have its own brain and connects to any AI model of your choice via API. It runs inside an editor and can answer all the relevant queries directly into the project.


## 2. Is it free? What did you actually use?
Yes it is free to install directly from VS code extensions. As it requires connectivity, I have used DeepSeek's Free API to function

## 3. Setup — reproducible commands
```bash
1. Install VS Code
2. Open VS Code → Extensions panel → search "Cline" → Install
3. Click the Cline icon in the sidebar → select DeepSeek as provider →
   paste free DeepSeek API key
4. File → Open Folder → select the demo-codebase project
```

## 4. Codebase understanding
Prompt used: "Explain what this codebase does, map the important files, and describe the main data flow."
Cline corectly identified the project as a todo list app built, correctly mapped each content and described the data flow.

## 5. Project instructions testng
Agents: Yes, tested and followed. When asked to read and follow it. Cline obeyed and respected all the instructions, constraint by not changing existing file. Confirmed its own explanation after building main_interactive.py.

## 6. Practical task performed
CHANGE TASK: Prompted to add a new file main_interactive.py to the project....Cline proposed and created a 44-line interactive menu app .Evidence:
  evidence/Cline-3.PNG (proposed diff), evidence/Cline-5.PNG (me running
  it myself, adding/completing/viewing a task).
DEBUG TASK: Asked Cline to explain the codebase and check for issues. It independently noticed that a code comment describing a "known bug" in high_priority_pending() no longer matched the actual code — the bug had already been fixed in an earlier session, but the comment was stale and still described the old broken behavior. Cline confirmed via pytest that all 6 tests currently passed, then asked whether to update the comment. I approved the cleanup. Evidence: evidence/Cline-1.PNG (it flagging the mismatch), evidence/Cline-2.PNG (the diff fixing the stale comment, plus
6 passed).
TEST VERIFICATION: Cline ran pytest itself and reported all test passing. I independently ran pytest myself afterward and confirmed the same result.  Evidence: evidence/Cline-4.PNG (duplicate folder cleanup + re-
  verification), evidence/Cline-6.PNG (my own final independent test run).


## 7. Permissions & approval workflow
Cline always showed a proposed plan or diff before making any file change, with explicit Save/Reject buttons, and waited for my approval before applying anything. It also had an "Auto-approve" toggle (visible as "Auto-approve: Read, Commands" in my screenshots) controlling which actions it could take automatically — but file edits still required my manual click-through in every case I tested. When it wanted to delete a stray duplicate folder, it explained exactly what it would remove before asking permission (evidence/Cline-4.PNG).

## 8. What worked well / what failed / what you had to fix manually
It correctly diagnosed and fixed a logical bug with an accurate explanation, caught an unrelevant issue on its own and asked before making any change.
MANUAL FIX: main_interactive.py was created inside the VS Code
workspace folder I had open, which was not the same folder as my Git
repository — I had to manually copy the file into my repo folder afterward
so it would be tracked by Git. This wasn't really a Cline mistake, more a
workflow detail I had to manage myself.

## 9. Best use cases, limitations, and recommendation
I'd recommend Cline for small, scoped, in-editor tasks like bug fixes and
small feature additions, where seeing a diff and approving each change
before it happens matters. It felt well-suited for a beginner because
everything stays visible inside VS Code rather than a separate terminal
window.



What I personally learned testing Cline: it's genuinely useful for reviewing changes before they happen since every edit shows a diff first, but I had to stay alert about which folder it was actually working in, since it doesn't automatically sync with my separate Git repo folder.
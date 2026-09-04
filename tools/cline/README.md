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
CHANGE TASK: Prompted to add a new file main_interactive.py to the project....
DEBUG TASK: Run the test and find out the root cause of bug in test_high_priority_pending is failing then fixing it
TEST VERIFICATION:Cline ran pytest itself and reported all test passing  


## 7. Permissions & approval workflow
Cline always showed a proposed a plan before making any file change and waited for me to approve before responding.

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

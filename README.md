
```markdown
# Evolution of Todo: Phase 1 (In-Memory Console App)

## 🚀 Project Overview
This project represents **Phase 1** of the "Evolution of Todo" Hackathon II. It is a Spec-Driven, AI-native console application built using Python, Typer, and Rich. The application demonstrates the core principles of "Agentic Development" where the architecture is defined by specifications (`.spec-kit`) and implemented by AI agents.

## 🎯 Phase 1 Objectives
- **Core Functionality:** Create a CLI-based Task Manager.
- **Data Persistence:** In-memory / JSON-file based storage (`tasks.json`).
- **Development Methodology:** Strict Spec-Driven Development (SDD) using Spec-Kit Plus.
- **Tooling:** Python 3.13, Typer, Rich.

## 🏗️ Project Structure
This repository follows the **Spec-Kit Plus** monorepo standard:


```

.
├── .spec-kit/          # Spec-Kit configuration
├── specs/              # Source of Truth (Specifications)
│   ├── features/       # Feature requirements (phase1.md)
│   ├── api/            # API definitions
│   └── database/       # Schema definitions
├── backend/            # Application Source Code
│   └── src/
│       └── main.py     # Entry point (Typer App)
├── AGENTS.md           # The Constitution for AI Agents
├── CLAUDE.md           # Shim for Claude Code context
├── tasks.json          # Local storage (Gitignored in production)
└── requirements.txt    # Python dependencies

```

## ✨ Features Implemented
- [x] **Add Task:** Create new tasks with titles.
- [x] **List Tasks:** View all tasks in a formatted Rich table.
- [x] **Update Task:** Mark tasks as "Completed" (Green status).
- [x] **Delete Task:** Remove tasks by ID.
- [x] **Persistence:** Tasks survive application restarts via JSON.

## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **CLI Framework:** [Typer](https://typer.tiangolo.com/)
- **UI/Formatting:** [Rich](https://rich.readthedocs.io/)
- **Methodology:** Spec-Kit Plus (Panaversity)

## ⚡ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/evolution-of-todo-phase1.git](https://github.com/YOUR_USERNAME/evolution-of-todo-phase1.git)
   cd evolution-of-todo-phase1

```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Application:**
```bash
# Add a task
python backend/src/main.py add "Finish Hackathon Phase 1"

# List tasks
python backend/src/main.py list

# Complete a task
python backend/src/main.py complete 1

# Delete a task
python backend/src/main.py delete 1

```



## 📜 Constitution (Spec-Driven Rules)

This project adheres to the rules defined in `AGENTS.md`:

1. No code generation without a referenced Task ID.
2. Workflow: **Specify → Plan → Tasks → Implement**.
3. Strict adherence to Python 3.13 and Typer.

---

*Submitted by Muhammad Bilal Khalid for GIAIC Hackathon II (Saturday Afternoon).*

```

### ⚡ Quick Git Commands to Push NOW
Run these inside your project folder (`Hackathon_Phase1_Submission`):

```powershell
# Create the README file
Set-Content -Path README.md -Value "PASTE_THE_CONTENT_ABOVE_HERE"

# Add and Push
git add README.md
git commit -m "Add Phase 1 Documentation"
git push -u origin main

```

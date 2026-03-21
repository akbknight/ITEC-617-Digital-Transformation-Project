# Quick Start: Claude Code

This guide walks you through setting up and using the Enterprise IT Navigator Simulation with Claude Code. This path is for students who have a Claude Pro subscription.

## Prerequisites

You need the following before you begin:

| Prerequisite | How to Check | Install Link |
|-------------|-------------|-------------|
| **Git** | Open a terminal and type `git --version` | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **VS Code** (recommended) | Open VS Code — if it launches, you're set | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Claude Pro** | Sign in at [claude.ai](https://claude.ai/) and check your plan | [$20/month subscription](https://claude.ai/) |

> **Opening a terminal**: On Mac, press `Cmd+Space` and type "Terminal". On Windows, press the Windows key and type "Command Prompt" or "PowerShell".

## Step 1: Get Claude Pro

1. Go to [https://claude.ai/](https://claude.ai/).
2. Create an account or sign in.
3. Subscribe to Claude Pro ($20/month). This gives you access to Claude Code with usage included in your subscription.

## Step 2: Install Claude Code

You have two options for running Claude Code. Choose whichever fits your workflow.

### Option A: VS Code Extension (Recommended)

1. Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/) if you do not already have it.
2. Open VS Code.
3. Open the Extensions panel: press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac).
4. Search for "Claude Code" and install the extension.
5. When prompted, sign in with your Anthropic account.

### Option B: Command-Line Interface (CLI)

1. Install Node.js from [https://nodejs.org/](https://nodejs.org/) (LTS version recommended).
2. Open a terminal and run:

```bash
npm install -g @anthropic-ai/claude-code
```

3. Start Claude Code by running:

```bash
claude
```

4. Follow the prompts to sign in with your Anthropic account.

## Step 3: Create Your Team's Repo and Clone It

Each team creates their own private copy using GitHub's template feature.

1. Go to [github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach](https://github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach).
2. Click the green **"Use this template"** button near the top right.
3. Select **"Create a new repository"**.
4. Name your repo (e.g., `Team-Name-DT-Project`).
5. Set visibility to **Private** (recommended).
6. Click **"Create repository"**.

Then clone **your new repo**:

1. Open a terminal (or use the terminal in VS Code).
2. Navigate to the directory where you want to store the project.
3. Run the following command (replace with your actual repo URL):

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

4. If using VS Code, open the cloned folder: **File > Open Folder**, then select your repo folder.
5. If using the CLI, navigate into the cloned directory: `cd YOUR-REPO-NAME`

> **Don't have Git?** Install it from [git-scm.com/downloads](https://git-scm.com/downloads). Choose the installer for your operating system and accept the default options. After installing, **restart your terminal** before running the clone command.

## Step 4: Fill In Your Project Brief

The simulation relies on your project brief to provide relevant feedback. Fill it in thoroughly.

### Bring Your Existing Work (Optional)

If you have already completed earlier assignments (Team Charter, Industry/Company selection, etc.), drop copies of those deliverables (PDF, DOCX, or TXT) into `student-workspace/source-docs/`. The setup assistant will extract relevant context from them, saving you from re-entering information you have already worked on.

### Option A: Interactive Setup (Recommended)

Let Claude walk you through each section conversationally:

1. In Claude Code, type `/setup-project`.
2. Claude will detect your current assignment milestone, scan for any source documents in `student-workspace/source-docs/`, and adapt its questions to your stage in the project. Early-stage students get focused guidance on company/industry selection; later-stage students dive deeper into financials and change management.
3. After gathering your answers, it writes the completed brief and reviews it for quality — flagging vague areas calibrated to what is expected at your milestone.
4. For students working on ROI (Assignment 5) or OCM (Assignment 6), the setup flow can also fill in the companion templates at `student-workspace/roi-summary.md` and `student-workspace/ocm-assessment.md`.

This takes about 10-15 minutes and ensures every section has the specificity that executive personas expect. Run it again whenever you advance to the next assignment.

### Option B: Manual Editing

If you prefer to fill in the brief yourself:

1. Open `student-workspace/project-brief.md`.
2. Complete every section:
   - **Team Information**: Team name, member names, date
   - **Target Company**: Company name, industry, business unit, size
   - **Business Problem**: The specific challenge or opportunity (use data)
   - **Proposed Technology Solution**: The emerging technology and how it addresses the problem
   - **Primary Benefit Type**: Select one category
   - **Proposed Timeline**: Pilot duration and key milestones
   - **Initial Financial Estimate**: Pilot cost, expected ROI, funding source
   - **Key Risks**: Top 3-5 identified risks
   - **Stakeholders**: Affected groups and their concerns
   - **Additional Notes**: Any other relevant context
3. Save the file.

## Step 5: Start the Simulation

1. Open Claude Code:
   - **VS Code**: Open the Claude Code panel from the sidebar.
   - **CLI**: Run `claude` from the project directory.
2. Ask Claude to analyze your project and recommend executive personas. For example:

> Please read my project brief in student-workspace/project-brief.md, analyze it against the rubrics in the rubrics/ directory, and recommend which executive personas I should consult first.

Claude will read your project brief and provide an assessment of strengths, gaps, and a recommended consultation sequence.

## Step 6: Consult Executive Personas

Use slash commands to activate persona consultations. Each executive will introduce themselves, read your project brief, and begin a challenging conversation from their perspective.

| Command | Executive | Focus Areas |
|---------|-----------|-------------|
| `/cio` | Jordan Chen, CIO | IT strategy, governance, enterprise architecture |
| `/ciso` | Anika Patel, CISO | Cybersecurity, risk, privacy, compliance |
| `/cfo` | Robert Okafor, CFO | Financial analysis, ROI, TCO, budget impact |
| `/coo` | Maria Santos, COO | Operations, implementation, pilot design |
| `/chro` | David Washington, CHRO | Change management, people, culture |
| `/cto` | Priya Ramanathan, CTO | Technology, innovation, architecture |
| `/cdo` | Sarah Kim, CDO | Data strategy, governance, AI ethics |
| `/legal` | Jonathan Shapiro, General Counsel | Legal, regulatory, IP, compliance |
| `/procurement` | Lisa Fernandez, VP Procurement | Vendor strategy, contracts, negotiation |

**Recommended consultation order:**

1. Start with `/cio` -- IT strategy and enterprise architecture alignment
2. Then `/cfo` -- financial justification and ROI
3. Then `/ciso` -- security, risk, and compliance
4. Follow recommendations for additional personas based on your specific project

**During each consultation:**

- Respond to the executive's questions with specifics, numbers, and evidence
- Ask the executive to challenge areas where you feel uncertain
- Take note of any frameworks they reference (e.g., Kraljic Matrix, NIST CSF, Kotter's 8-step)
- After the conversation, update your project brief with new insights

## Step 7: Evaluate Your Proposal

After consulting with 3-4 executive personas, get a comprehensive rubric evaluation:

Type `/evaluate` to run the evaluation. Claude will:

- Score your proposal across all 9 rubric dimensions (1-5 scale)
- Calculate your composite weighted readiness score
- Determine your readiness level (Ready to Present, Nearly Ready, Making Progress, Early Stage, or Needs Rethinking)
- Highlight your top 3 strengths and top 3 gaps
- Recommend which personas to consult next based on your lowest-scoring areas

Use this as your primary progress check throughout the simulation.

## Step 8: Extract Your Presentation for AI Feedback (Optional)

Once you have draft PowerPoint slides, the simulation can analyze your **actual presentation** — including visuals.

> **Claude Code can read `.pptx` and `.pdf` files directly.** You can simply place your slides in `student-workspace/slides/` and ask Claude to review them — no extraction step needed. The extraction script produces a structured markdown file that gives more consistent slide-by-slide feedback, but it is optional.

1. **Keep your original PowerPoint safe.** Always keep your master `.pptx` file in a separate folder outside this repository (e.g., your Desktop or OneDrive). AI tools can sometimes modify files in your workspace inadvertently.
2. Place a **copy** of your `.pptx` file in `student-workspace/slides/`
3. **Save a snapshot of your work** so you can always recover a previous version:
   ```
   git add -A && git commit -m "Snapshot before AI feedback session"
   ```
   > **What does this do?** `git add -A` stages all your current files, and `git commit` saves a snapshot. If anything goes wrong, you can always get back to this point.
4. Run the extraction command:
   ```
   uv run extract_presentation.py
   ```
5. This extracts all slide text, speaker notes, tables, and structure into `student-workspace/extracted/presentation-content.md`
6. **For visual feedback** on charts, diagrams, and layout: also export your presentation as PDF from PowerPoint (File > Export > Create PDF) and save it in `student-workspace/slides/`. Claude Code can read PDFs directly and analyze your slide visuals.

Now when you use persona skills or `/evaluate`, you get **slide-by-slide feedback** — which slides are strong, which need work, and what's missing.

> **Re-run extraction each time you update your slides** to keep feedback current. Each time, copy the latest version of your `.pptx` into the slides folder and commit before running.

### Installing Python and uv (for extraction only)

You only need Python and `uv` if you want to run the extraction script. Since Claude Code can read `.pptx` files directly, this is optional.

1. **Install Python 3.12+** from [python.org/downloads](https://www.python.org/downloads/). On Windows, check the box that says **"Add Python to PATH"** during installation.
2. **Install uv** (a fast Python package manager):
   - **Mac/Linux**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - **Windows** (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - Full instructions: [docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/)
3. **Restart your terminal** after installing, then verify:
   ```
   python3 --version
   uv --version
   ```

## Step 9: Practice Mock Q&A

This simulates the 2-3 minute Q&A session with industry judges after your presentation.

1. First, fill in `student-workspace/presentation-notes.md` with your slide-by-slide notes and talking points.
2. Type `/presentation-prep` to start the mock Q&A session.
3. Claude will role-play as a panel of industry judges and:
   - Ask 5-7 tough, realistic questions focused on your weakest areas
   - Challenge your financial numbers, technical decisions, security posture, and change management approach
   - Provide feedback after each of your responses
   - Deliver a debrief at the end covering what went well and what needs improvement

## Link Validation

After reorganizing files or before sharing documentation, run the `/markdown-link-validation` skill to check for broken internal links:

```bash
uv run scripts/validate_markdown_links.py --root .
```

This catches broken references after file moves or renames.

## Tips

- **Claude Code can read all workspace files.** It has full access to your project brief, presentation notes, the primer reference materials, and the rubric definitions. This means it provides deeply contextual feedback specific to your project.
- **Update your project brief as you get feedback.** After each persona consultation, strengthen the relevant sections of `student-workspace/project-brief.md`. The simulation evaluates what you have written, so keeping it current is essential.
- **The `/evaluate` command is your best progress check.** Run it after every 2-3 persona consultations to see how your scores are changing and where to focus next.
- **Be specific in your conversations.** Instead of "What do you think of our proposal?", try "Can you evaluate whether our 18-month ROI projection of 2.3x is realistic given our TCO assumptions?" Specific questions yield specific, actionable feedback.
- **Study the primer before consultations.** The `primer/` directory contains 16 reference sections, including consolidated advice from past industry judges. Reading the relevant sections before talking to an executive helps you engage at a higher level and demonstrate framework fluency.
- **Persona skills work best with a filled-in project brief.** If your brief is mostly placeholder text, the executives will have little to challenge and the feedback will be generic. Fill in as much detail as you can before starting.
- **Start early and iterate.** The most effective approach is to begin using the simulation several weeks before the April 27 presentation, consulting personas incrementally as your project develops, rather than trying to do everything in one session.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git: command not found` | Install Git from [git-scm.com/downloads](https://git-scm.com/downloads), then **restart your terminal** |
| `git clone` fails with "permission denied" | Make sure you're using the HTTPS URL (starts with `https://`), not SSH |
| Claude Code doesn't recognize `/cio` or other skills | Make sure you opened the **cloned project folder** in VS Code (File > Open Folder) or navigated to it in the CLI with `cd`. Claude Code reads skills from `.claude/skills/` inside the project |
| Claude Code says "I can't find that file" | Make sure you're in the project directory. In the CLI, run `pwd` to check your current directory |
| Claude Code VS Code extension not appearing | Make sure you installed the "Claude Code" extension (not "Claude" or another variant). Restart VS Code after installation |
| `uv: command not found` | Install uv from [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/), then **restart your terminal** |
| `python: command not found` | Install Python from [python.org/downloads](https://www.python.org/downloads/). On Mac, try `python3` instead of `python` |
| `extract_presentation.py` fails | Run it as `uv run extract_presentation.py` (not `python extract_presentation.py`). Or skip extraction — Claude Code can read `.pptx` files directly |

Still stuck? Ask your instructor or TA for help.

# Quick Start: VS Code + GitHub Copilot

This guide walks you through setting up and using the Enterprise IT Navigator Simulation with VS Code and GitHub Copilot. This is the recommended path for students who have access to GitHub Education.

## Prerequisites

You need all three of the following before you begin:

| Prerequisite | How to Check | Install Link |
|-------------|-------------|-------------|
| **Git** | Open a terminal and type `git --version` | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **VS Code** | Open VS Code — if it launches, you're set | [code.visualstudio.com](https://code.visualstudio.com/) |
| **GitHub Education** | Go to [github.com/settings/copilot](https://github.com/settings/copilot) and check your plan | [education.github.com](https://education.github.com/) |

> **Opening a terminal**: On Mac, press `Cmd+Space` and type "Terminal". On Windows, press the Windows key and type "Command Prompt" or "PowerShell".

## Step 1: Get GitHub Education

GitHub Education gives you free access to GitHub Pro and GitHub Copilot Pro, which includes 300 premium requests per month.

1. Go to [https://education.github.com/](https://education.github.com/).
2. Click "Join GitHub Education."
3. Verify your student status. You will need either a `.edu` email address or a photo of your student ID.
4. Wait for approval (typically 1-3 business days).
5. Once approved, you receive GitHub Pro and GitHub Copilot Pro at no cost.

## Step 2: Set Up VS Code

1. Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Open VS Code.
3. Open the Extensions panel: press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac).
4. Search for "GitHub Copilot" and install it.
5. Search for "GitHub Copilot Chat" and install it (if not already bundled).
6. When prompted, sign in with your GitHub account that has GitHub Education.

## Step 3: Create Your Team's Repo and Clone It

Each team creates their own private copy using GitHub's template feature.

1. Go to [github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach](https://github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach).
2. Click the green **"Use this template"** button near the top right.
3. Select **"Create a new repository"**.
4. Name your repo (e.g., `Team-Name-DT-Project`).
5. Set visibility to **Private** (recommended).
6. Click **"Create repository"**.

Then clone **your new repo**:

1. Open a terminal (Terminal > New Terminal in VS Code, or your system terminal).
2. Navigate to the directory where you want to store the project.
3. Run the following command (replace with your actual repo URL):

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

4. Open the cloned folder in VS Code: **File > Open Folder**, then select your repo folder.

> **Don't have Git?** Install it from [git-scm.com/downloads](https://git-scm.com/downloads). Choose the installer for your operating system and accept the default options. After installing, **restart your terminal** before running the clone command.

## Step 4: Fill In Your Project Brief

This is the most important step. The quality of feedback you receive depends directly on the quality of your project brief.

### Bring Your Existing Work (Optional)

If you have already completed earlier assignments (Team Charter, Industry/Company selection, etc.), drop copies of those deliverables (PDF, DOCX, or TXT) into `student-workspace/source-docs/`. The setup assistant will extract relevant context from them, saving you from re-entering information you have already worked on.

### Option A: Interactive Setup (Recommended)

Let the AI walk you through each section conversationally:

1. Open Copilot Chat by pressing `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac).
2. Click the prompt icon (slash icon) or type `/` to see available prompt templates.
3. Select **setup-project**.
4. Copilot will detect your current assignment milestone, scan for any source documents in `student-workspace/source-docs/`, and adapt its questions to your stage in the project. Early-stage students get focused guidance on company/industry selection; later-stage students dive deeper into financials and change management.
5. After gathering your answers, it writes the completed brief and reviews it for quality — flagging vague areas calibrated to what is expected at your milestone.
6. For students working on ROI (Assignment 5) or OCM (Assignment 6), the setup flow can also fill in the companion templates at `student-workspace/roi-summary.md` and `student-workspace/ocm-assessment.md`.

This takes about 10-15 minutes and ensures every section has the specificity that executive personas expect. Run it again whenever you advance to the next assignment.

### Option B: Manual Editing

If you prefer to fill in the brief yourself:

1. In the VS Code file explorer, open `student-workspace/project-brief.md`.
2. Fill in every section:
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
3. Save the file (`Ctrl+S` / `Cmd+S`).

## Step 5: Start the Simulation

1. Open Copilot Chat by pressing `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac).
2. Click the prompt icon (slash icon) or type `/` to see available prompt templates.
3. Select **start-simulation**.
4. Copilot will read your project brief and provide:
   - A summary of your business problem, technology, and solution
   - An assessment of current strengths and gaps
   - A recommended sequence of executive personas to consult
   - Clear next steps

## Step 6: Consult Executive Personas

In Copilot Chat, type `@` followed by the persona name to start a consultation. Each executive will introduce themselves, read your project brief, and begin asking challenging questions.

| Command | Executive | Focus Areas |
|---------|-----------|-------------|
| `@cio` | Jordan Chen, CIO | IT strategy, governance, enterprise architecture |
| `@ciso` | Anika Patel, CISO | Cybersecurity, risk, privacy, compliance |
| `@cfo` | Robert Okafor, CFO | Financial analysis, ROI, TCO, budget impact |
| `@coo` | Maria Santos, COO | Operations, implementation, pilot design |
| `@chro` | David Washington, CHRO | Change management, people, culture |
| `@cto` | Priya Ramanathan, CTO | Technology, innovation, architecture |
| `@cdo` | Sarah Kim, CDO | Data strategy, governance, AI ethics |
| `@legal` | Jonathan Shapiro, General Counsel | Legal, regulatory, IP, compliance |
| `@procurement` | Lisa Fernandez, VP Procurement | Vendor strategy, contracts, negotiation |

**Recommended consultation order:**

1. Start with `@cio` -- IT strategy and enterprise architecture alignment
2. Then `@cfo` -- financial justification and ROI
3. Then `@ciso` -- security, risk, and compliance
4. Follow the simulation's recommendations for additional personas based on your project

**During each consultation:**

- Be prepared to defend your proposal with specifics
- Ask the executive for their perspective on your weakest areas
- Take note of frameworks they reference (these come from the Enterprise IT Primer)
- After the conversation, update your project brief with what you learned

## Step 7: Evaluate Your Proposal

After consulting with 3-4 executive personas:

1. In Copilot Chat, type `/` to open the prompt menu.
2. Select **evaluate-proposal**.
3. Copilot will score your proposal across all 9 rubric dimensions and provide:
   - An overall readiness score and level
   - A summary table of all 9 dimension scores
   - Detailed analysis per dimension with specific improvements
   - Your top 3 strengths and top 3 gaps
   - Recommended next steps

Use this evaluation to identify which areas need the most work and which personas to consult next.

## Step 8: Extract Your Presentation for AI Feedback (Optional)

Once you have draft PowerPoint slides, the simulation can provide feedback on your **actual presentation** — not just the project brief. This step requires Python and `uv` (see install instructions below).

> **This step is optional.** Copilot can still evaluate your project based on your brief, primer content, and rubrics without extracting slides. Extraction gives more targeted slide-by-slide feedback.

1. **Keep your original PowerPoint safe.** Always keep your master `.pptx` file in a separate folder outside this repository (e.g., your Desktop or OneDrive). AI tools can sometimes modify files in your workspace inadvertently.
2. Place a **copy** of your `.pptx` file in `student-workspace/slides/`
3. **Save a snapshot of your work** so you can always recover a previous version. In the VS Code terminal (Terminal > New Terminal), run:
   ```
   git add -A && git commit -m "Snapshot before AI feedback session"
   ```
   > **What does this do?** `git add -A` stages all your current files, and `git commit` saves a snapshot. If anything goes wrong, you can always get back to this point.
4. Run the extraction command:
   ```
   uv run extract_presentation.py
   ```
5. This extracts all slide text, speaker notes, tables, and structure into `student-workspace/extracted/presentation-content.md`
6. **For visual feedback** on charts, diagrams, and layout: also export your presentation as PDF from PowerPoint (File > Export > Create PDF) and save it in `student-workspace/slides/`

Now when you consult personas or run evaluation, they will provide **slide-by-slide feedback** — identifying which slides are strong, which need work, and what content is missing.

> **Re-run extraction each time you update your slides** to keep the AI feedback current. Each time, copy the latest version of your `.pptx` into the slides folder and commit before running.

### Installing Python and uv (for Step 8 only)

You only need Python and `uv` if you want to run the presentation extraction script. If you don't plan to extract slides, skip this.

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

This step simulates the 2-3 minute Q&A session with industry judges that follows your presentation.

1. First, fill in `student-workspace/presentation-notes.md` with your slide-by-slide notes and talking points.
2. In Copilot Chat, type `/` and select **presentation-prep**.
3. Copilot will role-play as a panel of industry judges and:
   - Ask 5-7 tough, realistic questions based on your weakest areas
   - Challenge your financial justification, technical feasibility, security posture, and change management plan
   - Provide feedback after each of your responses
   - Deliver a debrief at the end with what went well and what needs work

## Step 10: Get Next Steps

For a prioritized improvement plan:

1. Type `/` and select **next-steps**.
2. You will receive recommendations organized into three tiers:
   - **Critical**: Must address before the presentation
   - **Important**: Will significantly strengthen the proposal
   - **Nice-to-have**: Polish items that demonstrate sophistication
3. Each recommendation includes what to improve, why it matters, which primer section to study, which persona to consult, and what deliverable to produce.

## Link Validation

After reorganizing files or before sharing documentation, run the **Validate Markdown Links** VS Code task to check for broken internal links. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`), select **Tasks: Run Task**, then choose **"Validate Markdown Links"**.

You can also run it from the terminal:

```bash
uv run scripts/validate_markdown_links.py --root .
```

## Tips

- **Budget your requests.** You get 300 premium Copilot requests per month with GitHub Education. Each persona consultation and evaluation uses requests, so plan your simulation sessions.
- **Update your project brief continuously.** After each persona conversation, go back and strengthen the relevant sections of `student-workspace/project-brief.md`. The executives can only evaluate what you have written.
- **Be specific in your questions.** Instead of asking "What do you think?", try "Can you evaluate our ROI assumptions for the cloud migration?" or "What security risks are we missing for our IoT deployment?"
- **Use the evaluate prompt as a progress check.** Run it after every 2-3 persona consultations to see how your scores are improving.
- **Study the primer.** The `primer/` directory contains 16 reference sections covering every topic the executives will challenge you on, plus consolidated advice from past industry judges. Reading the relevant sections before a consultation will help you engage at a higher level.
- **Start early.** The most effective teams start using the simulation several weeks before the presentation and iterate multiple times.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git: command not found` | Install Git from [git-scm.com/downloads](https://git-scm.com/downloads), then **restart your terminal** |
| `git clone` fails with "permission denied" | Make sure you're using the HTTPS URL (starts with `https://`), not SSH |
| Copilot doesn't show persona agents (`@cio`, etc.) | Make sure you opened the **cloned project folder** in VS Code (File > Open Folder), not a parent directory. Copilot reads agent files from `.github/agents/` |
| Copilot Chat doesn't show prompt templates | Click the slash icon `/` or type `/` in Copilot Chat. If no templates appear, make sure you opened the project folder and the GitHub Copilot Chat extension is up to date |
| Copilot says "I don't have access to that file" | Copilot may need you to open the file first. Try opening `student-workspace/project-brief.md` in VS Code before asking Copilot about it |
| `uv: command not found` | Install uv from [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/), then **restart your terminal** |
| `python: command not found` | Install Python from [python.org/downloads](https://www.python.org/downloads/). On Mac, try `python3` instead of `python` |
| `extract_presentation.py` fails | Make sure you're running `uv run extract_presentation.py` (not `python extract_presentation.py`). The script automatically installs its dependencies via uv |

Still stuck? Ask your instructor or TA for help.

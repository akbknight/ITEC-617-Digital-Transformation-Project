# ITEC-617 Digital Transformation Project Coach

An AI-powered simulation that helps you prepare your Digital Transformation (DT) team project presentation by challenging you from multiple executive perspectives.

Built for **ITEC-617: Information and Technology** at American University's Kogod School of Business.

## What It Does

You propose a business case for a pilot application of emerging technology. This simulation lets you:

1. **Consult 9 executive personas** who challenge your proposal from their domain perspective
2. **Get scored on 9 rubric dimensions** (45 criteria) aligned to what industry judges evaluate
3. **Track progress** across multiple evaluations with improvement metrics
4. **Practice mock Q&A** with a simulated judge panel targeting your weakest areas
5. **Iterate and improve** with prioritized, actionable recommendations

All personas incorporate insights from **4 years of industry judge feedback** (2021-2024), coaching you on the 10 recurring themes that judges consistently evaluate.

All personas and evaluations are grounded in the [Enterprise IT Primer](https://leifulstrup.github.io/enterprise-it-primer/) course content.

## The Executive Personas

| Persona | Name | Focus Areas |
|---------|------|-------------|
| **CIO** | Jordan Chen | IT strategy, governance, enterprise architecture |
| **CISO** | Anika Patel | Cybersecurity, risk, privacy, compliance |
| **CFO** | Robert Okafor | Financial analysis, ROI, TCO, budget impact |
| **COO** | Maria Santos | Operations, implementation, pilot design |
| **CHRO** | David Washington | Change management, people, culture |
| **CTO** | Priya Ramanathan | Technology, innovation, architecture |
| **CDO** | Sarah Kim | Data strategy, governance, AI ethics |
| **General Counsel** | Jonathan Shapiro | Legal, regulatory, IP, compliance |
| **VP Procurement** | Lisa Fernandez | Vendor strategy, contracts, negotiation |

## What You Need

Before you start, make sure you have the following installed:

| Tool | What It's For | Install Link |
|------|---------------|-------------|
| **Git** | Downloading and tracking changes to project files | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **VS Code** | Code editor where you'll interact with the AI | [code.visualstudio.com](https://code.visualstudio.com/) |
| **An AI assistant** | Choose one of the paths below | See Step 3 |

You do **not** need to know how to code. The AI assistants handle all the technical work — you focus on your business case.

## Getting Started

### Step 1: Install Git and VS Code

1. **Install Git** from [git-scm.com/downloads](https://git-scm.com/downloads). Choose the installer for your operating system (Windows, Mac, or Linux) and accept the default options.
2. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/) if you don't already have it.

To verify Git is installed, open a terminal (on Mac: search for "Terminal" in Spotlight; on Windows: search for "Command Prompt" or "PowerShell") and type:

```
git --version
```

If you see a version number (e.g., `git version 2.43.0`), you're good to go.

### Step 2: Create your team's copy of this repo

Each team creates their own private copy using GitHub's template feature. This gives you a clean starting point with your own git history.

1. Go to [github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach](https://github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach)
2. Click the green **"Use this template"** button near the top right
3. Select **"Create a new repository"**
4. Name your repo (e.g., `Team-Name-DT-Project`)
5. Set visibility to **Private** (recommended)
6. Click **"Create repository"**

Then open a terminal and clone **your new repo**:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
code .
```

This downloads your team's project files and opens them in VS Code.

> **What does this do?** "Use this template" creates a fresh copy of the project under your GitHub account. You then clone (download) that copy to your computer so you can work with the files locally.

### Step 3: Choose your AI assistant path

Pick **one** of these two paths based on what you have access to. Each has its own detailed setup guide:

#### Path A: VS Code + GitHub Copilot (Recommended)

Best for students with a [GitHub Education](https://education.github.com/) account (free Copilot Pro).

1. Install the GitHub Copilot extension in VS Code
2. Open Copilot Chat and use `@cio`, `@cfo`, `@ciso`, etc. to consult personas
3. Use prompt templates (`/setup-project`, `/start-simulation`, `/evaluate-proposal`, `/presentation-prep`)

See **[QUICKSTART-COPILOT.md](QUICKSTART-COPILOT.md)** for full setup instructions.

#### Path B: Claude Code

Best for students with a [Claude Pro](https://claude.ai/) subscription.

1. Install Claude Code and open this repo
2. Use slash commands: `/cio`, `/cfo`, `/ciso`, etc. to consult personas
3. Use `/setup-project` to fill in your brief, `/evaluate` for scoring, `/presentation-prep` for mock Q&A

See **[QUICKSTART-CLAUDE-CODE.md](QUICKSTART-CLAUDE-CODE.md)** for full setup instructions.

### Step 4: Fill in your project brief

If you have completed earlier assignments (Team Charter, Industry/Company, etc.), drop copies of your deliverables into `student-workspace/source-docs/` first.

Then use the interactive setup: run `/setup-project` in Claude Code, or select the **setup-project** prompt in Copilot Chat. The AI will detect your current assignment milestone, extract context from any source documents you provided, and adapt its questions to your stage. It writes the brief for you and reviews it for quality.

For ROI and OCM work, dedicated companion templates are available at `student-workspace/roi-summary.md` and `student-workspace/ocm-assessment.md`.

Alternatively, open `student-workspace/project-brief.md` and complete every section manually. The more detail you provide, the better the executive feedback.

### Presentation Feedback

Once you have draft slides, the simulation provides **slide-by-slide feedback**:

1. Place a **copy** of your `.pptx` in `student-workspace/slides/`
2. Extract the text content so the AI can analyze it:
   ```bash
   uv run extract_presentation.py
   ```
3. For visual feedback on charts and layout, also export your slides as PDF from PowerPoint

**Claude Code users**: Claude Code can read `.pptx` and `.pdf` files directly — you can skip the extraction step and just ask it to review your slides.

**Don't have `uv` installed?** See the [Python and uv install instructions](#optional-install-python-and-uv) below. This step is optional — the AI can still evaluate your project brief without extracting slides.

> **Protect your work.** Always keep your original PowerPoint in a separate folder outside this repository (e.g., your Desktop or OneDrive). AI tools can sometimes modify files in your workspace inadvertently. Save backup copies or use `git commit` to snapshot your work before each AI feedback session so you can always recover a previous version.

### Optional: Install Python and uv

The `extract_presentation.py` script requires Python and the `uv` package manager. You only need this if you want to extract text from PowerPoint files for AI analysis.

1. **Install Python 3.12+** from [python.org/downloads](https://www.python.org/downloads/). During installation on Windows, check the box that says "Add Python to PATH."
2. **Install uv** by following the instructions at [docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/). The simplest method:
   - **Mac/Linux**: Open a terminal and run: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - **Windows**: Open PowerShell and run: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
3. Verify both are installed:
   ```
   python3 --version
   uv --version
   ```

## Evaluation Rubric

Proposals are scored across 9 weighted dimensions:

| Dimension | Weight | Key Questions |
|-----------|--------|---------------|
| Business Case Strength | 20% | Is the problem clear? Is there a compelling value proposition? |
| Financial Analysis | 15% | Is the ROI credible? Is TCO fully accounted for? |
| Implementation Strategy | 15% | Is the pilot well-scoped? Is the timeline realistic? |
| Technology Selection | 10% | Is the tech mature enough? Were alternatives considered? |
| Risk & Security | 10% | Are threats identified? Is privacy addressed? |
| Change Management | 10% | Are stakeholders mapped? Is there a training plan? |
| Presentation Readiness | 10% | Is the narrative compelling? Can the team handle Q&A? |
| Data & Analytics | 5% | Are data requirements clear? Are ethics considered? |
| Vendor Strategy | 5% | Is vendor lock-in mitigated? Are SLAs defined? |

**Readiness Levels**: Ready to Present (90-100%) | Nearly Ready (75-89%) | Making Progress (60-74%) | Early Stage (40-59%) | Needs Rethinking (0-39%)

## Repository Structure

```
ITEC-617-Digital-Transformation-Project-Coach/
├── primer/                    # 16 reference sections (15 primer + judge advice)
├── rubrics/                   # 9 evaluation dimensions (45 criteria)
├── student-workspace/         # Your working directory
│   ├── project-brief.md       #   ← Fill this in first
│   ├── presentation-notes.md  #   Slide-by-slide notes template
│   ├── roi-summary.md         #   ROI analysis template (Assignment 5)
│   ├── ocm-assessment.md      #   OCM assessment template (Assignment 6)
│   ├── source-docs/           #   Drop prior assignment deliverables here
│   │   └── presentation-support/  #   AI-generated defense materials
│   ├── slides/                #   Place your .pptx and .pdf here
│   └── extracted/             #   Auto-generated by extract_presentation.py
├── scripts/
│   └── validate_markdown_links.py  # Internal link checker
├── extract_presentation.py    # Extracts .pptx content for AI analysis
├── .github/
│   ├── agents/                # 9 Copilot persona agents (@cio, @cfo, etc.)
│   ├── prompts/               # 5 Copilot prompt templates
│   └── copilot-instructions.md
├── .claude/
│   └── skills/                # 12 Claude Code skills (/cio, /evaluate, /setup-project, etc.)
├── STUDENT-GUIDE.md           # Comprehensive student guide
├── QUICKSTART-COPILOT.md      # VS Code + Copilot setup
├── QUICKSTART-CLAUDE-CODE.md  # Claude Code setup
└── CLAUDE.md                  # Claude Code context configuration
```

## Grounding Content

All simulation content is grounded in the **[Enterprise IT Primer](https://leifulstrup.github.io/enterprise-it-primer/)**, covering:

- **Governance**: IT governance frameworks, C-suite roles, IT budgeting
- **Technology**: Build vs. buy, cloud computing, enterprise applications, open source
- **Risk & Security**: Cybersecurity, data governance, shadow IT
- **Transformation**: Digital transformation, AI & emerging tech, innovation management
- **Management**: Vendor management, project management

## Course Context

- **Course**: ITEC-617 Information and Technology (MBA, 1.5 credits)
- **Project**: Teams present a business case for a pilot application of emerging technology
- **Format**: 10-minute presentation + 2-3 minutes Q&A to industry judges
- **Date**: April 27, 2026
- **Weight**: 50% of final grade

## Markdown Link Check

This repo includes a link validation tool that checks all internal markdown links are valid. It catches broken references after file moves or renames.

**VS Code**: Open the Command Palette, select **Tasks: Run Task**, then choose **"Validate Markdown Links"**.

**CLI**:
```bash
uv run scripts/validate_markdown_links.py --root .
```

**CI**: Link validation runs automatically on every push to `main` and on all pull requests. The report artifact can be downloaded from the GitHub Actions tab.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git: command not found` | Install Git from [git-scm.com/downloads](https://git-scm.com/downloads), then restart your terminal |
| `uv: command not found` | Install uv from [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/), then restart your terminal |
| `python: command not found` | Install Python from [python.org/downloads](https://www.python.org/downloads/). On Mac, try `python3` instead of `python` |
| `code: command not found` | Open VS Code manually, then install the shell command: press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows), type "shell command", and select "Install 'code' command in PATH" |
| Copilot not responding to `@cio` | Make sure you have the GitHub Copilot Chat extension installed and you're signed in with a GitHub Education account |
| Claude Code not recognizing `/cio` | Make sure you opened your project folder (not a parent folder) in VS Code or navigated to it in the CLI |
| `extract_presentation.py` fails | Make sure you have Python 3.12+ and uv installed (see [install instructions](#optional-install-python-and-uv)). Run it as `uv run extract_presentation.py` (not `python extract_presentation.py`) |

Still stuck? Ask your instructor or TA for help.

## License

This project is licensed under the [MIT License](LICENSE). It is for educational use within ITEC-617 at American University's Kogod School of Business.

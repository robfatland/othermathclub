# Python Bytes

A math + coding club for middle schoolers (ages 11–13). Weekly 90-minute sessions,
non-competitive, built around exploring mathematical ideas through Python.

The repo name is `othermathclub` (the club's original name). The program is **Python Bytes**.

## What's here

| Path | What it is |
|------|------------|
| `Curriculum/` | What we teach. Lean by design. `syntax/` (drill) + `projects/` (discovery). |
| `Resources/` | Advanced, overflow, and historical material. The larger sibling corpus. |
| `python_bytes_slides.md` | Parent-audience slide deck describing the program. |
| `Handout1_2026.md`, `Handout2_2026.md` | Student handouts. |
| `AgendaCoachCamp2026.md` | Coach camp agenda. |
| `InstallVSCode.md` | Setup notes for VS Code. |
| `TurtleIntro.py` | Turtle warm-up script. |

Start in `Curriculum/README.md` for the teaching spine.

## The three D's

Every session balances three forces:

- **Drill** — Python basics internalized through repetition. Students won't practice between meetings.
- **Discovery** — math ideas as the motivation for coding.
- **Delight** — surprising payoffs, peer interaction, punchlines.

## Running the code

Student-facing code targets two platforms: [trinket.io](https://trinket.io) (browser, no
install) and VS Code with a local Python. Files flag their status, e.g.
`# trinket: OK | vscode: OK`.

Most teaching code uses only the Python standard library (`turtle`, `random`, `math`,
`time`). A few topics reach for third-party libraries:

- `matplotlib`, `numpy` — fractal and visualization work
- `requests` — the server-interaction topics

See [`environment.yml`](environment.yml) / [`requirements.txt`](requirements.txt) for a
local environment.

> `turtle` needs a desktop Python with Tk. It does not run in Jupyter, and headless
> environments won't show its window.

## Conventions

- Prefer `.py` files over notebooks for student-facing material.
- Favor multiple short code examples over one long one.
- Prefer a plain `for` loop over `numpy`/`scipy` when the loop teaches more.
- Every topic includes a kinesthetic activity (or a placeholder noting one is needed).
- AI-written code self-identifies: `# AI in use: True`.

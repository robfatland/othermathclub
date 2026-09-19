# Python Bytes / OtherMathClub — Project Steering

## What This Is

A math+coding club for 6th/7th graders (ages 11–13), called **Python Bytes**. The repo
is `othermathclub` (the original non-competitive math club name). ~50 students across
four classrooms at start of year, ~30 by end. Meets once per week, 90 minutes, roughly
24–28 sessions per school year.

## The Book Project

The current effort is reorganizing the large body of existing material into a
**chapter-structured book** aimed at this audience. The book has two simultaneous lives:

1. **Instructor resource** — session plans, code, kinesthetic activities, punchlines
2. **Publishable text** — opt-in/opt-out tone where a reader encounters a topic, gets
   the hook, and can dive deeper or skip ahead

The metaphor is *exploration of a complex landscape*, not a linear textbook.

### Book Structure

```
chapter1/    — Pythonic Skills. Exercise-based muscle building. For-loops, variables,
               functions, libraries, input/output. By the end a student can write a
               for-loop from memory.

chapter2/    — Drawing with Python. Turtle graphics methods + drawing challenges up to
               multiple turtles interacting on the canvas.

chapter3/    — From Ms. Halfway to the Chaos Game. The chain: Ms. Halfway → Chaos Game
               → Sierpinski Gasket. Payoff: unexpected fractal from simple random process.

chapter4/    — Fibonacci and Meru Prastarah. Fibonacci iteration (3-variable logic),
               MP construction, negative-number row offsets, modulo-2 mask revealing
               Sierpinski. Connections back to Chapter 3.

chapter5–10/ — Seven more expedition topics (TBD, drawn from: Cellular Automata,
               L-Systems, Knights, dimension, music21, requests/server interaction,
               pygame games, etc.)

appendices/  — Overflow content: topics big and small that didn't fit the chapter flow.
               Also "Future Topics" including topology/Möbius.

Book2/       — Second book, parallel development. Includes "Rainbow" and other
               advanced/extended material.
```

Chapters 1–2 are **boot camp** covering 90%+ of the Python needed later.
Chapters 3–10 are **independent expeditions** sharing that foundation.

A **Book 2** may run in parallel for advanced/overflow material.

## The Triangular Tension (Design Constraint)

Every session balances three forces:

- **Drill** — Python basics must be internalized through repetition (students will NOT
  practice between meetings; 96% certainty)
- **Discovery** — Math/STEM ideas as source of coding motivation. Mantra: idea →
  think → calculate → code → experiment → close the loop on the idea
- **Delight** — Students bring their social selves. Peer interaction matters. Always
  seek punchlines and surprising payoffs.

## Pedagogical Principles

- Students will not read lengthy descriptions. Keep written material minimal and punchy.
- De novo introductions work best — don't assume prior knowledge even for "standard" topics
- Kinesthetic warm-ups (sitting on the floor in a circle, away from laptops) are effective
- "Rob's first rule: Put your computer away (get a piece of paper)"
- "Rob's second rule: Don't do what you're trying to do; do something easier"
- Always have a **punchline** — a surprising result that motivates getting the code working
- The process doesn't end when the code runs; the code running is the beginning of inquiry

## Working With Me (Kiro)

- Write to Rob as the instructor, not to students directly
- Help modes: building session plans, writing demo code, organizing/refactoring the repo,
  brainstorming connections between topics, drafting book chapters
- Favor multiple short code examples over one long one
- Don't use numpy/scipy when a for-loop teaches more
- When suggesting connections between topics, flag them explicitly — unexpected links
  between ideas are prized ("interesting unexpected connections")

## Hard Constraints

- **AI attribution**: All AI-written code must self-identify briefly, e.g. `# AI in use: True`
- **Kinesthetic placeholder**: Every topic must include a kinesthetic activity or at minimum
  a placeholder noting one is needed
- **Platform testing**: Code should be tested in both trinket.io and VS Code; flag results
  (e.g. `# trinket: OK | vscode: OK`)
- **Slide deck**: Maintain a Markdown slide deck for parent audiences describing the program
- **No over-scaffolding**: Present the pieces; let the student assemble them

## Repo Conventions (Going Forward)

- Chapter-based folder structure: `chapter1/`, `chapter2/`, etc.
- Old numbered folders (1_Forms, 2_Counting, ...) will migrate to chapter structure or Attic
- Each chapter folder contains:
  - `README.md` — chapter overview, session plan notes, kinesthetic activity
  - One or more `.py` files (preferred over notebooks for student use)
  - Notebooks (`.ipynb`) acceptable for instructor development/exploration
  - Supporting assets (images, etc.) in chapter folder
- File naming: lowercase, underscores, descriptive (e.g. `chaos_game.py`, `fibonacci_iteration.py`)
- The `A2_Attic/` folder is the graveyard for retired/superseded material
- The `mathvis/` folder contains mathematical visualization experiments (pre-book work)

## Key Abbreviations (from topics file)

- MP = Meru Prastarah (Pascal's Triangle)
- SG = Sierpinski Gasket
- SM = Stand-up Maths (YouTube channel, source of ideas)
- MS = middle school

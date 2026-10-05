# Resources Consolidation Map (working doc)

Status: **DRAFT for Rob's review.** Nothing has been moved, merged, or deleted. This is the
proposed plan for the editorial consolidation pass over `Resources/`. Mark each cluster with
your decision (keep-canonical / merge / defer / delete) and I'll execute approved items.

Conventions for the "Proposal" column:
- **CANONICAL** = the one file/home a topic should live in.
- **MERGE** = fold content into the canonical home, then retire the source.
- **DEDUP** = byte-level (or near) duplicate; keep one, delete the rest.
- **DEFER** = leave as-is this pass; revisit later.
- **CURRICULUM?** = possible candidate to promote into `Curriculum/` — Rob decides.

---

## 1. Confirmed duplicates (safe, mechanical)

### 1a. Dual spirals — exact duplicate
- `PythonBytes/dual_spirals.py`
- `PythonBytes/dualspirals.py`

Verified identical except a trailing newline. **DEDUP:** keep `dual_spirals.py` (underscore
matches repo naming convention), delete `dualspirals.py`.

---

## 2. Topic clusters with redundancy (need your judgment)

### 2a. Pursuit / Four Bugs / duck-wolf  ← your flagged example
Occurrences:
- `4_Models/pursuit/README.md`  — rich write-up: "Four Bugs" (Alpher, Bethe, Gamow, Dyson),
  turtle `towards()`/`setheading()`/`distance()` teaching, random-bugs extensions. **Strong
  canonical candidate.**
- `4_Models/pursuit/bugs.ipynb`
- `4_Models/pursuit/example.py` (138 lines)
- `4_Models/pursuit/example2.py` (32 lines)
- `4_Models/pursuit/randomturtles.py`
- `A2_Attic/Games/minecraft/.../otherideas/Resources/pursuit_curves.py`
- `PythonBytes/vscode_turtle_pursuit_example.py`
- images: `A3_Images/Mathematics/Pursuit/`

**Proposal:** create one canonical `Resources/pursuit/` (or a single `pursuit.md` as you
suggested for duck/wolf) built around the existing README prose, with the best one or two code
examples beside it. Fold/retire the scattered `.py` variants. Keep images linked. Need your
call on: markdown-only vs markdown + code folder, and which code example is "the good one."

> Note: this is the "duck/wolf" topic in a different costume (pursuit curves). Confirm you
> want it consolidated here and whether the duck/wolf *shadow* variant (from PBytes2026 notes)
> is the same file or a separate write-up to track down.

### 2b. Ms. Halfway
- `PythonBytes/mshalfway.py` (21 lines)
- `PythonBytes/ms_halfway_another_version.py` (120 lines)
- (The canonical teaching version now lives in `Curriculum/projects/01_ms_halfway/`.)

**Proposal:** Curriculum owns the teaching version. In Resources, keep **one** archived
reference (likely the 120-line `ms_halfway_another_version.py` as the richer variant) under a
`Resources/halfway/` or similar; delete or archive the 21-line stub. Your call.

### 2c. Chaos Game / Sierpinski
- `1_Forms/serpinsky/Chaos.ipynb`, `Chaos3D.ipynb`, `serpinsky.py`
- `A2_Attic/Games/minecraft/.../otherideas/Resources/ChaosGame.py`
- images: `A3_Images/Mathematics/Fractals/`, `.../MeruPrastarah/`

**Proposal:** This is a future **Curriculum** destination (the end of the seminal progression),
so I'd **DEFER** Resources consolidation here until we build the Chaos project, then decide what
stays archived vs promoted. Flag: note spelling `serpinsky` → `sierpinski` for any canonical name.

### 2d. Spirals (beyond the exact dup in 1a)
- `PythonBytes/spiral_inout.py`
- `PythonBytes/spiral_turtle.py`
- `PythonBytes/dual_spirals.py` (canonical from 1a)
- `PythonBytes/vscode_black_screen_spiral.py`
- `PythonBytes/vscode_turtle_spiral_quarter_circles.py`

**Proposal:** group under `Resources/turtle_spirals/` as a small gallery (these are genuinely
different spirals, not dups). Mostly a **MOVE/GROUP**, not a merge. Confirm you want them grouped.

### 2e. Meru Prastarah / Pascal — multiple READMEs
- `2_Counting/meruprastarah/MeruPrastarah.ipynb`
- `2_Counting/meruprastarah/pascal/README.md`
- `2_Counting/meruprastarah/pascal/README1.md`
- `2_Counting/meruprastarah/pascal/README2.md`
- `2_Counting/meruprastarah/pascal/rob_notes.py`

Three READMEs (README / README1 / README2) smell like iterative drafts. **Proposal:** read all
three, pick/merge into one canonical README, retire the others. **CURRICULUM?** — MP is on the
2026 curriculum list, so flag for later promotion. Need your OK to read + merge the drafts.

### 2f. Fibonacci
- `4_Models/fibonacci/fibonacci.ipynb`
- images: `A3_Images/Mathematics/Fibonacci/`

**Proposal:** **DEFER** — Fibonacci is Project 2 in the seminal progression; decide archive vs
promote when we build it.

### 2g. L-System / fractal fern / dragon / julia
- `PythonBytes/vscode_l_system_x_y_serp.py`
- `PythonBytes/vscode_fractal_fern.py`
- `1_Forms/fractals/dragon.ipynb`, `julia.ipynb`, `squaring_z.ipynb`

**Proposal:** group as `Resources/fractals/` gallery. The L-system code-along in `PBytes2026.md`
is the teaching version — flag the connection. Mostly **GROUP**, not merge.

### 2h. requests / server-client
- `6_Communication/requests/FunctionApp.py`, `requests.ipynb`
- `PythonBytes/vscode_requests_client_periodic_table.py`, `Sphinx42Client.py`
- `A2_Attic/ServerClientCode/HiveFinderClient.py`
- `torusmare/` (full client/server/deploy/docs — looks like a real project)
- root notes: `sphinx42.md`, `sphinx42_URL_probably_disposable_artifact.txt`

**Proposal:** `torusmare/` looks like a self-contained server project — leave intact. Group the
loose client scripts under `Resources/requests/`. The `sphinx42_URL_..._disposable_artifact.txt`
is self-labeled disposable — **DELETE?** (confirm). requests is on the 2026 curriculum list —
**CURRICULUM?** later.

---

## 3. Clear "archive and leave" (no consolidation needed this pass)

- `A2_Attic/` — already the designated graveyard; leave as-is. Contains Games (sudoku,
  tictactoe, nim, minecraft, collatz), Operating-PythonBytes notes, ServerClientCode,
  ProjectReport, "python project ideas". DEFER wholesale.
- `A3_Images/` — large image library, logically foldered by subject already. Leave as-is; it's
  the asset store other topics link into.
- `Book2/` — advanced/overflow (mathvis 4D polytopes, Lenia, Lorenz, Rainbows, stargirl,
  saltation). Self-contained; leave intact as the advanced track within Resources.
- `A1_Utility/` (charts, graphical_templates) — leave as instructor utilities.

---

## 4. Loose root-level files now in Resources (quick dispositions)

| File | Proposal |
|------|----------|
| `Coding1.ipynb`, `Coding2.ipynb` | Old combined curriculum notebooks — likely superseded by new Curriculum. READ + decide archive vs mine. |
| `CurriculumElementsSurvey.ipynb` | Planning artifact — DEFER / keep as reference. |
| `ShowNTell.ipynb`, `showntell.py` | Duplicate-ish pair (notebook + script). READ + DEDUP. |
| `reentrant.py` | Knight's-tour reentrant — belongs with Knights topic. GROUP later. |
| `chapter1/`, `chapter2/` | The *old* chapter attempts (now that fresh Curriculum exists). Superseded? READ + decide: mine for exercises or archive. **Important: not to be confused with new `Curriculum/`.** |
| `sphinx42.md` | Keep with requests cluster (2h). |
| `sphinx42_URL_probably_disposable_artifact.txt` | Self-labeled disposable — DELETE? |
| `_header.tex` | LaTeX header for PDF builds — keep (build machinery). |

---

## Recommended first batch (lowest risk, highest tidiness)

1. **1a** DEDUP the identical spiral file (1 deletion).
2. **2a** Build canonical pursuit home (your flagged example) — needs your format choice.
3. **2e** Merge the three MP pascal READMEs — needs your OK to read + merge.
4. **4** Dispose of `sphinx42_URL_..._disposable_artifact.txt` if you confirm it's trash.

Everything else (Chaos, Fibonacci, requests) I'd **DEFER** to when we build the matching
Curriculum project, so we decide promote-vs-archive with the project in front of us.


---

# EXECUTION LOG — Batch 1 (done, pending commit)

## Completed
- **Deleted** `sphinx42_URL_probably_disposable_artifact.txt` (confirmed disposable). Note:
  `sphinx42` was an early web server/client game attempt; `torusmare` is the restart and will
  return later this school year. `sphinx42.md` kept.
- **DEDUP:** deleted `PythonBytes/dualspirals.py` (byte-identical to `dual_spirals.py`).
- **Pursuit → `Resources/pursuit/`** (own folder, per Rob). Now contains:
  - `README.md` — canonical write-up covering all three flavors (built from the old Four Bugs
    README).
  - `simple_pursuit_two_turtles.py` (was `PythonBytes/vscode_turtle_pursuit_example.py`) — the
    2-turtle game.
  - `four_bugs.py` (was `4_Models/pursuit/example.py`) — commented teaching version.
  - `four_bugs_compact.py` (was `example2.py`) — compact list-based version.
  - `random_bugs.py` (was `randomturtles.py`) — **bug fixed**: `pencolors` → `pens` (was a
    NameError).
  - `wolf_and_duck.py` — **extracted** from a markdown cell in `Coding2.ipynb` ("gradient
    descent"); the duck/wolf pond + gradient-ascent escape. Original still in Coding2.ipynb.
  - `bugs.ipynb`, `bugpaths.png`, `bugpaths2.png` — moved from old pursuit folder.
  - Old `4_Models/pursuit/README.md` deleted (superseded by canonical). `4_Models/pursuit/`
    folder removed.
- **Meru Prastarah READMEs merged:** the three `pascal/README*.md` were three *sessions*, not
  duplicates. Merged into one ordered `README.md` (Session 1/2/3). Deleted `README1.md`,
  `README2.md`. `rob_notes.py` kept as instructor scratch (flagged: has early `sys.exit(0)`).

## Open question for Rob
- `wolf_and_duck.py` is extracted but the original copy still lives inside `Coding2.ipynb`.
  Leave the duplicate in the notebook, or strip that cell from Coding2 once you've confirmed
  the extraction is faithful? (I lean: leave it until Coding2 itself is adjudicated.)

---

## chapter1 / chapter2 (old attempts) — MINING FINDINGS

These two folders are a **previous AI-assisted attempt at the same two-track idea** we are now
rebuilding fresh in `Curriculum/`. They are high quality and worth mining — but promotion into
`Curriculum/` is **Rob's call**, so nothing moved.

**`chapter1/` (Pythonic Skills, text-only boot camp):**
- `README.md` — strong session-flow template (kinesthetic → predict-and-run → type-along →
  free practice → show&tell) and a 10-skill checklist.
- `exercises_tier1/2/3.py` — graded exercise ladder: hello/input/countdown → even?/powers/
  random-choice → is_prime/alternating-sum.
- Cites source material: `Coding1.ipynb`, `PBytes_topics_2025_2026.md`, the pascal README.

**`chapter2/` (Drawing with Python, turtle boot camp):**
- `README.md` — full turtle method reference + a 15-item drawing-challenge ladder ending on a
  **"Chaos Game preview"** (three fixed points, jump halfway to a random one) — i.e. it already
  anticipates the seminal progression's payoff.
- `turtle_basics.py`, `color_and_loops.py`, `multiple_turtles.py`.

**Recommendation (for Rob to rule on):**
- These map cleanly onto the new `Curriculum/syntax/` (chapter1) and `Curriculum/projects/`
  turtle slot (chapter2). I suggest **mining them as source** when we build Syntax 2+ and the
  Turtle project — i.e. keep them in Resources as reference, lift specific exercises as we go,
  rather than bulk-promoting. The 15-item turtle ladder and the tiered exercises are the most
  reusable pieces. **Confirm:** mine-as-we-go (my lean), or promote wholesale now?

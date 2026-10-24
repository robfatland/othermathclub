# WSL / Python Execution

## Don't run Python

Rob runs Python through a **miniconda** interpreter and its environments. Kiro usually
can't reach that interpreter, and falling back to the Windows-installed Python causes
confusion and wrong results.

So:

- **Do not run `python` / `python3`** (no execution, no probing, no `-c` snippets, no
  running `.py` files, no installing packages into an env).
- **Do** edit code and **provide** the exact command for Rob to run himself.
- Hand execution and its output back to Rob. Treat his pasted output as the source of truth.
- Non-Python shell commands (git, ls, file inspection) are still fine.

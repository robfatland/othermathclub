# Setting Up Python Bytes on Your Computer


Three steps: install Python, install VS Code, then install one library and test it. Takes about 15 minutes.


**Windows and Mac only.** On a Chromebook you can't install this software — use
[trinket.io](https://trinket.io) in a browser instead. We'll send trinket.io
instructions separately.


Do the steps in order.

---

## Step 1 — Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Click the big yellow **Download Python** button (it detects your OS).
3. Run the installer.

   - **Windows:** On the first screen, check the box **Add python.exe to PATH**
     at the bottom. This matters. Then click **Install Now**.
   - **Mac:** Open the downloaded `.pkg` and click through the installer.

4. Done. (The installer also adds a program called **IDLE**. Ignore it — we use
   VS Code, not IDLE.)

---

## Step 2 — Install VS Code

1. Go to [code.visualstudio.com](https://code.visualstudio.com/).
2. Download the version for your OS and install it.
   - **Mac:** drag **Visual Studio Code** into your **Applications** folder.
3. Open VS Code.
4. Install the Python extension:
   - Click the **Extensions** icon in the left bar (four squares).
   - Type `Python` in the search box.
   - Install the one from **Microsoft** (it's the first result).

---

## Step 3 — Install matplotlib and test it

We draw with a library called **matplotlib**. Install it from inside VS Code.

1. In VS Code, open a terminal: menu **Terminal → New Terminal**.
   A panel opens at the bottom (PowerShell on Windows, zsh on Mac).
2. Type the line for your computer and press Enter:

   - **Windows:**

     ```
     pip install matplotlib
     ```

     If Windows says `pip` is not found, use this instead:

     ```
     py -m pip install matplotlib
     ```

   - **Mac:** use `pip3` (the plain `pip` may be missing or point to an old Python):

     ```
     pip3 install matplotlib
     ```

3. Wait for it to finish (a few lines of download text, then back to a prompt).

**Quick test.** Create a file called `test.py`, paste this in, and run it with the
Run button (the **>** triangle in the top right):

```python
from matplotlib import pyplot as plt
plt.plot([0, 1, 2, 3], [0, 1, 4, 9])
plt.show()
```

A window with a curve should pop up. If it does, you're ready for club.

---

## Trouble?

- **`python` or `pip` not found (Windows):** Python was installed without "Add to
  PATH." Re-run the Python installer, check that box, and restart VS Code.
- **`python` or `pip` not found (Mac):** On a Mac the commands are usually `python3`
  and `pip3`, not `python` and `pip`. Use those. So to run a file from the terminal,
  type `python3 test.py`, and to install a library, `pip3 install matplotlib`.
- **The Run button doesn't appear:** Make sure the Microsoft Python extension
  from Step 2 is installed.
- **Still stuck:** Email us a screenshot of what you see. We'll sort it out at club.

---

## Plan B — can't get it installed?

Don't lose a week over it. Go to [trinket.io](https://trinket.io) and write Python
in your browser instead — nothing to install, works on any computer. Open a new
**Python** trinket and you can run the matplotlib test above right there.

Two things to know:
- Make a free account if you want your work saved (otherwise it disappears when you
  close the tab).
- Not every library we use later lives on trinket, so it's a backup, not the
  destination. Bring your laptop to club and we'll get the real setup working together.

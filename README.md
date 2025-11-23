💣 Minesweeper – Python Terminal Edition

Minesweeper is a fully interactive command-line implementation of the classic puzzle game — complete with recursive flood-fill reveal, difficulty levels, first-click safety, and even save/load support using JSON/pickle.

A simple, fast, and cross-platform Python version of one of the most iconic logic games ever made.

🔧 Tech Stack

Language: Python

Libraries:

random – bomb placement

pickle – game saving/loading

pathlib – platform-safe file handling

time – animations

Executable: Supports PyInstaller build

✨ Features

🎮 Classic Minesweeper mechanics (bombs, numbers, flood-fill zeros)

🏃 Smooth recursive reveal of all connected empty spaces

💾 Save & load game state (persistent across sessions)

⚙️ Difficulty levels (Easy, Medium, Hard, ??? mode)

🛡️ First-click bomb protection (board generates after first click)

📁 Automatic save folder creation with Path.home()

🖥️ Clean terminal UI with emoji grid (📦, 💣, 0, numbers)

📁 Project Structure
<pre> minesweeper/ ├── main.py # Game loop & difficulty menu ├── minesweeper_tools.py # Core logic (board gen, flood fill, reveal) ├── data_handler.py # Saving & loading (pickle) ├── animation_handler.py # Optional animations / printing effects ├── README.md # This file └── <generated> minesweeper_saves/ └── minesweeper.dat # Auto-created save file </pre>
🧠 Game Logic Overview
🔹 Board Creation

Generates an empty grid (📦)

Places bombs randomly

Computes adjacent bomb counts for all safe cells

🔹 First Click Handling

If the first chosen cell is a bomb:

A fresh board is regenerated

Ensures the first click is always safe

🔹 Number Assignment

Iterates through each tile

Counts bombs in the 8-tile neighborhood

Writes 1, 2, 3, or "0 " accordingly

🔹 Flood Fill Reveal

Recursive expansion when player clicks a zero

Reveals:

the zero cell

all surrounding cells

continues until edges are reached

🔹 Win/Loss Conditions

Lose: you uncover a bomb → all bombs revealed

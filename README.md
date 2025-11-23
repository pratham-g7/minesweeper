🧨 Minesweeper (Python CLI)
 . A clean and fully playable command-line Minesweeper game built in Python.
 . Features classic mechanics — safe first click, recursive flood-fill reveal, adjustable board sizes, difficulty settings, and save/load support.

🎮 Features
✔ Classic Minesweeper gameplay
✔ Safe first click (bombs only generate after first move)
✔ Recursive flood-fill revealing of empty cells
✔ Selectable difficulty levels
 . Easy
 . Medium
 . Hard
 . Secret Mode
✔ Save & Load game system
✔ Clean CLI rendering of board
✔ Modular code structure

🧠 How It Works
🔹 Board Generation
 . The board is created using dimensions based on chosen difficulty.
 . Bomb placement is performed after the first click to guarantee fairness.

🔹 Number Assignment
 . Every tile shows the count of bombs in its 8 adjacent cells.

🔹 Flood Fill
 . When a 0 tile is revealed, all connected empty tiles are automatically exposed.

🔹 Game Ending
 . Revealing a bomb shows all bombs and ends the game.
 . Revealing all safe tiles triggers a win.

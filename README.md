# 💣 Minesweeper – Terminal-Based Puzzle Game

A clean and fully playable **Minesweeper** game built in Python, running directly in the terminal.  
Features zero-adjacent auto-reveal (flood fill), safe first click, save/load system, and difficulty presets.

---

## 🔧 Tech Stack

- **Language:** Python 3  
- **Core Logic:** Recursion (Flood Fill), Board Generation, Input Validation  
- **Data Handling:** `pickle` for save/load system  
- **Utils:** `pathlib` for cross-platform save directory  

---

## ✨ Features

- 🎮 **Fully playable Minesweeper in terminal**  
- 💥 **Smart bomb generation** (generated after first safe click)  
- 🔍 **Auto-reveal flood fill** for zero tiles  
- 💾 **Save & load game** using generated room codes  
- 📊 **Difficulty presets** (Easy, Medium, Hard, ???)  
- 📂 **Cross-platform save directory** using the user's Documents folder  
- 🧹 **Clean board rendering** with emoji tiles  
- 🛡️ **Input validation** to prevent invalid moves  
- 🧠 **Accurate number generation** based on adjacent bombs  

---

## 📁 Project Structure
<pre>
  minesweeper/
├── animation_handler.py # Typing animations and UI effects
├── data_handler.py # Save/load logic using pickle
├── minesweeper_tools.py # Core game logic (board, flood fill, win/loss)
├── main.py # Entry point (difficulty, main game loop)
├── saves/ # (Old) save folder before using Path.home()
└── README.md
</pre>

---

## 🧩 How It Works

### 🎲 Board Generation
- Creates an empty visible grid (`📦`)  
- Bombs are generated **only after the first click**  
- Numbers on tiles represent nearby bombs (0–8)

### 🌊 Flood Fill Reveal  
Zero tiles (`0`) automatically reveal surrounding tiles recursively.

### ⚙️ Game Loop
- Display grid  
- Ask for coordinates  
- Reveal tile / trigger flood fill  
- Check win/lose conditions  
- Continue or terminate  

### 💾 Save System
- Game state stored as `.dat` using `pickle`  
- Automatically creates folder and file if missing  
- You get a unique 6-char code when saving  

---

## 🚀 Running the Game

1. Install Python 3  
2. Clone the repo:

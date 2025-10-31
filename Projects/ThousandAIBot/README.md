# 🎮 ThousandBot (MCTS AI)

This repository contains my final project for the **Artificial Intelligence** course.  
The goal was to develop a bot capable of playing the card game **"Thousand"** using the **Monte Carlo Tree Search (MCTS)** algorithm.  

The bot’s logic is divided into two main phases: **bidding** and **playing**.  

- **Bidding phase**: Based on probabilities. All possible hands are evaluated, counting winning tricks and points for melds. These values are aggregated to calculate the probability of achieving certain points, guiding the decision to play or pass.  
- **Playing phase**: Implemented using the MCTS algorithm. This runs only when no card is guaranteed to win a trick.  

The `FullGame.py` script simulates a full game with random players and prints detailed game data to the console.

---

## ⚙️ Dependencies

This project requires the following Python libraries:

- `typeguard` — runtime type checking  
- `pygame` — graphical interface and game mechanics *(currently in progress)*  
- `random`, `copy`, `logging`, `math`, `concurrent.futures` — part of the Python standard library

### Installation

Install external dependencies via:

```bash
pip install typeguard pygame
```

### 🚀 Usage

To run the **Thousand Bot**:

1. Ensure **Python 3.9** or higher is installed.
2. Install dependencies as shown above.
3. Run the simulation:
4. python FullGame.py

```bash

## 🗂️ Folder Structure

```text
ThousandBot/
├─ FullGame.py              # Main simulation script
├─ Auction.py               # Bidding logic
├─ Bot.py                   # Bot logic and decision making
├─ Card.py                  # Card representation and utilities
├─ CardsManipulator.py      # Helper functions to manipulate card sets
├─ Deck.py                  # Deck management
├─ Game.py                  # Game rules and flow
├─ GlobalVariables.py       # Global constants and variables
├─ MonteCarlo.py            # Monte Carlo Tree Search implementation
├─ Player.py                # Player class
├─ Thousand.py              # Game engine
├─ graphics/                # Card and board images
│   └─ *.png
└─ README.md

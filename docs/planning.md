

# The plan
---
## Classes

### Game-Board
Validates win conditions and game moves and is responsible for storing the game board.

Main tasks:
- Store a 6x7 grid
- Check if a move is valid
- Drop a stone
- Detect win conditions

### Player
Represents a human or computer.

Main tasks:
- Store player type (human or computer)
- Store player symbol or color

### Game
Enforces game rules and turn transitions.

Main tasks:
- Initialize the game
- Switch between players
- Handle user input
- End the game

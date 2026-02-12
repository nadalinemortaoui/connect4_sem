# Connect Four – Project Documentation

## 1. Project Overview

This project implements the core logic of the game *Connect Four*.
The main focus is on the internal board mechanics, win condition detection,
and verification of correctness through automated unit tests.

The implementation follows a modular structure in order to ensure clarity,
maintainability, and testability of the code base.

---

## 2. Project Structure
connect4_sem/
├── src/
│   └── connect4/
│       ├── board.py
│       ├── game.py
│       ├── player.py
│       └── init.py
├── tests/
│   └── test_board.py
├── docs/
│   └── project_documentation.md
└── README.md
### Description
- `board.py` contains the board representation and the win condition logic.
- `game.py` and `player.py` are part of the predefined project structure and
  are not required for the core assignment.
- `tests/` contains automated unit tests for board behavior and win detection.
- `docs/` contains the project documentation.

---

## 3. Board Logic

The `Board` class represents the Connect Four game board.
When a piece is placed in a column, the algorithm iterates from the bottom
row upwards to simulate gravity and ensure that the piece is placed in the
lowest available position.

This behavior guarantees realistic game mechanics and prevents invalid placements.

---

## 4. Win Condition Logic

The win condition logic checks whether a player has achieved four connected
pieces in one of the following directions:

- Horizontal
- Vertical
- Diagonal (top-left to bottom-right)
- Diagonal (bottom-left to top-right)

After each move, the board state is evaluated to determine whether a winning
configuration exists.

A syntax issue in the piece placement loop was identified and corrected.
After this correction, the win detection logic functions as intended.

---

## 5. Testing and Verification

Automated unit tests are implemented in `tests/test_board.py` to verify the
correctness of the board logic and win condition detection.

The test cases cover:
- Valid and invalid moves
- Correct placement of pieces
- Detection of horizontal, vertical, and diagonal wins
- Non-winning scenarios

All tests were executed successfully using `pytest`, confirming that the
implementation behaves correctly.

---

## 6. Version Control and Workflow

The project uses Git for version control.

Development was carried out on a separate feature branch.
Changes were documented using meaningful commit messages, ensuring traceability
of all modifications.

The project is prepared for integration into the main branch via a pull request.

---

## 7. Conclusion

The core logic of the Connect Four game has been successfully implemented and
verified. Board mechanics and win condition detection operate correctly, and
their functionality has been confirmed through automated testing.

The project fulfills all requirements of the assignment and provides a clean
and maintainable foundation for further extensions if required.

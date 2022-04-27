# A Checkerboard Game in Python

## Requirements

---

- Python 3.10+

## Installation

---

- Clone the repository:

```bash
git clone https://github.com/talhaibnmahmud/python-checkerboard.git
```

- Create a virtual environment:

```PowerShell
python -m venv venv
```

- Activate the virtual environment:

```PowerShell
. venv\Scripts\activate
```

- Upgrade pip:

```PowerShell
python -m pip install --upgrade pip
```

- Installing dependencies:

```PowerShell
python -m pip install -r requirements.txt
```

## Usage

---

```PowerShell
python main.py
```

- Use right mouse button to select a piece to move.
  If the selected piece has any valid moves, it will be highlighted.

- Use left mouse button to move the piece to any of the highlighted squares.

## Game Rules

---

Checkers is played by two opponents on opposite sides of the game board. One player has the dark pieces (usually black); the other has the light pieces (usually white or red). Players alternate turns. A player can not move an opponent's pieces. A move consists of moving a piece diagonally to an adjacent unoccupied square. If the adjacent square contains an opponent's piece, and the square immediately beyond it is vacant, the piece may be captured (and removed from the game) by jumping over it.

Only the dark squares of the checkerboard are used. A piece can only move diagonally into an unoccupied square. When capturing an opponent's piece is possible, capturing is mandatory in most official rules. If the player does not capture, the other player can remove the opponent's piece as penalty (or muffin). And where there are two or more such positions, the player forfeits pieces that cannot be moved. Although some rule variations make capturing optional. In almost all variants, the player without pieces remaining, or who cannot move due to being blocked, loses the game.

- Man

An uncrowned piece (man) moves one step diagonally forwards and captures an adjacent opponent's piece by jumping over it and landing on the next square. Multiple enemy pieces can be captured in a single turn provided this is done by successive jumps made by a single piece; the jumps do not need to be in the same line and may "zigzag" (change diagonal direction). In American checkers, men can jump only forwards; in international draughts and Russian draughts, men can jump both forwards and backwards.

- King

When a man reaches the farthest row forward, known as the kings row or crownhead, it becomes a king. It is marked by placing an additional piece on top of, or crowning, the first man. The king has additional powers, including the ability to move backwards and, in variants where men cannot already do so, capture backwards. Like a man, a king can make successive jumps in a single turn, provided that each jump captures an enemy piece.

In international draughts, kings (also called flying kings) move any distance along unblocked diagonals. They may capture an opposing man any distance away by jumping to any of the unoccupied squares immediately beyond it. Because jumped pieces remain on the board until the turn is complete, it is possible to reach a position in a multi-jump move where the flying king is blocked from capturing further by a piece already jumped.

Flying kings are not used in American checkers; a king's only advantage over a man is the additional ability to move and capture backwards.

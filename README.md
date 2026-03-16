# 📁 Grid Player
> A Python simulation of a player moving randomly on a 2D grid, built with abstraction, tuples, and coordinate based movement.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project uses abstract base classes and the `random` module to simulate a `player` navigating a 2D grid. An abstract Player class defines the shared movement logic, and a concrete `Pawn` subclass defines which directions are available. Leveling up unlocks diagonal moves, expanding the pawn's movement from 4 directions to 8. The project reinforces abstraction, tuple arithmetic, and working with coordinate systems.

## 🧠 What I Learned

- **Abstract classes for shared logic** — Unlike the Advanced Discount Calculator where `ABC` enforced an interface with no shared logic, here Player provides a working `make_move()` implementation while still requiring subclasses to define `level_up()`, showing that abstract classes can share and enforce behavior at the same time
- **Tuple arithmetic for coordinates** — Adding two tuples together element-by-element `(random_moves[0] + self.position[0], random_moves[1] + self.position[1])` to update a position on a 2D grid without needing a dedicated library
- **`random.choice()`** — Selecting a random move from the available list each turn, making each simulation run unique
- **Path tracking with a list** — Appending each position to self.path as the player moves, building a complete history of every coordinate visited
- **`+=` to extend a list** — Using `self.moves` += [...]` in `level_up()` to add diagonal moves to the existing list without replacing it
- **Designing for extensibility** — Structuring the code so new player types (e.g. a Knight or Bishop with different move sets) could be added simply by subclassing Player and defining their own moves and `level_up()`

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |
| `abc` | Defining the abstract base class and enforcing `level_up()` |
| `random` | Selecting a random move each turn |

## 💡 How It Works

`Player` defines all shared behavior, position tracking, path history, and the `make_move()` method. Concrete subclasses define what moves are available.

`Pawn` starts with 4 cardinal moves and gains 4 diagonal moves on level up:

| State | Available Moves |
|-------|-----------------|
| Default | Right, Left, Up, Down |
| After `level_up()` | + Diagonal (NW, NE, SE, SW) |

Each call to `make_move()` picks a random direction, updates the position, and appends it to the path.

**Example Output:**

```
pawn = Pawn()
for _ in range(5):
    print(pawn.make_move())

pawn.level_up()
print(pawn.moves)  # Now includes diagonals
```

## 🚀 Future Improvements

- [ ] Add a `Knight` subclass with L-shaped moves like a chess knight
- [ ] Visualise the path on a grid using `matplotlib` or a simple terminal renderer
- [ ] Add boundary limits so the player can't move outside a defined grid size
- [ ] Track how many times the player visits the same coordinate

## 📂 Project Structure

```
grid-player/
│
├── PlayerInterface.py    # Player ABC and Pawn subclass
└── README.md
```

*Part of my Python learning journey 🐍 — reinforcing abstraction and exploring coordinate based movement on a 2D grid*

# Project Outline
## Map
```
Overlook   Treasure
  ||         ||
 Foyer ->  Narrow
  ||
Outside
```

---

## Class Planning

**REPL Class**

- Print Name and Description of Current Room after movement.
- n , s , e , w are valid commands for movement
- Print item list of current room.
- Understand Verb , Object input.
- i command for inventory.

---

**ROOM Class**

- Name
- Description
- list [all items in room]
- n_to
- s_to
- w_to
- e_to

---

**Player Class**

- Name
- Current Room
- Inventory

---

**Item Class**

- Name
- Description
- onTake
- onDrop

---

```
├── FAQ.md
├── Pipfile
├── README.md
├── examples
│   ├── guessing_game.py
│   ├── history.txt
│   └── rock_paper_scissors.py
├── plan.md
└── src
    ├── adv.py
    ├── player.py
    └── room.py
```

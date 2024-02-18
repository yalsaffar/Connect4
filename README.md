# Connect 4 with MCTS

A Connect 4 game implementation in Python, featuring a Monte Carlo Tree Search (MCTS) agent to play against a human. Developed as a class project in 2022.


## Introduction

This project implements a Connect 4 game where players can compete against an MCTS agent. The MCTS algorithm allows the agent to simulate multiple game scenarios to determine the best move. This approach is different from traditional minimax or alpha-beta pruning, as it uses random game playouts rather than a deterministic evaluation function.

## Installation

To run this game, ensure Python is installed on your system. Clone the repository to your local machine and navigate to the directory.

```bash
git clone https://github.com/yalsaffar/Connect4
cd Connect4
```

## Usage

To start a game with the MCTS agent, run the `play.py` script from your terminal with Python. The depth of the MCTS algorithm can be specified as an argument, which influences the agent's lookahead capability. For example, to set the depth to 3000:

```bash
python play.py 3000
```

The game prompts you for your move as a human player against the agent.

## Features

- Connect 4 game logic.
- Human vs MCTS agent gameplay.
- Agent uses Monte Carlo Tree Search for decision-making.
- Configurable depth for the MCTS algorithm.

## Monte Carlo Tree Search vs Alpha-Beta Pruning

The MCTS algorithm offers several advantages over traditional alpha-beta pruning in games like Connect 4. While alpha-beta pruning requires a well-defined evaluation function to estimate the desirability of a game state, MCTS uses a more dynamic approach by simulating many game outcomes from the current state. This makes MCTS particularly effective in games with a high branching factor or when the evaluation of game states is complex or difficult to quantify. The randomness in MCTS can also introduce unpredictability in the agent's play style, making it more challenging for human players.

## Dependencies

- Python 3.11

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).



# MinMax-Noughts-Crosses

A simple Python Noughts & Crosses game that utilises the MinMax algorithm. Alpha-beta pruning has also been implemented to make the AI player work more efficiently.

## Features

- **MinMax Algorithm**: Implements the MinMax algorithm to determine the optimal move for the AI.
- **Alpha-Beta Pruning**: Enhances the MinMax algorithm by pruning unnecessary branches, significantly reducing the computation time.
- **Command-Line Interface**: A simple and interactive CLI for playing the game.

## Alpha-Beta Pruning

Alpha-beta pruning is an optimisation technique for the MinMax algorithm. It reduces the number of nodes evaluated by the MinMax algorithm in its search tree. While it doesn't affect the final result, it helps in cutting down the computation time by ignoring branches that won't affect the final decision.

### How it Works

- **Alpha**: The best value that the maximiser currently can guarantee at that level or above.
- **Beta**: The best value that the minimiser currently can guarantee at that level or above.

During the search, if the minimiser's current value is less than or equal to alpha, the maximizer will stop considering that branch. Similarly, if the maximiser's current value is greater than or equal to beta, the minimizer will stop considering that branch. This reduces the number of nodes to be evaluated in the search tree.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/joelb429078/MinMax-Noughts-Crosses.git

2. Navigate to the project directory:  cd MinMax-Noughts-Crosses

3. Run the game: python MinMax.py

## Usage
- **Human Player**: The human player is prompted to enter their move (1-9) when it is their turn.
- **Computer Player**: The computer player automatically makes the optimal move using the MinMax algorithm with alpha-beta pruning.

## License
This project is licensed under the MIT License.



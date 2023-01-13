# Tic-Tac-Toe-Game-with-Minimax-AI
This is a simple Tic-Tac-Toe game implemented in Python using the minimax algorithm for the computer's moves.

## How to run the game
1. Download the TicTacToe.py file
2. Run the file in your Python environment
3. Follow the on-screen prompts to make your move
4. The computer will make its move and the game will continue until a winner is determined or a tie is reached

## How to Play
The Tic-Tac-Toe game is a two-player game where each player chooses a symbol (X or O) and takes turns marking the spaces in a 3x3 grid. The player who succeeds in placing three of their symbols in a horizontal, vertical, or diagonal row wins the game.

To start the game, simply run the TicTacToe.py file in your preferred Python environment. The game will prompt you to make your first move by entering a number between 0-8, corresponding to the spaces on the game board. The computer will then make its move, and the game will continue in this fashion until a winner is determined or a tie is reached.

The game board is represented as a list with 9 spaces, indexed as follows:


              0 | 1 | 2 

              3 | 4 | 5 

              6 | 7 | 8 

You can also customize the symbol of the computer and the player by changing the self.computer and self.player in the constructor of the TicTacToe class.
The game uses the minimax algorithm to determine the computer's next move, so it will always play optimally.
Enjoy playing!

## How the computer's moves are determined
The computer's moves are determined using the minimax algorithm. This algorithm is a decision-making algorithm that is commonly used in two-player games such as Tic-Tac-Toe and chess. It evaluates all possible future moves and chooses the move that leads to the best outcome for the computer. In the case of Tic-Tac-Toe, the algorithm considers all possible future moves and chooses the move that leads to the computer winning or a tie.

## How to customize the game
You can change the player's symbol and computer's symbol in the init method of the TicTacToe class.

The game's rule can also be changed by editing the check_win and check_tie methods of the class.

## Note
This implementation is for demonstration purposes only and is not suitable for a production environment. The minimax algorithm does not include a depth limit, so the game will run indefinitely for certain combinations of moves.

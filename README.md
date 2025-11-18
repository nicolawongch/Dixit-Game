# Dixit Remote Scorekeeper

A command-line Python program to help a games master (GM) keep track of scores during a remote/grouped version of the board game Dixit. Designed for 3–5 teams, the tool assists the GM in managing rounds, votes, and point calculations while ensuring robust input validation for seamless use.

## Features

- **Flexible team management**: Supports 3 to 5 teams with customizable names.
- **Round-by-round scoring**: Input which team is storyteller, card assignments, and each team's vote each round.
- **Automated Dixit scoring**: Handles all classic Dixit scoring, including:
  - Storyteller scoring (all/none guess, regular guess)
  - Guessers scoring for correct guesses
  - Bonus points for cards voted for (but not the storyteller’s)
- **Input validation**: Prevents duplicate card numbers and voting for unplayed or own cards.
- **Instant score summary**: See scores updated after each round.
- **Command-line ease**: Intuitive to operate; no installation of extra libraries needed.

## Usage

### 1. Setup

Ensure you have Python 3 installed.

Clone or download this repository and launch the script:

```bash
python dixit_scorekeeper.py
```

### 2. Game Flow

1. Enter the number of teams (3–5).
2. Enter each team’s name.
3. For each round:
   - Choose the storyteller team.
   - Assign a unique card number to each team’s card.
   - Enter each team’s vote (cannot vote for own card or invalid card).
   - Score is automatically calculated and displayed.
   - Choose to play another round or end the game.

### 3. Scoring Rules Recap

- **Storyteller:**
    - 3 points if at least 1 but not all teams guess the storyteller's card.
    - 0 points if all or none guess correctly.
- **Guessing Teams:**
    - 3 points for correctly identifying the storyteller's card.
    - 2 points each if all or none guess correctly.
- **Bonus:**
    - 1 point for each vote received on your card if you are NOT the storyteller.

## Example

```bash
Welcome to Dixit Scorekeeper!
Number of teams (3-5): 4
Team 1 name: Sunflowers
Team 2 name: Butterflies
Team 3 name: Rainbows
Team 4 name: Mountains

--- Round 1 ---
0: Sunflowers (Score: 0)
1: Butterflies (Score: 0)
2: Rainbows (Score: 0)
3: Mountains (Score: 0)
Storyteller team index: 2
...
SCORES after this round:
Sunflowers: 2
Butterflies: 4
Rainbows: 3
Mountains: 1
```

## Notes

- Designed for manual operation by the games master (does not support player input).
- Will prompt for correction if you make a data entry mistake.

## License

MIT License

## Acknowledgments

Inspired by Dixit, designed by Jean-Louis Roubira, published by Libellud.


Defeat The Wizard Game.

This is a turn-based RPG battle game where players choose a character and engage in combat against the formidable Mad Wizard. The game features modular design, dynamic combat mechanics, and replayability with debug mode support.

Features

Player Character Options: Choose from a Warrior, Mage, Archer, Rogue, or Paladin.

Dynamic Combat: Each character has unique abilities, including core attacks, special attacks, and defensive moves.

Mad Wizard: A challenging opponent with regenerating health and powerful attacks.

State Management: Effects like stuns and damage reduction are tracked and applied dynamically.(Not yet)

Replayability: Replay with the same character or choose a new one.


Installation

Clone the repository:

git clone https://github.com/your-repo/rpg-battle-game.git
cd rpg-battle-game

Ensure you have Python 3.8+ installed.

Install any required dependencies:

pip install -r requirements.txt

How to Play

Run the game:

python game_main.py

Follow the prompts to choose a character and start the battle.

During combat, select your action each turn:

Attack with core attack.

Use a special attack.

Heal.

View your character's stats.

Defeat the Mad Wizard or be defeated.

Replay the game with the same or a new character.

Debug Mode

Enable debug mode to display detailed game state information:

python game_main.py --debug

File Structure

.
├── core_character.py         # Base Character class
├── warrior_character.py      # Warrior class
├── mage_character.py         # Mage class
├── archer_character.py       # Archer class
├── rogue_character.py        # Rogue class
├── paladin_character.py      # Paladin class
├── evil_wizard_character.py  # Mad Wizard class
├── character_selection.py    # Character selection logic
├── combat_system.py          # Combat mechanics
├── game_main.py              # Main game flow
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

Testing

Install unittest (included with Python) or pytest for testing.

Run the tests:

python -m unittest discover

For additional debug information during tests, enable debug mode.

Future Enhancements

Add difficulty levels.

Introduce more characters and enemy types.

Implement multiplayer mode.

Add save/load functionality.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Thank you for playing  Defeat The Wizard!


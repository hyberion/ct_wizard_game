from evil_wizard_character import EvilWizard
from character_selection import choose_character
from combat_system import combat

def initialize_combat_states(player, enemy):
    """
    Set up initial combat states for the player and enemy.
    """
    player.is_stunned = False
    enemy.is_stunned = False
    enemy.damage_reduction_active = False

def replay_game():
    """
    Allow the player to replay the game with the same or a new character.
    """
    player_character = choose_character()
    # Initialize character state properties
    player_character.is_stunned = False

    while True:
        mad_wizard = EvilWizard()
        mad_wizard.is_stunned = False
        mad_wizard.damage_reduction_active = False

        # Call combat without the 'states' argument
        combat(player_character, mad_wizard)

        print("\nWhat would you like to do?")
        print("1. Replay with the same character")
        print("2. Choose a new character")
        print("3. Exit the game")

        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            continue
        elif choice == "2":
            player_character = choose_character()
            # Reinitialize character state properties
            player_character.is_stunned = False
        elif choice == "3":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please choose again.")

def main():
    """
    Main function to handle a single playthrough of the game.
    """
    print("Welcome to the RPG Battle!")
    player_character = choose_character()
    # Initialize character state properties
    player_character.is_stunned = False

    mad_wizard = EvilWizard()
    mad_wizard.is_stunned = False
    mad_wizard.damage_reduction_active = False

    # Call combat without the 'states' argument
    combat(player_character, mad_wizard)

    print("Thank you for playing! Goodbye.")

# Run the game
if __name__ == "__main__":
    replay_game()
153
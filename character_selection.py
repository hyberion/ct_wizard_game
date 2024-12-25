from warrior_character import Warrior
from mage_character import Mage
from archer_character import Archer
from rogue_character import Rogue
from paladin_character import Paladin

def choose_character():
    """
    Allow the player to choose their character from available options.

    :return: An instance of the chosen character class.
    """
    characters = {
        "1": Warrior("Warrior"),
        "2": Mage("Mage"),
        "3": Archer("Archer"),
        "4": Rogue("Rogue"),
        "5": Paladin("Paladin")
    }

    print("Choose your character:")
    print("1. Warrior - High health, strong attacks, low dodge")
    print("2. Mage - Low health, spellcasting, mana-based abilities")
    print("3. Archer - Mid health, high dodge, ranged attacks")
    print("4. Rogue - Low health, high dodge, agile and sneaky")
    print("5. Paladin - High health, sturdy defense, balanced fighter")

    choice = None
    while choice not in characters:
        choice = input("Enter the number of your choice: ")
        if choice not in characters:
            print("Invalid choice. Please choose a valid character.")

    selected_character = characters[choice]
    print(f"You have chosen: {selected_character.name}")
    return selected_character

# Example usage
if __name__ == "__main__":
    player_character = choose_character()
    player_character.display_stats()

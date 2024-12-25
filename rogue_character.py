from core_character import Character
import random

class Rogue(Character):
    def __init__(self, name):
        """
        Initialize the Rogue character with specific attributes.

        :param name: str - The name of the rogue.
        """
        super().__init__(name, health=100, attack_power=20, dodge_chance=0.5)  # Low health, moderate attack, high dodge

    def dagger_swipe(self, target):
        """
        Perform a dagger swipe attack that can hit the target twice.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} performs a quick dagger swipe at {target.name}!")
        hits = 0
        for _ in range(2):
            if random.random() > target.dodge_chance:
                hits += 1
                print(f"A dagger swipe hits for {self.attack_power} damage!")
                target.health -= self.attack_power
            else:
                print(f"{target.name} dodges a dagger swipe!")
        print(f"{self.name}'s dagger swipe hits {hits} time(s)!")

    def backstab(self, target):
        """
        Perform a sneaky backstab on the target, dealing high damage.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} attempts a sneaky backstab on {target.name}!")
        if random.random() > target.dodge_chance:
            damage = self.attack_power * 3
            print(f"The backstab lands for {damage} damage!")
            target.health -= damage
        else:
            print(f"{target.name} senses the backstab and dodges it!")

    def fade_into_shadows(self):
        """
        Fade into the shadows to completely avoid an incoming attack.

        :return: bool - True if the ability is successful, False otherwise.
        """
        success = random.random() < self.dodge_chance
        if success:
            print(f"{self.name} fades into the shadows and avoids the attack!")
        else:
            print(f"{self.name} fails to fade in time and takes the hit!")
        return success

    def display_stats(self):
        """
        Display the current stats of the Rogue character, including special abilities.
        """
        super().display_stats()
        print("Special Abilities: Dagger Swipe (Double Strike), Backstab (High Damage), Fade Into Shadows (Avoid Attack)")

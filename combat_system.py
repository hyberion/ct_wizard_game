def combat(player, enemy):
    """
    Handles the turn-based combat between the player and the enemy.

    :param player: Character - The player's chosen character.
    :param enemy: Character - The enemy character (e.g., Mad Wizard).
    """
    import random

    turn_count = 0  # Tracks the number of turns

    print(f"\nCombat begins! {player.name} vs {enemy.name}")

    # Randomly determine who starts first
    player_turn = random.choice([True, False])
    if player_turn:
        print(f"{player.name} gets the first turn!")
    else:
        print(f"{enemy.name} gets the first turn!")

    while player.health > 0 and enemy.health > 0:
        turn_count += 1
        print(f"\n--- Turn {turn_count} ---")

        if player_turn:
            while True:  # Loop to allow restarting the turn after viewing stats
                print("Your options:")
                print("1. Attack with Core Attack")
                print("2. Use Special Attack")
                print("3. Heal")
                print("4. View Stats")

                action = input("Choose your action (1-4): ")

                if action == "1":
                    print("\nYou choose to attack!")
                    player.base_attack(enemy)
                    break
                elif action == "2":
                    print("\nYou choose to use your special attack!")
                    if hasattr(player, 'power_attack'):
                        player.power_attack(enemy)
                    elif hasattr(player, 'firebolt'):
                        player.firebolt(enemy)
                    elif hasattr(player, 'arrow_barrage'):
                        player.arrow_barrage(enemy)
                    elif hasattr(player, 'backstab'):
                        player.backstab(enemy)
                    elif hasattr(player, 'holy_strike'):
                        player.holy_strike(enemy)
                    else:
                        print("Special attack not available for this character.")
                    break
                elif action == "3":
                    print("\nYou choose to heal!")
                    player.heal()
                    break
                elif action == "4":
                    print("\nYou choose to view stats!")
                    player.display_stats()
                    restart = input("Press any key to restart the turn.")
                    continue  # Restart the turn
                else:
                    print("Invalid action. Please choose a valid option.")
        else:
            print(f"\n{enemy.name}'s turn!")
            enemy_action = random.choice(['lightning', 'frost_bolt'])
            if enemy_action == 'lightning' and hasattr(enemy, 'lightning_strike'):
                enemy.lightning_strike(player)
            elif enemy_action == 'frost_bolt' and hasattr(enemy, 'frost_bolt'):
                enemy.frost_bolt(player)

            if enemy.health > 0 and hasattr(enemy, 'regenerate_health'):
                enemy.regenerate_health()

        # Alternate turns
        player_turn = not player_turn

        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

    if player.health > 0:
        print(f"\n{player.name} has defeated {enemy.name} in {turn_count} turns!")
    else:
        print(f"\n{enemy.name} has defeated {player.name} in {turn_count} turns!")

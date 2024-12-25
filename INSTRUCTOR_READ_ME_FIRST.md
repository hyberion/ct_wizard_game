# Submission Notes for RPG Character Implementation

## Project Status (An apology)

So I fell down the rabbit hole on this one and after 4 days of mucking about with it I have to bite the bullet and turn it in.


---

## Notes and Observations

1. **State Tracking for Conditions (e.g., Stun, Blind)**
   -You wll see some ghosts (probably) of a state funciton tracking (stun, blinded, etc).  I have the core logic of it but kept
running into problems getting it to work across characters so it became a v2 thing, but you might see the remnants in there occasionally.

2. **Character Changes and Balance Issues**
   -I made some changes to the characters and how they work but that has borked the balance somewhat.  I'm working on getting it more balanced but, as I said, need to turn it in.


3. **Negative Health Display**
   - Currently, health can display as negative after damage. In future iterations, I would add a function to cap health at `0`.
   - Additionally, I would implement a mechanic where, if the player's health drops below 10, an automatic healing attempt would occur (provided healing potions are available).

4. **Special Ability Usage Limitation**
   - There was also an attempt to put a limiter on the special abilites (so the player just couldn't spam the big attacks) but I feel like I've run out of time.

5. **Taunt System**
   - I know I really should have the taunts for the Wizard coming from an external file but . . .time. . ran . . out.

6. **Modularization**
   - I alos decided halfway through to modularize the whole thing (because I'm insane and I hate myself) which also created it's own little slice of issues, which created issues.

---

## Areas for Improvement

- **Health Display and Handling:**
  - Prevent health from displaying negative values.
  - Implement an auto-healing mechanic when health is critically low.

- **Ability Balancing:**
  - Introduce a limiter for special abilities to prevent abuse.

- **File-Based Taunt Management:**
  - Move taunt strings to an external configuration file (e.g., JSON or YAML) to simplify updates and allow for localization or expansion.

- **State Tracking Implementation:**
  - Finalize and integrate state tracking (e.g., `stun`, `blinded`, etc.) across all characters in a consistent and maintainable manner.

- **Playtesting and Balancing:**
  - Perform more rigorous playtesting to fine-tune character abilities, game balance, and difficulty scaling.

---

## Acknowledgment

So I hit the point that I could either scrap it and start over to get it cleaner, or keep the ambitions (and the inevitalble bugs and balance issues) and just send it up the flagpole (as again, it's alrady been almost 5 days) and hope it doesn't catch on fire.

I throw myself upon your mercy.


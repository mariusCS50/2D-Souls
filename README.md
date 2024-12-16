# 2D-Souls## README

### Game Description
**2D Souls** is an engaging 2D RPG game developed using the Arcade library in Python. Players control a hero who navigates various levels, defeats hordes of monsters, and battles powerful bosses to achieve victory. The game combines strategic combat mechanics, exploration, and resource management to provide a challenging and rewarding experience.

The gameplay revolves around progressing through levels, collecting resources, and mastering combat mechanics. Each level features unique challenges, including enemies with distinct behaviors, environmental obstacles, and climactic boss battles.

### GitHub Repository
The project is hosted on GitHub. You can access it at: [GitHub Repository](https://github.com/mariusCS50/2D-Souls).

### Languages and Technologies Used
The game is implemented using:
- **Python**: The main programming language for game logic.
- **Arcade Library**: Used for graphics, animations, input handling, and game development features.

### Instructions for Running the Game
To run **2D Souls**, follow these steps:

1. **Install Dependencies**:
   Ensure you have Python installed on your system. Install the required modules by running the following command in the project directory:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Game**:
   Launch the game using the command:
   ```bash
   python game.py
   ```

3. **Controls**:
   - Use **W**, **A**, **S**, and **D** to move your character.
   - **Left-click** to perform an attack.
   - Press **Spacebar** to dodge enemy attack.
   - Press **E** to pick up items and **R** to drop them on the ground
   - Press **Q** to use special abilities unlocked during gameplay.
   - Use the **mouse wheel scroll** to change the current item
   - Use the **number keys** to switch abilities
   - Use the **Enter** and **ESC** keys to start the game or close it

The gameplay screen includes UI elements that display the player’s health, item and ability inventories, messages to notify the player about the number of enemies on the map and the spawn of the bosses.

### Contributions

As a team, we worked collaboratively to create the finished game, combining individual efforts with shared tasks. While we handled specific responsibilities independently, we also worked together on several featuresh. Below are some of the contributions made by each team member:

#### Marius Gaibu
- Created themed maps, using corresponding tilesets, textures and images
- Introduced the player spawn and camera. Introduced melee attacking mechanic
- Implemented the melee enemy logic, with the respective functionalities
- Implemented and fixed bugs related to collision mechanics affecting performance and gameplay
- Creaded the item inventory and ability slots mechanics and UI elements, with their respective functionalities
- Implemented a boss and created the boss unique abilities. Created the granting ability mechanic which allows the player to use the abilities of the defeated bosses.
- Implemented the separate views from the game and the logic behind changing the views.

#### Andrei Preda
- Created basic player controller with attack, dodge abilities and invincibility
- Created snowy plains island
- Added weapon support and assets (including assets for player animation based on type of weapon)
- Added health bar to player
- Implemented basic enemy abstract class and ranger enemy logic
- Added projectiles
- Added damage logic for player and enemies/bosses
- Added enemy coordinates for every island
- Implemented winter and volcano bosses
- Added UI status for island: number of enemies left and boss incoming announcement

### Challenges and Solutions

1. **Collision Detection**:
   Implementing accurate and efficient collision detection was challenging, particularly for projectiles and enemy interactions. The solution involved using precise hitboxes and a simplified collision model to maintain performance.

2. **Synchronizing Animations and Events**:
   Early issues with animations being out of sync with gameplay events were addressed by implementing an event-driven system that coordinated animations and logic seamlessly.

3. **Balancing Gameplay**:
   Finding the right difficulty balance was a significant challenge. The team tested various configurations for enemy behavior, boss mechanics, and player abilities to ensure the game remained challenging but fair.
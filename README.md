# Quest Generator for Board Games

A Python-based tool that generates unique quests for board games, complete with characters, a story, and random events. This tool dynamically generates a terrain map, populates it with characters, and creates quests, which can be exported to a PDF.

---

## Features

- **Dynamic Terrain Map**: Generates a grid-based map with random terrain types (e.g., Forest, Mountain, Desert).
- **Character Creation**: Randomly generates characters with unique names, roles, backstories, and locations on the map.
- **Quest Generation**: Creates random quests with objectives, details, and associations to characters or locations.
- **PDF Export**: Exports the entire quest, including the map, characters, and quests, to a PDF file.

---

## Requirements

To run the Quest Generator, you need the following Python libraries:

- `faker`: For generating random character names and backstories.
- `random`: For generating random events and map features.
- `fpdf`: For exporting the quest to a PDF file.

Install the dependencies using pip:

```bash
pip install faker fpdf
```

---

## How to Use

1. Clone or download this repository.
2. Run the Python script to generate a quest:

```bash
python quest_generator.py
```

3. The script will generate:
   - A random map.
   - A set of characters with roles and backstories.
   - A set of quests with objectives and details.
4. The generated quest will be exported to a PDF file named `board_game_quest.pdf` in the same directory.

---

## Customization

You can customize the quest generation by modifying the parameters in the script:

- **Grid Size**: Change the size of the map grid.
- **Number of Characters**: Adjust the number of characters on the map.
- **Number of Quests**: Change how many quests are generated.

Example customization in the script:
```python
quest_gen = QuestGenerator(grid_size=8, num_characters=6, num_quests=4)
```

---

## Example Output

### Terrain Map
```
Forest Mountain Lake Plains Desert
Mountain Desert Plains Forest Lake
Plains Plains Desert Forest Desert
Lake Mountain Forest Plains Plains
```

### Characters
- **Name**: John Smith  
  **Role**: Knight  
  **Backstory**: A brave warrior who has defended the realm against many foes.  
  **Location**: (2, 3)

- **Name**: Alice Johnson  
  **Role**: Merchant  
  **Backstory**: A cunning trader known for her sharp wit and resourcefulness.  
  **Location**: (1, 4)

### Quests
1. **Quest Giver**: John Smith  
   **Objective**: Find the lost artifact.  
   **Location**: (3, 2)  
   **Details**: Recover the fabled Amulet of Light hidden deep in the Forgotten Forest.  

---

## File Structure

- `quest_generator.py`: The main script to generate quests and export them to PDF.
- `board_game_quest.pdf`: The generated PDF file (created after running the script).

---

## License

This project is licensed under the [MIT LICENSE](LICENSE). Feel free to modify and use it for personal or commercial projects.
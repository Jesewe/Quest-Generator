import random
from faker import Faker
from fpdf import FPDF
from typing import List, Tuple, Dict

fake = Faker()

class QuestGenerator:
    """
    Generates a map, characters, and quests for a game and exports them to a PDF.
    """
    TERRAIN_TYPES = ['Forest', 'Mountain', 'Desert', 'Plains', 'Lake']
    CHARACTER_ROLES = ['Villager', 'Merchant', 'Knight', 'Mage']
    QUEST_OBJECTIVES = [
        "Find the lost artifact", 
        "Defeat the monster", 
        "Escort the merchant", 
        "Explore the ancient ruins", 
        "Deliver a secret message"
    ]
    
    def __init__(self, grid_size: int = 10, num_characters: int = 5, num_quests: int = 3):
        self.grid_size = grid_size
        self.num_characters = num_characters
        self.num_quests = num_quests
        self.map: List[List[str]] = []
        self.characters: List[Dict] = []
        self.quests: List[Dict] = []
    
    def generate_map(self) -> None:
        """Generate a random grid map with different terrain types."""
        try:
            self.map = [
                [random.choice(self.TERRAIN_TYPES) for _ in range(self.grid_size)]
                for _ in range(self.grid_size)
            ]
        except Exception as e:
            print(f"Error generating map: {e}")
    
    def generate_characters(self) -> None:
        """Generate random characters with roles, backstories, and locations."""
        try:
            self.characters = [
                {
                    "name": fake.name(),
                    "role": random.choice(self.CHARACTER_ROLES),
                    "backstory": fake.sentence(),
                    "location": (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
                }
                for _ in range(self.num_characters)
            ]
        except Exception as e:
            print(f"Error generating characters: {e}")
    
    def generate_quests(self) -> None:
        """Generate quests with objectives, quest givers, and details."""
        try:
            self.quests = [
                {
                    "quest_giver": (quest_giver := random.choice(self.characters))["name"],
                    "objective": random.choice(self.QUEST_OBJECTIVES),
                    "location": (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)),
                    "details": fake.paragraph()
                }
                for _ in range(self.num_quests)
            ]
        except Exception as e:
            print(f"Error generating quests: {e}")
    
    def _add_section_header(self, pdf: FPDF, title: str) -> None:
        """Add a styled section header to the PDF."""
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, title, ln=True)
        pdf.ln(5)
    
    def export_to_pdf(self, filename: str = "quest.pdf") -> None:
        """
        Export the generated map, characters, and quests to a PDF file.
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        try:
            # Add Map
            pdf.add_page()
            self._add_section_header(pdf, "Generated Map:")
            pdf.set_font("Courier", size=10)
            for row in self.map:
                pdf.cell(0, 6, ' '.join(f"{cell:8}" for cell in row), ln=True)
            
            # Add Characters
            pdf.add_page()
            self._add_section_header(pdf, "Characters:")
            pdf.set_font("Arial", size=12)
            for char in self.characters:
                pdf.multi_cell(0, 10, f"Name: {char['name']}\n"
                                      f"Role: {char['role']}\n"
                                      f"Backstory: {char['backstory']}\n"
                                      f"Location: {char['location']}")
                pdf.ln(5)
            
            # Add Quests
            pdf.add_page()
            self._add_section_header(pdf, "Quests:")
            pdf.set_font("Arial", size=12)
            for quest in self.quests:
                pdf.multi_cell(0, 10, f"Quest Giver: {quest['quest_giver']}\n"
                                      f"Objective: {quest['objective']}\n"
                                      f"Location: {quest['location']}\n"
                                      f"Details: {quest['details']}")
                pdf.ln(5)
            
            pdf.output(filename)
            print(f"Quest saved to {filename}")
        except Exception as e:
            print(f"Failed to save PDF: {e}")
    
    def generate_all(self) -> None:
        """Generate the map, characters, and quests."""
        self.generate_map()
        self.generate_characters()
        self.generate_quests()

if __name__ == "__main__":
    quest_gen = QuestGenerator(grid_size=8, num_characters=6, num_quests=4)
    quest_gen.generate_all()
    quest_gen.export_to_pdf("board_game_quest.pdf")
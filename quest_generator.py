import random
from faker import Faker
from fpdf import FPDF

fake = Faker()

class QuestGenerator:
    def __init__(self, grid_size=10, num_characters=5, num_quests=3):
        self.grid_size = grid_size
        self.num_characters = num_characters
        self.num_quests = num_quests
        self.map = []
        self.characters = []
        self.quests = []
        self.terrain_types = ['Forest', 'Mountain', 'Desert', 'Plains', 'Lake']
    
    def generate_map(self):
        self.map = [
            [random.choice(self.terrain_types) for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]
    
    def generate_characters(self):
        self.characters = [
            {
                "name": fake.name(),
                "role": random.choice(['Villager', 'Merchant', 'Knight', 'Mage']),
                "backstory": fake.sentence(),
                "location": (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
            }
            for _ in range(self.num_characters)
        ]
    
    def generate_quests(self):
        objectives = [
            "Find the lost artifact", 
            "Defeat the monster", 
            "Escort the merchant", 
            "Explore the ancient ruins", 
            "Deliver a secret message"
        ]
        for _ in range(self.num_quests):
            quest_giver = random.choice(self.characters)
            quest_location = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
            self.quests.append({
                "quest_giver": quest_giver["name"],
                "objective": random.choice(objectives),
                "location": quest_location,
                "details": fake.paragraph()
            })
    
    def export_to_pdf(self, filename="quest.pdf"):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add Map
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, "Generated Map:", ln=True)
        for row in self.map:
            pdf.cell(0, 10, ' '.join(row), ln=True)
        
        # Add Characters
        pdf.add_page()
        pdf.cell(0, 10, "Characters:", ln=True)
        for char in self.characters:
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, f"Name: {char['name']}, Role: {char['role']}", ln=True)
            pdf.cell(0, 10, f"Backstory: {char['backstory']}", ln=True)
            pdf.cell(0, 10, f"Location: {char['location']}", ln=True)
            pdf.ln(5)
        
        # Add Quests
        pdf.add_page()
        pdf.cell(0, 10, "Quests:", ln=True)
        for quest in self.quests:
            pdf.cell(0, 10, f"Quest Giver: {quest['quest_giver']}", ln=True)
            pdf.cell(0, 10, f"Objective: {quest['objective']}", ln=True)
            pdf.cell(0, 10, f"Location: {quest['location']}", ln=True)
            pdf.cell(0, 10, f"Details: {quest['details']}", ln=True)
            pdf.ln(5)
        
        pdf.output(filename)
        print(f"Quest saved to {filename}")
    
    def generate_all(self):
        self.generate_map()
        self.generate_characters()
        self.generate_quests()

if __name__ == "__main__":
    quest_gen = QuestGenerator(grid_size=8, num_characters=6, num_quests=4)
    quest_gen.generate_all()
    quest_gen.export_to_pdf("board_game_quest.pdf")
class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type: str, hard_drive_capactiy: int,
                memory: int, operating_system: str, year_made: int, 
                price: int):
                self.description = description
                self.processor_type = processor_type,
                self.hard_drive_capacity = hard_drive_capactiy,
                self.memory = memory,
                self.operating_system = operating_system,
                self.year_made = year_made,
                self.price = price
        
    # What methods will you need?
    #gathering all of an individual's details in a list when called
    def computerDetails(self):
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.year_made)
        print(self.price)

def main():
    c = Computer("MacPro", "Sierra", "750", "500", "Jaguar", "2019", "400")
print("computer made")
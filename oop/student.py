class Student:
    def __init__(self, name, clan):

        self.skill = None
        self.name = name  # this will call setter method
        self.clan = clan  # this will also call setter method

    def __str__(self):
        return f"{self.name} from {self.clan}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        clan = input("Clan: ")
        return cls(name, clan)
    
    def get_skill(self, skill):
        self.skill = skill

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name!")
        self._name = name

    @property  # getter
    def clan(self):
        return self._clan

    # this setter method will get called if you try to access .clan
    @clan.setter
    def clan(self, clan):
        if clan.lower() not in ["uzumaki", "uchiha", "senju", "hatake"]:
            raise ValueError("Invalid clan!")

        self._clan = clan

    def use_skill(self):
        match self.skill.lower():
            case "wind":
                return "Wind Style: RasenShuriken"
            case "wood":
                return "Wood Style: Wood Dragon Jutsu"
            case "fire":
                return "Fire Style: Fire Ball Jutsu"
            case "water":
                return "Water Style: Water Dragon Jutsu"
            case "lightning":
                return "Lightning Style: Chidori"
            case "earth":
                return "Earth Style: Mud Wall"
            case _:
                return "No Skill!"


def main():
    student = Student.get()
    print(student)


if __name__ == '__main__':
    main()
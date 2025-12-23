import random


class Define_Clan:
    # class variable
    clans = ["Uzumaki", "Uchiha", "Senju", "Hatake"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is from", random.choice(cls.clans), "clan.")


def main():
    Define_Clan.sort("Harry")


if __name__ == '__main__':
    main()

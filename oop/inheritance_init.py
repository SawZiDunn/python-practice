class Ninja:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name!")
        self.name = name


class Student(Ninja):
    def __init__(self, name, clan):
        super().__init__(name) # assigning to the constructor in parent class Ninja
        self.clan = clan


class Teacher(Ninja):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


def main():
    ninja = Ninja("Tsunade")
    student = Student("Naruto", "Uzumaki")
    teacher = Teacher("Kakashi", "Ninjutsu")

    print(f"{student.name} from {student.clan} clan")
    print(f"{teacher.name} teaches {teacher.subject}.")
    print(f"{ninja.name}")


if __name__ == '__main__':
    main()

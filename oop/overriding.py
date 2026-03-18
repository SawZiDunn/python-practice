# inheritance + overriding
class Person:
    def greet(self):
        return "Hello!"
class Student(Person):
    def greet(self):  # overriding the greet method
        return "Hi, I'm a student."
def main():
    person = Person()
    student = Student()
    print(person.greet())  # Output: Hello!
    print(student.greet())  # Output: Hi, I'm a student.
if __name__ == '__main__':
    main()
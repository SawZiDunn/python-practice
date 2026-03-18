"""
program stores courses
university stores programs

lecturer class -> store course instances, getCourses() return courses lectuere is giving

student -> stores takes

Takes -> store student instance and course instance, should have setGrade to set grades later



Transcript -> store student, calculate grade here by calling student.takes
"""

class University:
    def __init__(self, name: str):
        self.__name = name
        self.__students: dict = {}
        self.__programs: list[Program] = []

    def add_student(self, student_id: int, student: Student):
        self.__students[student_id] = student

    def add_program(self, program: Program):
        self.__programs.append(program)

    def get_student(self, student_id: int) -> Student:
        return self.__students.get(student_id)

    def __str__(self):
        return (f"University(name={self.__name}, "
                f"students={len(self.__students)}, programs={len(self.__programs)})")
    
class Program:
    def __init__(self, level: str, name: str, start: str):
        self.__level = level
        self.__name = name
        self.__start = start
        self.__courses: dict = {}

    def addCourse(self, course: Course) -> None:
        self.__courses[id(course)] = course

    def getCourse(self, key) -> Course:
        return self.__courses.get(key)

    def __str__(self):
        return (f"Program(name={self.__name}, level={self.__level}, "
                f"start={self.__start}, courses={len(self.__courses)})")

class Lecturer:
    def __init__(self, name: str):
        self.__name = name         
        self.__courses: list[Course] = []

    def getCourses(self) -> list[Course]:  
        return self.__courses

    def _add_course(self, course):
        self.__courses.append(course)

    def __str__(self):
        return f"Lecturer(name={self.__name}, teaching courses={len(self.__courses)})"
    
class Course:
    def __init__(self, credit: int, course_id: int, name: str,
                 semester: str, lecturer: Lecturer):
        self.__credit = credit
        self.__id = course_id
        self.__name = name
        self.__semester = semester
        self.__lecturer: Lecturer = lecturer
        lecturer._add_course(self) # add to lecturer's taken courses
        self.__student_list: list[Student] = []

    def enroll(self, student: Student) -> Takes:
        self.__student_list.append(student)
        takes = student.enroll_in(self)   # Student creates the Takes
        return takes                       # return so you can set grade later

    def getName(self):
        return self.__name

    def getCredit(self):
        return self.__credit

    def getLecturer(self) -> Lecturer:
        return self.__lecturer

    def getStudents(self) -> list[Student]:
        return self.__student_list

    def __str__(self):
        return (f"Course(id={self.__id}, name={self.__name}, "
                f"semester={self.__semester}, credit={self.__credit})")
    
class Student:
    def __init__(self, name: str, status: str = "normal"):
        self.__name = name
        self.__status = status
        self.__enrollments: dict = {}   # {course_id: Takes}
        self.__transcript: Transcript | None = None

    def get_name(self):
        return self.__name

    def enroll_in(self, course) -> Takes:
        takes = Takes(self, course)
        self.__enrollments[id(course)] = takes
        # self.__transcript.addTakes(takes) # add take to transcript now
        return takes   # caller can save this to set grade later

    def get_takes(self, course) -> Takes:
        return self.__enrollments.get(id(course))

    def set_transcript(self, transcript):
        self.__transcript = transcript

    def get_transcript(self):
        return self.__transcript

    def __str__(self):
        return f"Student(name={self.__name}, status={self.__status})"

# like junction table?
class Takes:
    def __init__(self, student, course):  # no grade yet at enrollment
        self.__student = student
        self.__course = course
        self.__grade = None
        self.__scores = None

    def set_grade(self, grade: str, scores: int):
        self.__grade = grade
        self.__scores = scores

    def getCourse(self):
        return self.__course

    def getGrade(self):
        return self.__grade

    def getScores(self):
        return self.__scores

    def __str__(self):
        return f"Takes(course={self.__course.getName()}, grade={self.__grade}, scores={self.__scores})"


class Transcript:
    def __init__(self, complete: bool, issue_date: str):
        self.__complete = complete
        self.__issue_date = issue_date
        self.__takes: list[Takes] = []

    def addTakes(self, takes: Takes):
        self.__takes.append(takes)

    def printTranscript(self):
        print(f"Transcript [issued: {self.__issue_date}, complete: {self.__complete}]")
        print(f"{'Course':<20} {'Grade':<10} {'Scores'}")
        print("-" * 40)
        for take in self.__takes:
            print(f"{take.getCourse().getName():<20} {str(take.getGrade()):<10} {take.getScores()}")

    def __str__(self):
        return f"Transcript(complete={self.__complete}, issue_date={self.__issue_date})"


if __name__ == "__main__":
    lecturer = Lecturer("Dr. Smith")
    course1  = Course(3, 101, "Intro to CS", "Fall", lecturer)
    course2  = Course(2, 102, "Calculus", "Fall", lecturer)

    student  = Student("Alice")

    # enroll student to course
    takes1 = course1.enroll(student)
    takes2 = course2.enroll(student)

    # set grade to that take obj
    takes1.set_grade("A", 95)
    takes2.set_grade("B+", 82)

    # build transcript
    transcript = Transcript(True, "2024-12-01")
    transcript.addTakes(takes1)
    transcript.addTakes(takes2)
    student.set_transcript(transcript)

    # Print it
    student.get_transcript().printTranscript()
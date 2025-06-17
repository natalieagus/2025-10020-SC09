# why do we want some methods or attributes to be private? 
class Student:
    def __init__(self, name: str, year: int) -> None:
        self.__name = name
        self.year = year
        self.__address = "somewhere"

    # the getter
    def name(self):
        return self.__name 
    
    def __str__(self) -> str:
        return f"{self.name} (Year {self.year})"

        
class Course:
    def __init__(self, code: str, title: str) -> None:
        self.code = code
        self.title = title
        self.roster: list[Student] = []

    def enroll(self, student: Student) -> None:
        print("self", self)
        """Add a student to the course roster."""
        self.roster.append(student)

    def list_students(self) -> list[str]:
        """Return a list of human-readable student names."""
        return [str(s) for s in self.roster]


alice = Student("Alice", 2)
alice.__address = "something else" # dont do this

bob   = Student("Bob",   3)
cs101 = Course("CS101", "Intro to Programming")
cs102 = Course("CS102", "Advanced Programming")

cs101.enroll(bob)
cs102.enroll(alice)


print(cs101.list_students())
print(alice)


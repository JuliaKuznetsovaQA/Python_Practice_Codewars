"""At the end of the last semester, Prof. Joey Greenhorn implemented an online report card
for his students in order to save paper. Everything seemed to be working fine back then,
but since the start of the new semester he has received several emails from students
complaining about erroneous grades showing up in their online report cards.
Can you help him correct his implementation of the "Student" class?

The "Student" class should behave like this :

someStudent = Student()
someOtherStudent = Student()
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
someStudent.grades == [98] # Evaluates to True
someOtherStudent.grades == [77] # Evaluates to True
But right now, this is happening :

someStudent = Student()
someOtherStudent = Student()
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
someStudent.grades == [98, 77] # Evaluates to True
someOtherStudent.grades == [98, 77] # Evaluates to True"""


class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades or []

    def add_grade(self, grade):
        # if len(self.grades) == 0:
        #     self.grades = []
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)


johnDoe = Student('John', 'Doe')
janeDoe = Student('Jane', 'Doe')
jamesSmith = Student('James', 'Smith')
jennaSmith = Student('Jenna', 'Smith')
students = johnDoe, janeDoe, jamesSmith, jennaSmith

# First graded assessment
# Update students' grades so they can see them on the online report card
firstAssessmentGrades = [63, 92, 82, 75]
for i, student in enumerate(students):
    student.add_grade(firstAssessmentGrades[i])
    print(student.__dict__, student.grades)


print(johnDoe.grades)
print(jamesSmith.grades)

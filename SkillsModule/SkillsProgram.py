class GradeBook(object):
    testGrades = []
    projectGrades = []
    quizGrades = []
    studentsGrades = {} #
    studentLetterGrades = {}

    def __init__(self):
        self.average = 0

    # Prints out each student's letter and percentage grade
    def get_student_scores(self):
        for item in self.studentsGrades:
            print "%s received a %s with a percentage of %.2f" % (item, self.studentLetterGrades[item], \
            self.studentsGrades[item])

    # Averages all the student totals to get an average for the class
    def get_class_average(self):
        self.average = 0
        for item in self.studentsGrades:
            self.average += self.studentsGrades[item]
        self.average =  self.average/len(self.studentsGrades)
        return self.average

    def get_letter_grade(self, grade):
        if grade > 90:
            return "A"
        elif grade > 80:
            return "B"
        elif grade > 70:
            return "C"
        elif grade > 60:
            return "D"
        else:
            return "F"

    def assign_student_letter_grades(self):
        students = self.studentsGrades.keys()
        grades = self.studentsGrades.values()
        for i in range(len(students)):
            self.studentLetterGrades[students[i]] = self.get_letter_grade(grades[i])

class Student(object):
    tests = [] # test grades
    projects = [] # project grades
    quizzes = [] # quiz grades
    totalGrade = 0 # total grade

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Updates the student's overall grade
    def update_grade(self):
        self.update_test_grade()
        self.update_quiz_grade()
        self.update_project_grade()
        self.totalGrade = self.testGrade*0.4 + self.projectGrade*0.3 + self.quizGrade*0.3

    def update_test_grade(self):
        self.testGrade = float(sum(self.tests)) / len(self.tests)

    def update_quiz_grade(self):
        self.quizGrade = float(sum(self.quizzes)) / len(self.quizzes)

    def update_project_grade(self):
        self.projectGrade = float(sum(self.projects)) / len(self.projects)

# Created some global variables to be used throughout the program
assignmentType = "" # Will be used to specify whether a line we're reading from the textfile is for tests, projects or quizzes
gradebook = GradeBook() # Will store student

# I create a student named Kevin and gather his grades from the textfile
kevin = Student("Kevin", 123)
with open("kevinsGrades.txt", "r") as myFile:
    for i in range(3):
        line = myFile.readline().split()
        assignmentType = line[0]
        line = line[1::]

        if assignmentType == "tests":
            kevin.tests = [int(x) for x in line]
        elif assignmentType == "projects":
            kevin.projects = [int(x) for x in line]
        else:
            kevin.quizzes = [int(x) for x in line]

# More students are created and their grades are also fetched from their corresponding textfiles
tom = Student("Tom", 124)
emily = Student("Emily", 125)
chris = Student("Chris", 126)
ashley = Student("Ashley", 127)

with open("tomGrades.txt", "r") as myFile:
    for i in range(3):
        line = myFile.readline().split()
        assignmentType = line[0]
        line = line[1::]

        if assignmentType == "tests":
            tom.tests = [int(x) for x in line]
        elif assignmentType == "projects":
            tom.projects = [int(x) for x in line]
        else:
            tom.quizzes = [int(x) for x in line]

with open("emilyGrades.txt", "r") as myFile:
    for i in range(3):
        line = myFile.readline().split()
        assignmentType = line[0]
        line = line[1::]

        if assignmentType == "tests":
            emily.tests = [int(x) for x in line]
        elif assignmentType == "projects":
            emily.projects = [int(x) for x in line]
        else:
            emily.quizzes = [int(x) for x in line]

with open("chrisGrades.txt", "r") as myFile:
    for i in range(3):
        line = myFile.readline().split()
        assignmentType = line[0]
        line = line[1::]

        if assignmentType == "tests":
            chris.tests = [int(x) for x in line]
        elif assignmentType == "projects":
            chris.projects = [int(x) for x in line]
        else:
            chris.quizzes = [int(x) for x in line]

with open("ashleyGrades.txt", "r") as myFile:
    for i in range(3):
        line = myFile.readline().split()
        assignmentType = line[0]
        line = line[1::]

        if assignmentType == "tests":
            ashley.tests = [int(x) for x in line]
        elif assignmentType == "projects":
            ashley.projects = [int(x) for x in line]
        else:
            ashley.quizzes = [int(x) for x in line]

# Now that we have everyone's grades, we can calculate their total grades
kevin.update_grade()
tom.update_grade()
emily.update_grade()
chris.update_grade()
ashley.update_grade()

# We update the gradebook to have all the test grades
gradebook.testGrades.append(kevin.testGrade)
gradebook.testGrades.append(tom.testGrade)
gradebook.testGrades.append(emily.testGrade)
gradebook.testGrades.append(chris.testGrade)
gradebook.testGrades.append(ashley.testGrade)

# We update the gradebook to have all the quiz grades
gradebook.quizGrades.append(kevin.quizGrade)
gradebook.quizGrades.append(tom.quizGrade)
gradebook.quizGrades.append(emily.quizGrade)
gradebook.quizGrades.append(chris.quizGrade)
gradebook.quizGrades.append(ashley.quizGrade)

# We update the gradebook to have all the project grades
gradebook.projectGrades.append(kevin.projectGrade)
gradebook.projectGrades.append(tom.projectGrade)
gradebook.projectGrades.append(emily.projectGrade)
gradebook.projectGrades.append(chris.projectGrade)
gradebook.projectGrades.append(ashley.projectGrade)

# We add each student and their overall grade to the students dictionary in gradebook
gradebook.studentsGrades[kevin.name] = kevin.totalGrade
gradebook.studentsGrades[tom.name] = tom.totalGrade
gradebook.studentsGrades[emily.name] = emily.totalGrade
gradebook.studentsGrades[chris.name] = chris.totalGrade
gradebook.studentsGrades[ashley.name] = ashley.totalGrade

# Now that we have all the grade data inside gradebook, we can use its methods to calculate the class average,
# average on tests, projects, quizzes, etc

# We first get the class average in percentage form
print "The class average is: %.2f" % gradebook.get_class_average()

# We can get the average letter grade for the class
print "The average letter grade is: %s" % (gradebook.get_letter_grade(gradebook.average))

# This function assigns letter grades to each student based on their percentage grade
gradebook.assign_student_letter_grades()

# We can print each student's scores
gradebook.get_student_scores()





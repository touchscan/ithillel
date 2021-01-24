class Student:
	def __init__(self, name, age):
		if len(name) > 0 and str(name).isalpha():
			self.__name = name
		if 0 < age < 60 and str(age).isalnum():
			self.__age = age
		self.__grades = []

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property
	def grades(self):
		return self.__grades

	@grades.setter
	def grades(self, grades):
		self.__grades = grades

	def add_grade(self, grade):
		self.__grades.append(grade)

	def __str__(self):
		return 'Name: {n}, age: {a}, grades: {g}'.format(
			n=self.__name,
			a=self.__age,
			g=', '.join(str(grade) for grade in self.__grades)
		)
					
class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def __str__(self):
        return 'Group: {g}\n{st}\n'.format(
            g=self.__name,
            st='\n'.join(str(s) for s in self.__students)
        )


st1 = Student('John', 38)
st1.grades = [12, 10, 4, 5, 7, 1]
st2 = Student('Cocroach', 19)
st2.grades = [4, 4, 4, 4, 7, 12]
st3 = Student('ElTorro', 24)
st3.grades = [8, 7, 12, 10, 6, 3]

g = Group('Stars')
g.add_students(st1, st2, st3)
print(g)
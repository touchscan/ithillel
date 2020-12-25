class Student:
	def __init__(self, name, age, grades):
		self.__name = name
		self.__age = age
		self.__grades = grades
	
	def set_name(self, name):
		if len(name) > 0 and name.isalpha():
			name = name.lower()
			if (name[0:2] == 'o\'' or name[0:2] == 'mc') and len(name) > 2:
				self.__name = (name[0:2:2].upper() + name[2:-1])
			else:
				self.__name = name.capitalize()
	
	def set_age(self, age):
		if 0 < age < 100 and str(age).isalnum():
			self.__age = age
	
	def set_grades(self, grades):
		if 0 <= grades <= 100 and str(grades).isalnum():
			self.__grades = grades
	
	def get_student(self, flag):
		if flag == 'name':
			return self.__name
		elif flag == 'age':
			return self.__age
		elif flag == 'grades':
			return self.__grades

class Group:
	def __init__(self, faculty, university):
		self.__faculty = faculty
		self.__university = university
	
	def set_group(self, faculty, university):
		if len(faculty) > 0 and  len(university) > 0:
			self.__faculty = faculty
			self.__university = university
	
	def get_group(self, flag):
		if flag == 'faculty':
			return self.__faculty
		elif flag == 'university':
			return self.__university



class Question: 

	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

class Student: 

	def __init__(self, name, major, gpa, is_on_probation):
		self.name = name
		self.major = major
		self.gpa = gpa
		self.is_on_probation = is_on_probation

class Book: 

	def __init__(self, title, author, owner):
		self.title = title
		self.owner = owner
		self.author = author
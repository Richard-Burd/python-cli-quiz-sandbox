class Question: 

	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

# Python won't read the whole script before executing it
# You need to import the <<GlobalTracker>> class even though it's in this very file
# You could also define the <<GlobalTracker>> class before defining the <<Student>> class
from Global import GlobalTracker

# The <<Student>> class will inherit from the <<GlobalTracker>> class
class Student(GlobalTracker): 

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

# This is a repeat of what is in the Global.py file...sort of...but it is ignored by the program.
class GlobalTracker:
    
    def global_tracking_device(self):
    	print("This instance of GlobalTracker is completely ignored by the program")


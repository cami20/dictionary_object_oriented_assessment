"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main advantages of object oriented programming are abstraction,
   encapsulation, and polymorphism. Abstraction is when we hide details that 
   we do not need in all parts of the code. Encapsulation is how we keep all 
   the similar things in our code together. Polymorphism is gives us the ability
   to interchange componets of our code with other componets.

2. What is a class?

	A class is a collection of vairables and methods used in a program to remove 
	reptition and make it easier to read, and to debug.

3. What is an instance attribute?

	An instance attribute is a attribute that is applied to the class when it is
	inicalized.

4. What is a method?
	
	A method is a function within a class.

5. What is an instance in object orientation?

	An instance is when the class is called and used outside of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is used to define an attribute with in a class, a instance 
   attribute defines an attribute when the class is inicalized. You would use a 
   class attribute when you want an attribute to have a specific value throughout 
   the program. You would use a instance attribute to give an attribute value one 
   in that one specific moment.


"""

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

	"""Stores students first and last names and their addresses"""

	first_name = ""
	last_name = ""
	address = ""


class Questions(object):

	"""Stores a question and a correct answer"""

	question = ""
	correct_answer = ""

	def prints_question(self):
		answer = raw_input()

		print question

		if answer == self.correct_answer:
			return True
		else:
			return False


class Exam(object):

	"""Holds questions for an exam"""

	def __init__(self, name):
		exam_name = name

	def takes_question_and_answer(self, question, correct_answer):
		question = self.question
		correct_answer = self.correct_answer

	def admminister(self):
		score = 0.00
		correct = 0.00

		if super(prints_question, self).__init__(self) == True:
			corect = correct + 1

		score = correct / 100.00


class StudentExam(object):
	def __init__(self):
		super(Student, self).__init__(first_name, last_name, address)

		test_key = {}
		while True:
			super(Questions, self).__init__(question, correct_answer)
            test_key[question] = correct_answer

	def take_test(self):
		super(admminister, self).__init__(question, correct_answer)
		print self.score

	def __repr__(self):

def example(questions, answers):
	new_exam = Exam()
	new_student = Student()

	new_exam.takes_question_and_answer()
	new_exam.admminister()

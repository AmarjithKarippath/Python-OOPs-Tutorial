"""
Python OOPs for beginers video-1.

Class, instances and methods.

There are several ways you can help back! Easiest way is LIKE, SUBCRIBE, and SHARE this video. 

Video url: https://youtu.be/RTaN8iE1mj8
"""
class Employee:
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary
		self.email = first + "." + last + "@company.com"

	def full_name(self):
		return ("{} {}".format(self.first, self.last))

emp1 = Employee("Amarjith", "Karippath", 50000)
emp2 = Employee("Sam", "Jhon", 40000)


print (Employee.full_name(emp2))

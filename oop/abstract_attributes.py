from abc import ABC, abstractmethod

class Animal(ABC):
	@property
	@abstractmethod
	def age(self):
		pass

	@age.setter
	@abstractmethod
	def age(self, value):
		pass

class Dog(Animal):
	@property
	def age(self):
		return self._age

	@property.setter
	def setter(self, value):
		if value < 0:
			raise ValueError("Age cannot be less than 0")
		self._age = value
		
	
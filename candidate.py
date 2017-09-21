import uuid

class Candidate:
	__id = None
	__first_name = None
	__last_name = None
	__experience = None

	def __init__(self, first_name, last_name, experience):
		self.__id = uuid.uuid4()
		self.__first_name = first_name
		self.__last_name = last_name
		self.__experience = experience

	@property
	def id(self):
		return self.__id

	@property
	def first_name(self):
		return self.__first_name

	@first_name.setter
	def first_name(self, value):
		self.__first_name = value

	@property
	def last_name(self):
		return self.__last_name

	@last_name.setter
	def last_name(self, value):
		self.__last_name = value

	@property
	def experience(self):
		return self.__experience

	@experience.setter
	def experience(self, value):
		self.__experience = value

	def serialize(self):
		return {
		"id": self.__id,
		"first_name": self.__first_name,
		"last_name": self.__last_name,
		"experience": [exp.serialize() for exp in self.__experience]
		}

	def add_experience(self, experience):
		self.__experience.append(experience)
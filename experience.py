class Experience:
	__domain = None
	__years = None
	__projects = None

	def __init__(self, domain, years, projects = []):
		self.__domain = domain
		self.__years = years
		self.__projects = projects

	@property
	def domain(self):
		return self.__domain

	@domain.setter
	def domain(self, value):
		self.__domain = value

	@property
	def years(self):
		return self.__years

	@years.setter
	def years(self, value):
		self.__years = value

	@property
	def projects(self):
		return self.__projects

	@projects.setter
	def projects(self, value):
		self.__projects = value

	def serialize(self):
		return {
		"domain": self.__domain,
		"years": self.__years,
		"projects": [proj.serialize() for proj in self.__projects]
		}
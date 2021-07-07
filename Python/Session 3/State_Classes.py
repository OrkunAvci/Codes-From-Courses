class ComputerState(object):
	name = "state"
	allowed_states = []

	def switch(self, state):
		""" Switch to new state """
		if state.name in self.allowed_states:
			print('Current:', self, ' => switched to new state', state.name)
			self.__class__ = state
		else:
			print('Current:', self, ' => switching to', state.name, 'not possible.')

	def __str__(self):
		return self.name


class Off(ComputerState):
	name = "off"
	allowed_states = ['on']


class On(ComputerState):
	""" State of being powered on and working """
	name = "on"
	allowed_states = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
	""" State of being in suspended mode after switched on """
	name = "suspend"
	allowed_states = ['on']


class Hibernate(ComputerState):
	""" State of being in hibernation after powered on """
	name = "hibernate"
	allowed_states = ['on']


class Computer(object):
	""" A class representing a computer """

	def __init__(self, model='HP'):
		self.model = model
		# State of the computer - default is off.
		self.state = Off()

	def change(self, state):
		""" Change state """
		self.state.switch(state)

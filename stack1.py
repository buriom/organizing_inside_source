class Stack(object):

	def __init__(self):
		self.container = []

	def isEmpty(self):
		if self.container == []:
			return(True)
		else:
			return(False)
	def push(self,item):
		self.container.append(item)

	def peek(self):
		if self.container == []:
			return('is empty')
		else:
			return(self.container[-1])

	def pop(self):
		if self.container == []:
			return('is empty')
		else:
			a=self.container[-1]
			self.container.remove(self.container[-1])
			return(a)
	def size(self):
		return(len(self.container))	

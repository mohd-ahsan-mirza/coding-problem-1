class CodingProblem1:
	def __init__(self,list,k):
		self.k = k;
		self.list= list;
	def check(self):
		checkedNumbers = [];
		for number in self.list:
			if self.k - number in checkedNumbers:
				return "True -> " + str(number)  + " + " + str(self.k - number) + " = " + str(self.k);
			else:
				checkedNumbers.append(number);
		return "false";
	def printOutput(self):
		print(self.check());

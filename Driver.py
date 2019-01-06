from module import *
import random

def runFunction(passedList,k):
	print(*passedList);
	print("---------------------------");
	print("k = " + str(k));
	print("---------------------------");
	codingProblem = CodingProblem1(passedList,k);
	codingProblem.printOutput();
	print("---------------------------");


print("First Test");
print("---------------------------");
runFunction([10, 15, 3, 7],17);


size = 5;
tests = 100;
startingRange = 0;
endingRange = 50;
print("Running " + str(tests) + " tests with random lists of Size " + str(size) + " and range " + str(startingRange) + " - " + str(endingRange) +  " and K");
print("---------------------------");
for testRun in range(tests):
	passedList = [];
	for run in range(size):
		passedList.append(random.randint(startingRange,endingRange));
	runFunction(passedList,random.randint(startingRange,endingRange));


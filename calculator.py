termInGxs = []

class TermInGx:
	def __init__(self, coefficient, variable, exponent):
		self.coefficient = coefficient
		self.variable = variable
		self.exponent = exponent

termInHxs = []

class TermInHx:
	def __init__(self, coefficient, variable, exponent):
		self.coefficient = coefficient
		self.variable = variable
		self.exponent = exponent

inputQuestions = [
"What type of function do you want to derive? ", 
"To derive a function with the power rule, press 0. ", 
"To derive a function with the product rule, press 1. ", 
"To derive a function with the quotient rule, press 2. ", 
"To derive a function with the chain rule, press 3. ", 
"If you don't want to derive a function, press 4. ", 
]


def main():
	printHeader()
	while True:
		derivativeType = int(getDerivativeType())
		while not derivativeType in range (0,5):
			derivativeType = int(errorMessage())
		if derivativeType == 0:
			printPowerRuleDerivative(termInGxs)
		elif derivativeType == 1:
			printProductRuleDerivative(termInGxs, termInHxs)
		elif derivativeType ==  2:
			printQuotientRuleDerivative(termInGxs, termInHxs)
		elif derivativeType == 3:
			printChainRuleDerivative(termInGxs, termInHxs)
		elif derivativeType == 4:
			sayGoodbye()
			break


#User Messages
def printHeader():
	print ("")
	print ("Hello! Welcome to the Derivative Calculator! ")
	print ("")

def printInputQuestions():
	print (inputQuestions[0])
	print (inputQuestions[1])
	print (inputQuestions[2])
	print (inputQuestions[3])
	print (inputQuestions[4])
	print (inputQuestions[5])
	print ("")

def errorMessage():
	print ("")
	return input("I'm sorry, that's not one of the options. Please type either 0, 1, 2, or 3: ")

def sayGoodbye():
	print ("")
	print ("Okay, Goodbye! ")
	print ("")


#Function Retrieval
def getDerivativeType():
	printInputQuestions()
	return input("Type selection and press enter: ")

def getGx(gx):
	print ("")
	userPrompt = "Enter the number of terms in the function: "
	if gx:
		userPrompt = userPrompt[:-2]
		userPrompt = userPrompt + " g(x): "
	numberOfTerms = int(input(userPrompt))
	while not numberOfTerms in range (1,6):
		print ("")
		print ("I'm sorry, that's not a valid number of terms. ")
		numberOfTerms = int(input("Please enter an integer between 1 and 5: "))
		print ("")
	for i in range (0, numberOfTerms):
		getGxTerm(i, gx)

def getGxTerm(i, gx):
	instruction = "For term " + str(i+1) + ", "
	if gx:
		instruction = instruction[:-2]
		instruction = instruction + " g(x), "
	print (instruction)
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	variable = "x^"
	termInGxs.append(TermInGx(coefficient, variable, exponent))

def getHx(hx):
	print ("")
	if hx:
		numberOfTerms = int(input("Enter the number of terms in the function h(x): "))
		while not numberOfTerms in range (1,6):
			print ("")
			print ("I'm sorry, that's not a valid number of terms. ")
			numberOfTerms = int(input("Please enter an integer between 1 and 5: "))
	else:
		print ("For this type of function, h(x) can only have one term." )
		numberOfTerms = 1
	for i in range (0, numberOfTerms):
		getHxTerm(i,hx)

def getHxTerm(i,hx):
	if hx:
		print ("For term " + str(i+1) + " in h(x), ")
	else:
		print ("For the term in h(x), ")
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	variable = "x^"
	termInHxs.append(TermInHx(coefficient, variable, exponent))


#Power Rule
def printPowerRuleDerivative(termInGxs):
	gx = False
	getGx(gx)
	function = functionPowerRule(termInGxs)
	derivedFunction = derivativePowerRule(termInGxs)
	printFunctions(derivedFunction, function)

def functionPowerRule(termInGxs):
	function = "f(x) = "
	for termInGx in termInGxs:
		function = function + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	function = function[:-3]
	return function

def derivativePowerRule(termInGxs):
	derivedFunction = "f'(x) = "
	for termInGx in termInGxs:
		derivedFunction = derivedFunction + str(termInGx.coefficient*termInGx.exponent) + "x^" + str(termInGx.exponent-1) + " + "
	derivedFunction = derivedFunction[:-3]
	return derivedFunction


#Product Rule
def printProductRuleDerivative(termInGxs, terminHxs):
	gx = True
	hx = True
	print ("")
	print ("Please enter one multiple function as g(x) and one as h(x). ")
	getGx(gx)
	getHx(hx)
	function = functionProductRule(termInGxs, terminHxs)
	derivedFunction = derivativeProductRule(termInGxs, terminHxs)
	printFunctions(derivedFunction, function)

def functionProductRule(termInGxs, terminHxs):
	function = "f(x) = ("
	for termInGx in termInGxs:
		function = function + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	function = function[:-3] + ")("
	for termInHx in termInHxs:
		function = function + str(termInHx.coefficient) + termInHx.variable + str(termInHx.exponent) + " + "
	function = function[:-3] + ")"
	return function

def derivativeProductRule(termInGxs, terminHxs):
	gxDerivation = ""
	for termInGx in termInGxs:
		gxDerivation = gxDerivation + str(termInGx.coefficient*termInGx.exponent) +  "x^" + str(termInGx.exponent-1) + " + "
	gxDerivation = gxDerivation[:-3]
	hxDerivation = ""
	for termInHx in termInHxs:
		hxDerivation = hxDerivation + str(termInHx.coefficient*termInHx.exponent) +  "x^" + str(termInHx.exponent-1) + " + "
	hxDerivation = hxDerivation[:-3]
	derivedFunction = "f'(x) = ("
	for termInGx in termInGxs:
		derivedFunction = derivedFunction + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	derivedFunction = derivedFunction[:-3] + ")(" + hxDerivation + ") + ("
	for termInHx in termInHxs:
		derivedFunction = derivedFunction + str(termInHx.coefficient) + termInHx.variable + str(termInHx.exponent) + " + "
	derivedFunction = derivedFunction[:-3] + ")(" + gxDerivation + ")"
	return derivedFunction


#Quotient Rule
def printQuotientRuleDerivative(termInGxs, termInHxs):
	gx = True
	hx = True
	print ("")
	print ("Please enter the numerator function as g(x) and the denominator one as h(x). ")
	getGx(gx)
	getHx(hx)
	function = functionQuotientRule(termInGxs, termInHxs)
	derivedFunction = derivativeQuotientRule(termInGxs, termInHxs)
	printFunctions(derivedFunction, function)

def functionQuotientRule(termInGxs, terminHxs):
	function = "f(x) = ("
	for termInGx in termInGxs:
		function = function + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	function = function[:-3] + ")/("
	for termInHx in termInHxs:
		function = function + str(termInHx.coefficient) + termInHx.variable + str(termInHx.exponent) + " + "
	function = function[:-3] + ")"
	return function

def derivativeQuotientRule(termInGxs, terminHxs):
	gxDerivation = ""
	for termInGx in termInGxs:
		gxDerivation = gxDerivation + str(termInGx.coefficient*termInGx.exponent) +  "x^" + str(termInGx.exponent-1) + " + "
	gxDerivation = gxDerivation[:-3]
	hxDerivation = ""
	for termInHx in termInHxs:
		hxDerivation = hxDerivation + str(termInHx.coefficient*termInHx.exponent) +  "x^" + str(termInHx.exponent-1) + " + "
	hxDerivation = hxDerivation[:-3]
	derivedFunction = "f'(x) = (("
	for termInHx in termInHxs:
		derivedFunction = derivedFunction + str(termInHx.coefficient) + termInHx.variable + str(termInHx.exponent) + " + "
	derivedFunction = derivedFunction[:-3] + ")(" + gxDerivation + ") - ("
	for termInGx in termInGxs:
		derivedFunction = derivedFunction + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	derivedFunction = (derivedFunction[:-3] + ")(" + hxDerivation + "))")
	derivedFunction = derivedFunction + "/(("
	for termInHx in termInHxs:
		derivedFunction = derivedFunction + str(termInHx.coefficient) + termInHx.variable + str(termInHx.exponent) + " + "
	derivedFunction = derivedFunction[:-3] + ")^2)"
	return derivedFunction


#Chain Rule
def printChainRuleDerivative(termInGxs, termInHxs):
	gx = True
	hx = False
	print ("")
	print ("Please enter the inside function as g(x) and the outside one as h(x). ")
	getGx(gx)
	getHx(hx)
	function = functionChainRule(termInGxs, termInHxs)
	derivedFunction = derivativeChainRule(termInGxs, termInHxs)
	printFunctions(derivedFunction, function)

def functionChainRule(termInGxs, termInHxs):
	function = "f(x) = "
	for termInHx in termInHxs:
		function = function + str(termInHx.coefficient) + "("
	for termInGx in termInGxs:
		function = function + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	function = function[:-3] + ")^"
	for termInHx in termInHxs:
		function = function + str(termInHx.exponent)
	return function

def derivativeChainRule(termInGxs, termInHxs):
	gxDerivation = ""
	for termInGx in termInGxs:
		gxDerivation = gxDerivation + str(termInGx.coefficient*termInGx.exponent) +  "x^" + str(termInGx.exponent-1) + " + "
	gxDerivation = gxDerivation[:-3]
	gx = ""
	for termInGx in termInGxs:
		gx = gx + str(termInGx.coefficient) + termInGx.variable + str(termInGx.exponent) + " + "
	gx = gx[:-3]
	derivative = "f'(x) = (" 
	for termInHx in termInHxs:
		derivative = derivative + str(termInHx.coefficient*termInHx.exponent)
	derivative = derivative + "(" + str(gx) + ")^"
	for termInHx in termInHxs:
		derivative = derivative + str(termInHx.exponent-1)
	derivative = derivative + ")(" + str(gxDerivation) + ")"
	return derivative


#Function Printing
def printFunctions(derivedFunction, function):
	print ("")
	print (function)
	print ("")
	print (derivedFunction)
	print ("")
	del termInGxs[:]
	del termInHxs[:]
	function = ""
	derivedFunction = ""


main()
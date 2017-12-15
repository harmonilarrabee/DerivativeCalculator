terms = []

class Term:
	def __init__(self, coefficient, variable, exponent):
		self.coefficient = coefficient
		self.variable = variable
		self.exponent = exponent

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
			printPowerRuleDerivative(terms)
		elif derivativeType == 1:
			printProductRuleDerivative(termInGxs, termInHxs)
		elif derivativeType ==  2:
			printQuotientRuleDerivative(termInGxs, termInHxs)
		elif derivativeType == 3:
			printChainRuleDerivative(termInGxs, termInHxs)
		elif derivativeType == 4:
			sayGoodbye()
			break

def printHeader():
	print ("")
	print ("Hello! Welcome to the Derivative Calculator! ")
	print ("")

def getDerivativeType():
	printInputQuestions()
	return input("Type selection and press enter: ")

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

def getFunction():
	print ("")
	numberOfTerms = int(input("Enter the number of terms in the function: "))
	while not numberOfTerms in range (1,6):
		print ("")
		print ("I'm sorry, that's not a valid number of terms. ")
		numberOfTerms = int(input("Please enter an integer between 1 and 5: "))
		print ("")
	for i in range (0, numberOfTerms):
		getTerm(i)

def getTerm(i):
	print ("For term " + str(i+1) + ", ")
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	variable = "x^"
	terms.append(Term(coefficient, variable, exponent))

def getGx():
	print ("")
	numberOfTerms = int(input("Enter the number of terms in the function g(x): "))
	while not numberOfTerms in range (1,6):
		print ("")
		print ("I'm sorry, that's not a valid number of terms. ")
		numberOfTerms = int(input("Please enter an integer between 1 and 5: "))
		print ("")
	for i in range (0, numberOfTerms):
		getGxTerm(i)

def getGxTerm(i):
	print ("For term " + str(i+1) + " in g(x), ")
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	variable = "x^"
	termInGxs.append(TermInGx(coefficient, variable, exponent))

def getHx():
	print ("")
	numberOfTerms = int(input("Enter the number of terms in the function h(x): "))
	while not numberOfTerms in range (1,6):
		print ("")
		print ("I'm sorry, that's not a valid number of terms. ")
		numberOfTerms = int(input("Please enter an integer between 1 and 5: "))
		print ("")
	for i in range (0, numberOfTerms):
		getHxTerm(i)

def getHxTerm(i):
	print ("For term " + str(i+1) + " in h(x), ")
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	variable = "x^"
	termInHxs.append(TermInHx(coefficient, variable, exponent))

def getHx2():
	print ("")
	print ("For this type of function, h(x) can only have one term." )
	print ("For the term in h(x), ")
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	variable = "x^"
	termInHxs.append(TermInHx(coefficient, variable, exponent))


def printPowerRuleDerivative(terms):
	getFunction()
	function = functionPowerRule(terms)
	derivedFunction = derivativePowerRule(terms)
	printFunctions(derivedFunction, function)

def functionPowerRule(terms):
	function = "f(x) = "
	for term in terms:
		function = function + str(term.coefficient) + term.variable + str(term.exponent) + " + "
	function = function[:-3]
	return function

def derivativePowerRule(terms):
	derivedFunction = "f'(x) = "
	for term in terms:
		derivedFunction = derivedFunction + str(term.coefficient*term.exponent) + "x^" + str(term.exponent-1) + " + "
	derivedFunction = derivedFunction[:-3]
	return derivedFunction

def printProductRuleDerivative(termInGxs, terminHxs):
	print ("")
	print ("Please enter one multiple function as g(x) and one as h(x). ")
	getGx()
	getHx()
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

def printQuotientRuleDerivative(termInGxs, termInHxs):
	print ("")
	print ("Please enter the numerator function as g(x) and the denominator one as h(x). ")
	getGx()
	getHx()
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

def printChainRuleDerivative(termInGxs, termInHxs):
	print ("")
	print ("Please enter the inside function as g(x) and the outside one as h(x). ")
	getGx()
	getHx2()
	function = functionChainRule(termInGxs, termInHxs)
	derivedFunction = derivativeChainRule(termInGxs, termInHxs)
	printFunctions(derivedFunction, function)

def functionChainRule(termInGxs, termInHxs):
	function = "f(x) = "
	return function

def derivativeChainRule(termInGxs, termInHxs):
	derivative = "f'(x) = "
	return derivative

def printFunctions(derivedFunction, function):
	print ("")
	print (function)
	print ("")
	print (derivedFunction)
	print ("")
	del terms[:]
	del termInGxs[:]
	del termInHxs[:]
	function = ""
	derivedFunction = ""

def sayGoodbye():
	print ("")
	print ("Okay, Goodbye! ")
	print ("")

main()
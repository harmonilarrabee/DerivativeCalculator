terms = []

class Term:
  def __init__(self, coefficient, exponent):
    self.coefficient = coefficient
    self.exponent = exponent

terms = []

def main():
	printHeader()
	while True:
		derivativeType = int(getDerivativeType())
		while not derivativeType in range (0,5):
			derivativeType = int(errorMessage())
		if derivativeType == 0:
			printPowerRuleDerivative(terms)
		elif derivativeType == 1:
			printProductRuleDerivative(terms)
		elif derivativeType ==  2:
			printQuotientRuleDerivative(terms)
		elif derivativeType == 3:
			printChainRuleDerivative(terms)
		elif derivativeType == 4:
			sayGoodbye()
			break

def getDerivativeType():
	printInputQuestions()
	return input("Type selection and press enter: ")

def printHeader():
	print ("")
	print ("Hello! Welcome to the Derivative Calculator! ")
	print ("")

def printInputQuestions():
	print("What type of function do you want to derive? ")
	print ("To derive a function with the power rule, press 0. ")
	print ("To derive a function with the product rule, press 1. ")
	print ("To derive a function with the quotient rule, press 2. ")
	print ("To derive a function with the chain rule, press 3. ")
	print ("If you don't want to derive a function, press 4. ")
	print ("")

def errorMessage():
	print ("")
	return input("I'm sorry, that's not one of the options. Please type either 0, 1, 2, or 3: ")

def printPowerRuleDerivative(terms):
	getFunction()
	print ("")
	print ("f(x) = ")
	for term in terms:
		print (str(term.coefficient) + "x^" + str(term.exponent))
	print ("")
	print ("f'(X) = ")
	for term in terms:
		print (str(term.coefficient*term.exponent) + "x^" + str(term.exponent-1))
	clearTerms()

def printProductRuleDerivative(terms):
	getFunction()
	print ("")
	clearTerms()

def printQuotientRuleDerivative(terms):
	getFunction()
	print ("")
	clearTerms()

def printChainRuleDerivative(terms):
	getFunction()
	print ("")
	clearTerms()

def getFunction():
	print ("")
	numberOfTerms = int(input("Enter the number of terms in the function: "))
	while not numberOfTerms in range (1,6):
		print ("")
		print ("I'm sorry, that's not a valid number of terms. ")
		numberOfTerms = int(input("Please enter an integer between 1 and 5: "))
		print ("")
	for i in range (0, numberOfTerms):
		getTerm()

def getTerm():
	print ("For this term, ")
	coefficient = int(input("enter the coefficient: "))
	exponent = int(input("enter the exponent: "))
	terms.append(Term(coefficient, exponent))

def clearTerms():
	del terms[:]

def sayGoodbye():
	print ("")
	print ("Okay, Goodbye! ")
	print ("")


main()
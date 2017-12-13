terms = []

class Term:
  def __init__(self, coefficient, exponent):
    self.coefficient = coefficient
    self.exponent = exponent

terms = []

derivedTerms = []

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
			printPowerRuleDerivative(terms, derivedTerms)
		elif derivativeType == 1:
			printProductRuleDerivative(terms, derivedTerms)
		elif derivativeType ==  2:
			printQuotientRuleDerivative(terms, derivedTerms)
		elif derivativeType == 3:
			printChainRuleDerivative(terms, derivedTerms)
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

def printPowerRuleDerivative(terms, derivedTerms):
	getFunction()
	for term in terms:
		derivedTerms.append(str(term.coefficient*term.exponent) + "x^" + str(term.exponent-1))
	printFunctions(terms, derivedTerms)

def printProductRuleDerivative(terms, derivedTerms):
	getFunction()
	printFunctions(terms, derivedTerms)

def printQuotientRuleDerivative(terms, derivedTerms):
	getFunction()
	printFunctions(terms, derivedTerms)

def printChainRuleDerivative(terms, derivedTerms):
	getFunction()
	printFunctions(terms, derivedTerms)

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
	terms.append(Term(coefficient, exponent))

def printFunctions(terms, derivedTerms):
	print ("")
	print ("f(x) = ")
	for term in terms:
		print (str(term.coefficient) + "x^" + str(term.exponent))
	print ("")
	print ("f'(x) = ")
	for derivedTerm in derivedTerms:
		print (derivedTerm)
	print ("")
	clearTerms()
	clearDerivedTerms()

def clearTerms():
	del terms[:]

def clearDerivedTerms():
	del derivedTerms[:]

def sayGoodbye():
	print ("")
	print ("Okay, Goodbye! ")
	print ("")


main()
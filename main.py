def main():
	while True:
		derivativeType = int(getDerivativeType())
		while not derivativeType in range (0,5):
			printErrorMessage()
		if derivativeType == 0:
			printPowerRuleDerivative()
		elif derivativeType == 1:
			printProductRuleDerivative()
		elif derivativeType ==  2:
			printQuotientRuleDerivative()
		elif derivativeType == 3:
			printChainRuleDerivative()
		elif derivativeType == 4:
			sayGoodbye()
			break

main()
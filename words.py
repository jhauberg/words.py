# makes random words that adheres to a specific ruleset.

import sys
import re
import random
import json

def from_rule(rule, symbols):
	"""
	Generates a word that matches the specified rules.
	"""
	result = []

	for symbol in rule:
		# determine whether the symbol is upper-case, in which case it has
		# to be replaced with a random word part.
		if re.match('^[A-Z]$', symbol):
			if symbol not in symbols:
				# the replaceable part was not defined in the symbol set.
				continue

			possibilities = symbols[symbol]

			i = random.randint(0, len(possibilities) - 1)

			result.append(possibilities[i])
		else:
			# otherwise, consider it a static part of the word.
			result.append(symbol)

	return ''.join(result)

def from_rules(ruleset, max_amount):
	"""
	Generates `amount` of words from the rules defined in `ruleset`. 

	It is not guaranteed to reach `amount` of words, in case the ruleset does not contain enough unique combinations.
	In such a case, all possible combinations will be created.
	"""
	input = open(ruleset, 'r')

	json_data = json.load(input)

	input.close()

	if json_data is None:
		raise Exception(
				'SyntaxException: the ruleset contains invalid JSON data.'
			)

		return

	rules = json_data['rules']

	if '~' not in rules:
		raise Exception(
				'RulesetException: the ruleset must contain a rule definition named `~`.'
			)

	results = []

	pairings = rules['~']
	symbols = rules['symbols']

	if len(pairings) == 0 or len(symbols) == 0:
		# bail out since there's no rules defined.
		return results

	generated_amount = 0
	retries = 0

	while generated_amount < max_amount:
		# keep going until we've generated as close to max_amount as possible.
		rule = pairings[random.randint(0, len(pairings) - 1)]

		result = from_rule(rule, symbols)

		if result in results:
			# we have a duplicate, retry.
			retries += 1

			# just bruteforce it - more retries = more processing time, but also higher
			# likelyhood of reaching all combinations in case of duplicates.
			# this could definitely be improved :)
			if retries == 100:
		 		break

		 	continue

		results.append(result)

		generated_amount += 1
	
	return results;

def main(argv):
	if len(argv) < 2:
		raise Exception(
				'MissingParameterException: the first argument should be a path to a file containing ruleset data in a JSON format.'
			)

	amount = 1

	if len(argv) > 2:
		amount = int(argv[1])

	results = from_rules(argv[2], amount)

	print json.dumps(results, sort_keys=True, indent=4)

if __name__ == "__main__":
    main(sys.argv)
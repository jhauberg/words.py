# Generate strings from simple rules

import sys
import argparse
import re
import random
import json


def from_rule(rule, parameters):
    """
    Generates a string that matches the specified rules.
    """
    if not rule or not parameters:
        return None

    # Find all parameters that are wrapped in curly braces (e.g. {foo})
    matches = re.finditer('\\{(.*?)\\}', rule)

    result = rule

    for match in matches:
        parameter = match.group(1)

        if parameter not in parameters:
            continue

        possibilities = parameters[parameter]

        next_possibility_index = random.randint(0, len(possibilities) - 1)

        pick = possibilities[next_possibility_index]

        # Remove the braces surrounding the parameter
        result = result.replace('{', '')
        result = result.replace('}', '')

        # Insert the word that was picked
        result = result.replace(parameter, pick, 1)

    return result


def from_rules(ruleset, max_amount):
    """
    Generates up to `max_amount` of strings from the rules
    defined in the file `ruleset`.

    It is not guaranteed to reach `max_amount` of strings, in case the ruleset
    does not contain enough unique combinations.

    In such a case, all possible combinations will be created.
    """
    input = open(ruleset, 'r')

    try:
        json_data = json.load(input)
    except ValueError:
        json_data = None

    input.close()

    if json_data is None:
        raise Exception('The ruleset contains invalid JSON data.')

    rules = json_data

    if 'formats' not in rules:
        raise Exception('The ruleset must contain a rule definition '
                        'named `formats`.')

    if 'parameters' not in rules:
        raise Exception('The ruleset must contain a parameter definitions '
                        'named `parameters`.')

    pairings = rules['formats']
    parameters = rules['parameters']

    results = []

    if len(pairings) == 0 or len(parameters) == 0:
        # Bail out since there's no rules defined
        return results

    generated_amount = 0
    retries = 0

    while generated_amount < max_amount:
        # Keep going until we've generated as close to max_amount as possible
        next_rule_index = random.randint(0, len(pairings) - 1)

        rule = pairings[next_rule_index]

        result = from_rule(rule, parameters)

        if result is not None and result in results:
            # Result was a duplicate, so retry...
            retries += 1

            # This could definitely be improved :)
            if retries == 100:
                break

            continue

        results.append(result)

        generated_amount += 1

    return results


def main(argv):
    parser = argparse.ArgumentParser(
        description='Generate strings from simple rules')

    parser.add_argument('-f', '--filename',
                        help='The path to a JSON file containing rules',
                        required=True)

    parser.add_argument('-n', '--amount',
                        type=int,
                        default=5,
                        help='The amount of strings to generate',
                        required=False)

    args = vars(parser.parse_args())

    rules = args['filename']
    amount = args['amount']

    if amount <= 0:
        amount = 1

    results = from_rules(rules, amount)

    print json.dumps(
        results,
        sort_keys=True,
        indent=2)

if __name__ == "__main__":
    main(sys.argv)

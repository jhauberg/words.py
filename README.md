Run from command line:

	python words.py 5 rules/test.json

Output:

	[
	    "Fireball",
	    "Water Axe",
	    "Windball",
	    "Staff of Yo Momma",
	    "Sword of Strength"
	]

Rules are defined using the following JSON structure (rules/test.json):

	{
		"rules": {
			"~": [
				"ES",
				"ES X",
				"E W",
				"W X"
			],
			"symbols": {
				"E": [
					"Fire",
					"Water",
					"Earth",
					"Wind"
				],
				"W": [
					"Axe",
					"Sword",
					"Staff"
				],
				"S": [
					"ball",
					"spray",
					"gust"
				],
				"X": [
					"of Doom!",
					"of Strength",
					"of Yo Momma"
				]
			}
		}
	}
## Usage

Run from command line:

    python words.py rules/test.json 5

Output:

```json
[
    "Fireball",
    "Water Axe",
    "Windball",
    "Staff of Yo Momma",
    "Sword of Strength"
]
```

Rules are defined using the following JSON structure (e.g. [rules/test.json](https://github.com/shrt/words/blob/master/rules/test.json)):

```json
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
```

[Here's the blogpost](http://scriptogr.am/jacob/post/words) explaining some of the madness.
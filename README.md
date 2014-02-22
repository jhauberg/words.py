## Description

Generate words or sentences using simply defined rules.

## Usage

Run from command line:

    $ python words.py rules/example.json 5

Output:

```json
[
  "Fireball",
  "Water Axe",
  "Windgust",
  "Stupid Sword of Yo Momma",
  "Sword of Strength"
]
```

Rules are defined using the following JSON structure (e.g. [rules/example.json](https://github.com/jhauberg/words/blob/master/rules/example.json)):

```json
{
  "formats": [
    "{Element}{Suffix}",
    "{Element}{Suffix} {Suffix (longer)}",
    "{Element} {Weapon}",
    "Stupid {Weapon} {Suffix (longer)}"
  ],
  "parameters": {
    "Element": [
      "Fire",
      "Water",
      "Earth",
      "Wind"
    ],
    "Weapon": [
      "Axe",
      "Sword",
      "Staff"
    ],
    "Suffix": [
      "ball",
      "spray",
      "gust"
    ],
    "Suffix (longer)": [
      "of Doom!",
      "of Strength",
      "of Yo Momma"
    ]
  }
}
```

## License

    Copyright 2014 Jacob Hauberg Hansen.

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    This part is in all uppercase. 
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    http://en.wikipedia.org/wiki/MIT_License
# Lab Results Parser
My solution uses only standard library so no need to install anything.

To run the unit tests: `python3 test_parser.py`

To run the program which prints the two results from lab2.txt: `python3 parser.py`

## Assumptions

- The Lab Results File starts with index 1 and increases by 1 for each new result. Similar to the examples given.

- nil_3plus '+' '++' both map to -2.0 as specified in the spec.

- LaboratoryTestResult class does not validation of input.

- Parser class does not validate that the input value matches the format type. Parser maps the input to the float value only.

- The `\n` character goes between comments but not at the end. Similar to the example.

- Any float values will not overflow

- Invalid filename with throw an exception and set the results array to `None`
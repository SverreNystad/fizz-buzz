# Fizz Buzz

This is a modular implementation of the Fizz Buzz problem. The fizzbuzz function lets the user specify the range of numbers to be checked and the rules to be applied. The rules are specified as a dictionary where the keys are the numbers and the values are the strings to be printed when the number is divisible by the key. The function returns a list of strings with the results.


This task is often given to candidates in job interviews to test their basic programming skills. 

I first solved it using if statements and then refactored it to use a dictionary to store the rules. This way, the function can be easily extended to include more rules without changing the core code.

The test suite checks for several cases, including the default rules, the case where the rules are changed, and the case where the rules are extended.

## Usage

```python
python fizzbuzz.py
```

## Tests

```python
pytest
```
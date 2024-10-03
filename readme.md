# Fizz Buzz
A modular solution to the classic Fizz Buzz problem. The fizzbuzz function allows you to specify a range of numbers and inject the rules. Each rule is defined as a function and an associated result string, enabling easy extension without altering core logic.

This task is often given to candidates in job interviews to test their basic programming skills. 

Initially solved with if statements, then refactored to dictionaries and in the end the implementation was refactored to accept dynamic rules. This makes it easy to add conditions like divisibility, prime checks, or specific numbers.

## Usage

```python
python fizzbuzz.py
```

## Tests
The test suite checks for several cases, including the default rules, the case where the rules are changed, and the case where the rules are extended.

```python
pytest
```

## Documentation
- [Developer Setup](/docs/developer_setup.md)
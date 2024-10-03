from dataclasses import dataclass
from typing import Callable


@dataclass
class Rule:
    check: Callable[[int], bool]
    result: str


def get_production_rules() -> list[Rule]:
    return [
        Rule(lambda x: x % 3 == 0, "Fizz"),
        Rule(lambda x: x % 5 == 0, "Buzz"),
    ]


def fizzbuzz(
    amount: int, production_rules: list[Rule] = get_production_rules(), separator: str = " "
) -> list[str]:
    """
    Creates the words from fizzbuzz game.

    To learn more see: https://en.wikipedia.org/wiki/Fizz_buzz

    Args:
        amount: (int) the number of words to generate
        production_rules: (list[Rule], optional) the rules to produce the rules from.
        separator: (str, optional) the separator to use between the words

    Returns:
        the amount of words requested using the given production rules

    Examples:
        >>> rules = [Rule(lambda x: x % 3 == 0, "Fizz"), Rule(lambda x: x % 5 == 0, "Buzz")]
        >>> fizzbuzz(0, rules)
        []
        >>> fizzbuzz(3, rules)
        ["1", "2", "Fizz"]
        >>> fizzbuzz(15, rules)
        ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]
    """
    words = []
    for number in range(1, amount + 1):
        word = ""
        for rule in production_rules:
            if rule.check(number):
                word += rule.result + separator
        if word != "":
            words.append(word.strip())
        else:
            words.append(str(number))

    return words


if __name__ == "__main__":
    rules = get_production_rules()
    rules.append(Rule(lambda x: x == 15, "Bang"))
    print(fizzbuzz(100, rules))

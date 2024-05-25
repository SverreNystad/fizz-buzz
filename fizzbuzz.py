# Fizzbuzz
# num dividable by 3 write fizz
# Num dividable by 5 write buzz
# for both write fizzbuzz


def get_production_rules() -> dict[int, str]:
    return {
        3: "Fizz",
        5: "Buzz",
    }


def fizzbuzz(
    amount: int, production_rules: dict[int, str] = get_production_rules()
) -> list[str]:
    """
    Creates the words from fizzbuzz game.

    To learn more see: https://en.wikipedia.org/wiki/Fizz_buzz

    Args:
        amount: (int) the number of words to generate
        production_rules: (dict[int, str], optional) the rules to produce the rules from.

    Returns:
        the amount of words requested using the given production rules

    Examples:
        >>> rules = {3: "Fizz", 5: "Buzz"}
        >>> fizzbuzz(0, rules)
        []
        >>> fizzbuzz(3, rules)
        ["1", "2", "Fizz"]
        >>> fizzbuzz(15, rules)
        ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]
    """
    words = []
    for i in range(1, amount + 1):
        word = ""
        for rule in production_rules.keys():
            if i % rule == 0:
                word += production_rules[rule] + " "
        if word != "":
            words.append(word.strip())
        else:
            words.append(str(i))

    return words


if __name__ == "__main__":

    print(fizzbuzz(16))

import pytest
from fizzbuzz import Rule, fizzbuzz


@pytest.mark.parametrize(
    "input,expected",
    [
        (0, []),  # Edge case (no words to generate)
        (1, ["1"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "Fizz Buzz",
            ],
        ),
    ],
)
def test_simple_rule_set_for_multiple_cases(input, expected):
    """Parameterized test to check multiple cases at once."""
    simple_rules = [
        Rule(lambda x: x % 3 == 0, "Fizz"),
        Rule(lambda x: x % 5 == 0, "Buzz"),
    ]
    result = fizzbuzz(input, simple_rules)
    assert result == expected


def test_complex_rule_set_for_multiple_cases():
    """Test with a more complex rule set."""
    complex_rules = [
        Rule(lambda x: x % 2 == 0, "Foo"),
        Rule(lambda x: x % 3 == 0, "Bar"),
        Rule(lambda x: x % 5 == 0, "Baz"),
    ]
    result = fizzbuzz(15, complex_rules)
    expected = [
        "1",
        "Foo",
        "Bar",
        "Foo",
        "Baz",
        "Foo Bar",
        "7",
        "Foo",
        "Bar",
        "Foo Baz",
        "11",
        "Foo Bar",
        "13",
        "Foo",
        "Bar Baz",
    ]
    assert result == expected


def test_negative_rules():
    """Test with an edge case rule set."""
    edge_case_rules = [
        Rule(lambda x: x % -1 == 0, "Foo"),
        Rule(lambda x: x % -2 == 0, "Bar"),
        Rule(lambda x: x % -3 == 0, "Baz"),
    ]

    result = fizzbuzz(3, edge_case_rules)
    expected = ["Foo", "Foo Bar", "Foo Baz"]
    assert result == expected

def test_change_separator():
    expected_result = ["FizzBuzz"]
    rules = [Rule(lambda x: x % 1 == 0, "Fizz"), Rule(lambda x: x % 1 == 0, "Buzz")]
    result = fizzbuzz(1, rules, separator="")
    assert result == expected_result
    
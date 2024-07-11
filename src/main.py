#!/usr/bin/env python3
import re


class RejectedPattern():
    def __init__(self, pattern, reason) -> None:
        self.pattern = pattern
        self.reason = reason

    def test(self, plate) -> bool:
        return re.match(self.pattern, plate)


patterns = [
    RejectedPattern(
        "^.*\W.*$",
        "Contains non-alphanumeric characters"
    ),
    RejectedPattern(
        "^\w{7,}$",
        "Longer than 7 characters"
    ),
    RejectedPattern(
        "^\d{,4}$",
        "Less than 5 numbers on a numbers only plate"
    ),
    RejectedPattern(
        "^\w$",
        "Less than 2 characters for any other plate"
    ),
    RejectedPattern(
        "^.*0.*$",
        "Contains the number zero (only allowed on call letter plates)"
    ),
    RejectedPattern(
        "^[A-Z]{3}\d{,4}$",
        "3 alpha, up to 4 numeric (AAA1234)"
    ),
    RejectedPattern(
        "^\d{,5}[A-Z]{2}$",
        "Up to 5 numeric, 2 alpha (12345AA)"
    ),
    RejectedPattern(
        "^[A-Z]\d{,6}$",
        "1 alpha, up to 6 numeric (A123456)"
    ),
    RejectedPattern(
        "^[A-Z]{2}\d{2}[A-Z]{2}$",
        "2 alpha, 2 numeric, 2 alpha (AA12AA)"
    ),
    RejectedPattern(
        "^\d{2}[A-Z]{2}\d{3}$",
        "2 numeric, 2 alpha, 3 numeric (12AA123)"
    ),
    RejectedPattern(
        "^[A-Z]\d{,4}[A-Z]$",
        "1 alpha, up to 4 numeric, 1 alpha (A1234A)"
    ),
    RejectedPattern(
        "^\d[A-Z]{2}\d{,4}$",
        "1 numeric, 2 alpha, up to 4 numeric (1AA1234)"
    ),
    RejectedPattern(
        "^\d{,5}[A-Z]\d$",
        "Up to 5 numeric, 1 alpha, 1 numeric (12345A1)"
    ),
    RejectedPattern(
        "^\d{,4}[A-Z]{2}\d$",
        "Up to 4 numeric, 2 alpha, 1 numeric (1234AA1)"
    ),
    RejectedPattern(
        "^[A-Z]\d[A-Z]\d{,4}$",
        "1 alpha, 1 numeric, 1 alpha, 4 numeric (A1A1234)"
    ),
    RejectedPattern(
        "^\d{2}[A-Z]\d{2}$",
        "2 numeric, 1 alpha, 2 numeric (12A12)"
    ),
    RejectedPattern(
        "^\d{,6}[A-Z]$",
        "Up to 6 numeric, 1 alpha (123456A)"
    ),
    RejectedPattern(
        "^\d{,3}[A-Z]{3}$",
        "Up to 3 numeric, 3 alpha (123AAA)"
    ),
    RejectedPattern(
        "^[A-Z]{3}\d{,3}$",
        "3 alpha, up to 3 numeric (AAA123)"
    ),
    RejectedPattern(
        "^[A-Z]{2}\d{,4}$",
        "2 alpha up to 4 numeric (AA1234)"
    ),
    RejectedPattern(
        "^[A-Z]{4}\d{2}$",
        "4 alpha, and 2 numeric (AAAA12)"
    )
]

plate = input("Plate?: ").upper()
print(f"Testing string: {plate}")
rejection_reasons = "\n".join([pattern.reason for pattern in patterns if pattern.test(plate)])
if rejection_reasons:
    print(f"Rejected for the following reasons:\n{rejection_reasons}")
else:
    print("Plate passes all test patterns!")

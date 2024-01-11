#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string)):
        current_value = roman_numerals[roman_string[i]]
        prev_value = roman_numerals[roman_string[i - 1]] if i > 0 else 0

        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value

    return result

import unittest
from expand_string import expand_string, StringExpressionError


class TestExpandString(unittest.TestCase):

    PLAIN_STRING = ('PLAIN', 'PLAIN')
    NESTED_STRING = ('2(3(NW)2(W2(EE)W))', 'NWNWNWWEEEEWWEEEEWNWNWNWWEEEEWWEEEEW')
    DOUBLE_DIGIT_STRING = ('W10(R)E', 'WRRRRRRRRRRE')
    MISMATCHED_PARENTHESIS = ('2(3(NW)2(W2(EE)W)', )

    def test_expands_strings_with_nested_parenthesis(self):
        expanded_string = expand_string(self.NESTED_STRING[0])

        self.assertEquals(self.NESTED_STRING[1], expanded_string)

    def test_handles_plain_strings(self):
        expanded_string = expand_string(self.PLAIN_STRING[0])

        self.assertEquals(self.PLAIN_STRING[1], expanded_string)

    def test_handles_double_and_more_digit_strings(self):
        expanded_string = expand_string(self.DOUBLE_DIGIT_STRING[0])

        self.assertEquals(self.DOUBLE_DIGIT_STRING[1], expanded_string)

    def test_handles_mismatching_opening_and_closing_parenthesis(self):
        self.assertRaises(StringExpressionError, expand_string, self.MISMATCHED_PARENTHESIS[0])


if __name__ == '__main__':
    unittest.main()

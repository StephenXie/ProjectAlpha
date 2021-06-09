from django.test import TestCase
from django.test import SimpleTestCase
from formatter.scripts import *
# Create your tests here.


class FormatterTestCase(SimpleTestCase):
    def setUp(self):
        pass

    def test_uppercase(self):
        assert GetResult("hello", "upper") == "HELLO"

    def test_lowercase(self):
        assert GetResult("HELLO", "lower") == "hello"

    def test_titlecase(self):
        assert GetResult("Hello World", "title") == "Hello World"

    def test_weirdcase(self):
        assert GetResult("Hello World", "weird").lower() == "hello world"

    def test_extend(self):
        def extend_case(case):
            original = case.split()
            result = GetResult(case, "extend").split()
            for i, n in enumerate(result):
                assert n[:len(original[i])] == original[i]
                assert len(set(n[len(original[i]):])) == 1
                assert n[len(original[i])] == original[i][-1]
        extend_case("hello world")

    def test_reverse(self):
        assert GetResult("Hello World", "reverse") == "dlroW olleH"
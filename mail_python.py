import pytest
from math import sqrt


class TestSet:
    @staticmethod
    def test_1():
        s = {'m', 'a', 'i', 'l'}
        s2 = s.copy()
        s2.add('l')
        assert s == s2

    @staticmethod
    def test_2():
        s = {'m', 'a', 'i', 'l', '.', 'r', 'u'}
        try:
            assert s.remove('kek')
        except KeyError:
            pass

    @staticmethod
    @pytest.mark.parametrize('test_input, expected_result', [('kek', set()), ('.ru', {'.', 'r', 'u'}), ('b', {'b'})])
    def test_3(test_input, expected_result):
        a = set('abc mail.ru')
        assert a.intersection(set(test_input)) == expected_result


class TestStr:
    @staticmethod
    def test_1():
        str = 'Hello, World'
        try:
            assert str == 503
        except AssertionError:
            pass

    @staticmethod
    def test_2():
        str1 = 'Hello, World'
        str2 = 'hello, world'.title()
        assert str1 == str2

    @staticmethod
    @pytest.mark.parametrize('test_input, expected_result', [('ma', 0), ('.', 4), ('hello', -1)])
    def test_3(test_input, expected_result):
        str = 'mail.ru'
        assert str.find(test_input) == expected_result

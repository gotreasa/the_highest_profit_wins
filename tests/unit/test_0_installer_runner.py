import pytest

from modules import min_max_profit


def describe_dummy_kata():
    def should_error_when_input_string():
        """🧪 should error saying that the input must be a list for input 'blah'"""
        with pytest.raises(ValueError, match="Input must be a list"):
            min_max_profit.min_max("blah")

    def should_get_max_and_min_for_1():
        """🧪 should say the maximum is 1 and minimum is 1 for input [1]"""
        assert min_max_profit.min_max([1]) == [1, 1]

    def should_get_max_and_min_for_2():
        """🧪 should say the maximum is 2 and minimum is 2 for input [2]"""
        assert min_max_profit.min_max([2]) == [2, 2]

    def should_get_max_and_min_for_2():
        """🧪 should say the maximum is 5 and minimum is 1 for input [1,2,3,4,5]"""
        assert min_max_profit.min_max([1, 2, 3, 4, 5]) == [1, 5]

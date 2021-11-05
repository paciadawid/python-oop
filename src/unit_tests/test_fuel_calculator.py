from src.fuel_calculator import calculate_fuel


class TestsFuelCalculator:

    def test_fuel_12(self):
        assert calculate_fuel(12) == 2

    def test_float_number(self):
        assert calculate_fuel(12.0) == 2

    def test_not_3_divided_number(self):
        assert calculate_fuel(13) == 2

    def test_string(self):
        assert not calculate_fuel("test")

    def test_empty_string(self):
        assert not calculate_fuel("")

    def test_negative_number(self):
        assert not calculate_fuel(-1)

    def test_fuel_3(self):
        assert calculate_fuel(3) == 1

    def test_string_number(self):
        assert calculate_fuel("10") == 1

    def test_non_str_num_param(self):
        assert calculate_fuel([1, 2]) == False
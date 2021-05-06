from calc import Calc


class TestClac:
    def test_multiplication(self):
        assert 15 == Calc.multiplication(3, 5)
        assert 25 == Calc.multiplication(5, 5)

    def test_division(self):
        assert 3 == Calc.division(3, 1)
        assert 2 == Calc.division(8, 4)
        assert 5 == Calc.division(25, 5)

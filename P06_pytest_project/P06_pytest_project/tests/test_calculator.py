from calculator.calculator import Calculator
import pytest as pytest
class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arange
        a = 200
        b= 100
        cal = Calculator()

        # act 
        result = cal.subtract(a,b)

        # assert 
        expected = 100
        assert result == expected
    
    def test_multiply(self):
        # arange
        a = 2
        b= 4
        cal = Calculator()

        # act 
        result = cal.multiply(a,b)

        # assert 
        expected = 8
        assert result == expected

    def test_devide(self):
        # arange
        a = 40
        b= 4
        cal = Calculator()

        # act 
        result = cal.divide(a,b)

        # assert 
        expected = 10
        assert result == expected
    
    def test_divide_by_zero(self):
        # arange
        a = 4321
        b= 0
        cal = Calculator()

        # act & Assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)
        

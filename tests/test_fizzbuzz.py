from fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_2():
    assert fizzbuzz(2) == 2

def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_4():
        assert fizzbuzz(4) == 4

def test_fizzbuzz_5():
        assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz_6():
        assert fizzbuzz(6) == 'fizz'

def test_fizzbuzz_600():
        assert fizzbuzz(600) == 'fizzbuzz'

value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result = [1,2,'fizz',4,'buzz','fizz',7,8,'fizz','buzz',11,'fizz',13,14,'fizzbuzz']
pairs = zip(value,result)
@pytest.mark.parametrize(('value','result'), pairs)
def test_fizzbuzz(value, result):
    assert fizzbuzz(value) == result

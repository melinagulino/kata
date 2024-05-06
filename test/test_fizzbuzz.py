from src.fizzbuzz import Fizzbuzz


def test_retornar_fizz_si_el_numero_es_divisible_por_3():
    fizzbuzz = Fizzbuzz()

    assert fizzbuzz.resultado(3) == "Fizz"
    assert fizzbuzz.resultado(6) == "Fizz"
    assert fizzbuzz.resultado(9) == "Fizz"


def test_retornar_buzz_si_es_divisible_por_5():
    fizzbuzz = Fizzbuzz()

    assert fizzbuzz.resultado(5) == "Buzz"
    assert fizzbuzz.resultado(10) == "Buzz"
    assert fizzbuzz.resultado(20) == "Buzz"


def test_retornar_fizzbuzz_si_es_divisible_por_3_y_5():
    fizzbuzz = Fizzbuzz()

    assert fizzbuzz.resultado(15) == "FizzBuzz"
    assert fizzbuzz.resultado(30) == "FizzBuzz"
    assert fizzbuzz.resultado(75) == "FizzBuzz"


def test_retornar_numero_si_no_es_divisible_por_3_y_por_5():
    fizzbuzz = Fizzbuzz()

    assert fizzbuzz.resultado(1) == 1
    assert fizzbuzz.resultado(4) == 4


def test_retornar_whiz_si_el_numero_es_primo():
    fizzbuzz = Fizzbuzz()

    assert fizzbuzz.resultado(2) == "Whiz"
    assert fizzbuzz.resultado(7) == "Whiz"
    assert fizzbuzz.resultado(11) == "Whiz"


def test_retornar_fizzbuzz_si_el_numero_es_primo_y_divisible_por_r():
    fizzbuzz = Fizzbuzz()

    assert fizzbuzz.resultado(5) == "BuzzWhiz"















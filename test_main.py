#from main.py import *
from main import BinaryNumber
from main import subquadratic_multiply





## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2*2
def test_multiply2():
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)).decimal_val == 3*3
def test_multiply3():
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(7)).decimal_val == 4*7
def test_multiply4():
    assert subquadratic_multiply(BinaryNumber(15), BinaryNumber(45)).decimal_val == 15*45
def test_multiply5():
    assert subquadratic_multiply(BinaryNumber(225), BinaryNumber(475)).decimal_val == 225*475
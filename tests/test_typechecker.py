from typechecker import type_checker
from main import pytest
from main import datetime

def test_check_int_with_int():
        assert type_checker.check_int(10) == 10
    
def test_check_int_with_float():
        assert type_checker.check_int(10.5) == 10         # Since we convert floats to ints in TypeChecker
    
def test_check_int_with_date():
        assert type_checker.check_int("2024-09-13") == None
        
        
def test_check_float_with_float():
        assert type_checker.check_float(10.5) == 10.5
    
def test_check_float_with_int():
        assert type_checker.check_float(10) == 10.0
        
def test_check_float_with_date():
        assert type_checker.check_float("2024-09-13") == None


def test_check_date_with_date():
        assert type_checker.check_date("2024-09-13") == datetime(2024, 9, 13, 0, 0)
    
def test_check_date_with_int():
        assert type_checker.check_date(10) == None
    
def test_check_date_with_float():
        assert type_checker.check_date(10.5) == None
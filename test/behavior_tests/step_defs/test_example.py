#import pytest_bdd methods and feature file for this test
import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from pathlib import Path

#global variable for this test
def pytest_configure():
    pytest.count = 0

scenarios('../features/example.feature')

@given('the basket has 2 cucumbers')
def basket():
    pytest.count = 2
    
@when('4 cucumbers are added to the basket')
def add_cucumber():
    pytest.count = pytest.count + 4
    
@then('the basket contains 6 cucumbers')
def basket_has_total():
    assert pytest.count==6
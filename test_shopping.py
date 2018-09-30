from shopping import is_in_shopping_list
import pytest

@pytest.mark.parametrize("candidate, expected",[
	("apple", True),
	("pear", True),
	(" pear", True) 
])

def test_is_in_shopping_list(candidate, expected):
	response = is_in_shopping_list(candidate)
	assert response == expected

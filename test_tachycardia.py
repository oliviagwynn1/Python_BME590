from tachycardia import is_tachycardic
import pytest

@pytest.mark.parametrize("candidate, expected",[
	("tachycardic", True),
	(" tachycardic", True),
	("tachycardic ", True),
	("Tachycardic", True),
	("tachy cardic", True),
	("Tachy cardic", True),
	(" Tachy Cardic", True)
])

def test_is_tachycardic(candidate, expected):
	response = is_tachycardic(candidate)
	assert response == expected

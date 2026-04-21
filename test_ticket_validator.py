import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total


# ── validate_ticket ──────────────────────────────────────────────

def test_valid_ticket():
    assert validate_ticket("TK123456") is True

def test_invalid_prefix():
    assert validate_ticket("AB123456") is False

def test_wrong_length_short():
    assert validate_ticket("TK12345") is False

def test_wrong_length_long():
    assert validate_ticket("TK1234567") is False

def test_non_digit_suffix():
    assert validate_ticket("TK12A456") is False

def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        validate_ticket(12345678)


# ── get_ticket_tier ───────────────────────────────────────────────

@pytest.mark.parametrize("code, expected", [
    ("TK012345", "General"),
    ("TK412345", "VIP"),
    ("TK712345", "Platinum"),
])
def test_ticket_tiers(code, expected):
    assert get_ticket_tier(code) == expected

def test_tier_boundary_3_and_4():
    assert get_ticket_tier("TK312345") == "General"
    assert get_ticket_tier("TK412345") == "VIP"

def test_invalid_ticket_raises_value_error():
    with pytest.raises(ValueError):
        get_ticket_tier("BADCODE")


# ── calculate_total ───────────────────────────────────────────────

def test_total_no_discount():
    assert calculate_total([10.0, 20.0]) == 30.0

def test_total_with_discount():
    assert calculate_total([10.0, 20.0], 0.1) == 27.0

def test_empty_prices_raises():
    with pytest.raises(ValueError):
        calculate_total([])

def test_discount_out_of_range_raises():
    with pytest.raises(ValueError):
        calculate_total([10.0], 1.5)

def test_discount_boundary_one_raises():
    # discount of exactly 1.0 is out of range per spec
    with pytest.raises(ValueError):
        calculate_total([10.0, 20.0], 1.0)

def test_prices_not_list_raises_type_error():
    with pytest.raises(TypeError):
        calculate_total("not a list")
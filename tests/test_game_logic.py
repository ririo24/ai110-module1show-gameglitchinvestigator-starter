import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

#FIX: Added test cases to see if hint message was corrected using Claude
def test_too_high_hint_says_go_lower():
    # Bug: original code returned "Go HIGHER!" when guess was too high.
    # Fixed code must say "Go LOWER!" when guess exceeds the secret.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message}"
    assert "HIGHER" not in message, f"Hint must not say HIGHER when guess is too high, got: {message}"


def test_too_low_hint_says_go_higher():
    # Bug: original code returned "Go LOWER!" when guess was too low.
    # Fixed code must say "Go HIGHER!" when guess is below the secret.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message}"
    assert "LOWER" not in message, f"Hint must not say LOWER when guess is too low, got: {message}"

#FIX: Added test cases to see if display message range was corrected for each difficulty level using Claude
def test_difficulty_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_difficulty_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_difficulty_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200

def test_difficulty_range_unknown_defaults_to_normal():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

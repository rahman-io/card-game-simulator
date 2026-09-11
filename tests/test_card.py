from card import Card

def test_that_constructor_stores_rank_and_suit_correctly():
    # Arrange: set up card and data
    card = Card("A", "Hearts")

    # Act: run the functions
    result = card.value

    # Assert: check the results
    assert result == ("A", "Hearts")

def test_that_display_info_returns_correct_format():
    # Arrange: set up card and data
    card = Card("A", "Hearts")

    # Act: run the functions
    result = card.display_info()

    # Assert: check the results
    assert result == "A of Hearts"


from anki.word_card import Word


def test_Word_repr():
    word = Word('hi', [''], ['привет'])
    assert str(word) == 'hi / привет'

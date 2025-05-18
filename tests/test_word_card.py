from anki.word_card import Card, parser
import pytest


def test_Card_repr():
    word = Card('hi', '', 'привет')
    assert str(word) == 'hi / привет'

@pytest.mark.parametrize('sentence, card', [
    ("I *thought* you finished / думать", Card('think', 'I _____(2) you finished', 'думать')),
    ("I've *seen* him last week / видеть", Card('see', "I've _____(3) him last week", 'видеть')),
    ("I've *wisited* him last week / видеть", Card('wisite', "I've _____ed him last week", 'видеть')),
    ("I'll *do* a lot of things. / делать", Card('do', "I'll _____ a lot of things.", "делать")),
    ("She *shows* me the room / показать", Card('show', 'She _____s me the room', 'показать')),

    ("I * thought* you finished / думать", Card('think', 'I _____(2) you finished', 'думать')),
    ("I've *  seen* him last week / видеть", Card('see', "I've _____(3) him last week", 'видеть')),
    ("I've *visited * him last week / видеть", Card('visited', "I've _____ed him last week", 'видеть')),
    ("I'll * do * a lot of things. / делать ", Card('do', "I'll _____ a lot of things.", "делать")),
    ("She *shows* me the room /показать", Card('show', 'She _____s me the room', 'показать')),
    ("I've *finished*/закончить", Card('finish', "I've _____ed", 'закончить')),

    ("I'll * do * a lot of things. \ делать ", Card('do', "I'll _____ a lot of things.", "делать")),    # NOTE: DeprecationWarining
    ("I'll * do * a lot of things. \\ делать ", Card('do', "I'll _____ a lot of things.", "делать")),
])
def test_parser(sentence, card):
    res = parser(sentence)
    assert res.word == card.word
    assert res.context == card.context
    assert res.translation == card.translation

from dataclasses import dataclass, field
from typing import List, Self
from uuid import uuid4
import spacy
import logging


logging.basicConfig(level=logging.INFO)
NLP = spacy.load('en_core_web_lg')


@dataclass
class Card:
    word: str
    context: str
    translation: str
    id: str = field(default_factory=lambda: str(uuid4()))

    # def __eq__(self, value: object, /) -> bool:
    #     if not isinstance(value, Card):
    #         return False
    #     return self.word == value.word and self.translation == value.translation and self.contex == value.contex

    def __repr__(self):
        return f"{self.word} / {self.translation}"


def parser(query: str) -> Card:

    logging.info(f'\nQuery: {query}')

    # Обработка перевода
    split_query = (
        query.strip().split('/') if '/' in query else query.split('\\')
    )
    if len(split_query) != 2:
        raise ValueError("Please use only one slash (/) as a separator of context example and translation.")
    translation = split_query[1].strip()
    if len(translation) < 2:
        raise ValueError("Empty translation.")
    logging.info(f'Translation: {translation}')

    # Обработка слова: приведение к нормальной форме
    raw_context = split_query[0]
    split_context = raw_context.split('*')
    if len(split_context) != 3:
        raise ValueError(
            "Incorrect mark for word in context. "
            "Please use this template to give word card.\n"
            "Example: My context sentence for *word* I want to translate. / перевод"
        )

    raw_word = split_context[1].strip()

    sentence = ' '.join(split_context)
    word_token = [token for token in NLP(sentence) if token.text == raw_word][0]
    word = word_token.lemma_
    logging.info(f'The word and lemma: {raw_word}, {word}')

    # Формирование формочки пропуска слова
    dash = '_____'
    if word_token.pos_ == 'VERB':
        logging.info(f'It is VERB. Morphology:\n{word_token.morph}')

        if raw_word != word:
            ending = None
            for end in ['ed', 'ing', 's']:
                logging.debug(f'{raw_word}, {end}, {raw_word.endswith(end)}')
                if raw_word.endswith(end):
                    ending = end
                    break
            logging.debug(f'ending: {ending}')
            if ending is not None:
                dash += f'{ending}'
            elif 'Tense=Past' in word_token.morph:
                verb_form = 2
                if 'Aspect=Perf' in word_token.morph:
                    verb_form += 1
                dash = f'{dash}({verb_form})'

    context = f'{split_context[0].strip()} {dash} {split_context[2].strip()}'.strip()
    logging.info(f'Context: {context}')


    return Card(word, context, translation)


if __name__ == '__main__':
    wc = parser("I *thought* you finished / думать")
    wc = parser("I've *seen* him last week / видеть")
    wc = parser("I've *wisited* him last week / видеть")
    wc = parser("I'll *do* a lot of things. / делать")
    wc = parser("She *shows* me the room / показать")

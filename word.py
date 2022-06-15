from dataclasses import dataclass
import pandas as pd
import os.path


@dataclass
class Word:
    italian: str
    english: str


def get_words():
    words = []

    csv_file = 'data/words_to_learn.csv'
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        for entry in df.values:
            word = Word(italian=entry[1], english=entry[2])
            words.append(word)
    else:
        csv_file = 'data/frequency_words.csv'
        df = pd.read_csv(csv_file)
        for entry in df.values:
            word = Word(italian=entry[0], english=entry[1])
            words.append(word)

    return words

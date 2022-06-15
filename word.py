from dataclasses import dataclass
import pandas as pd


@dataclass
class Word:
    italian: str
    english: str


def get_words():
    csv_file = 'data/frequency_words.csv'
    df = pd.read_csv(csv_file)
    words = []

    for entry in df.values:
        word = Word(italian=entry[0], english=entry[1])
        words.append(word)

    return words

import random
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_of_jokes):
    """Generates 'number_of_jokes' amount of jokes from [nouns], [adverbs] and [adjectives] lists"""
    for n in range(number_of_jokes):
        print(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}', end=', ')


get_jokes(3)

# Не понял как сделать неповторяющиеся шутки. Удалял слова из списков после использования,
# но в таком случае будет максимум 5 шуток. А ведь каждое слово может быть использовано еще и в других комбинациях
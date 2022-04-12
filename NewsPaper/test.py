val = '''Текст третьей новости нужно сделать более 20 слов, чтобы проверить работу фильтра :) Но слов очень мало, 
поэтому пишу всякую фигню и получается как раз 20 с лишним. Редиска редиска'''

BAD_WORDS = ['редиска', ]


def censor(value):
    lst = []
    lst_2 = []
    st = ''

    if isinstance(value, str):
        for symb in value:
            if symb.isalpha():
                st += symb
                if len("".join(lst) + st) == len(value):
                    lst.append(st)
            else:
                if len(st):
                    lst.append(st)
                lst.append(symb)
                st = ''
        for word in lst:
            for b_word in BAD_WORDS:
                if b_word.lower() == word.lower():
                    word = word[0]+('*' * (len(word)-1))
            lst_2.append(word)
        return "".join(lst_2)
    else:
        raise ValueError('Фильтр можно применять только к строке')

print(censor(val))

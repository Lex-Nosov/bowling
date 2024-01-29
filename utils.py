from bowling import Bowling, FirstThrow, FirstThrowNewRules


def data_checking(result):
    max_frame = 10
    min_frame = 2
    result = result.upper()
    result_without_x = result.replace('X', '')
    quantity_frames = result.count('X') + len(result_without_x) // 2
    valid_characters = ['X', '/', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(result_without_x) % 2 == 0:
        if min_frame <= quantity_frames <= max_frame:
            for idx, char in enumerate(result_without_x):
                if char in valid_characters:
                    # проверяю есть в первом броске знак "/"
                    if idx == 0 or idx % 2 == 0:
                        if char == '/':
                            raise ValueError(f'Первый бросок не может быть SPARE, {result}')
                    continue
                else:
                    raise ValueError(f'Не корректный символ {char}, допустимые символы {valid_characters}')
        else:
            raise ValueError(
                f'Не корректное количество фреймов - {quantity_frames}, допустимо от {min_frame} до {max_frame}')
    else:
        raise ValueError('В фрейме не совершён второй бросок')
    return result


def get_score(result):
    result = list(data_checking(result))
    context = Bowling(FirstThrow(), result)
    while context.result:
        context.first_throw()
        context.second_throw()
    return context.score


def get_score_new_rules(result):
    result = list(data_checking(result))
    context = Bowling(FirstThrowNewRules(), result)
    while context.result:
        context.first_throw()
        context.second_throw()

    return context.score

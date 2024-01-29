from abc import ABC, abstractmethod


class Bowling:
    _state = None

    def __init__(self, state, result):
        self.change_state(state)
        self.score = 0
        self.STRIKE = 20
        self.SPARE = 15
        self.result = result
        self.first_throw_value = 0
        # сделал переменую флаг
        self.it_was_x = False

    def change_state(self, state):
        self._state = state
        self._state.bowling = self

    def first_throw(self):
        self._state.first_throw()

    def second_throw(self):
        self._state.second_throw()


class State(ABC):

    @property
    def bowling(self):
        return self._bowling

    @bowling.setter
    def bowling(self, bowling):
        self._bowling = bowling

    @abstractmethod
    def first_throw(self):
        pass

    @abstractmethod
    def second_throw(self):
        pass


class FirstThrow(State):

    def first_throw(self):
        symbol = self.bowling.result.pop(0)
        # вовремя тестирования нашёл уязвимость при получении последовательности "-/" код падал
        if symbol.isdigit():
            symbol = int(symbol)
        if symbol != '-':
            self.bowling.first_throw_value = symbol
        if symbol == 'X':
            self.bowling.it_was_x = True
            self.bowling.score += self.bowling.STRIKE
        elif symbol == '-':
            pass
        else:
            self.bowling.score += int(symbol)
        self.bowling.change_state(SecondThrow())

    def second_throw(self):
        pass


class SecondThrow(State):

    def first_throw(self):
        pass

    def second_throw(self):
        if not self.bowling.it_was_x:
            symbol = self.bowling.result.pop(0)
            if symbol.isdigit():
                symbol = int(symbol)
            if symbol == '-':
                pass
            elif symbol == '/':
                self.bowling.score += (self.bowling.SPARE - int(self.bowling.first_throw_value))
            else:
                if self.bowling.first_throw_value + symbol > 9:
                    raise ValueError('Сумма фрейма больше количества кеглей', self.bowling.result)
                self.bowling.score += int(symbol)
        self.bowling.it_was_x = False
        # обновляю значение тк если в первом броске выпадет условие, что символ равен "-"
        # то значение не обновится и итог будет не верный
        # примеру если будет прошлый фрейм 35, а текущий -/
        # то значение "first_throw_value" будет равно 5, а не 0 как должно быть и оно не обновится
        # без условия в первом броске
        # пример: фрейм "X34-/", без условия результат будет 39, а должен быть 42
        self.bowling.first_throw_value = 0
        self.bowling.change_state(FirstThrow())


class FirstThrowNewRules(State):

    def first_throw(self):
        _STRIKE = 10
        symbol = self.bowling.result.pop(0)
        # вовремя тестирования нашёл уязвимость при получении последовательности "-/" код падал
        if symbol.isdigit():
            symbol = int(symbol)
        if symbol != '-':
            self.bowling.first_throw_value = symbol
        if symbol == 'X':
            __score = self.counter(self.bowling.result)
            self.bowling.it_was_x = True
            self.bowling.score += (_STRIKE + __score)
        elif symbol == '-':
            pass
        else:
            self.bowling.score += int(symbol)
        self.bowling.change_state(SecondThrowNewRules())

    def second_throw(self):
        pass

    def counter(self, result):
        score = 0
        throws = result[:2]
        for char in throws:
            if char == 'X':
                score += 10
            elif char == '/':
                score += (10 - int(throws[0]))
            else:
                if char.isdigit():
                    score += int(char)
        return score


class SecondThrowNewRules(State):

    def first_throw(self):
        pass

    def second_throw(self):
        _SPARE = 10
        _score = 0
        if not self.bowling.it_was_x:
            symbol = self.bowling.result.pop(0)
            if symbol.isdigit():
                symbol = int(symbol)
            if symbol == '-':
                pass
            elif symbol == '/':
                if self.bowling.result:
                    _score = self.counter(self.bowling.result[0])
                self.bowling.score += (_SPARE - self.bowling.first_throw_value + _score)
            else:
                if self.bowling.first_throw_value + symbol > 9:
                    raise ValueError('Сумма фрейма больше количества кеглей', self.bowling.result)
                self.bowling.score += int(symbol)
        self.bowling.it_was_x = False
        # обновляю значение тк если в первом броске выпадет условие, что символ равен "-"
        # то значение не обновится и итог будет не верный
        # примеру если будет прошлый фрейм 35, а текущий -/
        # то значение "first_throw_value" будет равно 5, а не 0 как должно быть и оно не обновится
        # без условия в первом броске
        # пример: фрейм "X34-/", без условия результат будет 39, а должен быть 42
        self.bowling.first_throw_value = 0
        self.bowling.change_state(FirstThrowNewRules())

    def counter(self, char):
        score = 0
        if char:
            if char == 'X':
                score += 10
            else:
                if char.isdigit():
                    score += int(char)
        return score

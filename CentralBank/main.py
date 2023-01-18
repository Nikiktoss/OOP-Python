class MoneyR:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        if type(other) == MoneyD:
            valute = 'dollar'
        elif type(other) == MoneyE:
            valute = 'euro'
        else:
            return self.volume < other.volume

        return (self.volume / self.cb.rates['rub']) < (other.volume / other.cb.rates[valute])

    def __ge__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        valute = ''
        if type(other) == MoneyD:
            valute = 'dollar'
        elif type(other) == MoneyE:
            valute = 'euro'
        else:
            return self.volume >= other.volume

        return (self.volume / self.cb.rates['rub']) >= (other.volume / other.cb.rates[valute])

    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        valute = ''
        if type(other) == MoneyD:
            valute = 'dollar'
        elif type(other) == MoneyE:
            valute = 'euro'
        else:
            return abs(self.volume - other.volume) <= 0.1

        return abs((self.volume / self.cb.rates['rub']) - (other.volume / other.cb.rates[valute])) <= 0.1


class MoneyD:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __ge__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        valute = ''
        if type(other) == MoneyR:
            valute = 'rub'
        elif type(other) == MoneyE:
            valute = 'euro'
        else:
            return self.volume >= other.volume

        return (self.volume / self.cb.rates['dollar']) >= (other.volume / other.cb.rates[valute])

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        valute = ''
        if type(other) == MoneyR:
            valute = 'rub'
        elif type(other) == MoneyE:
            valute = 'euro'
        else:
            return self.volume < other.volume

        return (self.volume / self.cb.rates['dollar']) < (other.volume / other.cb.rates[valute])

    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        valute = ''
        if type(other) == MoneyR:
            valute = 'rub'
        elif type(other) == MoneyE:
            valute = 'euro'
        else:
            return abs(self.volume - other.volume) <= 0.1

        return abs((self.volume / self.cb.rates['dollar']) - (other.volume / other.cb.rates[valute])) <= 0.1


class MoneyE:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        valute = ''
        if type(other) == MoneyR:
            valute = 'rub'
        elif type(other) == MoneyD:
            valute = 'dollar'
        else:
            return abs(self.volume - other.volume) <= 0.1

        return abs((self.volume / self.cb.rates['euro']) - (other.volume / other.cb.rates[valute])) <= 0.1

    def __ge__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        if type(other) == MoneyR:
            valute = 'rub'
        elif type(other) == MoneyE:
            valute = 'dollar'
        else:
            return self.volume >= other.volume

        return (self.volume / self.cb.rates['euro']) >= (other.volume / other.cb.rates[valute])

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        if type(other) == MoneyR:
            valute = 'rub'
        elif type(other) == MoneyD:
            valute = 'dollar'
        else:
            return self.volume < other.volume

        return (self.volume / self.cb.rates['euro']) < (other.volume / other.cb.rates[valute])


class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money):
        money.cb = cls

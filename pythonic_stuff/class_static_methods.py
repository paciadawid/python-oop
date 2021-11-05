class Animal:
    def __init__(self, paws, color):
        self.paws = paws
        self.color = color

    @classmethod
    def cat(cls, color):
        return cls(4, color)


cat = Animal.cat("white")


class Watch:
    def __init__(self, hours, mins, secs, mili=None):
        self.hours = hours
        self.mins = mins
        self.secs = secs
        if mili:
            self.mili = mili

    @classmethod
    def use_english_format(cls, half_of_the_day, hours, mins, secs, mili=None):
        hours_ = hours
        if half_of_the_day == "PM":
            hours_ += 12
        return cls(hours_, mins, secs, mili)


watch = Watch.use_english_format("PM", 1, 10, 10)
print(watch.hours)


class Calc:
    default_value_a = 1
    default_value_b = 2

    @classmethod
    def add_values(cls):
        return cls.default_value_a + cls.default_value_b


result = Calc.add_values()
print(result)

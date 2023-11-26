class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()  # Вызываем функцию сокращения при создании дроби

    def reduce(self):
        divisor = self.gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def get_value(self):
        return self.numerator / self.denominator

    def get_fraction(self):
        return (self.numerator, self.denominator)


# Создание двух рациональных чисел
rational1 = Rational(1, 2)
rational2 = Rational(2, 3)

# Выполнение операции сложения
result_sum = rational1 + rational2
print("Сумма:", result_sum.get_fraction())  # Выводим результат в виде пары (числитель, знаменатель)

# Выполнение операции вычитания
result_diff = rational1 - rational2
print("Разность:", result_diff.get_fraction())

# Выполнение операции умножения
result_mul = rational1 * rational2
print("Произведение:", result_mul.get_fraction())

# Выполнение операции деления
result_div = rational1 / rational2
print("Частное:", result_div.get_fraction())

# Сравнение рациональных чисел
print("Равны?", rational1 == rational2)
print("Сравнение:", rational1.get_value(), "больше чем", rational2.get_value(), ":", rational1 > rational2)
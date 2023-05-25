"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start_value):
        self.start_value = start_value
        self.count = 0

    def __repr__(self):
        return f"start: {self.start_value}, next value: {self.start_value + self.count}"

    def generate(self):
        value = self.start_value
        if self.count != 0:
            value += self.count
        self.count += 1
        return f"value: {value}"

    def reset(self):
        self.count = 0


serial = SerialGenerator(100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())

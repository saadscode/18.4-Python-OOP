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

    def __init__(self, start):
        """Initializes the SerialGenerator object

        Args:
            start (int): starting value of the generator
        """
        self.start = start
        self.next = start

    def generate(self):
        """Generates the next number in the sequence

        Returns:
            int: generated number
        """
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Resets generator to the starting value
        """
        self.next = self.start

    def __repr__(self):
        """provides a string representing the SerialGenerator object

        Returns:
            str: a string representing the object
        """
        return f"<SerialGenerator start={self.start} next={self.next}>"

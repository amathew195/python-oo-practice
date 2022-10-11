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
        """Create serial generator from a start number"""
        self.start = start - 1
        self.serial_number = self.start

    def __repr__(self):
        """representation method of instance to view start value"""
        return (f"< SerialGenerator start = {self.start} " +
                f"serial_number = {self.serial_number} >")

    def generate(self):
        """Generate increments the start attribute by 1 and returns the
        new value"""
        self.serial_number += 1
        return self.serial_number

    def reset(self):
        """Reset assigns the value of self.start to original start value"""
        self.serial_number = self.start

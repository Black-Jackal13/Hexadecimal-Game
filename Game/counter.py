import random


class Counter:
    def __init__(self, start=0):
        if not 0 <= start <= 255:
            raise ValueError("Counter value must be between 0 and 255")
        self.count = start

    def increment(self, amount=1):
        new_value = (self.count + amount) % 256
        self.count = new_value

    def reset(self):
        self.count = 0

    def get_binary(self):
        return format(self.count, '08b')

    def random(self):
        self.count = random.randint(0, 255)
        return self.get_binary()


if __name__ == '__main__':
    import time
    counter = Counter()

    for _ in range(255):
        counter.increment()
        print(f"\r{counter.get_binary()}", end="")
        time.sleep(0.1)

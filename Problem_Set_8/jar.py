import emoji


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "\U0001F36A"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self.capacity

    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.size

    def size(self, size):
        if size < 1:
            raise ValueError
        self._size = size


def main():
    jar = Jar()
    jar.deposit(1)
    print(jar)


if __name__ == "__main__":
    main()

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def soma(self, a, b):
        return a + b


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 == s2)
    print(s1.soma(1, 2))
    print(s2.soma(1, 2))

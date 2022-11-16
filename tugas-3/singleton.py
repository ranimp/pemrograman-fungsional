class Singleton:
    __instance = None

    def __new__(x, value = None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(x)
        Singleton.__instance.value = value
        return Singleton.__instance
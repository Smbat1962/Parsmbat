class Singleton:
    singleton = None
    def __new__(cls):
        if cls.singleton is None:
            cls.singleton = object.__new__(cls)
        return cls.singleton


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)
print(id(singleton1),id(singleton2))

singleton3 = Singleton()
print(singleton3 is singleton1)
print(id(singleton3))




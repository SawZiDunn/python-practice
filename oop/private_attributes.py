class Clock:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_time(self):
        am_pm = "a.m" if self.__hour <= 12 else "a.m"
        return f"{self.format(self.__hour)}: {self.format(self.__minute)}: {self.format(self.__second)} {am_pm}"

    def tick(self):
        self.__second += 1

    def format(self, x):
        return x if x >= 10 else '0' + str(x)

def main():
    clock = Clock(5, 8, 10)
    print(clock.get_time())
    clock.set_time(12, 9, 2)

    '''
    If we use double underscore and try to access it using clock.__hour, we can also print clock.__hour later.
    But, if we don't change the value using clock.__hour and try to print clock__hour directly, it will throw error.
    That's how private attribute works in python OOP.
    It works only for double underscore.
    '''
    # clock.__hour = 8
    # print(clock.__hour)
    clock.tick()

    print(clock.get_time())

main()
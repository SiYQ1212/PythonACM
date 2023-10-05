from random import choice, randint


class Person:
    # 私有类属性
    __FirstName = list("ABCDEFG")
    __LastName = list("12345678")

    __slots__ = ["_name", "_score"]

    def __init__(self, name, score=0):
        # 实例属性
        self._name = name  # 私有属性
        self._score = score
        """在外用 {Person}.xx = xx 可以实现实例属性的添加, 对此可以用__slots__限制属性的添加"""

    # 实例方法
    def say(self):
        print(f"Hello I am {self._name}")

    # 类方法
    @classmethod
    def create(cls):
        return cls(choice(cls.__FirstName) + choice(cls.__LastName))

    # 静态方法
    @staticmethod
    def nothing():
        print("This is a staticmethod")

    def changeScore(self, n, max_xcore=100):
        self._score += n
        self._score = min(self._score, max_xcore)
        self._score = max(self._score, 0)

    @property   # 实例方法 ==> 实例属性   cls.score()  <==>  cls.score
    def score(self):
        return self._score

    @score.setter  # cls.score(10)  <==>  cls.score = 10
    def score(self, value):
        if type(value) not in (int, float):
            print("Nothing Happened")
        elif 0 <= value <= 100:
            self._score = value


    def __str__(self):  # 当直接打印类或者对象的时候返回
        return f"<{self._name} -- {self._score}>"

    def __repr__(self):
        return f"<{self._name} -- {self._score}>"


if __name__ == '__main__':
    stus = [Person.create() for _ in range(5)]
    print(stus)
    for _ in range(100):
        choice(stus).changeScore(randint(-20, 20))
    print(stus)
    for i in stus:
        print(i.score, end='        ')
    print()
    stus[0].score = 99
    print(stus)

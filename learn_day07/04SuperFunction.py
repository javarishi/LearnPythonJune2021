class Simple:
    def __init__(self):
        print("Simple Parent Class")

    def simple_method(self):
        print("Method from Simple Class")

    def another_method(self):
        print("test method from supersimple")


class SuperSimple(Simple):
    def __init__(self):
        super().__init__()
        print("SuperSimple Child Class")

    def simple_method(self):
        super(SuperSimple, self).simple_method()
        super(SuperSimple, self).another_method()
        print("Method from SuperSimple Class")


obj = SuperSimple()
obj.simple_method()

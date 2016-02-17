class Monad:
    pass

class Option:
    def __init__(self, content):
        self.__content = content

    def get(self):
        return self.__content

    def getOrElse(self, els):
        value = self.get()
        return els if value == None else value

    def flatMap(self, f):
        if hasattr(self.__content, 'map'):
            result = self.__content.map(f)
        else:
            raise Exception("has not attribute")
        return self

    def map(self, f):
        self.__content = f(self.__content)
        return self

class Some(Option):
    pass

class Either:
    pass

class Try:
    pass

print Option("hoge").map(lambda x: x == "piyo").get()
        

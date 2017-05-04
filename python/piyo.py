#!/usr/bin/env python3

from typing import Text

class Animal:
    def __init__(self, name: Text) -> None:
        self._name = name
    def __str__(self) -> Text:
        return "<Animale: {}>".format(self._name)

if __name__ == '__main__':
    animal = Animal('sarval')
    print(animal)

